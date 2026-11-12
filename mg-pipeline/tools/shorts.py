"""본편에서 세로 쇼츠 만들기 (2026-11-12 담당자: "우리 영상을 쇼츠 1분 내외로 만들어 유입을 올리자").
   python tools/shorts.py <프로젝트> <쇼츠id>      (projects/<프로젝트>/out/shorts/<쇼츠id>.json)

spec = {"ranges": [[시작초, 끝초], ...],          # 본편(out/<프로젝트>_final.mp4) 에서 이어 붙일 구간 (자막 시각 기준)
        "top": "작은 윗줄", "title": ["흰 줄", "노랑 줄"],
        "end": ["끝 화면 흰 줄", "노랑 줄"], "end_bg": "에셋 id", "end_sec": 3.0}
화면 1080x1920: 위 = 제목 · 가운데 = 본편 장면(아래 자막 띠는 잘라 냄) · 그 아래 = 큰 자막 · 뒤 = 같은 장면을 흐리게.
쇼츠 오른쪽 버튼·아래 제목 자리를 피해 자막은 y 1060~1400, 좌우 여백 70/150.
끝 화면: "본편은 관련 영상에서" (쇼츠 '관련 동영상' 링크로 본편을 건다). 음량 -14 LUFS."""
import os, sys, re, json, subprocess, pathlib
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name, sid = sys.argv[1], sys.argv[2]
P = os.path.join(KIT, 'projects', name); OUT = os.path.join(P, 'out', 'shorts'); os.makedirs(OUT, exist_ok=True)
S = json.load(open(os.path.join(OUT, sid + '.json'), encoding='utf-8'))
FINAL = os.path.join(P, 'out', f'{name}_final.mp4'); TMP = os.path.join(OUT, '_' + sid); os.makedirs(TMP, exist_ok=True)
FONTS = os.path.join(KIT, 'fonts')
def run(cmd): subprocess.run(cmd, check=True)

# 1) 구간 자르기 (본편 영상+소리) → 이어 붙이기
parts = []
for i, (a, b) in enumerate(S['ranges']):
    f = os.path.join(TMP, f'p{i}.mp4'); parts.append(f)
    run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{a:.3f}', '-i', FINAL, '-t', f'{b - a:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', f])
lst = os.path.join(TMP, 'list.txt'); open(lst, 'w').write(''.join(f"file '{f}'\n" for f in parts))
body = os.path.join(TMP, 'body.mov'); run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', body])

# 2) 자막(ASS): 본편 자막에서 구간 안의 문장을 새 시각으로
def srt(p):
    out = []
    for b in re.split(r'\n\s*\n', open(p, encoding='utf-8-sig').read().strip()):
        l = b.strip().split('\n')
        if len(l) < 3: continue
        t = [sum(float(x) * m for x, m in zip(s.replace(',', '.').split(':'), (3600, 60, 1))) for s in l[1].split(' --> ')]
        out.append((t[0], t[1], ' '.join(l[2:])))
    return out
CUES = srt(os.path.join(P, 'input', 'narration.srt'))
def wrap(t, n=13):
    w = t.split(' '); lines = ['']
    for x in w:
        if len(lines[-1]) + len(x) + 1 > n and lines[-1]: lines.append(x)
        else: lines[-1] = (lines[-1] + ' ' + x).strip()
    return '\\N'.join(lines[:3])
ev = []; off = 0.0
for a, b in S['ranges']:
    for s, e, t in CUES:
        if e <= a + 0.05 or s >= b - 0.05: continue
        s2, e2 = max(s, a) - a + off, min(e, b) - a + off
        ev.append((s2, e2, wrap(t.rstrip('.'))))
    off += b - a
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); return f'{h}:{m:02d}:{x % 60:05.2f}'
ass = os.path.join(TMP, 'sub.ass')
open(ass, 'w', encoding='utf-8').write(
    '[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n[V4+ Styles]\n'
    'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
    'Style: S,Gmarket Sans TTF,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,3,8,70,150,1110,1\n\n'
    '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
    + ''.join(f'Dialogue: 0,{ts(s)},{ts(e)},S,,0,0,0,,{t}\n' for s, e, t in ev))

