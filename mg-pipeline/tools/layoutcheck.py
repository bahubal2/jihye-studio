"""HTML 장면 배치 검사: 화면 요소끼리 겹침 · 화면 밖 넘침 · 자막 자리 침범을 찾는다 (렌더 전에 돌린다, 무료).
   python tools/layoutcheck.py <이름> [sNN ...]

장면마다 시간의 30% · 60% · 95% 지점에서 보이는 요소의 실제 상자를 재어,
두 요소가 작은 쪽 넓이의 12% 넘게 겹치거나, 화면 가로 밖으로 나가거나, 자막 자리(y 940 아래)로 내려가면 알려 준다.
"""
import os, sys, json, pathlib
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KIT, 'engine'))
from web import SEEK

JS = r"""() => {
  const SEL = '.tag,.logo,.bubble,.node,.card,.chip,.stamp,.article,.inset,.cut,.phone,.line > .in,.flow > span,.bar,.vs,.glowbox,.pictos,.punch,.rankbadge,.ranks';
  const vis = el => { for (let e = el; e && e !== document.body; e = e.parentElement) { const c = getComputedStyle(e); if (+c.opacity < 0.5 || c.display === 'none' || c.visibility === 'hidden') return false; } return true; };
  const els = [...document.querySelectorAll(SEL)].filter(vis);
  const top = els.filter(e => !els.some(o => o !== e && o.contains(e) && !o.matches('.line > .in')));
  return top.map(e => { const r = e.getBoundingClientRect(); return { k: (e.className || e.tagName).toString().split(' ')[0], t: (e.innerText || '').replace(/\s+/g, ' ').slice(0, 24), x: r.left, y: r.top, w: r.width, h: r.height }; })
            .filter(b => b.w > 4 && b.h > 4);
}"""

def check(boxes):
    out = []
    for i, a in enumerate(boxes):
        if a['x'] < -4 or a['x'] + a['w'] > 1924: out.append(f"화면 밖(가로): {a['k']} '{a['t']}'")
        if a['y'] + a['h'] > 948 and a['k'] not in ('cut', 'phone', 'pictos'): out.append(f"자막 자리 침범: {a['k']} '{a['t']}' (아래 끝 y={a['y'] + a['h']:.0f})")
        for b in boxes[i + 1:]:
            ix = max(0, min(a['x'] + a['w'], b['x'] + b['w']) - max(a['x'], b['x'])); iy = max(0, min(a['y'] + a['h'], b['y'] + b['h']) - max(a['y'], b['y']))
            small = min(a['w'] * a['h'], b['w'] * b['h'])
            if small and ix * iy / small > .12 and not ({a['k'], b['k']} & {'cut', 'inset'} and ix * iy / small < .35):
                out.append(f"겹침: {a['k']} '{a['t']}' ↔ {b['k']} '{b['t']}' ({ix * iy / small:.0%})")
    return out

def main():
    a = sys.argv[1:]; name = a[0]; only = set(a[1:])
    sc_dir = os.path.join(KIT, 'projects', name, 'scenes')
    files = sorted([f for f in os.listdir(sc_dir) if f.endswith('.html') and f.startswith('s')], key=lambda f: int(f[1:-5]))
    from playwright.sync_api import sync_playwright
    bad = 0
    with sync_playwright() as pw:
        br = pw.chromium.launch(); page = br.new_page(viewport={'width': 1920, 'height': 1080})
        for f in files:
            if only and f[:-5] not in only: continue
            page.goto(pathlib.Path(os.path.join(sc_dir, f)).resolve().as_uri()); page.wait_for_load_state('networkidle')
            L = page.evaluate('KIT.len'); probs = []
            for k in (.3, .6, .95):
                page.evaluate(f'({SEEK})({L * k})'); probs += [p for p in check(page.evaluate(JS)) if p not in probs]
            if probs:
                bad += 1; print(f'{f[:-5]}:'); [print('   ', p) for p in probs]
        br.close()
    print(f'검사 끝: 문제 있는 장면 {bad}개' + ('' if bad else ' — 없음'))

if __name__ == '__main__': main()
