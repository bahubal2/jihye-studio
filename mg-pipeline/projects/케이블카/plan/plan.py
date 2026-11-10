"""케이블카·출렁다리 몰락 TOP7 — 장면 계획. 규칙(2026-11-09~): 인트로 40초, 인트로만 긴박 음악, 쿵 5회 이하, clist 본문 40%+, 재탕 0.
fal 잔액 없음 → 그림 대신 실사(Pixabay·위키미디어) + 모션그래픽."""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.55; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')

PLAN = [
# ================= 인트로 (0:00~0:37) =================
{'from': '강원도 화천의 아침', 'enter': 'flash', 'bg': [('g_hwacheon_town2', None), ('g_mountain_road', '오십분을'), ('g_checkpoint', '검문을')], 'cam': [('push', '+0.0', 50, 55, 1.04)], 'items': [
    intro30(), raw('<style>.bg{--dark:.75; --blur:0px}</style>'), cutsfx('오십분을', '검문을'),
    puppet('c_shuttle', '+0.0', 140, 650, w=540, move='walk', dx=1750, dur=4.0, step=0.28, tilt=0.8, until='오십분을', sfx=None),
    kin('강원 화천의 아침 / *셔틀버스* 한 대', '+0.1', y=170, size=104, mode='drop', until='오십분을'),
    kin('*50분* 달리고 / 군 검문 !2번!', '오십분을', y=200, size=124, mode='pop'),
]},
{'from': '들어간 돈은', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('들어간 돈', '+0.0', y=150, size=90, mode='drop'),
    roll(0, 371, '삼백칠십일억', y=300, size=250, suffix='억 원', tone='bad'),
]},
{'from': '그런데 작년 한 해 탄 사람을', 'enter': 'zoom', 'bg': [('g_baegam_cablecar', None)], 'cam': [('crash', '오십오', 22, 45, 1.35)], 'items': [
    intro30(), SOFT,
    kin('작년 탄 사람 ÷ 365일', '+0.1', y=180, size=90, mode='slide', until='오십오'),
    kin('하루 / !55명!', '오십오', y=200, size=210, mode='pop', sfx='hit'),
]},
{'from': '같은 세금으로 지은', 'enter': 'wipe', 'bg': [('g_yedang_bridge', None), ('v:s_rope_bridge', '왜 어디는')], 'cam': [('cardL', '+0.2')], 'items': [
    intro30(), CLEAR, cutsfx('왜 어디는'),
    clist([('같은 *세금*', '같은 세금으로'), ('예산 출렁다리 *1,000만 명*', '천만'), ('어디는 하루 !55명!', '오십오')], size=62),
]},
{'from': '처음 내건 기대와', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('teal'),
    kin('기준 = 처음 내건 *기대* ↔ / 지금 남은 *발길*', '+0.1', y=200, size=88, until='그 셔틀버스는'),
    kin('그 셔틀버스는 / *1위*에서 다시', '그 셔틀버스는', y=220, size=110, until='칠 위부터'),
    kin('*7위*부터', '칠 위부터', y=250, size=180, mode='pop', sfx='whoosh'),
]},
{'from': '이천십이 년 가을, 영남알프스', 'enter': 'fade', 'bg': None, 'items': [mgbg('teal')]},   # 본문 자리(임시)
]
