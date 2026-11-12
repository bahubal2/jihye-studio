"""제목·썸네일·도입부 일치 검사 (2026-11-12 담당자 절대 규칙: "제목과 썸네일과 첫 도입부분이 반드시 일치해야 한다. 롱폼에서 절대적으로 지킬 것").
   python3 tools/hook_check.py <대본.txt> --title "제목" --thumb "썸네일 윗줄" "썸네일 큰 글씨" ...

검사 (대본 숫자는 한글로 풀어 써 있어도 숫자로 바꿔 비교):
  ① 썸네일의 핵심 말(숫자·낱말)이 첫 15초(약 105자) 안에 나오는가  → 첫 화면 = 썸네일과 같은 장면·숫자
  ② 제목의 핵심 말이 인트로(첫 300자) 안에 나오는가
  ③ 제목의 따옴표 문구(있으면)가 인트로에서 소리로 나오는가
하나라도 빠지면 [불합격]. 대본을 고치거나(녹음 전) 썸네일·제목을 도입부에 맞춘다(녹음 후)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subdigits import convert
STOP = set('그리고 그런데 하지만 이유 진짜 결국 우리 정말 이렇게 어떻게 무엇 왜 이 그 저 것 수 등 더 또 TOP5 TOP7 TOP10 몰락 사연 정체 충격 근황 반전'.split())
def keys(t):
    t = re.sub(r'["“”‘’\'…·.,!?~()\[\]#]', ' ', t)
    out = []
    for w in t.split():
        w = re.sub(r'(은|는|이|가|을|를|에|에서|으로|로|의|도|만|까지|부터|이다|였다|했다|됐다|한|된|인)$', '', w)
        if len(w) >= 2 and w not in STOP: out.append(w)
    return out
def norm(s):
    c = convert(s); c = c[0] if isinstance(c, tuple) else c
    return re.sub(r'\s+', '', c)
def main():
    a = sys.argv[1:]; path = a[0]; title = a[a.index('--title') + 1]
    thumbs = a[a.index('--thumb') + 1:] if '--thumb' in a else []
    body = '\n'.join(l for l in open(path, encoding='utf-8').read().splitlines() if not l.startswith('#')).strip()
    first15, intro = norm(body[:105]), norm(body[:300])
    bad = 0
    def show(label, ks, zone, zname):
        nonlocal bad
        hit = [k for k in ks if norm(k) in zone]; miss = [k for k in ks if norm(k) not in zone]
        rate = len(hit) / max(1, len(ks)); ok = rate >= 0.5 and (not miss or len(hit) >= 2)
        bad += 0 if ok else 1
        print(f'{"합격" if ok else "[불합격]"} {label} → {zname}: 맞음 {hit} / 없음 {miss}')
    for t in thumbs: show(f'썸네일 "{t}"', keys(t), first15, '첫 15초')
    show(f'제목', keys(title), intro, '인트로 300자')
    q = re.findall(r'["“]([^"”]+)["”]', title)
    for x in q:
        ok = norm(x) in intro; bad += 0 if ok else 1
        print(f'{"합격" if ok else "[불합격]"} 제목 따옴표 문구 "{x}" → 인트로에서 그대로 {"나옴" if ok else "안 나옴 (도입부에 그대로 넣는다)"}')
    print('결과: ' + ('제목·썸네일·도입부 일치' if not bad else f'불일치 {bad}곳 → 대본 도입부를 고친다 (녹음 뒤라면 썸네일·제목을 도입부에 맞춘다)'))
if __name__ == '__main__': main()
