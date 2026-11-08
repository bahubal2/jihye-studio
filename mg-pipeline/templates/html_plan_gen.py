"""장면 계획(plan/plan.py) → scenes/sNN.html 생성.   python plan/gen.py
계획 파일을 scenes/ 밖에 두는 이유: scenes/_* 파일은 렌더 도구가 "모든 장면의 공용 코드"로 보아,
고칠 때마다 전 장면을 다시 렌더한다. 여기 두면 내용이 바뀐 장면만 다시 렌더된다.
장면은 대본 문구로 잡는다: 'from' 에 그 장면이 시작되는 자막의 문구 일부를 적으면 자막 번호를 찾아 준다.
요소의 등장 시각도 문구로: '계급을' (그 낱말이 나오는 자막에서 그 낱말) / '+0.2' (장면 시작 뒤 초).
"""
import os, re, sys, html, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); SC = os.path.join(ROOT, 'scenes')

def read_srt(p):
    cues = []
    for block in re.split(r'\n\s*\n', open(p, encoding='utf-8-sig').read().strip()):
        ln = block.strip().split('\n')
        if len(ln) >= 3: cues.append(' '.join(ln[2:]).strip())
    return cues
_SRT = os.path.join(ROOT, 'input', 'narration_한글숫자.srt')   # 자막을 숫자로 바꾼 뒤에도 대본 문구(한글 숫자)로 찾는다
if not os.path.exists(_SRT): _SRT = os.path.join(ROOT, 'input', 'narration.srt')
CUES = read_srt(_SRT)
def _ts(x): h, m, r = x.split(':'); return int(h) * 3600 + int(m) * 60 + float(r.replace(',', '.'))
TIMES = [_ts(b.strip().split('\n')[1].split(' --> ')[0]) for b in re.split(r'\n\s*\n', open(_SRT, encoding='utf-8-sig').read().strip()) if len(b.strip().split('\n')) >= 3]
def _total():
    import glob, subprocess
    for f in sorted(glob.glob(os.path.join(ROOT, 'input', 'narration.*'))):
        if f.endswith(('.wav', '.mp3', '.m4a')):
            try: return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)
            except Exception: return 0
    return 0
TOTAL = _total()
try: WORDS = __import__('json').load(open(os.path.join(ROOT, 'input', 'words.json'), encoding='utf-8'))
except Exception: WORDS = []

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
        self.s, self.c0, self.c1 = s, c0, c1; self.sfx = []
    def secs(self, spec, off=0.0):
        """등장 시각(영상 전체 기준 초). 효과음 자리를 잡을 때 쓴다."""
        v = self.at(spec); t0 = TIMES[self.c0 - 1]
        if v.startswith('+'): return t0 + float(v[1:]) + off
        if v.startswith('end'): return None
        n, w = v.split(':', 1); n = int(n); t = TIMES[n - 1]
        if n - 1 < len(WORDS):
            for x in WORDS[n - 1]:
                if w in x['w']: t = x['t0']; break
        return t + off
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
def A(sc, spec, off=None, attr='data-at', sfx=None):
    """sfx = 효과음 종류 (pop, tick, whoosh, swish, hit, stamp, boom). 등장 순간에 자동으로 깔린다 (tools/sfx.py)."""
    if sfx: sc.sfx.append((spec, sfx, off or 0))
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
            body = body.replace(E(m), f'<span class="{key}{" hot" if hot else ""}" {A(sc, wat or at, None if wat else 0.4, sfx=None)}>{E(m)}</span>', 1)
            roomy = roomy or key in ('bx', 'ci')
        pos = 'left:0; right:0; text-align:center;' if center or x is None else f'left:{x}px;'
        stl = f'{pos} top:{y}px;' + (f' font-size:{size}px;' if size else '') + (f' color:{color};' if color else '')
        return f'<div class="line {cls}{" roomy" if roomy else ""}" style="{stl}"><span class="in" {A(sc, at, off)}>{body}</span></div>'
    return f
def stamp(text, at, x=1250, y=560, size=110, rot=-8):
    """도장: 비스듬히 쾅 ('반전', '과장', '오류' 같은 한두 낱말)."""
    return lambda sc: f'<div class="stamp" {A(sc, at, sfx="stamp")} style="left:{x}px; top:{y}px; font-size:{size}px; --rot:{rot}deg">{E(text)}</div>'
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
def cover(at, y=60, w=2100, h=900):
    """가리개 판: 배경이 대본과 덜 맞을 때 가운데를 크게 덮는다. 그 위에 글자를 크게 올린다."""
    return lambda sc: f'<div class="coverbox" {A(sc, at, -0.2)} style="top:{y}px; width:{w}px; height:{h}px"></div>'
def steps(rows, x=150, y=240, gap=120, size=64):
    """PPT식 왼쪽 정렬 목록: rows = [(글자, 시각), ...] 위에서 아래로 차례로, 왼쪽에서 밀려 들어온다."""
    return [line(t, at, x=x, y=y + i * gap, cls='say', size=size) for i, (t, at) in enumerate(rows)]
def rulebar(at, x=560, y=520, w=800):
    return lambda sc: f'<div class="rulebar" {A(sc, at)} style="left:{x}px; top:{y}px; width:{w}px"></div>'
def big(text, at, y=330, size=220, color=None, num=None, fmt='comma', suffix='', prefix='', dur=1.2, center=True, x=None, off=-0.1):
    """큰 숫자·낱말. num 을 주면 0에서 그 값까지 올라간다."""
    def f(sc):
        inner = (f'{E(prefix)}<span class="num" data-to="{num}" data-fmt="{fmt}" {A(sc, at, off)} data-dur="{dur}">0</span>{E(suffix)}' if num is not None else E(text))
        pos = 'left:0; right:0; text-align:center;' if center and x is None else f'left:{x}px;'
        st = f'{pos} top:{y}px; font-size:{size}px;' + (f' color:{color};' if color else '')
        return f'<div class="line big" style="{st}"><span class="in" {A(sc, at, off, sfx="ding" if size >= 160 else "pop")}>{inner}</span></div>'
    return f
