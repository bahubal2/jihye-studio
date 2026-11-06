from plan_a import A
from plan_b import B
from plan_c import C
from gen import qbadge, puppet
PLAN = A + B + C

# ===== 2026-11-06 담당자 확정: 시선 붙잡기 (배경 교체로 1분 8~9컷 · 질문 추적 배지 · 주인공 할아버지) =====
SW = {   # 장면 시작 문구: [(배경, 장면 시작 기준 초), ...]
 '또 병 때문일까요': [('v:s_dead_forest', 5.5)],
 '이름에 밤이 붙어': [('i_park_bench', 6)],
 '남의 나라 일만은': [('v:s_conkers', 5), ('v:s_autumn_park', 10)],
 '그런데 이 이야기에 늘': [('v:s_falling_leaves', 9), ('i_appalachia', 18), ('i_us_forest', 25)],
 '그렇다고 피해가 작았다는': [('i_us_forest', 7)],
 '도시 길모퉁이에선': [('v:s_newyork', 6)],
 '그런데 이 장면이 지금': [('v:s_mountain_village', 8)],
 '천구백십사 년, 버지니아': [('i_country_store', 7), ('i_train_station', 13)],
 '나무도 돈이었습니다': [('i_train_station', 7), ('i_us_forest', 14)],
 '천구백오십팔 년, 충청북도': [('v:s_mountain_village', 8)],
 '그런데 한국은 미국과': [('v:s_mountain_village', 7)],
 '결과는 숫자로 남았습니다': [('v:s_cargo_ship', 6), ('i_korea_harvest', 12)],
 '첫 번째 의심은 역시 병': [('v:s_dead_forest', 7), ('i_empty_slope', 14), ('v:s_mountain_village', 21)],
 '두 번째 의심입니다': [('v:s_seoul', 8), ('i_korea_harvest', 15), ('v:s_supermarket', 22)],
 '그런데 국내 숫자는': [('v:s_supermarket', 8), ('v:s_cargo_ship', 16), ('i_empty_slope', 24)],
 '경제학 교과서는': [('v:s_seoul', 7)],
 '중국은 오랫동안': [('v:s_supermarket', 9), ('v:s_cargo_ship', 18)],
 '애팔래치아의 밤이 기차를': [('v:s_cargo_ship', 6), ('v:s_seoul', 14)],
 '정부와 업계가 손을': [('i_korea_harvest', 8)],
 '그리고 올가을, 그 장면이': [('v:s_mountain_village', 8), ('i_empty_slope', 16)],
 '손이 덜 간 밭은': [('v:s_falling_leaves', 7), ('v:s_mountain_village', 14)],
 '밤 농사는 가을 몇 주에': [('v:s_mountain_village', 10)],
 '그런데 같은 곰팡이를 맞고도': [('v:s_dead_forest', 5), ('i_genoa_1938', 12)],
 '비밀은 곰팡이에 붙은': [('v:s_lab', 8), ('i_stump_sprouts', 14)],
 '이제 처음에 말씀드린 장면': [('v:s_cargo_ship', 7), ('v:s_newyork', 14)],
 '여기서 하나가 더': [('v:s_supermarket', 8), ('v:s_lab', 16)],
 '미국은 아직 싸우는': [('i_stump_sprouts', 7)],
 '유전자를 바꾼 밤나무로': [('v:s_sprout', 9), ('i_bronx_planting', 16)],
 '한국 밤에도 숨 돌릴': [('v:s_mountain_village', 9)],
 '처음 질문으로 돌아가': [('v:s_dead_forest', 9), ('v:s_cargo_ship', 15), ('i_empty_slope', 21)],
 '이건 밤만의 이야기가': [('i_empty_slope', 8)],
 '오늘 해 볼 수 있는 일이': [('v:s_conkers', 6), ('v:s_supermarket', 12), ('v:s_phone_elderly', 18)],
 '다시 그 동물원입니다': [('v:s_sprout', 7)],
 '다음 이야기도 골라': [('v:s_autumn_park', 9)],
}
FARMER = {   # 4막 주인공: 밤 농가 할아버지 (오른쪽 아래, 장면마다 다른 몸짓)
 '두 번째 의심입니다': ('idle', '+1'), '그럼 왜 하필 우리 밤이': ('nod', '+0.5'), '정부와 업계가 손을': ('idle', '+1'),
 '그런데 값과 수출길만으로는': ('enter', '+0.3'), '셋째, 가장 큰 원인은': ('nod', '+0.5'), '보통은 이렇게 생각합니다': ('idle', '+0.5'),
 '그리고 올가을, 그 장면이': ('shiver', '+1'), '그 밤밭이 우리 부모님': ('enter', '+0.3'),
}
Q1 = '<b>왜 안 주울까?</b>미국 <i>✔ 독 열매</i> · 한국 <u>?</u>'
Q2 = '<b>왜 안 주울까?</b>미국 <i>✔ 독</i> · 한국 <i>✔ 주울 사람이 없다</i>'
NOBADGE = ('그 숲에 곰팡이가', '길에 떨어진 밤, 왜 아무도 안 주울까요. 미국')
on = 0
for sc in PLAN:
    f = sc['from']
    for k, v in SW.items():
        if f.startswith(k):
            base = sc['bg'] if isinstance(sc['bg'], str) else sc['bg'][0][0]
            sc['bg'] = [(base, None)] + [(b, f'+{t}') for b, t in v]
    for k, (mv, at) in FARMER.items():
        if f.startswith(k):
            x0, dx = (1960, -480) if mv == 'enter' else (1480, 0)
            sc['items'].append(puppet('c_old_farmer', at, x0, 500, w=340, move=mv, dx=dx, dur=5, step=0.6, flip=(mv == 'enter'), sfx=None))
    if f.startswith('그런데 이 이야기에 늘'): on = 1
    if f.startswith('그 밤밭이 우리 부모님'): on = 2
    if f.startswith('처음 질문으로 돌아가'): on = 0
    if on and not f.startswith(NOBADGE):
        sc['items'].append(qbadge(Q1 if on == 1 else Q2, pop=f.startswith(('그런데 이 이야기에 늘', '그 밤밭이 우리 부모님'))))
