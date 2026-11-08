from plan_a import A
from plan_b import B
from plan_c import C
from gen import qbadge, rankbadge
PLAN = A + B + C
# 순위 배지(왼쪽 위, 칸 내내) · 질문 추적 배지(오른쪽 위: 문을 연 건?)
RANKS = [('오 위는 그 자작나무가', '5', '영양 자작나무숲'), ('사 위는 화순 적벽입니다', '4', '화순 적벽'), ('삼 위는 거제 저도입니다', '3', '거제 저도'),
         ('이 위는 전남 나주 금성산', '2', '나주 금성산'), ('일 위는 서울 북악산', '1', '서울 북악산'), ('오늘의 순위를 다시', None, None)]
QS = [('천구백팔십오 년, 전남 화순에', '화순 <u>?</u> · 저도 <u>?</u> · 금성산 <u>?</u> · 북악산 <u>?</u>'),
      ('적벽은 한 덩어리가', '화순 <i>✔ 협약</i> · 저도 <u>?</u> · 금성산 <u>?</u> · 북악산 <u>?</u>'),
      ('자, 여기까지 모인 단서를', '화순 <i>✔</i> · 저도 <i>✔ 협약</i> · 금성산 <u>?</u> · 북악산 <u>?</u>'),
      ('어릴 때 소풍 가던 뒷산을', '화순 <i>✔</i> · 저도 <i>✔</i> · 금성산 <i>✔ 협약</i> · 북악산 <u>?</u>'),
      ('여기서 우리 자신을', '화순 <i>✔</i> · 저도 <i>✔</i> · 금성산 <i>✔</i> · 북악산 <i>✔ 협의</i>'),
      ('처음 질문으로 돌아가', None)]
rk = None; q = None
for sc in PLAN:
    f = sc['from']; mg = sc['bg'] is None
    for k, r, n in RANKS:
        if f.startswith(k): rk = (r, n) if r else None; first = True; break
    else: first = False
    if rk and not first and not mg: sc['items'].append(rankbadge(rk[0], rk[1], '+0', still=True))
    for k, v in QS:
        if f.startswith(k): q = v; break
    if q: sc['items'].append(qbadge('<b>문을 연 건?</b>' + q, pop=any(f.startswith(k) for k, _ in QS)))
# 긴 장면 배경 교체 (7.5초마다, 같은 칸 장소의 실사·일러스트) — swaps.json
import json, os
SW = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'swaps.json'), encoding='utf-8'))
for sc in PLAN:
    if sc['from'] in SW:
        base = [(sc['bg'], None)] if isinstance(sc['bg'], str) else list(sc['bg'])
        sc['bg'] = base + [(b, f'+{t}') for b, t in SW[sc['from']]]
