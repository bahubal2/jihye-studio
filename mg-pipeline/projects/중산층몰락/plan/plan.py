"""중산층몰락 (폐업 100만 시대 · 은퇴자 노후자금 증발) — 장면 계획 (2026-11-14).
절대 규칙: 제목·썸네일·첫 도입부 일치 → 첫 화면에 썸네일 문구 그대로(thumbtext, 0초부터 선명).
인트로 0:00~0:33 · 전환 문단 0:33~0:57 (밝은 골목으로 그림·말투가 풀린다).
화면 스타일은 이 영상의 레퍼런스(돈흐르네)를 따라 실사 다큐 사진풍 · 움직이는 영상은 글자 없는 3컷만(768P·10초).
그림은 대본 문장과 1:1(input/그림_대본대조.json) · 스톡 7일 텀·한 영상 1회 · 쿵 5회 이하.
녹음 파일에 담당자 인트로 배경음악이 이미 섞여 있음(0~52초) → mix_bgm 에서 인트로 음악을 따로 깔지 않는다."""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw, flow,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist, droppile, thumbtext, shutter)
SOFT = raw('<style>.bg{--dark:.66; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.8; --blur:0px}</style>')
CALM = raw('<style>.bg{--dark:.95; --blur:0px}</style>')        # 전환 문단: 밝고 따뜻한 골목 그대로 (--dark 는 밝기: 클수록 밝다)
RED = raw('<style>.tt .y{color:#ff3b3b}</style>')                 # 썸네일 셋째 줄 빨강과 같게
CRISP = raw('<style>.scene{animation: sOut .26s var(--exit) forwards cubic-bezier(.6,0,.9,.4) !important}</style>')

PLAN = [
# ================= 인트로 (0:00~0:33) — 2026-11-14 v2: 레퍼런스(돈흐르네 5XcxqFJOd3U)처럼 실사 다큐 사진풍 =================
# 글자 있는 장면 = 멈춘 사진 + 카메라 이동 + 글자 움직임 / 글자 없는 장면 = 768P·10초 영상(원래 속도)
{'from': '월급 빼고 다 올랐는데', 'bg': [('ph_wallet_couple', None)], 'cam': [('push', '+0.0', 55, 50, 1.1)], 'items': [
    intro30(), CRISP, CALM,
    thumbtext('폐업 100만 시대', '월급 빼고 다 올랐는데', '누가 돈을 씁니까', '대한민국'), RED,
    kin('노후자금이 / *조용히 증발*', '노후자금이', y=150, size=124, mode='drop'),
]},
{'from': '서울 황학동', 'enter': 'zoom', 'bg': [('ph_hwanghak_fridges', None)], 'items': [      # 영상 (글자 없음)
    intro30(), CALM, cutsfx('+0.0'),
]},
{'from': '이상한 건, 올해 나라가', 'enter': 'flash', 'bg': [('ph_export_port', None), ('ph_empty_wallet_table', '그런데 우리')], 'cam': [('push', '+0.0', 50, 50, 1.12)], 'items': [
    intro30(), SOFT, cutsfx('+0.0', '그런데 우리'),
    kin('나라 실질 소득 / *49년 만에* 최대', '+0.05', y=120, size=110, mode='pop', until='그런데 우리'),
    kin('그런데 우리 지갑만 / !텅텅!', '그런데 우리', y=120, size=124, mode='drop'),
]},
{'from': '끈을 따라가 보니', 'enter': 'zoom', 'bg': [('ph_shutter_two_men', None)], 'items': [      # 영상 + 끝에 도장 하나
    intro30(), CALM, cutsfx('+0.0'),
    stamp('같은 또래', '같은 또래', x=1180, y=150, size=124, rot=-6),
]},
# ================= 전환 문단 (0:33~0:57) — 말투·그림이 밝아지며 풀린다 =================
{'from': '사실 이건 남의 동네', 'enter': 'fade', 'bg': [('ph_alley_morning', None)], 'items': [      # 영상 (글자 없음) — 밝은 아침 골목으로 긴장이 풀린다
    intro30(), CALM,
]},
{'from': '무슨 일이 있었는지', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('teal'),
    clist([('무슨 일이 *있었나*', '무슨 일이'), ('흔한 얘기, *맞나?*', '흔히들'), ('!진짜 원인!은 어디?', '진짜 원인')], x=470, y=270, size=86),
]},
{'from': '그리고 끝에는 같은 은퇴 세대', 'enter': 'fade', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('같은 은퇴 세대인데 / *끄떡없는 분들*', '+0.05', y=230, size=110, mode='rise', until='그분들이'),
    kin('생각보다 / *거창하지 않았다*', '그분들이', y=230, size=120, mode='pop'),
]},
]
try:
    from plan_body import BODY
except ImportError:
    BODY = [{'from': '이 거리는 원래 돈이', 'bg': None, 'items': [mgbg('teal')]}]   # 본문 작성 전 자리 표시
PLAN += BODY
