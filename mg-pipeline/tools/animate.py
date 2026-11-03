"""배경 그림 → 짧은 영상 (fal 이미지→영상 모델) → 장면 길이만큼 앞뒤로 이어 붙인 반복 영상.
   python tools/animate.py <이름> [--yes] [id ...]

projects/<이름>/motion.json
  {"model": "fal-ai/minimax/hailuo-02/standard/image-to-video", "resolution": "512P", "duration": "6", "loop_sec": 15, "extend": "slow",
   "style": "모든 프롬프트 뒤에 붙는 움직임 지시",
   "clips": [{"id": "bg_school_winter", "prompt": "students slowly walking away down the hallway"}, ...]}
입력 그림은 assets/<id>.png, 결과는 captures/<id>.mp4 (1920x1080, 30fps). 길이는 슬로우 모션으로 loop_sec 초까지(최대 2.5배) 늘린다.
클립마다 "sec"(목표 길이), "extend": "pingpong"(빠른 움직임 영상만 되감기 반복)을 줄 수 있다.
이미 있는 것은 건너뛴다. --yes 없이는 목록과 예상 비용만 보여 준다 (유료).
"""
import os, sys, io, json, time, base64, subprocess, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, KIT)
import mgp
from PIL import Image

PRICE = {'512P': 0.017, '768P': 0.045}          # 달러/초 (Hailuo-02 Standard, 2026-10 fal 가격표)

def _req(url, key, body=None):
    req = urllib.request.Request(url, json.dumps(body).encode() if body is not None else None, {'Authorization': 'Key ' + key, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.load(r)

def _uri(path):
    buf = io.BytesIO(); Image.open(path).convert('RGB').save(buf, 'JPEG', quality=92)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

def make(c, spec, proj, key, ff):
    raw = os.path.join(proj, 'captures', '_raw', c['id'] + '.mp4'); out = os.path.join(proj, 'captures', c['id'] + '.mp4')
    if not os.path.exists(raw):
        body = {'prompt': ', '.join(x for x in (c['prompt'], spec.get('style', '')) if x), 'image_url': _uri(os.path.join(proj, 'assets', c['id'] + '.png')),
                'duration': spec.get('duration', '6'), 'resolution': spec.get('resolution', '512P'), 'prompt_optimizer': False}
        try:
            sub = _req('https://queue.fal.run/' + spec['model'], key, body); t_end = time.time() + 900
            while _req(sub['status_url'], key).get('status') != 'COMPLETED':
                if time.time() > t_end: raise RuntimeError('15분 안에 끝나지 않았습니다.')
                time.sleep(4)
            res = _req(sub['response_url'], key)
        except urllib.error.HTTPError as e: raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
        with urllib.request.urlopen(res['video']['url'], timeout=300) as r: open(raw, 'wb').write(r.read())
    # 길이 늘리기: 기본은 슬로우 모션(프레임 보간, 최대 2.5배). 되감기 반복은 빠른 움직임 영상에만 ("extend": "pingpong")
    mode = c.get('extend', spec.get('extend', 'slow')); loop = float(c.get('sec', spec.get('loop_sec', 15)))
    if mode == 'pingpong':
        vf = '[0:v]fps=30,scale=1920:1080:flags=lanczos,setsar=1,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,loop=-1:size=32767,trim=0:%g,setpts=N/30/TB[v]' % loop
    else:
        dur = float(subprocess.run([ff, '-i', raw], capture_output=True, text=True).stderr.split('Duration: ')[1].split(',')[0].split(':')[-1])
        k = min(2.5, max(1.0, loop / dur))
        if k <= 1.01:   # 이미 충분히 길다 (스톡 영상 등): 크기만 맞추고 목표 길이로 자른다
            vf = '[0:v]fps=30,scale=1920:1080:flags=lanczos:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,trim=0:%g,setpts=PTS-STARTPTS[v]' % loop
        else:
            vf = '[0:v]setpts=%.4f*PTS,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1,scale=1920:1080:flags=lanczos,setsar=1[v]' % k
    subprocess.run([ff, '-v', 'error', '-y', '-i', raw, '-filter_complex', vf,
                    '-map', '[v]', '-an', '-c:v', 'libx264', '-crf', '20', '-preset', 'fast', '-pix_fmt', 'yuv420p', out], check=True)
    return c['id']

def main():
    a = sys.argv[1:]; yes = '--yes' in a; a = [x for x in a if x != '--yes']
    mgp.load_env(); proj = mgp.use(a[0]); only = set(a[1:])
    from mg import ffmpeg_exe
    spec = json.load(open(os.path.join(proj, 'motion.json'), encoding='utf-8'))
    todo = [c for c in spec['clips'] if (not only or c['id'] in only) and not os.path.exists(os.path.join(proj, 'captures', c['id'] + '.mp4'))]
    sec = float(spec.get('duration', '6')); cost = len(todo) * sec * PRICE.get(spec.get('resolution', '512P'), 0.05)
    for c in todo: print(f"  {c['id']:22s} {c['prompt'][:70]}")
    print(f'{len(todo)}개 × {sec:g}초 · {spec.get("resolution", "512P")} · 예상 약 ${cost:.2f}')
    if not yes: print('유료입니다. 확인 후 --yes 를 붙여 실행하세요.'); return
    key = os.environ.get('FAL_KEY') or os.environ.get('FAL_API_KEY')
    if not key: raise SystemExit('.env 에 FAL_KEY 가 없습니다.')
    os.makedirs(os.path.join(proj, 'captures', '_raw'), exist_ok=True); ff = ffmpeg_exe(); bad = []
    def run(c):
        try: print('  완료', make(c, spec, proj, key, ff), flush=True)
        except Exception as e: bad.append(c['id']); print(f"  실패 {c['id']}: {e}", flush=True)
    with ThreadPoolExecutor(4) as ex: list(ex.map(run, todo))
    print(f'성공 {len(todo) - len(bad)}개' + (f', 실패 {len(bad)}개: {bad} → 같은 명령을 다시 실행하면 실패한 것만 다시 시도합니다.' if bad else ''))

if __name__ == '__main__': main()
