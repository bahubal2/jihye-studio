"""온수매트 TOP5 — 장면 계획. 규칙(2026-11-09~): 인트로 40초, 첫 10초는 제작 그림(스톡 금지), 인트로만 긴박 음악, 쿵 5회 이하, clist 본문 40%+, 재탕 0.
그림: Gemini(g_*), 실사 스톡(v:s_*), 모션그래픽."""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.55; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')

PLAN = [
# ================= 인트로 (0:00~0:39) =================
{'from': '십이월, 미국 북부의', 'enter': 'flash', 'bg': [('g_camp_blizzard', None), ('g_tent_frost', '영하')], 'cam': [('push', '+0.0', 50, 45, 1.06), ('crash', '영하', 50, 40, 1.3)], 'items': [
    intro30(), raw('<style>.bg{--dark:.72; --blur:0px}</style>'), cutsfx('영하'),
    kin('12월 / 미국 북부 *겨울 캠핑장*', '+0.1', y=170, size=110, mode='drop', until='영하'),
    kin('영하 / !20도!', '영하', y=200, size=200, mode='pop'),
]},
{'from': '침낭을 세 겹이나', 'enter': 'zoom', 'bg': [('g_cold_man', None)], 'cam': [('push', '+0.0', 45, 50, 1.12), ('shake', '얼음장', 50, 50, 1.0)], 'items': [
    intro30(), SOFT,
    kin('침낭 *3겹*을 덮어도', '+0.1', y=150, size=104, mode='drop', until='얼음장'),
    kin('등이 / !얼음장!', '얼음장', y=200, size=180, mode='pop'),
]},
{'from': '그런데 옆 텐트 부부는', 'enter': 'wipe', 'bg': [('g_split_contrast', None), ('g_mat_boiler', '바닥에')], 'cam': [('push', '+0.0', 72, 40, 1.18), ('crash', '온수매트', 50, 60, 1.25)], 'items': [
    intro30(), raw('<style>.bg{--dark:.85; --blur:0px}</style>'), cutsfx('바닥에'),
    kin('옆 텐트 부부는 / *반팔 차림*', '+0.2', y=130, size=100, mode='slide', until='바닥에'),
    kin('바닥에 깔린 건 / *한국 온수매트* 한 장', '바닥에', y=150, size=110, mode='drop'),
]},
{'from': '이상한 일입니다', 'enter': 'flash', 'bg': [('g_1912', None)], 'cam': [('push', '전기담요를', 40, 45, 1.1)], 'items': [
    intro30(), SOFT,
    kin('이상한 일', '+0.0', y=330, size=170, mode='pop', until='전기담요를'),
    kin('전기담요를 처음 만든 나라 / = *미국*', '전기담요를', y=150, size=100, mode='drop'),
]},
{'from': '그런 나라의 캠핑족이', 'enter': 'zoom', 'bg': [('v:s_snow_camp_night', None)], 'cam': [('pull', '+0.0', 50, 50, 1.15)], 'items': [
    intro30(), raw('<style>.bg{--dark:.6; --blur:0px}</style>'),
    kin('왜 / *한국 매트 한 장*에 / !놀랐을까?!', '+0.2', y=180, size=120, mode='mix'),
    qbadge('왜 놀랐나?', '놀랐을까요', pop=True),
]},
{'from': '일 위에는 우리 아버지', 'enter': 'flash', 'bg': [('g_agungi', None), ('g_basement', '지하실까지')], 'cam': [('push', '+0.0', 35, 55, 1.12), ('crash', '지하실까지', 30, 45, 1.25)], 'items': [
    intro30(), SOFT, cutsfx('지하실까지'),
    kin('*1위* / 아버지 세대의 !아궁이!', '+0.1', y=150, size=110, mode='drop', until='지하실까지'),
    kin('→ 미국 집 / *지하실*까지', '지하실까지', y=180, size=130, mode='pop'),
]},
{'from': '순위는 미국 사람들이', 'enter': 'wipe', 'bg': None, 'items': [
    intro30(), mgbg('teal'),
    kin('순위 기준', '+0.0', y=150, size=90, mode='drop'),
    kin('미국이 *놀란 이유*를 / 얼마나 크게 설명하나', '놀란', y=320, size=100, mode='slide'),
]},
{'from': '오 위부터 같이', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('*5위*부터', '+0.0', y=300, size=220, mode='pop', sfx='whoosh'),
]},
]
try:
    from plan_body import BODY
except ImportError:
    BODY = [{'from': '오 위는 물건', 'bg': None, 'items': [mgbg('teal')]}]   # 본문 작성 전 자리 표시
PLAN += BODY
