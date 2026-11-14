"""대본 종합 검수 (2026-11-14 · brand/대본_플레이북.md 기준을 한 번에)
   python3 tools/script_check.py <대본.txt> [--title "제목"] [--thumb "썸네일1" "썸네일2" ...]

보는 것: ① 인트로 길이(첫 '전환 문단' 전까지, 300자) ② 전환 문단 유무와 지시형 문구("숨 고르세요") ③ 한 문장에 숫자 2개 이상
④ 글말·번역투 ⑤ 궁금증 고리(여는 말) 개수와 위치 ⑥ 구독 멘트 위치(2분 안) ⑦ 말맛(malmat_check) ⑧ 제목·썸네일·도입부 일치(hook_check, 제목을 주면)."""
import re, sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subdigits import convert
a = sys.argv[1:]; path = a[0]
t = '\n'.join(l for l in open(path, encoding='utf-8').read().splitlines() if not l.startswith('#')).strip()
paras = [p for p in t.split('\n\n') if p.strip()]
CPS = 415 / 60
def at(i): s = i / CPS; return f'{int(s // 60)}:{int(s % 60):02d}'
bad = 0
# ① ② 인트로·전환
BRIDGE = ['하나씩 짚어', '짚어 보겠', '따라가며', '같이 걸으면서', '순서는', '부터 시작합니다', '부터 보겠습니다', '살펴보겠']
bi = next((i for i, p in enumerate(paras[:8]) if any(k in p for k in BRIDGE)), None)
intro = sum(len(p) for p in paras[:bi]) if bi is not None else sum(len(p) for p in paras[:4])
print(f'① 인트로 {intro}자 ≈ {intro / CPS:.0f}초 ' + ('합격' if intro <= 320 else '[넘침] 300자(40초) 이내로 줄인다'))
bad += intro > 320
if bi is None: print('② [없음] 전환 문단(말투로 풀기 + 길 안내 + 궁금증 한 줄)이 인트로 뒤에 없다'); bad += 1
else:
    br = paras[bi]; print(f'② 전환 문단 {len(br)}자 (문단 {bi + 1}, {at(sum(len(p) + 2 for p in paras[:bi]))})')
    for w in ['숨 한번', '숨을 고르', '편하게 들으', '편안하게 들으', '집중해 주']:
        if w in br: print(f'   [지시형] "{w}" → 말로 지시하지 말고 말투로 풀어지게'); bad += 1
# ③ 숫자 두 개 이상 문장
sents = re.split(r'(?<=[.?!])\s+', t); many = []
for s in sents:
    c = convert(s); c = c[0] if isinstance(c, tuple) else c
    c = re.sub(r'\d+\s*(년|월|일|분기|년생|세 이상|살 이상|시)', '', c)        # 날짜·연령 기준은 세지 않는다
    n = len(re.findall(r'\d[\d,.]*', c))
    if n >= 3: many.append((n, s[:60]))
print(f'③ 한 문장에 숫자 3개 이상: {len(many)}곳' + ('' if not many else ' → 앞뒤 문장으로 나눈다'))
for n, s in many[:6]: print(f'   ({n}개) {s}…')
# ④ 글말·번역투
GEUL = ['에 대해 알아보', '라고 할 수 있습니다', '하는 것은', '것으로 보여집니다', '되어지', '에 있어서', '을 천천히', '를 천천히', '함에 있어', '것이 사실입니다', '여겨집니다']
gl = [(w, t.index(w)) for w in GEUL if w in t]
print('④ 글말·번역투: ' + ('없음' if not gl else ', '.join(f'"{w}"({at(i)})' for w, i in gl)))
bad += len(gl)
# ⑤ 궁금증 고리
OPEN = ['열쇠', '함정', '믿으면 안', '안 맞는', '맞지 않는', '왜 ', '무엇이 달랐', '그 답은', '그 전에', '다음 편', '나중에', '마지막에', '처음에 말씀', '궁금']
pos = [i for i in range(0, len(t), 1) if False]
opens = [m.start() for w in OPEN for m in re.finditer(re.escape(w), t)]
mins = len(t) / 415; gaps = sorted(opens)
longest = max([b - a for a, b in zip([0] + gaps, gaps + [len(t)])] or [0])
gi = max(range(len(gaps) + 1), key=lambda k: ([b - a for a, b in zip([0] + gaps, gaps + [len(t)])])[k]) if gaps else 0
start = ([0] + gaps)[gi]
print(f'⑤ 궁금증 여는 말 {len(opens)}번(1분당 {len(opens) / max(mins, .1):.1f}) · 가장 긴 빈 구간 {longest / CPS / 60:.1f}분' + (f' [길다] {at(start)}부터 3분 넘게 새 궁금증이 없다: "{t[start:start + 30]}…"' if longest / CPS > 180 else ''))
# ⑥ 구독 멘트
sub = t.find('구독'); print('⑥ 구독 멘트 ' + (at(sub) + (' 합격' if sub / CPS <= 130 else ' [늦음] 2분 안에') if sub >= 0 else '[없음]'))
# ⑦ 말맛 · ⑧ 일치
print('⑦ 말맛 ─────'); subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'malmat_check.py'), path])
if '--title' in a:
    print('⑧ 제목·썸네일·도입부 ─────'); subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'hook_check.py')] + a)
print(f'\n종합: 고칠 곳 {bad}개 (말맛·일치 결과는 위 각 항목 참고)')
