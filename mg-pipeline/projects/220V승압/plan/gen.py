"""장면 계획(plan/plan.py) → scenes/sNN.html 생성.   python plan/gen.py
계획 파일을 scenes/ 밖에 두는 이유: scenes/_* 파일은 렌더 도구가 "모든 장면의 공용 코드"로 보아,
고칠 때마다 전 장면을 다시 렌더한다. 여기 두면 내용이 바뀐 장면만 다시 렌더된다.
장면은 대본 문구로 잡는다: 'from' 에 그 장면이 시작되는 자막의 문구 일부를 적으면 자막 번호를 찾아 준다.
요소의 등장 시각도 문구로: '계급을' (그 낱말이 나오는 자막에서 그 낱말) / '+0.2' (장면 시작 뒤 초).
"""
import os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); SC = os.path.join(ROOT, 'scenes')

def read_srt(p):
    cues = []
    for block in re.split(r'\n\s*\n', open(p, encoding='utf-8-sig').read().strip()):
        ln = block.strip().split('\n')
        if len(ln) >= 3: cues.append(' '.join(ln[2:]).strip())
    return cues
CUES = read_srt(os.path.join(ROOT, 'input', 'narration.srt'))

# 자막을 한 줄로 이어 붙여 찾는다 → 문구가 자막 두 개에 걸쳐 있어도 찾는다
import bisect
JOINED = ''; STARTS = []
for _c in CUES: STARTS.append(len(JOINED)); JOINED += _c + ' '
def cue_at(pos): return bisect.bisect_right(STARTS, pos)
def find(phrase, start=1):
    i = JOINED.find(phrase, STARTS[start - 1])
    if i < 0: raise SystemExit(f'자막에서 "{phrase}" 를 찾지 못했습니다 ({start}번부터).')
    return i
def cue_of(phrase, start=1):
    """phrase 가 시작되는 자막 번호 (start 번부터 찾는다)."""
    return cue_at(find(phrase, start))

class Scene:
    def __init__(self, s, c0, c1):
        self.s, self.c0, self.c1 = s, c0, c1
    def at(self, spec):
        """'+0.3' | '낱말' | '문구:낱말' | 'end-1.0' → kit.js 의 data-at 값 ("자막번호:낱말")."""
        spec = str(spec)
        if spec.startswith('+') or spec.startswith('end'): return spec
        phrase, word = spec.split(':', 1) if ':' in spec else (spec, spec)
        w = word.split(' ')[0]
        i = find(phrase, self.c0); j = JOINED.find(w, i)
        n = cue_at(j)
        if n > self.c1: raise SystemExit(f'"{spec}" 는 이 장면({self.c0}~{self.c1}번, "{self.s["from"]}") 밖의 {n}번 자막입니다.')
        if not any(w in x for x in CUES[n - 1].split(' ')): raise SystemExit(f'{n}번 자막에 "{w}" 가 없습니다: {CUES[n - 1]}')
        return f'{n}:{w}'

def E(t): return html.escape(str(t))
def A(sc, spec, off=None, attr='data-at'):
    s = f'{attr}="{sc.at(spec)}"'
    if off is not None: s += f' data-off{attr[7:]}="{off}"'
    return s

# ---------------- 화면 요소 (모두 sc 를 받아 HTML 조각을 돌려준다) ----------------
def label(text, at='+0.05'):
    return lambda sc: f'<div class="label" {A(sc, at)}>{E(text)}</div>'
def line(text, at, x=None, y=300, cls='head', off=-0.15, center=False, mk=None, mkat=None, size=None, color=None,
         bx=None, bxat=None, st=None, stat=None, ci=None, ciat=None, ul=None, ulat=None):
    """한 줄 슬라이드. 강조는 그 낱말을 적는다 ('!' 를 붙이면 빨강):
       mk 형광펜 · bx 네모 박스 · st 취소선 · ci 동그라미 · ul 밑줄. 각각 ...at 으로 그려지는 시각 (없으면 줄 등장 + 0.4초)."""
    def f(sc):
        body = E(text); roomy = False
        for key, word, wat in (('mk', mk, mkat), ('bx', bx, bxat), ('st', st, stat), ('ci', ci, ciat), ('ul', ul, ulat)):
            if not word: continue
            hot = word.startswith('!'); m = word.lstrip('!')
            if E(m) not in body: raise SystemExit(f'"{text}" 안에 강조할 "{m}" 이 없습니다.')
            body = body.replace(E(m), f'<span class="{key}{" hot" if hot else ""}" {A(sc, wat or at, None if wat else 0.4)}>{E(m)}</span>', 1)
            roomy = roomy or key in ('bx', 'ci')
        pos = 'left:0; right:0; text-align:center;' if center or x is None else f'left:{x}px;'
        stl = f'{pos} top:{y}px;' + (f' font-size:{size}px;' if size else '') + (f' color:{color};' if color else '')
        return f'<div class="line {cls}{" roomy" if roomy else ""}" style="{stl}"><span class="in" {A(sc, at, off)}>{body}</span></div>'
    return f