def glow(text, at, y=540, size=100, off=-0.15):
    return lambda sc: f'<div class="glowbox slam" {A(sc, at, off, sfx="hit")} style="top:{y}px; font-size:{size}px">{E(text)}</div>'
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
def ranks(at, now=None, nowat=None, opened=None, top=300, n=5, sfx='swish'):
    """순위 카드 n장(5 또는 7). opened = {순위: (이름, 열리는 시각 또는 None=처음부터)}, now = 지금 다루는 순위(불 켜짐).
       2026-10-31 기법 레이더(경제상담소 TOP7): '?' 카드를 줄 세워 두고 하나씩 뒤집어 여는 블라인드 랭킹 → 끝까지 보게 만든다."""
    opened = opened or {}
    def f(sc):
        out = [f'<div class="ranks n{n}" style="top:{top}px">']
        for i, r in enumerate(range(n, 0, -1)):
            cls = 'rk'; extra = ''
            if r in opened:
                name, oat = opened[r]
                cls += ' open'; extra += f' {A(sc, oat, None, "data-at2", sfx=sfx)}' if oat else ' style="--t2:0s"'
            if r == now: cls += ' now'; extra += f' {A(sc, nowat or at, None, "data-at3")}'
            body = f'<div class="n">{r}위</div><div class="q">?</div>' + (f'<div class="a">{E(opened[r][0])}</div>' if r in opened else '')
            out.append(f'<div class="{cls}" {A(sc, at, round(i * 0.08, 2))}{extra}>{body}</div>')
        return ''.join(out) + '</div>'
    return f
def rankbadge(rank, name, at='+0', until=None, still=False):
    """섹션 내내 왼쪽 위에 붙어 있는 순위 배지 ('7위 피죤'). 레이더: 상단 고정 배너로 지금 몇 위인지 늘 보이게."""
    return lambda sc: f'<div class="rankbadge{" still" if still else ""}" {A(sc, at)}{_until(sc, until)}><b>{rank}위</b>{E(name)}</div>'
def punch(text, at, y=430, size=150, sfx='hit'):
    """통념 깨기 펀치: 가운데에 빨간 판으로 쾅 (예: '아닙니다'). 레이더: 통념 칩을 먼저 띄우고 정중앙에 반박을 때려 박는다."""
    return lambda sc: f'<div class="punch" {A(sc, at, -0.05, sfx=sfx)} style="top:{y}px; font-size:{size}px">{E(text)}</div>'
def swapnum(old, new, at, at2, x=None, y=360, size=150, tone='bad'):
    """빨간 사선 + 바뀐 숫자 (레이더: 지식한입 '레드 슬래시 & 스왑'). old 가 먼저 뜨고 at2 에 줄이 그어지며 new 가 쾅."""
    def f(sc):
        pos = 'left:0; right:0; justify-content:center;' if x is None else f'left:{x}px;'
        return (f'<div class="swapnum" style="{pos} top:{y}px; font-size:{size}px" {A(sc, at)} {A(sc, at2, None, "data-at2", sfx="hit")}>'
                f'<span class="old">{E(old)}</span><span class="arr">▶</span><span class="new {tone}">{E(new)}</span></div>')
    return f
def igrid(icon, n, at, lit=0, litat=None, cols=10, x=None, y=380, size=110, tone='bad', half=False, drop=0, dropat=None, sfx='swish'):
    """아이콘 n개 격자 (익숙한 단위로 체감: 열 통 중 세 통 반, 버스 42대). lit = 앞에서부터 색칠할 개수(litat 에), drop = 뒤에서부터 흐려질 개수(dropat 에).
       half=True 면 lit 번째 다음 하나를 반만 칠한다(세 통 반)."""
    svg = icon_svg(icon)
    def f(sc):
        w = cols * size * 1.18; pos = f'left:{(1920 - w) / 2:.0f}px;' if x is None else f'left:{x}px;'
        cells = []
        for i in range(n):
            cls = 'ic'
            if i < lit: cls += ' lit'
            elif half and i == lit: cls += ' lit half'
            if drop and i >= n - drop: cls += ' drop'
            cells.append(f'<i class="{cls}" style="--i:{i}">{svg}</i>')
        at2 = f' {A(sc, litat, None, "data-at2", sfx=sfx)}' if litat else ''
        at3 = f' {A(sc, dropat, None, "data-at3")}' if dropat else ''
        return f'<div class="igrid {tone}" {A(sc, at)}{at2}{at3} style="{pos} top:{y}px; width:{w:.0f}px; --sz:{size}px">' + ''.join(cells) + '</div>'
    return f
def donut(pct, at, label='', x=760, y=250, d=400, tone='bad', cap=None):
    """점유율 도넛: 0 에서 pct% 까지 차오른다. 가운데 큰 숫자, 아래 label."""
    return lambda sc: (f'<div class="donut {tone}" {A(sc, at)} style="left:{x}px; top:{y}px; width:{d}px; height:{d}px; --pct:{pct}">'
                       f'<div class="dv">{pct:g}%</div>' + (f'<div class="dl">{E(label)}</div>' if label else '') + '</div>')
def timeline(points, y=360):
    """가로 연표: points = [(연도, 설명, 켜지는 시각[, 'hot'])] 왼쪽부터 차례로 켜진다. (레이더: 무릎탁경제 타임라인 바)"""
    def f(sc):
        n = len(points); out = [f'<div class="tline" style="top:{y}px">']
        for i, p in enumerate(points):
            yr, tx, at = p[:3]; hot = ' hot' if len(p) > 3 and p[3] else ''
            out.append(f'<div class="tp{hot}" {A(sc, at, sfx="tick")} style="left:{(i + .5) / n * 100:.1f}%"><b>{E(yr)}</b><i></i><span>{E(tx)}</span></div>')
        return ''.join(out) + '</div>'
    return f
def spot(label, at, x, y, w, h, until=None):
    """스포트라이트: (x, y, w, h) 상자만 밝게, 나머지는 어둡게 + 위에 노란 포인터 배지. (레이더: 이상하TV)"""
    return lambda sc: f'<div class="spot" {A(sc, at, sfx="riser")}{_until(sc, until)} style="left:{x}px; top:{y}px; width:{w}px; height:{h}px"><div class="pin">{E(label)}</div></div>'
def hook(html_text, at, y=330, size=200, sfx='hit'):
    """인트로용 초대형 쾅 글자: 3배에서 떨어지며 흔들리고 빨간 밑줄이 그어진다. <em>노랑</em> <strong>빨강</strong> 강조 가능."""
    return lambda sc: f'<div class="hook" {A(sc, at, -0.05, sfx=sfx)} style="top:{y}px; font-size:{size}px">{html_text}</div>'
def flashhit(at):
    """화면 번쩍 (컷 전환 강조)."""
    return lambda sc: f'<div class="flashhit" {A(sc, at, -0.05)}></div>'
