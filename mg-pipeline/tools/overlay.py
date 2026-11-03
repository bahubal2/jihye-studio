"""HTML 장면 → 투명 배경 글자 레이어 영상 (CapCut 같은 편집기에서 스톡 영상 위에 얹는다).
   python tools/overlay.py <이름> [--fmt mov|webm|green|all] [--from 초] [--to 초]

장면의 .bgonly 요소(미리보기용 바탕)는 빼고, 페이지 바탕을 투명하게 찍는다. 장면이 없는 구간은 투명.
결과 (projects/<이름>/out/overlay/):
  <이름>_overlay.mov        ProRes 4444 (알파 포함) — 편집기 호환성이 가장 넓다. 파일이 크다
  <이름>_overlay.webm       VP9 알파 — 작다. 편집기에 따라 투명이 안 될 수 있다
  <이름>_overlay_green.mp4  초록 바탕 — 투명 파일이 안 될 때 편집기의 크로마키로 지운다
  narration.wav, <이름>.srt 같은 시각의 음성과 자막
"""
import os, sys, shutil, subprocess, argparse
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, KIT)
import mgp

ap = argparse.ArgumentParser(); ap.add_argument('project'); ap.add_argument('--fmt', default='all')
ap.add_argument('--from', dest='t_from', type=float, default=0); ap.add_argument('--to', dest='t_to', type=float, default=None)
a = ap.parse_args()
mgp.load_env(); p = mgp.use(a.project)
import numpy as np, cv2
import timeline, web
from mg import FPS, W, H, ffmpeg_exe

HIDE = 'html, body, .stage { background: transparent !important; } .bgonly { display: none !important; }'
sc = [s for s in timeline.scenes() if timeline.is_html(s)]
if not sc: raise SystemExit('HTML 장면(scenes/sNN.html)이 없습니다.')
web.write_timing()
tot = timeline.total_frames(); f0 = int(a.t_from * FPS); f1 = tot if a.t_to is None else min(tot, int(a.t_to * FPS))
out = os.path.join(p, 'out', 'overlay'); os.makedirs(out, exist_ok=True); name = os.path.basename(p)
fmts = ['mov', 'webm', 'green'] if a.fmt == 'all' else a.fmt.split(',')
raw = ['-f', 'rawvideo', '-pix_fmt', 'bgra', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']
enc = {'mov': ['-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', '-alpha_bits', '8', '-qscale:v', '11', '-vendor', 'apl0', f'{name}_overlay.mov'],
       'webm': ['-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '0', '-crf', '30', '-row-mt', '1', '-deadline', 'good', '-cpu-used', '4', '-auto-alt-ref', '0', f'{name}_overlay.webm'],
       'green': ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'fast', f'{name}_overlay_green.mp4']}
procs = {}
for f in fmts:
    procs[f] = subprocess.Popen([ffmpeg_exe(), '-v', 'error', '-y'] + raw + enc[f][:-1] + [os.path.join(out, enc[f][-1])], stdin=subprocess.PIPE)
green = np.zeros((H, W, 3), np.float32); green[:] = (0, 255, 0)            # BGR
blank = np.zeros((H, W, 4), np.uint8); styled = set(); cur = None
print(f'투명 레이어 {f0 / FPS:.1f}~{f1 / FPS:.1f}초 ({f1 - f0}프레임) → {out}', flush=True)
for fi in range(f0, f1):
    s = next((s for s in sc if s['f0'] <= fi < s['f1']), None)
    if s is None: img = blank
    else:
        page, t0, errs = web._page(s)
        if s['name'] not in styled: page.add_style_tag(content=HIDE); styled.add(s['name'])
        page.evaluate(web.SEEK, fi / FPS - t0)
        img = cv2.imdecode(np.frombuffer(page.screenshot(type='png', omit_background=True), np.uint8), cv2.IMREAD_UNCHANGED)
        if errs: raise SystemExit(f"{s['name']}.html 오류: {errs}")
    for f, pr in procs.items():
        if f == 'green':
            al = img[:, :, 3:4].astype(np.float32) / 255
            pr.stdin.write(np.dstack([(img[:, :, :3] * al + green * (1 - al)).astype(np.uint8), np.full((H, W), 255, np.uint8)]).tobytes())
        else: pr.stdin.write(img.tobytes())
    if s is not cur: cur = s; print(f"  {s['name'] if s else '(빈 구간)'}  {fi / FPS:.1f}초~", flush=True)
for pr in procs.values(): pr.stdin.close(); pr.wait()
inp = os.path.join(p, 'input'); wav = next((os.path.join(inp, x) for x in os.listdir(inp) if x.startswith('narration.') and not x.endswith('.srt')), None)
if wav: shutil.copy(wav, os.path.join(out, 'narration' + os.path.splitext(wav)[1]))
if os.path.exists(os.path.join(inp, 'narration.srt')): shutil.copy(os.path.join(inp, 'narration.srt'), os.path.join(out, name + '.srt'))
for f in sorted(os.listdir(out)): print(f'  {f}  {os.path.getsize(os.path.join(out, f)) / 1e6:.1f}MB')
