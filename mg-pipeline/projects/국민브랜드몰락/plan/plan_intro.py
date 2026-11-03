"""국민 브랜드 몰락 TOP 7 — 인트로 0:00~0:43 (자막 1~16). 화풍 A 다큐.
기법 레이더(2026-10-31) 반영: 블라인드 순위 카드(?) · 통념 칩 → 정중앙 '아닙니다' 펀치.
가습기 장면(자막 6~9)은 무거운 구간: 효과음·튀는 등장 없이 페이드만."""
from gen import (tag, logo, stamp, roll, split, side, big, cover, ranks, punch, pictos, line, raw)

INTRO = [
# 0:00 "다시는 안 삽니다." — 물건을 도로 내려놓는 손님 (클립)
{'from': '다시는 안 삽니다', 'enter': 'flash', 'bg': 'ph_put_back', 'items': [
    big('“다시는 안 삽니다”', '+0.05', y=380, size=190),
]},
# 0:02 국민 1등 브랜드 일곱 곳 — 블라인드 순위 카드 7장
{'from': '한때 온 국민이', 'enter': 'slide', 'bg': 'st_hypermarket', 'items': [
    cover('+0.02'),
    tag('국민 1등 브랜드', '국민이', 560, 120, icon='flag', tone='red', size=66),
    ranks('국민이', n=7, top=380),
]},
# 0:05 손님들이 조용히 내린 결론 — 로고 7개 + 떠나는 사람들
{'from': '손님들이 조용히', 'bg': 'ph_mart_crowd_wide', 'items': [
    raw('<style>.row .logo{margin-right:26px} .pictos svg{width:120px; height:120px}</style>'),
    lambda sc: '<div class="row" style="left:120px; top:200px; flex-wrap:wrap; width:1700px; row-gap:26px">' + ''.join(logo(n, '+0.05', 0, 0, h=72)(sc) for n in ('pigeon', 'purmil', 'mrpizza', 'namyang', 'daewoo', 'tongyang', 'oxy')) + '</div>',
    pictos(6, '+0.3', '조용히', 200, 560, dx=1100, fade=True, dur=2.0),
]},
# 0:08 회장 대신 고개 숙인 가맹점주들 (클립)
{'from': '회장 대신', 'enter': 'mask', 'bg': 'ph_owners_bow', 'items': [
    tag('회장 대신', '회장', 120, 150, icon='user', tone='red', size=66),
    tag('고개 숙인 가맹점주들', '가맹점주들이', 120, 290, icon='users', size=58),
    logo('mrpizza', '피자집', 1180, 160, h=70),
]},
# 0:12 1조 적자 → 1,000억 흑자 장부 (클립)
{'from': '적자를', 'enter': 'slide', 'bg': 'ph_ledger', 'items': [
    tag('실제  적자 1조 원', '적자를', 140, 200, icon='trending-down', tone='red', size=64),
    tag('장부  흑자 1,000억 원', '흑자로', 140, 380, icon='file-invoice', tone='green', size=64),
    stamp('거짓 장부', '적어', x=1150, y=560, size=120),
]},
# 0:16 겨울밤, 아이 머리맡의 작은 기계 (클립, 무거운 구간: 페이드만)
{'from': '그리고 겨울밤', 'enter': 'fade', 'bg': 'ph_humidifier_night', 'items': [
    line('겨울밤, 아이 머리맡', '겨울밤', x=150, y=200, cls='say', size=84),
    line('작은 기계 하나', '기계', x=150, y=340, cls='say', size=110),
]},
# 0:21 그 기계에 무엇을 넣었는지는 맨 마지막에 — 1위 카드에만 불
{'from': '그 기계에 무엇을', 'bg': 'ph_humidifier_night', 'items': [
    cover('+0.02'),
    ranks('+0.1', n=7, now=1, nowat='마지막에', top=330),
    tag('맨 마지막에 공개', '마지막에', 700, 640, icon='lock', tone='dark', size=62),
]},
# 0:26 같은 우유 진열대
{'from': '같은 우유 진열대', 'enter': 'flash', 'bg': 'ph_milk_aisle', 'items': [
    tag('같은 우유 진열대', '우유', 560, 420, icon='building-store', size=80),
]},
# 0:29 8년 새 +4,000억 vs -4,000억 (좌우 대비)
{'from': '한쪽 회사는', 'enter': 'slide', 'bg': 'ph_milk_aisle', 'items': [
    cover('+0.02'),
    raw('<style>.side{top:200px; gap:34px}</style>'),
    *split('+0.05', vs=True),
    side('l', '+0.1', logo('maeil', '+0.1', 0, 0, h=72), tag('8년 새 매출', '+0.2', 0, 0, icon='trending-up', tone='green', size=56),
         roll(0, 4000, '가까이', y=0, size=170, prefix='+', suffix='억', tone='good', dur=1.0)),
    side('r', '바로', logo('namyang', '바로', 0, 0, h=72), tag('같은 기간', '바로', 0, 0, icon='trending-down', tone='red', size=56),
         roll(0, 4000, '바로', y=0, size=170, prefix='-', suffix='억', tone='bad', dur=1.0)),
]},
# 0:36 같은 마트 · 같은 저출산 · 같은 불황 → 경기 탓? → 아닙니다 (통념 깨기 펀치)
{'from': '같은 마트', 'enter': 'mask', 'bg': 'ph_mart_crowd_wide', 'items': [
    cover('+0.02'),
    tag('같은 마트', '마트', 160, 160, icon='building-store', tone='dark', size=72),
    tag('같은 저출산', '저출산', 160, 310, icon='users', tone='dark', size=72),
    tag('같은 불황', '불황이었습니다', 160, 460, icon='trending-down', tone='dark', size=72),
    tag('경기 탓?', '탓일까요', 1060, 260, icon='alert-triangle', size=84, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=610, size=170),
]},
]