def landmap(n, at, fillat, holes=(), holeat=None, cols=20, x=None, y=200, cell=60, sfx='swish'):
    """땅 지도: n칸이 fillat 에 파랗게 차오르고, holes(칸 번호들)는 holeat 에 빨갛게 깜빡인다 ('딱 한 필지만 못 샀다')."""
    def f(sc):
        w = cols * (cell + 6); pos = f'left:{(1920 - w) / 2:.0f}px;' if x is None else f'left:{x}px;'
        cells = ''.join(f'<i class="{"hole" if i in holes else ""}" style="--i:{i}"></i>' for i in range(n))
        h3 = f' {A(sc, holeat, None, "data-at3")}' if holeat else ''
        return (f'<div class="landmap" {A(sc, at)} {A(sc, fillat, None, "data-at2", sfx=sfx)}{h3} style="{pos} top:{y}px; '
                f'grid-template-columns:repeat({cols}, {cell}px); --c:{cell}px">' + cells + '</div>')
    return f
def bars(rows, top=330):
    """rows = [(이름, 비율0~1, 값 글자, 시각, dim)]"""
    def f(sc):
        nw = min(620, max(320, int(max(len(r[0]) for r in rows) * 52)))          # 이름이 길면 이름 칸을 넓힌다
        out = [f'<div class="bars" style="top:{top}px; --nw:{nw}px">']
        for name, w, val, at, dim in rows:
            out.append(f'<div class="bar{" dim" if dim else ""}" style="--w:{w}" {A(sc, at, sfx="swish")}><b>{E(name)}</b><i></i><em>{E(val)}</em></div>')
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
def foreshadow(text, at, label='기억해 두세요', until=None):
    """복선 카드 (레이더 2026-11-03, 경제탐사단): 가운데 크게 뜬 뒤 오른쪽 위 구석으로 줄어 붙어 장면 끝까지 남는다. '이 숫자, 1위에서 다시 나옵니다.'"""
    return lambda sc: (f'<div class="foreshadow" {A(sc, at, -0.05, sfx="ding")}{_until(sc, until)}><b>{E(label)}</b><span>{E(text)}</span></div>')
def flipcard(front, back, at, at2, y=330, size=88):
    """통념 → 현실 뒤집기 카드 (레이더: 경제히어로·경제상담소): at 에 '생각' 면, at2 에 위아래로 뒤집혀 빨간 '현실' 면."""
    return lambda sc: (f'<div class="flipcard" {A(sc, at, sfx="pop")} {A(sc, at2, None, "data-at2", sfx="hit")} style="top:{y}px; font-size:{round(size * K)}px">'
                       f'<div class="fc front"><i>생각</i>{E(front)}</div><div class="fc back"><i>현실</i>{E(back)}</div></div>')
PAST = raw('<style>.bg{filter: sepia(.85) contrast(1.08) brightness(.78) blur(var(--blur, 0px)) !important}</style>')   # 과거 장면 세피아 (레이더: 무궁화경제 아카이브 톤)

# ===== 2026-11-06 담당자 요청: 종이 인형극 기법 (누끼 그림이 뒤뚱뒤뚱 걷는다) · 입자 · 사진 액자 =====
def _lw(sc, until, inner):
    """사라지는 시각(until)을 감싸는 바깥 틀 — 안쪽 요소의 애니메이션과 섞이지 않게."""
    return f'<div class="lw"{_until(sc, until)}>{inner}</div>' if until else inner
def puppet(src, at, x, y, w=420, move='enter', dx=0, dur=2.4, step=0.45, tilt=6, flip=False, until=None, sfx='swish'):
    """누끼 그림(assets/src.png)을 종이 인형처럼 움직인다. 발밑을 축으로 좌우로 기우뚱하며 통통 튄다.
       move: 'walk' 걸어서 가로지름(dx) · 'enter' 걸어 들어와 멈춘 뒤 제자리 흔들 · 'idle' 제자리 흔들 · 'hop' 폴짝 · 'shiver' 덜덜 · 'nod' 끄덕
       flip=True 면 좌우 반전(왼쪽을 보고 걷게)."""
    n = max(2, round(dur / step))
    def f(sc):
        im = f'<img src="../assets/{src}.png"{" class=flip" if flip else ""}>'
        el = (f'<div class="pup m-{move}" {A(sc, at, -0.05, sfx=sfx)} style="left:{x}px; top:{y}px; width:{w}px; --dx:{dx}px; --dur:{dur}s; '
              f'--st:{step}s; --n:{n}; --tl:{tilt}deg"><div class="pin">{im}</div></div>')
        return _lw(sc, until, el)
    return f
def particles(kind, at='+0', until=None, n=16, seed=7):
    """화면 앞을 지나가는 입자: 'leaf' 낙엽 · 'snow' 눈 · 'ember' 불씨(위로) · 'spore' 포자(떠돔)."""
    import random
    def f(sc):
        r = random.Random(seed + len(kind)); out = []
        for k in range(n):
            sz = {'leaf': r.uniform(26, 54), 'snow': r.uniform(6, 16), 'ember': r.uniform(5, 11), 'spore': r.uniform(5, 12)}[kind]
            d = {'leaf': r.uniform(6, 11), 'snow': r.uniform(7, 13), 'ember': r.uniform(3.5, 7), 'spore': r.uniform(9, 16)}[kind]
            out.append(f'<i style="left:{r.uniform(-4, 100):.1f}%; --s:{sz:.0f}px; --d:{d:.1f}s; --dl:-{r.uniform(0, d):.1f}s; '
                       f'--sx:{r.uniform(-140, 140):.0f}px; --r:{r.uniform(-540, 540):.0f}deg; --o:{r.uniform(.55, 1):.2f}; --hue:{r.uniform(-25, 15):.0f}deg"></i>')
        return _lw(sc, until, f'<div class="ptc k-{kind}" {A(sc, at)}>{"".join(out)}</div>')
    return f

# ===== 2026-11-06 담당자 요청: 모션그래픽은 '애니메이션 일러스트' (플랫 벡터, 밝은 배경, 코드로 그려 비용 0) =====
TREE = '<svg viewBox="0 0 60 80"><rect x="26" y="46" width="8" height="30" rx="3" fill="#7a4b2a"/><circle cx="30" cy="28" r="22" fill="currentColor"/><circle cx="18" cy="38" r="13" fill="currentColor"/><circle cx="42" cy="38" r="13" fill="currentColor"/><circle cx="24" cy="20" r="6" fill="#fff" opacity=".18"/></svg>'
NUT = '<svg viewBox="0 0 60 60"><path d="M30 5C47 17 55 30 53 42C51 55 9 55 7 42C5 30 13 17 30 5Z" fill="#9a5226"/><path d="M8 40C19 47 41 47 52 40L53 47C41 56 19 56 7 47Z" fill="#efd3a8"/><ellipse cx="22" cy="24" rx="5" ry="10" fill="#fff" opacity=".22"/></svg>'
PERSON = '<svg viewBox="0 0 40 60"><circle cx="20" cy="12" r="9" fill="currentColor"/><path d="M5 58C5 36 10 26 20 26C30 26 35 36 35 58Z" fill="currentColor"/></svg>'
BOX = '<i class="box" style="--c:{c}"></i>'
def mgbg(tone='teal'):
    """모션그래픽 바탕: 밝고 깔끔한 그라데이션 + 점 무늬 (어두운 덮개 대신)."""
    return raw(f'<div class="mgbg {tone}"></div><style>.bg{{opacity:0 !important}}</style>')
