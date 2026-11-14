"""본편에서 세로 쇼츠 만들기 (2026-11-12 담당자: "우리 영상을 쇼츠 1분 내외로 만들어 유입을 올리자").
   python tools/shorts.py <프로젝트> <쇼츠id>      (projects/<프로젝트>/out/shorts/<쇼츠id>.json)

2026-11-14 담당자 규칙 (반드시):
  ① 작은 글씨 최소화 · 큰 글씨 위주  → 윗줄 작은 채널명 없음, 제목 두 줄 104/112px, 자막 94px 굵게 두 줄까지(긴 문장은 나눠 띄움)
  ② 그림·영상 위주                   → 가운데 장면을 1.3배 키움(1080x634, 장면 안 큰 글씨가 잘리지 않는 한도)
  ③ 효과음 적절하게                  → 시작 휙(whoosh) · 화살표 등장 딩(ding) · 끝 화면 쓱(swish) + 고조음(riser)이 처음으로 이어짐
  ④ 엔딩과 인트로가 계속 연결(루프)   → 끝 화면 = 첫 화면과 같은 장면 + 첫 문장으로 이어지는 말("loop": ["…", "…"])
  ⑤ 아래 본편 영상을 누르게           → 마지막 6초와 끝 화면에 노란 화살표 + "본편 보기"가 번쩍이며 아래(관련 영상 자리)를 가리킨다

spec = {"ranges": [[시작초, 끝초], ...],      # 본편(out/<프로젝트>_final.mp4)에서 이어 붙일 구간 (자막 시각 기준)
        "title": ["흰 줄", "노랑 줄"],         # 화면 위 큰 제목 (쇼츠 제목·첫 문장과 같은 말)
        "loop": ["끝 화면 흰 줄", "노랑 줄"],   # 첫 문장으로 이어지는 말 (예: "그래서 요즘 은퇴한 분들은" / "이렇게 말합니다")
        "end_sec": 3.0}
화면 1080x1920: 위 제목(y 110~360) · 가운데 장면(y 390~1024, 본편 아래 자막 띠는 잘라 냄) · 큰 자막(y 1060~) · 화살표(y 1410~, 왼쪽 아래 관련 영상 자리).
음량 -14 LUFS."""
import os, sys, re, json, subprocess, pathlib
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name, sid = sys.argv[1], sys.argv[2]
P = os.path.join(KIT, 'projects', name); OUT = os.path.join(P, 'out', 'shorts'); os.makedirs(OUT, exist_ok=True)
S = json.load(open(os.path.join(OUT, sid + '.json'), encoding='utf-8'))
FINAL = os.path.join(P, 'out', f'{name}_final.mp4'); TMP = os.path.join(OUT, '_' + sid); os.makedirs(TMP, exist_ok=True)
FONTS = os.path.join(KIT, 'fonts'); SFX = os.path.join(KIT, 'brand', 'sfx')
def run(cmd): subprocess.run(cmd, check=True)
def dur(f): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)

# 1) 구간 자르기 (본편 영상+소리) → 이어 붙이기
parts = []
for i, (a, b) in enumerate(S['ranges']):
    f = os.path.join(TMP, f'p{i}.mp4'); parts.append(f)
    run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{a:.3f}', '-i', FINAL, '-t', f'{b - a:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
         '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', f])
lst = os.path.join(TMP, 'list.txt'); open(lst, 'w').write(''.join(f"file '{f}'\n" for f in parts))
body = os.path.join(TMP, 'body.mov'); run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', body])
BD = dur(body)

# 2) 큰 자막(ASS): 두 줄까지. 긴 문장은 글자 수에 비례해 시간을 나눠 차례로 띄운다
def srt(p):
    out = []
    for b in re.split(r'\n\s*\n', open(p, encoding='utf-8-sig').read().strip()):
        l = b.strip().split('\n')
        if len(l) < 3: continue
        t = [sum(float(x) * m for x, m in zip(s.replace(',', '.').split(':'), (3600, 60, 1))) for s in l[1].split(' --> ')]
        out.append((t[0], t[1], ' '.join(l[2:])))
    return out