def stamp(text, at, x=1250, y=560, size=110, rot=-8):
    """도장: 비스듬히 쾅 ('반전', '과장', '오류' 같은 한두 낱말)."""
    return lambda sc: f'<div class="stamp" {A(sc, at)} style="left:{x}px; top:{y}px; font-size:{size}px; --rot:{rot}deg">{E(text)}</div>'
def chip(text, at, x, y, size=46, dark=False):
    """키워드 태그 (보고서 칩)."""
    return lambda sc: f'<div class="chip{" dark" if dark else ""}" {A(sc, at)} style="left:{x}px; top:{y}px; font-size:{size}px">{E(text)}</div>'
def flow(parts, y=420, size=72, color=None):
    """A ▶ B ▶ C : parts = [(글자, 시각), ...] 차례로 나타난다."""
    def f(sc):
        out = []
        for i, (t, at) in enumerate(parts):
            if i: out.append(f'<i {A(sc, at, -0.12)}></i>')
            out.append(f'<span {A(sc, at)}>{E(t)}</span>')
        return f'<div class="flow say" style="top:{y}px; font-size:{size}px;' + (f' color:{color};' if color else '') + '">' + ''.join(out) + '</div>'
    return f
def rulebar(at, x=560, y=520, w=800):
    return lambda sc: f'<div class="rulebar" {A(sc, at)} style="left:{x}px; top:{y}px; width:{w}px"></div>'
def big(text, at, y=330, size=220, color=None, num=None, fmt='comma', suffix='', prefix='', dur=1.2, center=True, x=None, off=-0.1):
    """큰 숫자·낱말. num 을 주면 0에서 그 값까지 올라간다."""
    def f(sc):
        inner = (f'{E(prefix)}<span class="num" data-to="{num}" data-fmt="{fmt}" {A(sc, at, off)} data-dur="{dur}">0</span>{E(suffix)}' if num is not None else E(text))
        pos = 'left:0; right:0; text-align:center;' if center and x is None else f'left:{x}px;'
        st = f'{pos} top:{y}px; font-size:{size}px;' + (f' color:{color};' if color else '')
        return f'<div class="line big" style="{st}"><span class="in" {A(sc, at, off)}>{inner}</span></div>'
    return f
def glow(text, at, y=540, size=100, off=-0.15):
    return lambda sc: f'<div class="glowbox slam" {A(sc, at, off)} style="top:{y}px; font-size:{size}px">{E(text)}</div>'
def card(k, v, at, x, y, w=560, h=300, vat=None, hot=False, num=None, suffix='', vsize=None):
    def f(sc):
        if num is not None: val = f'<span class="num" data-to="{num}" data-fmt="comma" {A(sc, vat or at)} data-dur="1.1">0</span>{E(suffix)}'
        else: val = E(v)
        vcls = 'v slam' if vat else 'v'
        vst = ' style="' + ('color:var(--hot);' if hot else '') + (f'font-size:{vsize}px;' if vsize else '') + '"'
        va = f' {A(sc, vat)}' if vat and num is None else ''
        return (f'<div class="card rise" {A(sc, at)} style="left:{x}px; top:{y}px; width:{w}px; height:{h}px">'
                f'<div class="k">{E(k)}</div><div class="{vcls}"{va}{vst}>{val}</div></div>')
    return f
def ranks(at, now=None, nowat=None, opened=None, top=300):
    """순위 카드 5장. opened = {순위: (이름, 열리는 시각 또는 None=처음부터)}, now = 지금 다루는 순위(불 켜짐)."""
    opened = opened or {}
    def f(sc):
        out = [f'<div class="ranks" style="top:{top}px">']
        for i, r in enumerate([5, 4, 3, 2, 1]):
            cls = 'rk'; extra = ''
            if r in opened:
                name, oat = opened[r]
                cls += ' open'; extra += f' {A(sc, oat, None, "data-at2")}' if oat else ' style="--t2:0s"'
            if r == now: cls += ' now'; extra += f' {A(sc, nowat or at, None, "data-at3")}'
            body = f'<div class="n">{r}위</div><div class="q">?</div>' + (f'<div class="a">{E(opened[r][0])}</div>' if r in opened else '')
            out.append(f'<div class="{cls}" {A(sc, at, round(i * 0.12, 2))}{extra}>{body}</div>')
        return ''.join(out) + '</div>'
    return f
def bars(rows, top=330):
    """rows = [(이름, 비율0~1, 값 글자, 시각, dim)]"""
    def f(sc):
        out = [f'<div class="bars" style="top:{top}px">']
        for name, w, val, at, dim in rows:
            out.append(f'<div class="bar{" dim" if dim else ""}" style="--w:{w}" {A(sc, at)}><b>{E(name)}</b><i></i><em>{E(val)}</em></div>')
        return ''.join(out) + '</div>'
    return f