def mg_forest(at, at2, n=40, cols=10, year=None, label=None, x=None, y=150, size=88, wave=.56):
    """나무 아이콘 숲: at 에 줄지어 돋아나고, at2 에 왼쪽부터 회색 물결이 지나가며 시들어 쓰러진다. year=(1904, 1940) 이면 연도 숫자가 함께 오른다."""
    def f(sc):
        rows = (n + cols - 1) // cols; w = cols * size * .92; pos = f'left:{(1920 - w) / 2:.0f}px;' if x is None else f'left:{x}px;'
        trees = ''.join(f'<i style="--i:{k}; --c:{k % cols}; --fall:{(-1) ** k * (6 + k % 5 * 3)}deg">{TREE}</i>' for k in range(n))
        yr = (f'<div class="mgyear num" data-from="{year[0]}" data-to="{year[1]}" data-dur="{6.4}" {A(sc, at2)}>{year[0]}</div>') if year else ''
        lb = f'<div class="mglabel" {A(sc, at)}>{E(label)}</div>' if label else ''
        return (f'<div class="mgforest" {A(sc, at, sfx="pop")} {A(sc, at2, None, "data-at2", sfx="whoosh")} style="{pos} top:{y}px; width:{w:.0f}px; --sz:{size}px; --ws:{wave}s">'
                f'{trees}</div>{yr}{lb}')
    return f
def mg_sap(at, at2, x=None, y=110):
    """나무 단면: 수액이 줄기를 타고 오르다(at), 곰팡이(주황 얼룩)가 번져 길을 막고 잎이 시든다(at2)."""
    def f(sc):
        pos = 'left:0; right:0; margin:0 auto;' if x is None else f'left:{x}px;'
        lines = ''.join(f'<line x1="{x0}" y1="560" x2="{x0}" y2="170" class="sap" style="--i:{k}"/>' for k, x0 in enumerate((178, 200, 222)))
        svg = (f'<svg viewBox="0 0 400 620" class="sapsvg"><circle cx="200" cy="150" r="130" class="crown"/><circle cx="120" cy="190" r="80" class="crown"/>'
               f'<circle cx="280" cy="190" r="80" class="crown"/><rect x="160" y="170" width="80" height="420" rx="18" fill="#8a5a36"/>{lines}'
               f'<ellipse cx="200" cy="420" rx="70" ry="60" class="rot"/><ellipse cx="190" cy="380" rx="40" ry="34" class="rot r2"/></svg>')
        return f'<div class="mgsap" {A(sc, at, sfx="pop")} {A(sc, at2, None, "data-at2", sfx="hit")} style="{pos} top:{y}px">{svg}</div>'
    return f
def mg_pile(at, at2, n=10, keep=4, cols=5, x=None, y=180, size=130, a_label='', b_label=''):
    """밤 아이콘 더미: at 에 n개가 쏟아지고, at2 에 keep 개만 남기고 떨어져 사라진다 (예: 10 → 4 = -60%)."""
    def f(sc):
        w = cols * size * 1.1; pos = f'left:{(1920 - w) / 2:.0f}px;' if x is None else f'left:{x}px;'
        nuts = ''.join(f'<i class="{"go" if k >= keep else ""}" style="--i:{k}">{NUT}</i>' for k in range(n))
        lab = (f'<div class="mgcap a" {A(sc, at)} {A(sc, at2, None, "data-at2")}>{E(a_label)}</div>' if a_label else '') + (f'<div class="mgcap b" {A(sc, at2)}>{E(b_label)}</div>' if b_label else '')
        return (f'<div class="mgpile" {A(sc, at, sfx="pop")} {A(sc, at2, None, "data-at2", sfx="whoosh")} style="{pos} top:{y}px; width:{w:.0f}px; --sz:{size}px">{nuts}</div>{lab}')
    return f
def mg_ship(at, at2, boxes=12, keep=1, a_label='', b_label='', y=230):
    """플랫 화물선: at 에 바다를 건너오고(상자 가득), at2 에 상자가 하나씩 날아가 keep 개만 남는다."""
    cols = ['#e07a3a', '#2f8f9d', '#f2b544', '#d6534f']
    def f(sc):
        bx = ''.join(f'<i class="box{" go" if k >= keep else ""}" style="--i:{k}; --c:{cols[k % 4]}"></i>' for k in range(boxes))
        lab = (f'<div class="mgcap a" {A(sc, at)} {A(sc, at2, None, "data-at2")}>{E(a_label)}</div>' if a_label else '') + (f'<div class="mgcap b" {A(sc, at2)}>{E(b_label)}</div>' if b_label else '')
        return (f'<div class="mgsea" {A(sc, at)} style="top:{y + 300}px"></div>'
                f'<div class="mgship" {A(sc, at, sfx="whoosh")} {A(sc, at2, None, "data-at2", sfx="pop")} style="top:{y}px"><div class="boxes">{bx}</div><div class="hull"></div></div>{lab}')
    return f
def mg_scale(at, at2, left='한국 밤', lval='10,000원', right='중국 밤', rval='6,000원', y=170):
    """가격 저울: 두 접시의 밤과 값표, at2 에 손님(사람 아이콘)이 싼 쪽으로 몰리며 저울이 기운다."""
    def f(sc):
        ppl = ''.join(f'<i style="--i:{k}">{PERSON}</i>' for k in range(5))
        return (f'<div class="mgscale" {A(sc, at, sfx="pop")} {A(sc, at2, None, "data-at2", sfx="whoosh")} style="top:{y}px">'
                f'<div class="post"></div><div class="beam"><div class="pan l"><b>{NUT}</b><span>{E(left)}<em>{E(lval)}</em></span></div>'
                f'<div class="pan r"><b>{NUT}</b><span>{E(right)}<em>{E(rval)}</em></span></div></div><div class="crowd">{ppl}</div></div>')
    return f