CUES = srt(os.path.join(P, 'input', 'narration.srt'))
W = 11                                       # 한 줄 글자 수 (94px 굵은 글꼴)
def lines(t):
    out = ['']
    for x in t.split(' '):
        if len(out[-1]) + len(x) + 1 > W and out[-1]: out.append(x)
        else: out[-1] = (out[-1] + ' ' + x).strip()
    return out
ev = []; off = 0.0
for a, b in S['ranges']:
    for s, e, t in CUES:
        if e <= a + 0.05 or s >= b - 0.05: continue
        s2, e2 = max(s, a) - a + off, min(e, b) - a + off
        L = lines(t.rstrip('.')); chunks = [L[i:i + 2] for i in range(0, len(L), 2)]
        tot = sum(len(''.join(c)) for c in chunks); cur = s2
        for c in chunks:
            d = (e2 - s2) * len(''.join(c)) / max(1, tot); ev.append((cur, cur + d, '\\N'.join(c))); cur += d
    off += b - a
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); return f'{h}:{m:02d}:{x % 60:05.2f}'
ass = os.path.join(TMP, 'sub.ass')
open(ass, 'w', encoding='utf-8').write(
    '[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n[V4+ Styles]\n'
    'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
    'Style: S,Gmarket Sans TTF Bold,94,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,-1,0,1,9,3,8,50,50,1060,1\n\n'
    '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
    + ''.join(f'Dialogue: 0,{ts(s)},{ts(e)},S,,0,0,0,,{t}\n' for s, e, t in ev))

# 3) 그림 (HTML → PNG): 제목 · 끝 화면 이어지는 말 · 화살표
CSS = f"""@font-face {{ font-family: GM; src: url('file://{FONTS}/GmarketSansTTFBold.ttf'); }}
* {{ margin: 0; box-sizing: border-box; }} body {{ width: 1080px; height: 1920px; position: relative; font-family: GM; background: transparent; overflow: hidden; }}
.c {{ position: absolute; left: 0; right: 0; text-align: center; white-space: nowrap; line-height: 1.1; letter-spacing: -2px; -webkit-text-stroke: 11px #000; paint-order: stroke fill; }}
.w {{ color: #fff; }} .y {{ color: #ffe500; }}"""
FIT = "<script>document.fonts.ready.then(()=>document.querySelectorAll('.c').forEach(e=>{const t=e.firstElementChild;if(!t)return;let s=parseFloat(getComputedStyle(e).fontSize);while(t.offsetWidth>1020&&s>44){s-=2;e.style.fontSize=s+'px'}}));</script>"
def page(b): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}{FIT}</body></html>'
t1, t2 = S['title']; l1, l2 = S.get('loop', ['', ''])
HTML = {
 'title': page(f'<div class="c w" style="top:110px; font-size:104px"><span>{t1}</span></div><div class="c y" style="top:235px; font-size:112px"><span>{t2}</span></div>'),
 'loop': page(f'<div style="position:absolute; left:0; right:0; top:1040px; height:260px; background:linear-gradient(180deg, transparent, rgba(0,0,0,.75) 25%, rgba(0,0,0,.75) 75%, transparent)"></div>'
              f'<div class="c w" style="top:1062px; font-size:90px"><span>{l1}</span></div><div class="c y" style="top:1170px; font-size:100px"><span>{l2}</span></div>'),
 'arrow': page('<div style="position:absolute; left:40px; top:0; width:520px; height:200px; display:flex; align-items:center; gap:18px">'
               '<svg width="150" height="190" viewBox="0 0 100 130" style="filter: drop-shadow(0 0 14px #ffe500) drop-shadow(0 6px 10px rgba(0,0,0,.8))">'
               '<path d="M30 0 H70 V70 H96 L50 128 L4 70 H30 Z" fill="#ffe500" stroke="#000" stroke-width="6" stroke-linejoin="round"/></svg>'
               '<div style="font-size:66px; color:#fff; background:#e3262f; border:6px solid #fff; border-radius:22px; padding:16px 26px 8px; white-space:nowrap; box-shadow:0 8px 24px rgba(0,0,0,.6)">본편 보기</div></div>'),
}
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
    for k, h in HTML.items():
        f = pathlib.Path(TMP, k + '.html'); f.write_text(h, encoding='utf-8'); pg.goto(f.as_uri()); pg.wait_for_timeout(900)
        pg.screenshot(path=os.path.join(TMP, k + '.png'), omit_background=True)
    br.close()
