"""전쟁사재기 (단독 다큐: 우리 집은 얼마나 대비하나) — 장면 계획.
규칙(2026-11-10~): 인트로 40초 · 인트로에 움직이는 애니메이션 10~20초(말풍선·병 쌓기·숫자·가방·도장) · 첫 10초 제작 그림 ·
그림은 대본 문장과 1:1 · 스톡 7일 텀·한 영상 1회 · 쿵 5회 이하 · clist 본문 40%+."""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist, droppile)
SOFT = raw('<style>.bg{--dark:.55; --blur:0px}</style>')

PLAN = [
# ================= 인트로 (0:00~0:35) · 0~18초 움직이는 애니메이션 =================
{'from': '이러다 전쟁 나는 거 아냐', 'enter': 'flash', 'bg': [('g_phone_night', None)], 'cam': [('push', '+0.0', 30, 45, 1.08)], 'items': [
    intro30(), raw('<style>.bg{--dark:.45; --blur:0px}</style>'),
    bubble('이러다 전쟁 나는 거 아냐?', '+0.05', 860, 120, size=58, tone='red'),
    bubble('생수 사 둬야 하나…', '+0.7', 1080, 290, size=52),
    bubble('마트 갔더니 텅텅 비었대', '이천이십육', 940, 440, size=52),
    bubble('재난 가방 400만 원 샀어', '십일월', 900, 590, size=52),
    bubble('사재기 인증합니다', '휴대폰', 960, 740, size=52),
    kin('2026년 11월 초', '이천이십육', y=800, size=84, mode='slide', x=100, w=760),
]},
{'from': '어느 집 베란다에는', 'enter': 'zoom', 'bg': [('g_veranda', None)], 'cam': [('push', '+0.0', 35, 70, 1.05)], 'items': [
    intro30(), raw('<style>.bg{--dark:.3; --blur:0px}</style>'),
    droppile('c_bottle', '+0.1', 36, 12, 80, 640, w=66, gap=6, every=0.08),
    roll(0, 36, '삼십육', y=150, size=210, suffix='병', tone='bad', dur=2.6, x=1150),
    kin('2리터 생수', '+0.2', y=80, size=80, mode='drop', x=1150, w=700),
]},
{'from': '사백만 원짜리 재난 가방', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    puppet('c_bag', '+0.1', 220, 230, w=560, move='hop', sfx='whoosh'),
    roll(0, 400, '사백만', y=300, size=220, suffix='만 원', tone='bad', dur=1.6, x=900),
    kin('재난 가방 *한 번에*', '+0.3', y=140, size=86, mode='drop', x=900, w=900),
]},
{'from': '급기야 마트 한쪽에는', 'enter': 'zoom', 'bg': [('g_empty_shelf', None)], 'cam': [('crash', '품절', 45, 45, 1.3)], 'items': [
    intro30(), SOFT,
    kin('급기야 / !품절!까지', '+0.1', y=150, size=130, mode='pop'),
    stamp('품절', '품절', x=780, y=430, size=170, rot=-10),
]},
{'from': '그런데 우리 군은 그 불씨를', 'enter': 'wipe', 'bg': [('g_observatory', None)], 'cam': [('push', '+0.0', 35, 40, 1.15)], 'items': [
    intro30(), SOFT,
    kin('그런데 우리 군은', '+0.1', y=140, size=96, mode='drop', until='보여주기라고'),
    stamp('보여주기', '보여주기라고', x=1150, y=560, size=130, rot=-6),
]},
{'from': '그렇다면 무엇이 진열대를', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('teal'),
    kin('무엇이 / *진열대*를 비웠나?', '+0.0', y=200, size=124, mode='pop', until='진짜 궁금한'),
    kin('진짜 궁금한 건', '진짜 궁금한', y=330, size=120, mode='drop'),
    qbadge('무엇이 비웠나?', '+0.2', pop=True),
]},
{'from': '우리 집은, 얼마나 대비하면', 'enter': 'zoom', 'bg': [('g_couple_check', None)], 'cam': [('push', '+0.0', 40, 60, 1.12)], 'items': [
    intro30(), SOFT,
    kin('*우리 집*은 / 얼마나 대비해야?', '+0.1', y=150, size=116, mode='pop', until='그 답은'),
    kin('생각보다 *싸고* / 생각보다 *가깝다*', '그 답은', y=170, size=116, mode='drop'),
]},
{'from': '같이 짚어 보시죠', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('같이 *짚어* 보시죠', '+0.0', y=300, size=150, mode='pop', sfx='whoosh'),
]},
]
try:
    from plan_body import BODY
except ImportError:
    BODY = [{'from': '시월 하순, 경기도 김포', 'bg': None, 'items': [mgbg('teal')]}]   # 본문 작성 전 자리 표시
PLAN += BODY