def mg_people(at, at2, n=10, keep=3, a_label='', b_label='', y=260):
    """사람 아이콘 줄: at 에 나란히 서고, at2 에 오른쪽부터 하나씩 흐려지며 keep 명만 남는다 (일손이 사라진다)."""
    def f(sc):
        ppl = ''.join(f'<i class="{"go" if k >= keep else ""}" style="--i:{k}; --j:{n - 1 - k}">{PERSON}</i>' for k in range(n))
        lab = (f'<div class="mgcap a" {A(sc, at)} {A(sc, at2, None, "data-at2")}>{E(a_label)}</div>' if a_label else '') + (f'<div class="mgcap b" {A(sc, at2)}>{E(b_label)}</div>' if b_label else '')
        return f'<div class="mgpeople" {A(sc, at, sfx="pop")} {A(sc, at2, None, "data-at2", sfx="whoosh")} style="top:{y}px">{ppl}</div>{lab}'
    return f
def qbadge(html, at='+0', pop=False):
    """질문 추적 배지 (오른쪽 위 고정): 제목의 질문과 지금까지 나온 답. pop=True 면 처음 한 번 튀어나온다."""
    return lambda sc: f'<div class="qbadge{" pop" if pop else ""}" {A(sc, at)}>{html}</div>'
def polaroid(src, at, x, y, w=560, rot=-4, cap=None, until=None):
    """실제 사진(assets/src.png, 위키미디어 등)을 테이프 붙은 인화지 액자로 툭 떨어뜨린다."""
    def f(sc):
        c = f'<div class="pc">{E(cap)}</div>' if cap else ''
        return _lw(sc, until, f'<div class="pola" {A(sc, at, -0.05, sfx="paper")} style="left:{x}px; top:{y}px; width:{w}px; --rot:{rot}deg">'
                              f'<img src="../assets/{src}.png">{c}</div>')
    return f

# ---------------- 카메라워크 · 그려 넣기 (2026-11-03 담당자: 전체 화면 → 1/5 로 줄며 선·화살표, 줌인·줌아웃·크래쉬줌) ----------------
def lens(sc, bg_html, moves):
    """장면의 'cam': [('crash'|'push'|'pull'|'shake', 시각, 초점x%, 초점y%, 배율), ...] → 배경만 움직인다 (글자는 그대로)."""
    out = bg_html
    for m in moves:
        kind, at = m[0], m[1]; ox, oy, z = (list(m[2:]) + [50, 50, 1.5])[:3] if len(m) > 2 else (50, 50, 1.5)
        snd = {'crash': 'whoosh', 'shake': 'hit'}.get(kind)
        out = f'<div class="lens {kind}" {A(sc, at, -0.05, sfx=snd)} style="--ox:{ox}%; --oy:{oy}%; --z:{z}">{out}</div>'
    return out
def shrink(src, at, x, y, w=640, h=360, cap=None, until=None):
    """전체 화면 사진이 at 에 (x, y, w, h) 작은 액자로 줄어든다 (보통 1/5 크기). 그 뒤 arrow·circ 로 짚는다."""
    def f(sc):
        c = f'<div class="scap">{E(cap)}</div>' if cap else ''
        return (f'<div class="shrink" {A(sc, at, -0.1, sfx="whoosh")}{_until(sc, until)} style="--x:{x}px; --y:{y}px; --w:{w}px; --h:{h}px">'
                f'<img src="../assets/{src}.png">{c}</div>')
    return f
def arrow(at, x1, y1, x2, y2, color='#ffd400', width=12, curve=0.18, dur=0.5):
    """손으로 긋는 화살표 (x1,y1) → (x2,y2). curve = 휘는 정도."""
    def f(sc):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2; dx, dy = x2 - x1, y2 - y1
        cx, cy = mx - dy * curve, my + dx * curve
        ang = math.degrees(math.atan2(y2 - cy, x2 - cx)); hs = width * 3.2
        return (f'<svg class="draw" {A(sc, at)} style="--dur:{dur}s" viewBox="0 0 1920 1080">'
                f'<path class="ln" pathLength="1" d="M{x1},{y1} Q{cx:.0f},{cy:.0f} {x2},{y2}" stroke="{color}" stroke-width="{width}"/>'
                f'<polygon class="hd" points="0,0 {-hs:.0f},{hs * .55:.0f} {-hs:.0f},{-hs * .55:.0f}" fill="{color}" transform="translate({x2},{y2}) rotate({ang:.1f})"/></svg>')
    return f
def circ(at, x, y, w, h, color='#ff3b3b', width=10, dur=0.6):
    """손으로 두르는 동그라미 (상자 x, y, w, h)."""
    def f(sc):
        rx, ry, cx, cy = w * .56, h * .64, x + w / 2, y + h / 2      # 네모난 글자 상자의 모서리까지 감싸도록 조금 크게
        d = f'M{cx - rx:.0f},{cy:.0f} A{rx:.0f},{ry:.0f} 0 1,1 {cx + rx:.0f},{cy:.0f} A{rx:.0f},{ry:.0f} 0 1,1 {cx - rx * .96:.0f},{cy - ry * .28:.0f}'
        return (f'<svg class="draw" {A(sc, at, sfx="scribble")} style="--dur:{dur}s" viewBox="0 0 1920 1080">'
                f'<path class="ln" pathLength="1" d="{d}" stroke="{color}" stroke-width="{width}"/></svg>')
    return f
def uline(at, x, y, w, color='#ff3b3b', width=10, dur=0.4):
    """밑줄 긋기."""
    return lambda sc: (f'<svg class="draw" {A(sc, at, sfx="scribble")} style="--dur:{dur}s" viewBox="0 0 1920 1080">'
                       f'<path class="ln" pathLength="1" d="M{x},{y} q{w * .5:.0f},{-8} {w},{4}" stroke="{color}" stroke-width="{width}"/></svg>')

# ---------------- 키트 2판 (레퍼런스 JV7ONuxsbm4) ----------------
K = 1.4    # 글자·칩·로고 배율 (2026-10-30 담당자: 폰·40대 이상 기준 1.28 → 2026-11-01 시청자 실측 55세+ 77.5% 로 1.4)
def _until(sc, until): return f' {A(sc, until, None, "data-until")}' if until else ''
def _pos(x): return 'left:0; right:0; margin:0 auto; width:max-content;' if x is None else f'left:{x}px;'
def tag(text, at, x, y, icon=None, tone='', size=52, until=None, strike=None):
    """흰 둥근 박스 칩. tone = '' | 'red' | 'green' | 'dark' | 'ghost'. icon = brand/icons 이름."""
    def f(sc):
        ic = f'<span class="ti">{icon_svg(icon)}</span>' if icon else ''
        snd = 'pop' if tone == 'red' and size >= 58 else None                    # 효과음은 빨간 핵심 칩에만
        st = f' {A(sc, strike, None, "data-at2")}' if strike else ''
        return f'<div class="tag {tone}{" strike" if strike else ""}" {A(sc, at, sfx=snd)}{_until(sc, until)}{st} style="{_pos(x)} top:{y}px; font-size:{round(size * K)}px">{ic}{E(text)}</div>'
    return f