def meter(total, lit, at, fillat=None, y=420, cap=None, capat=None):
    """칸 total 개 중 lit 칸(소수면 마지막 칸은 일부)이 차례로 차오른다. cap = 아래 설명 한 줄."""
    def f(sc):
        out = [f'<div class="meter" style="top:{y}px">']
        for i in range(total):
            fr = max(0.0, min(1.0, lit - i))
            out.append(f'<u style="--f:{fr:.3f}" {A(sc, at, round(i * 0.05, 2))} {A(sc, fillat or at, round(0.4 + i * 0.12, 2), "data-at2")}></u>')
        out.append('</div>')
        if cap: out.append(line(cap, capat or fillat or at, y=y + 200, cls='say', center=True)(sc))
        return ''.join(out)
    return f
def group(until, *items):
    """until 시각에 함께 사라지는 묶음."""
    return lambda sc: f'<div class="abs exit" {A(sc, until, None, "data-until")} style="inset:0">' + ''.join(i(sc) for i in items) + '</div>'
def raw(s): return lambda sc: s

PAGE = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="cues" content="{c0}-{c1}">
<link rel="stylesheet" href="../../../engine/web/kit.css"><link rel="stylesheet" href="../../../brand/web/channel.css">
</head><body data-bg="none">
<div class="stage">{bg}<div class="shade"></div><div class="cam">
{items}
</div></div>
<script src="_timing.js"></script><script src="../../../engine/web/kit.js"></script><script src="../../../brand/web/channel.js"></script>
</body></html>
"""

KB = [(0, 0, -50, -24, 1.06, 1.2), (-60, 10, 50, -10, 1.14, 1.14), (40, -24, -30, 20, 1.2, 1.07), (0, 36, 0, -36, 1.13, 1.13),
      (50, 20, -40, -20, 1.08, 1.18), (-30, -30, 30, 30, 1.18, 1.1)]   # (시작 x, y, 끝 x, y, 시작 배율, 끝 배율)

def background(sc, bg):
    """bg = 'bg_id' (assets/bg_id.png) | 'v:클립이름' (captures/클립이름.mp4) | None (기본 어두운 바탕). 두 장이면 [(id, 시각), ...] 로 바꿔 끼운다."""
    if not bg: return '<div class="plain"></div>'
    if isinstance(bg, str): bg = [(bg, None)]
    out = []
    for b, at in bg:
        swap = f' kb swap" {A(sc, at)}' if at else ' kb"'
        if not b.startswith('v:') and os.path.exists(os.path.join(ROOT, 'captures', b + '.mp4')): b = 'v:' + b   # 움직이는 배경이 있으면 그것을 쓴다 (tools/animate.py)
        name = b[2:] if b.startswith('v:') else b
        base = '--blur:1px; --dark:.74;' if name.startswith(('il_', 'cl_', 'cr_', 'cm_')) else ('--blur:2.5px; --dark:.6;' if name.startswith('st_') else '')   # 일러스트는 또렷하게, 스톡은 덜 흐리게
        kx0, ky0, kx1, ky1, z0, z1 = KB[(sc.c0 + len(out)) % len(KB)]                  # 장면마다 다른 방향으로 켄번스
        look = f' style="{base} --kx0:{kx0}px; --ky0:{ky0}px; --kx1:{kx1}px; --ky1:{ky1}px; --z0:{z0}; --z1:{z1}"'
        rate = f' data-rate="{sc.s["bgrate"]}"' if sc.s.get('bgrate') else ''
        if b.startswith('v:'): out.append(f'<img class="bg vid{swap} data-video="{name}" data-w="1920" data-h="1080"{rate}{look}>')
        else:
            src = f'../assets/{b}.png'
            if not os.path.exists(os.path.join(ROOT, 'assets', b + '.png')): out.append(f'<div class="plain{swap}></div>'); continue
            out.append(f'<img class="bg{swap} src="{src}"{look}>')
    return ''.join(out)

def build(plan):
    starts = []; last = 0                     # 앞 장면보다 뒤에서 찾는다 (같은 문구가 여러 번 나오는 대본)
    for s in plan: n = cue_of(s['from'], last + 1); starts.append(n); last = n
    if starts[0] != 1: raise SystemExit(f'첫 장면은 1번 자막에서 시작해야 합니다 (지금 {starts[0]}번).')
    os.makedirs(SC, exist_ok=True); keep = {f's{i + 1:02d}.html' for i in range(len(plan))}
    for f in os.listdir(SC):
        if re.fullmatch(r's\d+\.html', f) and f not in keep: os.remove(os.path.join(SC, f))
    for i, s in enumerate(plan):
        c0 = starts[i]; c1 = starts[i + 1] - 1 if i + 1 < len(plan) else len(CUES)
        sc = Scene(s, c0, c1)
        page = PAGE.format(c0=c0, c1=c1, bg=background(sc, s.get('bg')), items='\n'.join(it(sc) for it in s.get('items', [])))
        fp = os.path.join(SC, f's{i + 1:02d}.html')
        if not os.path.exists(fp) or open(fp, encoding='utf-8').read() != page: open(fp, 'w', encoding='utf-8').write(page)   # 바뀐 장면만 새로 쓴다
    print(f'장면 {len(plan)}개 생성 (자막 1~{len(CUES)}번)')

if __name__ == '__main__':
    sys.path.insert(0, HERE); from plan import PLAN; build(PLAN)
