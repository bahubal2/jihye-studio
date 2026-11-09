"""절임배추 단독 다큐 — 장면 계획.
2026-11-09 규칙: 인트로 40초(첫 막 0:36), 인트로만 긴박·미스터리 음악, 쿵 5회 이하, 분할 카드 체크리스트(clist) 본문 40%+, 재탕 0, 교체 80%."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, article, bubble, group, raw,
                 puppet, particles, mgbg, qbadge, polaroid, intro30, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.55; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')
REENACT = tag('재연', '+0', 1700, 40, tone='ghost', size=34)

PLAN = [
# ================= 인트로 (0:00~0:36) =================
{'from': '김장 날 아침', 'enter': 'flash', 'bg': [('i_door_boxes', None), ('i_wilted', '테이프를'), ('v:s_trash', '그 집의 김장은')], 'cam': [('push', '+0.0', 50, 60, 1.22)], 'items': [
    intro30(), SOFT, REENACT, cutsfx('그 집의 김장은'),
    kin('김장 날 아침 / 절임배추 *세 상자*', '+0.1', y=170, size=104, mode='drop', until='테이프를'),
    kin('테이프를 뜯자 / *시큼한 냄새*', '테이프를', y=200, size=116, mode='slide', until='그 집의 김장은'),
    kin('김장이 / !멈췄다!', '멈췄습니다', y=230, size=160, mode='pop', sfx='hit'),
]},
{'from': '김장하는 집 열 집 중 여섯', 'enter': 'zoom', 'bg': [('v:s_field', None), ('v:s_kimchi', '그런데 해마다'), ('i_suspect', '흔히들')], 'items': [
    intro30(), SOFT, cutsfx('그런데 해마다', '흔히들'),
    group('그런데 해마다', igrid('home', 10, '열 집', lit=6, litat='여섯이', cols=10, y=200, size=110, tone='good'),
          kin('10집 중 *6집*이 산다', '여섯이', y=430, size=100)),
    kin('그런데 해마다 / !물러서 버렸다!', '그런데 해마다', y=220, size=120, mode='pop', until='흔히들'),
    kin('범인은 / *중국산?*', '흔히들', y=230, size=150, mode='pop', sfx='whoosh'),
]},
{'from': '그런데 지난해 김장철', 'enter': 'wipe', 'bg': [('i_restaurant_kimchi', None), ('v:s_kimchi_red', '범인은 따로')], 'cam': [('cardL', '+0.4')], 'items': [
    CLEAR, cutsfx('범인은 따로'),
    clist([('지난해 원산지 위반 *142곳*', '백사십이'), ('그중 식당 !108곳!', '백여덟'), ('대부분 *식당 김치 접시*', '식당이었습니다')], x=1025, y=300, size=64, until='범인은 따로'),
    kin('범인은 / *따로 있었다*', '범인은 따로', x=1040, y=330, w=840, size=116, mode='pop', sfx='whoosh'),
]},
{'from': '단서는 상자 안이 아니라', 'enter': 'flash', 'bg': [('i_invoice', None)], 'cam': [('crash', '송장에', 50, 45, 1.45)], 'items': [
    intro30(), SOFT,
    kin('단서는 / 상자 *안*이 아니라 *겉*', '+0.1', y=180, size=110, mode='drop', until='송장에'),
    kin('택배 송장의 / *날짜*', '송장에', y=220, size=150, mode='pop'),
    stamp('날짜', '날짜입니다', x=1380, y=620, size=120),
]},
{'from': '상자를 연 그 집으로', 'enter': 'fade', 'bg': None, 'items': [mgbg('teal')]},   # 본문 자리(임시)
]