# 3) 제목·끝 화면 그림 (HTML → PNG)
CSS = f"""@font-face {{ font-family: GM; src: url('file://{FONTS}/GmarketSansTTFBold.ttf'); }}
* {{ margin: 0; box-sizing: border-box; }} body {{ width: 1080px; height: 1920px; position: relative; font-family: GM; background: transparent; overflow: hidden; }}
.c {{ position: absolute; left: 0; right: 0; text-align: center; white-space: nowrap; line-height: 1.1; letter-spacing: -2px; -webkit-text-stroke: 10px #000; paint-order: stroke fill; }}
.top {{ top: 120px; font-size: 44px; color: #2bff5a; -webkit-text-stroke: 7px #000; }}
.w {{ color: #fff; }} .y {{ color: #ffe500; }} .ch {{ position: absolute; left: 0; right: 0; text-align: center; font-size: 34px; color: #fff; opacity: .85; }}"""
FIT = "<script>document.fonts.ready.then(()=>document.querySelectorAll('.c').forEach(e=>{const t=e.firstElementChild;let s=parseFloat(getComputedStyle(e).fontSize);while(t.offsetWidth>1000&&s>36){s-=2;e.style.fontSize=s+'px'}}));</script>"
def page(b, bg=''): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body{bg}>{b}{FIT}</body></html>'
t1, t2 = S['title']
title_html = page(f"""<div class="c top"><span>{S.get('top', '')}</span></div>
  <div class="c w" style="top:200px; font-size:92px"><span>{t1}</span></div><div class="c y" style="top:315px; font-size:100px"><span>{t2}</span></div>""")
e1, e2 = S['end']
endbg = os.path.join(P, 'assets', S.get('end_bg', '') + '.png')
end_html = page(f"""<div style="position:absolute; inset:0; background:url('file://{endbg}') center/cover; filter: blur(14px) brightness(.45); transform: scale(1.1)"></div>
  <div class="c w" style="top:640px; font-size:90px"><span>{e1}</span></div><div class="c y" style="top:780px; font-size:96px"><span>{e2}</span></div>
  <div class="c" style="top:1010px; font-size:64px; color:#fff; -webkit-text-stroke:0"><span style="background:#e3262f; padding:22px 40px 14px; border-radius:20px">▶ 본편은 관련 영상에서</span></div>
  <div class="ch" style="top:1220px">지혜호수 경제연구소</div>""", ' style="background:#000"')
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
    for fn, h, transp in (('title', title_html, True), ('end', end_html, False)):
        f = pathlib.Path(TMP, fn + '.html'); f.write_text(h, encoding='utf-8'); pg.goto(f.as_uri()); pg.wait_for_timeout(900)
        pg.screenshot(path=os.path.join(TMP, fn + '.png'), omit_background=transp)
    br.close()

# 4) 세로 합성: 흐린 배경 + 가운데 장면(자막 띠 잘라 냄) + 제목 + 큰 자막
vert = os.path.join(TMP, 'vert.mp4'); assd = ass.replace(':', r'\:')
fc = ('[0:v]crop=1920:880:0:0,split[a][b];'                                   # 본편 아래 자막 띠는 배경에서도 뺀다
      '[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,eq=brightness=-0.28[bg];'
      '[b]crop=1680:880:120:0,scale=1080:566[fg];'                                   # 좌우 160px 잘라 20% 확대 (글자 읽히게)
      '[bg][fg]overlay=0:480[v1];[v1][1:v]overlay=0:0[v2];'
      f"[v2]subtitles='{assd}':fontsdir='{FONTS}'[v]")
run(['ffmpeg', '-loglevel', 'error', '-y', '-i', body, '-i', os.path.join(TMP, 'title.png'), '-filter_complex', fc, '-map', '[v]', '-map', '0:a',
     '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-c:a', 'pcm_s16le', vert])

# 5) 끝 화면 (짧은 음악) 붙이기 + 음량 -14 LUFS
es = float(S.get('end_sec', 3.0)); endv = os.path.join(TMP, 'end.mp4')
sting = os.path.join(P, 'sound', 'music_sting_clue.mp3')
run(['ffmpeg', '-loglevel', 'error', '-y', '-loop', '1', '-t', f'{es}', '-i', os.path.join(TMP, 'end.png'), '-i', sting,
     '-filter_complex', f'[1:a]volume=-8dB,apad,atrim=0:{es},afade=t=out:st={es - 0.8}:d=0.8,aformat=sample_rates=48000:channel_layouts=stereo[a]',
     '-map', '0:v', '-map', '[a]', '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', endv])
out = os.path.join(OUT, f'{name}_쇼츠_{sid}.mp4')
run(['ffmpeg', '-loglevel', 'error', '-y', '-i', vert, '-i', endv, '-filter_complex', '[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a];[a]loudnorm=I=-14:TP=-1.5[an]',
     '-map', '[v]', '-map', '[an]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True).stdout)
print(f'쇼츠 완성: {out} · {d:.1f}초 · 자막 {len(ev)}줄')
