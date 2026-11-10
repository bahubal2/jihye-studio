"""온수매트 (단독 주제 다큐: 인트로·5막·결말) — 장면 계획. 규칙(2026-11-09~): 인트로 40초, 첫 10초는 제작 그림(스톡 금지),
인트로만 긴박 음악, 쿵 5회 이하, clist 본문 40%+, 재탕 0. 그림: Gemini(g_*), 실사 스톡(v:s_*), 모션그래픽.
(순위형 대본은 input/script_순위형.txt · _순위형/ 에 보관)"""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.55; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')

PLAN = [
# ================= 인트로 (0:00~0:38.6) =================
{'from': '영하 이십 도의 미국', 'enter': 'flash', 'bg': [('g_camp_blizzard', None), ('g_tent_frost', '캠핑장입니다')], 'cam': [('push', '+0.0', 50, 45, 1.06), ('crash', '캠핑장입니다', 50, 40, 1.3)], 'items': [
    intro30(), raw('<style>.bg{--dark:.72; --blur:0px}</style>'), cutsfx('캠핑장입니다'),
    kin('영하 !20도! / 미국 *겨울 캠핑장*', '+0.1', y=170, size=124, mode='drop'),
]},
{'from': '한 텐트에서는 침낭을', 'enter': 'zoom', 'bg': [('g_cold_man', None)], 'cam': [('push', '+0.0', 45, 50, 1.12), ('shake', '시려', 50, 50, 1.0)], 'items': [
    intro30(), SOFT,
    kin('침낭 *3겹*을 덮어도', '+0.1', y=150, size=104, mode='drop', until='시려'),
    kin('등이 / !얼음장!', '시려', y=200, size=180, mode='pop'),
]},
{'from': '옆 텐트 부부는', 'enter': 'wipe', 'bg': [('g_split_contrast', None), ('g_mat_boiler', '차이는')], 'cam': [('push', '+0.0', 72, 40, 1.18), ('crash', '온수매트', 50, 60, 1.25)], 'items': [
    intro30(), raw('<style>.bg{--dark:.85; --blur:0px}</style>'), cutsfx('차이는'),
    kin('옆 텐트 부부는 / *반팔 차림*', '+0.1', y=130, size=104, mode='slide', until='차이는'),
    kin('차이는 / *한국 온수매트* 한 장', '차이는', y=150, size=116, mode='drop'),
]},
{'from': '이상한 일입니다', 'enter': 'flash', 'bg': [('g_1912', None)], 'cam': [('push', '전기담요를', 40, 45, 1.1)], 'items': [
    intro30(), SOFT,
    kin('이상한 일', '+0.0', y=330, size=170, mode='pop', until='전기담요를'),
    kin('전기담요를 처음 만든 나라 / = *미국*', '전기담요를', y=150, size=100, mode='drop'),
]},
{'from': '그런 나라의 캠핑족이', 'enter': 'zoom', 'bg': [('v:s_snow_camp_night', None)], 'cam': [('pull', '+0.0', 50, 50, 1.15)], 'items': [
    intro30(), raw('<style>.bg{--dark:.6; --blur:0px}</style>'),
    kin('왜 / *매트 한 장*에 / !놀랐을까?!', '+0.2', y=180, size=124, mode='mix'),
    qbadge('왜 놀랐나?', '놀랐을까요', pop=True),
]},
{'from': '한국 기술이 좋아서일까요', 'enter': 'flash', 'bg': [('g_smartbed', None)], 'cam': [('push', '미국에도', 45, 60, 1.12)], 'items': [
    intro30(), raw('<style>.bg{--dark:.7; --blur:0px}</style>'),
    kin('한국 *기술*이 / 좋아서?', '+0.0', y=260, size=150, mode='pop', until='미국에도'),
    kin('미국에도 / !같은 원리! 침대', '미국에도', y=150, size=120, mode='drop'),
]},
{'from': '답은 매트가 아니라', 'enter': 'wipe', 'bg': [('g_basement', None)], 'cam': [('push', '+0.0', 45, 50, 1.08), ('crash', '기계에', 40, 50, 1.35)], 'items': [
    intro30(), SOFT,
    kin('답은 / 매트가 !아니라!', '+0.1', y=150, size=120, mode='drop', until='지하실마다'),
    kin('미국 집 *지하실*의 / !한 기계!', '지하실마다', y=170, size=124, mode='pop'),
]},
{'from': '먼저 그 남자의 등이', 'enter': 'flash', 'bg': [('v:s_campfire_snow', None)], 'cam': [('pull', '+0.0', 50, 55, 1.12)], 'items': [
    intro30(), raw('<style>.bg{--dark:.62; --blur:0px}</style>'),
    kin('먼저 / 그 남자의 *등*부터', '+0.1', y=260, size=140, mode='pop', sfx='whoosh'),
]},
]
try:
    from plan_body import BODY
except ImportError:
    BODY = [{'from': '침낭을 세 겹 덮었는데', 'bg': None, 'items': [mgbg('teal')]}]   # 본문 작성 전 자리 표시
PLAN += BODY