def stack(rows, at0=None, x=120, y=200, gap=100, size=52):
    """칩을 위에서 아래로 차례로 쌓는다: rows = [(글자, 시각, icon, tone), ...]"""
    return [tag(r[0], r[1], x, y + i * gap, icon=r[2] if len(r) > 2 else None, tone=r[3] if len(r) > 3 else '', size=size) for i, r in enumerate(rows)]
LOGOS = os.path.join(os.path.dirname(os.path.dirname(ROOT)), 'brand', 'logos')
WORDMARK = {'samsung': ('SAMSUNG', '#1428a0'), 'indeed': ('indeed', '#2557a7'), 'gartner': ('Gartner', '#002856'), 'fsc': ('금융위원회', '#00479d'), 'bok': ('한국은행', '#0a3d8f'), 'chatgpt': ('ChatGPT', '#10a37f'), 'keis': ('한국고용정보원', '#005bac'), 'kicpa': ('한국공인회계사회', '#1d3f8c'), 'pigeon': ('피죤', '#e5007e'), 'purmil': ('푸르밀', '#0a7d3c'), 'mrpizza': ('MR.PIZZA', '#d8232a'), 'namyang': ('남양유업', '#0b3d91'), 'daewoo': ('DAEWOO', '#0a4ea2'), 'tongyang': ('동양', '#c8102e'), 'oxy': ('OXY', '#1d4f9c'), 'maeil': ('매일유업', '#1b6fb8'), 'kgm': ('KG모빌리티', '#e4002b'), 'homeplus': ('Homeplus', '#e2001a'), 'mbk': ('MBK Partners', '#13294b'), 'ocado': ('ocado', '#4d2c82'), 'meritz': ('MERITZ', '#d71920'), 'lotteshopping': ('LOTTE', '#da291c')}
def logo(name, at, x, y, h=56, until=None):
    """회사 로고 타일 (brand/logos/name.png, 없으면 브랜드 색 글자 로고)."""
    def f(sc):
        p = os.path.join(LOGOS, name + '.png')
        if os.path.exists(p): inner = f'<img src="../../../brand/logos/{name}.png">'
        else:
            t, c = WORDMARK.get(name, (name, '#e2001a')); inner = f'<span class="wm" style="--brand:{c}">{E(t)}</span>'
        return f'<div class="logo" {A(sc, at)}{_until(sc, until)} style="left:{x}px; top:{y}px; --lh:{round(h * K)}px">{inner}</div>'
    return f
def cut(src, at, x, y, h=600, move=None, moveat=None, until=None):
    """누끼(assets/src.png, 배경 지운 그림). move = (dx, dy, 배율) 로 moveat 시각에 옮기며 줄인다."""
    def f(sc):
        mv = ''
        if move: mv = f' move" {A(sc, moveat, None, "data-at2")} style="--mx:{move[0]}px; --my:{move[1]}px; --ms:{move[2]}; '
        else: mv = '" style="'
        return f'<div class="cut{mv}left:{x}px; top:{y}px; height:{h}px" {A(sc, at)}{_until(sc, until)}><img src="../assets/{src}.png"></div>'
    return f
def bubble(text, at, x, y, size=50, tone='', tail=22, until=None):
    return lambda sc: f'<div class="bubble {tone}" {A(sc, at, sfx="pop" if tone == "red" else None)}{_until(sc, until)} style="left:{x}px; top:{y}px; font-size:{round(size * K)}px; --tx:{tail}%">{E(text)}</div>'
def row(x, y, *items):
    """가로로 나란히 (로고 + 칩 등). 각 요소의 left/top 은 무시하고 차례로 흐른다."""
    return lambda sc: f'<div class="row" style="left:{x}px; top:{y}px">' + ''.join(i(sc) for i in items) + '</div>'
def split(at, vs=False):
    """좌우 분할: 가운데 세로선 (+ VS 원)."""
    out = [lambda sc: f'<div class="vline" {A(sc, at)}></div>']
    if vs: out.append(lambda sc: f'<div class="vs" {A(sc, at, 0.25, sfx="hit")}>VS</div>')
    return out
def side(which, at, *items_html):
    """분할 화면 한쪽 머리글 묶음: which = 'l' | 'r'. items 는 이 함수 안에서 HTML 로 쓴다 (logo/tag 를 left/top 없이)."""
    return lambda sc: f'<div class="side {which}" {A(sc, at)}>' + ''.join(i(sc) for i in items_html) + '</div>'
def article(outlet, date, headline, at, mark=None, markat=None, x=460, y=170, rot=-2.5, lines=3, until=None):
    """다시 쓴 기사 카드 (실제 캡처 대신). headline 은 보도 내용을 우리가 요약한 제목. mark = 밑줄 그을 낱말."""
    def f(sc):
        h = E(headline)
        if mark: h = h.replace(E(mark), f'<mark {A(sc, markat or at, None if markat else 0.6, "data-at2")}>{E(mark)}</mark>', 1)
        body = ''.join(f'<div class="ln" style="width:{[96, 88, 92, 70][i % 4]}%"></div>' for i in range(lines))
        return (f'<div class="article" {A(sc, at, sfx="paper")}{_until(sc, until)} style="left:{x}px; top:{y}px; --rot:{rot}deg"><div class="tape"></div>'
                f'<div class="meta">{E(outlet)} · {E(date)}</div><h3>{h}</h3>{body}</div>')
    return f
def pictos(n, at, moveat, x, y, dx=600, fade=False, icon='user', dur=1.6):
    """사람 픽토그램 n개가 moveat 에 dx 만큼 걸어간다 (fade=True 면 사라지며)."""
    svg = icon_svg(icon)
    return lambda sc: (f'<div class="pictos" {A(sc, at)} {A(sc, moveat, None, "data-at2")} style="left:{x}px; top:{y}px; --dx:{dx}px; --pd:{dur}s; --po:{0 if fade else 1}">'
                       + svg * n + '</div>')
def phone(src, at, x, y, until=None):
    """폰 목업 (assets/src.png 를 화면 안에서 천천히 스크롤)."""
    return lambda sc: f'<div class="phone" {A(sc, at)}{_until(sc, until)} style="left:{x}px; top:{y}px"><img src="../assets/{src}.png"></div>'
