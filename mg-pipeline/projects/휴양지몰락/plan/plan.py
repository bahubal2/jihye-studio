"""휴양지몰락 TOP5 — 장면 계획 (2026-11-12).
규칙: 인트로 40초대(5위 0:47) · 인트로 움직이는 애니메이션 10~20초(셔터·여행객 쏟아짐·좌석 쌓기·숫자·도장·걸어가는 인형) ·
첫 10초 제작 그림 · 그림은 대본 문장과 1:1(input/그림_대본대조.json) · 스톡 7일 텀·한 영상 1회 · 쿵 5회 이하 · clist 본문 40%+."""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist, droppile, shutter, thumbtext)
SOFT = raw('<style>.bg{--dark:.5; --blur:0px}</style>')

PLAN = [
# ================= 인트로 (0:00~0:47) =================
{'from': '괌 투몬 거리입니다', 'enter': 'flash', 'bg': [('g_tumon_busy', None)], 'cam': [('push', '+0.0', 40, 55, 1.1)], 'items': [
    thumbtext('괌 면세점도 셔터 내렸다', '차라리 일본 가고 맙니다', '한국인 발길 뚝 끊긴 휴양지 TOP5', '셔터를'),   # 첫 화면 = 썸네일 문구 (2026-11-12 절대 규칙)
    intro30(), raw('<style>.bg{--dark:.3; --blur:0px}</style>'),
    shutter('셔터를'),
]},
{'from': '한국인 발길이 뚝', 'enter': 'zoom', 'bg': [('g_tumon_empty', None)], 'cam': [('push', '+0.0', 60, 50, 1.12)], 'items': [
    intro30(), SOFT,
    kin('한국인 발길 *뚝* / 끊긴 해외 휴양지', '+0.05', y=140, size=118, mode='pop'),
]},
{'from': '그런데 작년 한 해', 'enter': 'wipe', 'bg': [('g_airport_crowd', None)], 'cam': [('push', '+0.0', 50, 40, 1.08)], 'items': [
    intro30(), SOFT,
    kin('작년 해외로 나간 국민', '+0.1', y=110, size=84, mode='drop'),
    roll(0, 2955, '이천구백', y=250, size=200, suffix='만 명', tone='good', dur=1.6),
    puppet('c_traveler', '+0.3', -200, 560, w=300, move='walk', dx=2300, dur=5.0),
    stamp('코로나 전보다 많다', '코로나', x=1180, y=520, size=84, rot=-6),
]},
{'from': '다들 어디로 갔을까요', 'enter': 'flash', 'bg': [('g_japan_street', None)], 'cam': [('crash', '일본입니다', 50, 45, 1.2)], 'items': [
    intro30(), SOFT,
    kin('다들 *어디로*?', '+0.0', y=150, size=120, mode='pop', until='일본입니다'),
    kin('!일본!', '일본입니다', y=110, size=150, mode='pop'),
    roll(0, 946, '구백', y=290, size=210, suffix='만 명', tone='bad', dur=1.4),
    stamp('역대 최다', '역대', x=1250, y=560, size=120, rot=-8),
    tag('"차라리 일본 가고 맙니다"', '역대', None, 770, tone='red', size=64),   # 제목 따옴표 문구를 도입부 화면에 (녹음엔 없어서 글자로)
]},
{'from': '바가지 탓일까요', 'enter': 'wipe', 'bg': [('g_price_board', None), ('g_japan_arrival', '그래도 한국인은')], 'cam': [('push', '+0.0', 55, 40, 1.08)], 'items': [
    intro30(), SOFT,
    kin('!바가지! 탓?', '+0.0', y=130, size=130, mode='pop', until='그래도 한국인은'),
    tag('일본도 외국인 요금 ↑', '외국인에게', 1080, 380, size=56, tone='bad', until='그래도 한국인은'),
    kin('그래도 일본으로 *우르르*', '그래도 한국인은', y=110, size=104, mode='drop'),
    raw('<style>.bg{--dark:.68; --blur:2px}</style>'),
    droppile('c_traveler', '우르르', 16, 8, 120, 600, w=180, gap=26, every=0.07),
]},
{'from': '오늘 순위에는', 'enter': 'zoom', 'bg': [('g_empty_cabin', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    intro30(), raw('<style>.bg{--dark:.45; --blur:0px}</style>'),
    droppile('c_seat', '+0.15', 36, 12, 110, 640, w=62, gap=8, every=0.045, sfx='tick'),
    kin('*180석*에 손님 !3명!', '손님이', y=120, size=120, mode='pop'),
]},
{'from': '그리고 일 위는', 'enter': 'flash', 'bg': [('g_island_teaser', None)], 'cam': [('push', '+0.0', 50, 60, 1.12)], 'items': [
    intro30(), raw('<style>.bg{--dark:.45; --blur:6px}</style>'),
    kin('1위는', '+0.0', y=120, size=110, mode='drop'),
    kin('리조트는 *다시 열고* / 비행기는 !사라진! 섬', '리조트는', y=270, size=104, mode='pop'),
    qbadge('어디일까?', '사라진 섬', pop=True),
]},
{'from': '부터 보겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('*5위*부터', '+0.0', y=300, size=170, mode='pop', sfx='whoosh'),
]},
]
try:
    from plan_body import BODY
except ImportError:
    BODY = [{'from': '비행기는 그대로 뜨는데', 'bg': None, 'items': [mgbg('teal')]}]   # 본문 작성 전 자리 표시
PLAN += BODY
