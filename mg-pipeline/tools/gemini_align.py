"""VREW 자막 시각이 엉망일 때: Gemini 받아쓰기(구절별 시작 초) → 대본 글자에 시각 매핑 → 쉼 위치에 맞춰 자막 생성.
   python gemini_align.py <프로젝트 폴더>   (input/_src/vrew.mp3, input/script.txt → input/narration.srt)"""
import os, re, sys, json, base64, difflib, subprocess, urllib.request, urllib.error
P = os.path.abspath(sys.argv[1]); KIT = os.path.dirname(os.path.dirname(P)); sys.path.insert(0, KIT)
import mgp; mgp.load_env(); KEY = os.environ['GEMINI_API_KEY']
AUD = os.path.join(P, 'input', '_src', 'vrew.mp3'); TMP = os.path.join(P, 'input', '_galign'); os.makedirs(TMP, exist_ok=True)
DUR = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', AUD], capture_output=True, text=True).stdout)
r = subprocess.run(['ffmpeg', '-v', 'info', '-i', AUD, '-af', 'silencedetect=noise=-35dB:d=0.2', '-f', 'null', '-'], capture_output=True, text=True).stderr
SS = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; SE = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = list(zip(SS, SE))
# 1) 약 60초 조각 (쉼 가운데서 자른다)
cuts = [0.0]
while cuts[-1] + 75 < DUR:
    want = cuts[-1] + 60; cand = [(a + b) / 2 for a, b in SIL if want - 12 < (a + b) / 2 < want + 12]
    cuts.append(min(cand, key=lambda m: abs(m - want)) if cand else want)
cuts.append(DUR)
ASK = ('이 한국어 음성을 들리는 그대로 받아 적으세요. 문장이나 쉼표로 끊기는 구절마다 줄을 바꾸고, 각 줄 맨 앞에 그 구절이 시작되는 시각을 '
       '이 음성 파일 시작 기준 초 단위(소수점 한 자리)로 [12.3] 처럼 적으세요. 숫자는 들리는 대로 한글로 적고, 다른 설명은 쓰지 마세요.')
LINES = []
for k in range(len(cuts) - 1):
    t0, t1 = cuts[k], cuts[k + 1]; mp3 = os.path.join(TMP, 'g%02d.mp3' % k); cache = mp3 + '.txt'
    if not os.path.exists(cache):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(t0), '-t', str(t1 - t0), '-i', AUD, '-ac', '1', '-b:a', '64k', mp3], check=True)
        body = {'contents': [{'parts': [{'text': ASK}, {'inline_data': {'mime_type': 'audio/mp3', 'data': base64.b64encode(open(mp3, 'rb').read()).decode()}}]}], 'generationConfig': {'temperature': 0}}
        txt = ''
        for model in ('gemini-flash-latest', 'gemini-3.8-flash', 'gemini-flash-latest'):
            try:
                req = urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent', json.dumps(body).encode(), {'Content-Type': 'application/json', 'x-goog-api-key': KEY})
                rr = json.load(urllib.request.urlopen(req, timeout=300)); txt = ''.join(p.get('text', '') for p in rr['candidates'][0]['content']['parts']).strip()
                if txt: break
            except Exception as e: print('  실패', model, str(e)[:120])
        open(cache, 'w', encoding='utf-8').write(txt)
    for ln in open(cache, encoding='utf-8').read().splitlines():
        m = re.match(r'\s*\[(\d+(?:\.\d+)?)\]\s*(.+)', ln)
        if m: LINES.append((t0 + float(m.group(1)), m.group(2)))
    print(f'조각 {k + 1}/{len(cuts) - 1} {t0:.0f}~{t1:.0f}초 · 누적 구절 {len(LINES)}', flush=True)
LINES.sort()
# 2) 받아쓴 글자마다 시각
H = lambda s: re.sub(r'[^가-힣]', '', s)
tc, tt = [], []
for i, (t, s) in enumerate(LINES):
    nxt = LINES[i + 1][0] if i + 1 < len(LINES) else DUR; h = H(s)
    for j, ch in enumerate(h): tc.append(ch); tt.append(t + (nxt - t) * j / max(1, len(h)))
TS = ''.join(tc)
# 3) 대본 → 자막 덩어리 (문장 단위, 긴 문장은 쉼표에서 나눔)
S = open(os.path.join(P, 'input', 'script.txt'), encoding='utf-8').read()
S = '\n'.join(l for l in S.splitlines() if not l.startswith('#')).strip()
sents = [x.strip() for x in re.split(r'(?<=[.?!])\s+', re.sub(r'\s+', ' ', S)) if x.strip()]
cues = []
for s in sents:
    if len(s) > 48 and ',' in s:
        parts = s.split(', '); best = min(range(1, len(parts)), key=lambda k: abs(len(', '.join(parts[:k])) - len(s) / 2))
        cues += [', '.join(parts[:best]) + ',', ', '.join(parts[best:])]
    else: cues.append(s)
SH = ''.join(H(c) for c in cues)
sm = difflib.SequenceMatcher(None, SH, TS, autojunk=False); blocks = [b for b in sm.get_matching_blocks() if b.size]
def t_of(pos):
    for a, b, n in blocks:
        if a <= pos < a + n: return tt[b + pos - a]
    prev = [b for b in blocks if b.a + b.size <= pos]; nxt = [b for b in blocks if b.a > pos]
    if prev and nxt:
        pa, pb = prev[-1].a + prev[-1].size - 1, tt[prev[-1].b + prev[-1].size - 1]; na, nb = nxt[0].a, tt[nxt[0].b]
        return pb + (nb - pb) * (pos - pa) / max(1, na - pa)
    return tt[0] if nxt else tt[-1]
starts = []; pos = 0
for c in cues: starts.append(t_of(pos)); pos += len(H(c))
# 4) 쉼 끝에 맞추기 (0.8초 안), 순서 유지
fixed = []
for i, t in enumerate(starts):
    near = [e for s, e in SIL if abs(e - t) < 0.8]
    t2 = min(near, key=lambda e: abs(e - t)) if near else t
    if fixed and t2 <= fixed[-1] + 0.4: t2 = max(t, fixed[-1] + 0.4)
    fixed.append(round(t2 - 0.05, 3) if i else 0.0)
def fmt(t): h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.', ',')
out = []
for i, c in enumerate(cues):
    a = fixed[i]; b = fixed[i + 1] if i + 1 < len(cues) else DUR
    out.append(f'{i + 1}\n{fmt(a)} --> {fmt(b)}\n{c}')
open(os.path.join(P, 'input', 'narration.srt'), 'w', encoding='utf-8').write('\n\n'.join(out) + '\n')
mr = sum(b.size for b in blocks) / max(1, len(SH))
print(f'자막 {len(cues)}개 · 대본 글자 일치율 {mr:.0%} · 받아쓴 구절 {len(LINES)}개')