def roll(a, b, at, y=330, size=200, suffix='', prefix='', tone='bad', dur=1.4, x=None):
    """숫자 A → B 롤링 (예: 190 → 128). tone = bad | good (도착 색)."""
    def f(sc):
        pos = 'left:0; right:0; text-align:center;' if x is None else f'left:{x}px;'
        return (f'<div class="line big" style="{pos} top:{y}px; font-size:{size}px"><span class="in" {A(sc, at, -0.1, sfx="ding")}>{E(prefix)}'
                f'<span class="num roll {tone}" data-from="{a}" data-to="{b}" data-fmt="comma" {A(sc, at)} data-dur="{dur}">{a:,}</span>{E(suffix)}</span></div>')
    return f

ICONS = os.path.join(os.path.dirname(os.path.dirname(ROOT)), 'brand', 'icons')
def icon_svg(name):
    p = os.path.join(ICONS, name + '.svg')
    if not os.path.exists(p): raise SystemExit(f'아이콘 {name} 이 brand/icons 에 없습니다.')
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8').read())
def inset(src, at, x, y, w=860, h=490, cap=None, until=None, zoom=(1.0, 1.14), pan=(0, 0), origin=(50, 50)):
    """작은 네모 창: 흰 테두리 + 그림자, 탄성 팝 등장, 안의 그림은 천천히 줌/팬.
       src = 에셋 id (assets/id.png) 또는 영상 id (captures/id.mp4 가 있으면 영상). until = 사라지는 시각."""
    def f(sc):
        vid = os.path.exists(os.path.join(ROOT, 'captures', src + '.mp4'))
        inner = (f'<img class="vid" data-video="{src}" data-w="1920" data-h="1080">' if vid else f'<img src="../assets/{src}.png">')
        st = (f'left:{x}px; top:{y}px; width:{w}px; height:{h}px; --s0:{zoom[0]}; --s1:{zoom[1]}; --px0:{pan[0]}px; --px1:{pan[1]}px; --ox:{origin[0]}%; --oy:{origin[1]}%')
        out = f' out" {A(sc, until, None, "data-at2")}' if until else '"'
        return f'<div class="inset{out} {A(sc, at)} style="{st}">{inner}' + (f'<div class="cap2">{E(cap)}</div>' if cap else '') + '</div>'
    return f
def node(icon, text, at, x, y, tone=''):
    """아이콘 노드 (둥근 원 아이콘 + 아래 글자). tone = '' | 'hot' | 'cool' (+ ' sm' 작게)."""
    return lambda sc: f'<div class="node {tone}" {A(sc, at)} style="left:{x}px; top:{y}px"><div class="ic">{icon_svg(icon)}</div><div class="nt">{E(text)}</div></div>'
def arrowline(at, x, y, w):
    """점선 화살표 (노드와 노드 사이)."""
    return lambda sc: f'<div class="arrowline" {A(sc, at)} style="left:{x}px; top:{y}px; width:{w}px"></div>'
def chain(items, y=300, x0=None, gap=None):
    """아이콘 흐름도: items = [(아이콘, 글자, 시각[, tone]), ...] 왼쪽에서 오른쪽으로 노드와 점선 화살표가 차례로. 4개 넘으면 작은 노드."""
    sm = len(items) > 3; W, R = (320, 90) if sm else (380, 120)
    gap = gap or (380 if sm else 560); x0 = x0 if x0 is not None else int((1920 - (gap * (len(items) - 1) + W)) / 2)
    out = []
    for i, it in enumerate(items):
        ic, tx, at = it[:3]; tone = (it[3] if len(it) > 3 else '') + (' sm' if sm else '')
        if i:
            a = x0 + (i - 1) * gap + W / 2 + R + 18; b = x0 + i * gap + W / 2 - R - 38
            out.append(arrowline(at, round(a), y + R - 3, round(b - a)))
        out.append(node(ic, tx, at, x0 + i * gap, y, tone))
    return out

PAGE = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="cues" content="{c0}-{c1}">
<link rel="stylesheet" href="../../../engine/web/kit.css"><link rel="stylesheet" href="../../../brand/web/channel.css">
</head><body data-bg="none"{enter}>
<div class="stage">{bg}<div class="shade"></div><div class="midlayer"></div><div class="cam">
{items}
</div><div class="fx"><div class="leak"></div><div class="dust"></div><div class="vig"></div></div>{prog}</div>
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

