"""숨은명소 TOP5 — 3위 거제 저도 · 2위 나주 금성산 (자막 92~182)."""
from gen import (hook, flashhit, tag, stamp, big, cover, glow, raw, stack, card, bars, flipcard, roll, igrid,
                 puppet, particles, mgbg, rankbadge)
BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
SOFT = raw('<style>.bg{--dark:.7; --blur:0px}</style>')
B = [
# ================= 3위 =================
{'from': '천구백칠십이 년, 경남 거제', 'enter': 'fade', 'bg': 'i_jeodo_island', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    BRIGHT,
    tag('1972 · 대통령 별장 “청해대”', '청해대라는', 120, 140, icon='calendar', tone='dark', size=56),
    stamp('출입 금지', '닫혔습니다', x=1100, y=520, size=110),
]},
{'from': '삼 위는 거제 저도입니다', 'enter': 'flash', 'bg': [('v:s_island_ferry', None), ('v:s_pine_coast', '일제강점기인')], 'items': [
    SOFT, rankbadge('3', '거제 저도', '삼 위는'),
    card('면적', '43만㎡', '사십삼만', 640, 200, w=640, h=280, vat='사십삼만'),
    tag('1920년대부터 군 기지', '일제강점기인', None, 560, icon='flag', tone='dark', size=54),
]},
{'from': '섬에 내리면 이백 살', 'enter': 'wipe', 'bg': [('v:s_pine_coast', None), ('i_jeodo_island', '거가대교를')], 'items': [
    BRIGHT,
    tag('200살 해송 · 동백숲 · 연리지 정원', '해송과', 120, 140, icon='heart-handshake', tone='dark', size=52),
    puppet('c_boat', '+0.5', -700, 520, w=620, move='walk', dx=2600, dur=16, step=1.4, tilt=1.5, sfx=None),
]},
{'from': '사실 대통령 별장을', 'enter': 'zoom', 'bg': 'i_villa_gate', 'items': [
    cover('+0.02'),
    card('청남대', '2003 개방 · 누구나', '이천삼', 220, 200, w=660, h=300, vat='이천삼'),
    card('저도', '아직 반쯤', '반쯤', 1040, 200, w=660, h=300, vat='반쯤', hot=True),
    tag('해군 작전 기지의 요충지', '요충지', None, 620, icon='alert-triangle', tone='red', size=56),
]},
{'from': '이 섬이 열린 건', 'enter': 'flash', 'bg': 'v:s_island_ferry', 'cam': [('crash', '사십칠 년 만이었죠', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    tag('2019.9.17 개방', '이천십구', None, 150, icon='calendar', tone='dark', size=58),
    big('47년 만', '사십칠 년 만이었죠', y=270, size=200, color='#ffcf4a'),
    tag('궁농항에서 유람선 20분', '이십 분이면', None, 600, icon='map-pin', tone='dark', size=54),
]},
{'from': '그런데 열린 방식이 특이했습니다', 'enter': 'zoom', 'bg': 'i_villa_gate', 'items': [
    cover('+0.02'),
    *stack([('1년 시범 개방', '시범', 'calendar', 'dark'), ('주 5일 · 하루 600명', '육백', 'users', 'red'),
            ('정비 기간엔 다시 닫힘', '정비', 'alert-triangle', 'red'), ('별장 내부는 비공개', '안을', 'user-x', 'dark')], x=200, y=150, gap=135, size=50),
    stamp('반쪽 개방', '반쪽', x=1150, y=560, size=100),
]},
{'from': '여기서 한번 계산해 보겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('cream'),
    tag('국민 5천만 명이 한 번씩 가려면?', '오천만', None, 150, icon='users', tone='dark', size=56),
    roll(0, 319, '삼백 년이', y=290, size=210, suffix='년+', tone='bad', dur=2.4),
    tag('손주의 손주도 순서가 안 올 수도', '손주의', None, 620, icon='alert-triangle', tone='red', size=54),
]},
{'from': '그런데 사람들의 반응은', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    tag('개방 첫해 · 하루 정원의 90%+', '구십', None, 140, icon='trending-up', tone='green', size=56),
    igrid('users', 10, '구십', lit=9, litat='아홉', cols=10, y=320, size=120, tone='good'),
    tag('최소 사흘 전 신청', '사흘', None, 640, icon='calendar', tone='dark', size=54),
]},
{'from': '못 들어가게 할수록', 'enter': 'wipe', 'bg': [('v:s_phone_news', None), ('v:s_seoul_night', '+8')], 'items': [
    cover('+0.02'),
    big('희소성', '희소성이라고', y=240, size=180, color='#ffcf4a'),
    glow('구하기 어려울수록 값어치를 높게 매긴다', '어려울수록', y=600, size=58),
]},
{'from': '다만 저도가 귀한 건', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    *stack([('국방부', '국방부와', 'flag', 'dark'), ('해군', '해군,', 'flag', 'dark'), ('행정안전부', '행정안전부', 'file-invoice', 'dark'),
            ('경상남도', '경상남도', 'map-pin', 'dark'), ('거제시', '거제시', 'map-pin', 'dark')], x=700, y=110, gap=105, size=50),
    tag('다섯 기관이 모두 도장을 찍어야 열린다', '도장을', None, 680, icon='key', tone='red', size=52),
]},
{'from': '자, 여기까지 모인 단서를', 'enter': 'flash', 'bg': 'v:s_seoul_wall', 'items': [
    cover('+0.02'),
    card('화순', '상생 협약', '화순은', 220, 180, w=660, h=280, vat='화순은'),
    card('저도', '5개 기관 협약', '다섯 기관의', 1040, 180, w=660, h=280, vat='다섯 기관의'),
    glow('문을 연 건 세월이 아니라 종이 한 장', '종이', y=540, size=62),
    tag('남은 조각: 군부대가 지키던 산은?', '군부대가', None, 690, icon='scan', tone='dark', size=50),
]},
# ================= 2위 =================
{'from': '나주 시내 어디서든', 'enter': 'fade', 'bg': 'i_geumseong', 'cam': [('push', '+0.1', 50, 40, 1.2)], 'items': [
    BRIGHT,
    tag('높이 451m · 동네 뒷산', '사백오십일', 120, 140, icon='map-pin', tone='dark', size=56),
    big('57년', '오십칠', y=420, size=200, color='#ff5a5a'),
]},
{'from': '이 위는 전남 나주 금성산', 'enter': 'flash', 'bg': [('i_geumseong', None), ('v:s_hike_deck', '+10'), ('v:s_mountain_peak', '+20')], 'items': [
    SOFT, rankbadge('2', '나주 금성산', '이 위는'),
    flipcard('바위가 험해서 막았나?', '등산로는 중턱까지 멀쩡', '바위가', '멀쩡히', y=230, size=72),
    puppet('c_child', '주말이면', -340, 540, w=320, move='enter', dx=500, dur=5),
]},
{'from': '그러면 꼭대기에 귀한', 'enter': 'zoom', 'bg': 'i_geumseong', 'items': [
    cover('+0.02'),
    flipcard('귀한 문화재라도?', '1966 · 정상에 군부대', '문화재라도', '군부대가', y=170, size=72),
    tag('같은 해 무등산 정상에도 방공포대', '무등산', None, 500, icon='alert-triangle', tone='red', size=52),
    tag('무등산도 2022년 말에야 개방 협약', '이천이십이', None, 640, icon='file-invoice', tone='dark', size=50),
]},
{'from': '금성산의 문이 열린 과정은', 'enter': 'wipe', 'bg': [('i_landmine', None), ('v:s_mountain_peak', '+16')], 'items': [
    BRIGHT,
    tag('2023.4 나주시 · 공군 상시 개방 협약', '사월', 120, 140, icon='file-invoice', tone='green', size=52),
    tag('길보다 먼저: 지뢰 제거', '지뢰를', 120, 300, icon='alert-triangle', tone='red', size=56),
    puppet('c_deminer', '지뢰를', -380, 500, w=360, move='walk', dx=900, dur=13, step=0.8),
]},
{'from': '인트로에서 말씀드린, 땅속부터', 'enter': 'flash', 'bg': [('i_deck_peak', None), ('v:s_hike_deck', '+11'), ('v:s_cherry', '+19')], 'items': [
    BRIGHT,
    tag('인트로의 그 산', '인트로에서', 120, 140, icon='key', tone='red', size=56),
    tag('585m 데크 길 · 2024.2 개통', '오백팔십오', 120, 300, icon='map-pin', tone='dark', size=54),
    tag('봄: 왕벚나무 340그루', '왕벚나무', 120, 460, icon='heart-handshake', tone='green', size=54),
]},
{'from': '다만 정상에 올라가 보면', 'enter': 'zoom', 'bg': 'i_deck_peak', 'items': [
    cover('+0.02'),
    card('정상 가림막', '2.5m × 22m', '이 점 오', 640, 160, w=640, h=280, vat='이 점 오'),
    tag('정상은 올라가도, 산 전체를 돌려받은 건 아니다', '돌려받은', None, 500, icon='alert-triangle', tone='red', size=48),
    tag('다 열지도, 다 막지도 않는 절충', '절충이었던', None, 650, icon='scan', tone='dark', size=52),
]},
{'from': '어릴 때 소풍 가던 뒷산을', 'enter': 'wipe', 'bg': [('v:s_mountain_peak', None), ('v:s_seoul_wall', '인트로의')], 'items': [
    BRIGHT,
    glow('그 산을 올려다보며 자란 아이가 할아버지가 됐다', '할아버지가', y=260, size=56),
    tag('1위는 훨씬 무거운 사건 하나로 닫혔다', '무거운', None, 600, icon='key', tone='red', size=52),
]},
{'from': '마지막 질문입니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    tag('질문 ③', '마지막 질문', None, 160, icon='scan', tone='red', size=64),
    big('시범·협약으로 열렸나?', '근거가', y=330, size=96, color='#ffcf4a'),
]},
]
