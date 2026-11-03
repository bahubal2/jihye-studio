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
def _ts(x): h, m, r = x.split(':'); return int(h) * 3600 + int(m) * 60 + float(r.replace(',', '.'))
TIMES = [_ts(b.strip().split('\n')[1].split(' --> ')[0]) for b in re.split(r'\n\s*\n', open(os.path.join(ROOT, 'input', 'narration.srt'), encoding='utf-8-sig').read().strip()) if len(b.strip().split('\n')) >= 3]
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
        return f'<div class="line big" style="{st}"><span class="in" {A(sc, at, off, sfx="boom" if size >= 160 else "pop")}>{inner}</span></div>'
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

# ---------------- 키트 2판 (레퍼런스 JV7ONuxsbm4) ----------------
K = 1.28   # 글자·칩·로고 배율 (2026-10-30 담당자: 폰·40대 이상 기준으로 더 크게)
def _until(sc, until): return f' {A(sc, until, None, "data-until")}' if until else ''
def tag(text, at, x, y, icon=None, tone='', size=52, until=None):
    """흰 둥근 박스 칩. tone = '' | 'red' | 'green' | 'dark' | 'ghost'. icon = brand/icons 이름."""
    def f(sc):
        ic = f'<span class="ti">{icon_svg(icon)}</span>' if icon else ''
        snd = 'pop' if tone == 'red' and size >= 58 else None                    # 효과음은 빨간 핵심 칩에만
        return f'<div class="tag {tone}" {A(sc, at, sfx=snd)}{_until(sc, until)} style="left:{x}px; top:{y}px; font-size:{round(size * K)}px">{ic}{E(text)}</div>'
    return f
def stack(rows, at0=None, x=120, y=200, gap=100, size=52):
    """칩을 위에서 아래로 차례로 쌓는다: rows = [(글자, 시각, icon, tone), ...]"""
    return [tag(r[0], r[1], x, y + i * gap, icon=r[2] if len(r) > 2 else None, tone=r[3] if len(r) > 3 else '', size=size) for i, r in enumerate(rows)]
LOGOS = os.path.join(os.path.dirname(os.path.dirname(ROOT)), 'brand', 'logos')
WORDMARK = {'homeplus': ('Homeplus', '#e2001a'), 'mbk': ('MBK Partners', '#13294b'), 'ocado': ('ocado', '#4d2c82'), 'meritz': ('MERITZ', '#d71920'), 'lotteshopping': ('LOTTE', '#da291c')}
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
        return (f'<div class="article" {A(sc, at, sfx="whoosh")}{_until(sc, until)} style="left:{x}px; top:{y}px; --rot:{rot}deg"><div class="tape"></div>'
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
        return (f'<div class="line big" style="{pos} top:{y}px; font-size:{size}px"><span class="in" {A(sc, at, -0.1, sfx="boom")}>{E(prefix)}'
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

SCENES = []
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
        page = PAGE.format(c0=c0, c1=c1, enter=(f' data-enter="{s["enter"]}"' if s.get('enter') else ''), bg=background(sc, s.get('bg')), items='\n'.join(it(sc) for it in s.get('items', [])))
        fp = os.path.join(SC, f's{i + 1:02d}.html')
        if not os.path.exists(fp) or open(fp, encoding='utf-8').read() != page: open(fp, 'w', encoding='utf-8').write(page)   # 바뀐 장면만 새로 쓴다
    sfx = []
    for sc_ in SCENES:
        for spec, kind, off in sc_.sfx:
            t = sc_.secs(spec, off)
            if t is not None: sfx.append([round(max(0, t), 3), kind])
    sfx.sort(); keep = []
    for t, k in sfx:                                                          # 0.22초 안에 겹치면 하나만 (센 소리를 남긴다)
        if keep and t - keep[-1][0] < 1.2:
            if ['tick', 'pop', 'swish', 'whoosh', 'hit', 'boom', 'stamp'].index(k) > ['tick', 'pop', 'swish', 'whoosh', 'hit', 'boom', 'stamp'].index(keep[-1][1]): keep[-1] = [keep[-1][0], k]
            continue
        keep.append([t, k])
    __import__('json').dump(keep, open(os.path.join(HERE, 'sfx.json'), 'w'), ensure_ascii=False)
    plain = sum(1 for s_ in plan if not s_.get('bg'))
    print(f'장면 {len(plan)}개 생성 (자막 1~{len(CUES)}번) · 효과음 {len(keep)}개 → plan/sfx.json · 검은 바탕 장면 {plain}개')

if __name__ == '__main__':
    sys.path.insert(0, HERE); from plan import PLAN; build(PLAN)