SCENES = []
# ---------------- 인트로 30초 기본 키트 (2026-11-08 채널 표준) ----------------
# 첫 30초는 ① 배경 2~3초마다 교체(스톡·일러스트·사진 번갈아, 휙 넘기기) ② 모든 문장 움직이는 글자(kin) ③ 멈춘 화면 금지.
INTRO_CSS = """<style>
.bg.kb.swap, .bg.swap { animation: kb var(--len) 0s both linear, whipIn .34s var(--t) both cubic-bezier(.2,.9,.3,1); }
@keyframes whipIn { 0% { opacity: 0; transform: translateX(10%) scale(1.2); filter: blur(16px) brightness(1.6); } 100% { opacity: 1; transform: none; filter: none; } }
.kin { position: absolute; left: 0; right: 0; text-align: center; font-family: 'BH', sans-serif; color: #fff; line-height: 1.12; z-index: 7; padding: 0 60px;
  text-shadow: 0 6px 0 rgba(0,0,0,.45), 0 12px 44px rgba(0,0,0,.7); animation: kinDrift 5s var(--t) both ease-in-out infinite alternate; }
.kin .w { display: inline-block; margin: 0 .13em; opacity: 0; animation: var(--a) .52s calc(var(--t) + var(--i) * .1s) both cubic-bezier(.2,1.5,.4,1); }
.kin .w.k { color: #ffd400; position: relative; animation: var(--a) .52s calc(var(--t) + var(--i) * .1s) both cubic-bezier(.2,1.5,.4,1), kinPulse .9s calc(var(--t) + var(--i) * .1s + .55s) infinite alternate ease-in-out; }
.kin .w.r { color: #ff4b4b; }
.kin .w.k::after { content: ''; position: absolute; left: -3%; right: -3%; bottom: .02em; height: .16em; background: #ff3b3b; border-radius: .08em; z-index: -1;
  transform: scaleX(0); transform-origin: left; animation: kinBar .4s calc(var(--t) + var(--i) * .1s + .35s) forwards ease-out; }
@keyframes kinDrop { 0% { opacity: 0; transform: translateY(-130%) scale(1.5); } 100% { opacity: 1; transform: none; } }
@keyframes kinPop { 0% { opacity: 0; transform: scale(2.6); filter: blur(8px); } 100% { opacity: 1; transform: none; filter: none; } }
@keyframes kinSlide { 0% { opacity: 0; transform: translateX(-90%) skewX(-14deg); } 100% { opacity: 1; transform: none; } }
@keyframes kinRise { 0% { opacity: 0; transform: translateY(100%) rotate(8deg); } 100% { opacity: 1; transform: none; } }
@keyframes kinPulse { 0% { transform: scale(1) rotate(0); } 100% { transform: scale(1.09) rotate(-1.5deg); } }
@keyframes kinBar { to { transform: scaleX(1); } }
@keyframes kinDrift { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(0, -16px) scale(1.04); } }
.lw.out { animation: kinGone .3s var(--u) forwards ease-in; }
@keyframes kinGone { to { opacity: 0; transform: scale(.9); } }
</style>"""
def intro30(): return lambda sc: INTRO_CSS
KMODES = {'mix': ['kinDrop', 'kinPop', 'kinSlide', 'kinRise'], 'drop': ['kinDrop'], 'pop': ['kinPop'], 'slide': ['kinSlide'], 'rise': ['kinRise']}
def kin(text, at, y=330, size=110, mode='mix', until=None, sfx=None):
    """움직이는 글자: 낱말이 0.1초 간격으로 떨어지고·튀고·밀려 들어오며, 전체는 계속 천천히 떠다닌다.
    *낱말* = 노랑 강조(밑줄 + 맥박), !낱말! = 빨강, '/' = 줄바꿈. 사용 장면에 intro30() 을 함께 넣는다."""
    def f(sc):
        ms = KMODES[mode]; out = []; i = 0
        for line in text.split('/'):
            ws = []
            for w in line.split():
                cls = 'w'
                if w.startswith('*') and w.endswith('*'): cls += ' k'; w = w[1:-1]
                elif w.startswith('!') and w.endswith('!'): cls += ' r'; w = w[1:-1]
                ws.append(f'<span class="{cls}" style="--i:{i}; --a:{ms[i % len(ms)]}">{E(w)}</span>'); i += 1
            out.append(' '.join(ws))
        inner = f'<div class="kin" {A(sc, at, -0.05, sfx=sfx)} style="top:{y}px; font-size:{size}px">{"<br>".join(out)}</div>'
        return _lw(sc, until, inner)
    return f
def cutsfx(*ats, kind='swish'):
    """배경이 바뀌는 순간마다 휙 소리 (보이지 않는 표식)."""
    return lambda sc: ''.join(f'<i style="display:none" {A(sc, a, sfx=kind)}></i>' for a in ats)

def build(plan):
    starts = []; last = 0                     # 앞 장면보다 뒤에서 찾는다 (같은 문구가 여러 번 나오는 대본)
    for s in plan: n = cue_of(s['from'], last + 1); starts.append(n); last = n
    if starts[0] != 1: raise SystemExit(f'첫 장면은 1번 자막에서 시작해야 합니다 (지금 {starts[0]}번).')
    os.makedirs(SC, exist_ok=True); keep = {f's{i + 1:02d}.html' for i in range(len(plan))}
    for f in os.listdir(SC):
        if re.fullmatch(r's\d+\.html', f) and f not in keep: os.remove(os.path.join(SC, f))
    for i, s in enumerate(plan):
        c0 = starts[i]; c1 = starts[i + 1] - 1 if i + 1 < len(plan) else len(CUES)
        sc = Scene(s, c0, c1); SCENES.append(sc)
        T0 = TIMES[c0 - 1]; T1 = TIMES[c1] if c1 < len(TIMES) else TOTAL
        prog = f'<div class="progress" style="--p0:{T0 / TOTAL:.4f}; --p1:{T1 / TOTAL:.4f}; --pd:{max(.1, T1 - T0):.2f}s"></div>' if TOTAL else ''
        page = PAGE.format(prog=prog, c0=c0, c1=c1, enter=(f' data-enter="{s["enter"]}"' if s.get('enter') else ''), bg=(lens(sc, background(sc, s.get('bg')), s['cam']) if s.get('cam') else background(sc, s.get('bg'))), items='\n'.join(it(sc) for it in s.get('items', [])))
        fp = os.path.join(SC, f's{i + 1:02d}.html')
        if not os.path.exists(fp) or open(fp, encoding='utf-8').read() != page: open(fp, 'w', encoding='utf-8').write(page)   # 바뀐 장면만 새로 쓴다
    sfx = []
    for sc_ in SCENES:
        for spec, kind, off in sc_.sfx:
            t = sc_.secs(spec, off)
            if t is not None: sfx.append([round(max(0, t), 3), kind])
    sfx.sort(); keep = []; ORDER = ['tap', 'tick', 'paper', 'blip', 'pop', 'scribble', 'swish', 'whoosh', 'riser', 'ding', 'hit', 'boom', 'stamp']
    for t, k in sfx:                                                          # 0.22초 안에 겹치면 하나만 (센 소리를 남긴다)
        if keep and t - keep[-1][0] < 1.2:
            if ORDER.index(k) > ORDER.index(keep[-1][1]): keep[-1] = [keep[-1][0], k]
            continue
        keep.append([t, k])
    boom = None; out = []                                                    # 쿵은 인트로 35초 뒤로는 2분에 한 번까지 (2026-10-31 담당자: 쿵이 많다 → 숫자 공개는 ding)
    for t, k in keep:
        if k == 'boom':
            if t >= 35 and boom is not None and t - boom < 120: continue
            boom = t
        out.append([t, k])
    keep = out
    out = []                                                                 # 2026-11-03: 뾱(pop)·틱은 앞 소리와 6초 넘게 떨어질 때만, 나머지도 4초 간격 (담당자: 뾱 소리 너무 많다)
    for t, k in keep:
        gap = t - out[-1][0] if out else 99
        if k in ('pop', 'tick', 'swish', 'tap', 'paper') and gap < 6: continue
        if gap < 4 and k not in ('stamp', 'ding'): continue
        out.append([t, k])
    keep = out
    __import__('json').dump(keep, open(os.path.join(HERE, 'sfx.json'), 'w'), ensure_ascii=False)
    plain = sum(1 for s_ in plan if not s_.get('bg'))
    print(f'장면 {len(plan)}개 생성 (자막 1~{len(CUES)}번) · 효과음 {len(keep)}개 → plan/sfx.json · 검은 바탕 장면 {plain}개')

if __name__ == '__main__':
    sys.path.insert(0, HERE); from plan import PLAN; build(PLAN)