run(['ffmpeg', '-loglevel', 'error', '-y', '-i', os.path.join(TMP, 'arrow.png'), '-vf', 'crop=1080:220:0:0', os.path.join(TMP, 'arrow_c.png')])

# 4) 세로 합성 공통 그래프: 흐린 배경 + 가운데 큰 장면(1.6배, 아래 자막 띠 잘라 냄) + 제목
BASE = ('[0:v]crop=1920:880:0:0,split[a][b];'
        '[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,eq=brightness=-0.3[bg];'
        '[b]crop=1500:880:210:0,scale=1080:634[fg];'
        '[bg][fg]overlay=0:390[v1];[v1][1:v]overlay=0:0[v2]')
ARW_Y = "1410+16*abs(sin(t*7))"                                        # 통통 튀며
BLINK = "lt(mod(t,0.55),0.36)"                                          # 번쩍이며
tA = max(0.0, BD - 6.0)
assd = ass.replace(':', r'\:')
vert = os.path.join(TMP, 'vert.mp4')
run(['ffmpeg', '-loglevel', 'error', '-y', '-i', body, '-i', os.path.join(TMP, 'title.png'), '-loop', '1', '-i', os.path.join(TMP, 'arrow_c.png'),
     '-filter_complex', BASE + f";[v2]subtitles='{assd}':fontsdir='{FONTS}'[v3];"
     f"[v3][2:v]overlay=0:'{ARW_Y}':enable='gte(t,{tA:.2f})*{BLINK}':shortest=1[v]",
     '-map', '[v]', '-map', '0:a', '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-c:a', 'pcm_s16le', '-t', f'{BD:.3f}', vert])

# 5) 끝 화면 = 첫 화면과 같은 장면 + 첫 문장으로 이어지는 말 + 화살표 (루프)
es = float(S.get('end_sec', 3.0)); first = os.path.join(TMP, 'first.png'); endv = os.path.join(TMP, 'end.mp4')
run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', '0.15', '-i', body, '-frames:v', '1', first])
run(['ffmpeg', '-loglevel', 'error', '-y', '-loop', '1', '-t', f'{es}', '-i', first, '-i', os.path.join(TMP, 'title.png'), '-i', os.path.join(TMP, 'loop.png'),
     '-loop', '1', '-i', os.path.join(TMP, 'arrow_c.png'), '-i', os.path.join(SFX, 'swish.wav'), '-i', os.path.join(SFX, 'riser.wav'),
     '-filter_complex', BASE + f";[v2][2:v]overlay=0:0[v3];[v3][3:v]overlay=0:'{ARW_Y}':enable='{BLINK}':shortest=1,trim=0:{es},setpts=PTS-STARTPTS[v];"
     f"[4:a]volume=-4dB,apad[s1];[5:a]volume=-9dB,adelay={int((es - 1.6) * 1000)}|{int((es - 1.6) * 1000)},apad[s2];"
     f"[s1][s2]amix=inputs=2:normalize=0,atrim=0:{es},aformat=sample_rates=48000:channel_layouts=stereo[a]",
     '-map', '[v]', '-map', '[a]', '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', endv])

# 6) 이어 붙이기 + 효과음(시작 휙 · 화살표 딩) + 음량 -14 LUFS
out = os.path.join(OUT, f'{name}_쇼츠_{sid}.mp4'); ta = int(tA * 1000)
run(['ffmpeg', '-loglevel', 'error', '-y', '-i', vert, '-i', endv, '-i', os.path.join(SFX, 'whoosh.wav'), '-i', os.path.join(SFX, 'ding.wav'),
     '-filter_complex', '[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a0];'
     f'[2:a]volume=-6dB[w];[3:a]volume=-6dB,adelay={ta}|{ta}[d];[a0][w][d]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[an]',
     '-map', '[v]', '-map', '[an]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
print(f'쇼츠 완성: {out} · {dur(out):.1f}초 · 자막 {len(ev)}줄 · 화살표 {tA:.1f}초부터')
