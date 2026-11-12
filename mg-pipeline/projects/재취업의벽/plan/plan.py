"""재취업의벽 (사라지는 직업 3탄 · 은퇴 후 재취업의 벽 TOP5) — 장면 계획 (2026-11-12).
절대 규칙: 제목·썸네일·첫 도입부 일치 → 첫 화면에 썸네일 문구 그대로(thumbtext). 인트로 45초(5위 0:44) · 움직이는 애니메이션 10~20초 ·
그림은 대본 문장과 1:1(input/그림_대본대조.json) · 스톡 7일 텀·한 영상 1회 · 쿵 5회 이하 · clist 본문 40%+."""
from gen import (puppet, tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw, flow,
                 mgbg, qbadge, rankbadge, polaroid, intro30, kin, cutsfx, clist, droppile, thumbtext)
SOFT = raw('<style>.bg{--dark:.5; --blur:0px}</style>')
CYAN = raw('<style>.tt .y{color:#18e6ff}</style>')      # 썸네일 둘째 줄 하늘색과 같게
# 첫 프레임 = 썸네일처럼 선명하게: 장면 등장 효과(투명·흐림에서 시작) 끄기 (나갈 때 효과는 유지)
CRISP = raw('<style>.scene{animation: sOut .26s var(--exit) forwards cubic-bezier(.6,0,.9,.4) !important}</style>')

PLAN = [
# ================= 인트로 (0:00~0:45) =================
{'from': '경비도 안 받아 줘요', 'bg': [('g_guard_booth', None)], 'cam': [('push', '+0.0', 35, 50, 1.08)], 'items': [
    intro30(), CRISP, raw('<style>.bg{--dark:.35; --blur:0px}</style>'),
    thumbtext('"경비도 안 받아줘요"', '교장 선생님도 대기업 임원도', '60 넘으면 갈 곳이 없습니다', None), CYAN,
    puppet('c_oldman', '+1.2', 1500, 470, w=300, move='walk', dx=-1700, dur=8.0),   # 그림이 왼쪽을 보고 있어 반전 없이 왼쪽으로 (2026-11-12 뒷걸음질 수정)
]},
{'from': '서울 중구의 한 인력파견업체', 'enter': 'zoom', 'bg': [('g_agency_resumes', None)], 'cam': [('push', '+0.0', 40, 45, 1.1)], 'items': [
    intro30(), SOFT,
    kin('서울 중구 · *인력파견업체*', '+0.05', y=110, size=90, mode='slide', x=90, w=1100, until='경비원 한 명'),
    kin('경비원 *1명* 공고에', '경비원 한 명', y=110, size=100, mode='drop'),
    droppile('c_resume', '이력서가', 30, 10, 140, 650, w=95, gap=8, every=0.05),
    roll(0, 170, '백칠십', y=260, size=210, suffix='장', tone='bad', dur=1.6, x=1150),
]},
{'from': '일하는 쉰다섯 살 이상이', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('teal'),
    kin('일하는 55세 이상', '+0.0', y=150, size=96, mode='drop'),
    roll(0, 1000, '천만', y=300, size=220, suffix='만 명', tone='good', dur=1.6),
    stamp('역대 처음', '처음으로', x=1250, y=600, size=110, rot=-7),
]},
{'from': '눈높이 탓일까요', 'enter': 'wipe', 'bg': [('g_resume_line', None)], 'cam': [('push', '+0.0', 60, 45, 1.12)], 'items': [
    intro30(), SOFT,
    kin('*눈높이* 탓?', '+0.0', y=140, size=130, mode='pop', until='이 백칠십'),
    kin('이미 !바닥까지! 낮춘 / 170명', '이 백칠십', y=140, size=116, mode='drop'),
]},
{'from': '오늘은 은퇴 후 재취업 현실을', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('은퇴 후 / *재취업 현실* TOP5', '+0.0', y=230, size=140, mode='pop', sfx='whoosh'),
]},
{'from': '교단을 떠난 분이 체력 인증서를', 'enter': 'zoom', 'bg': [('g_principal_gate', None)], 'cam': [('push', '+0.0', 55, 40, 1.15)], 'items': [
    intro30(), raw('<style>.bg{--dark:.45; --blur:4px}</style>'),
    kin('교장 선생님이 / *체력 인증서*를 들고', '+0.05', y=150, size=110, mode='pop'),
]},
{'from': '그리고 경비 일자리를 두고', 'enter': 'flash', 'bg': [('g_young_guard', None)], 'cam': [('crash', '이십 대', 50, 45, 1.25)], 'items': [
    intro30(), raw('<style>.bg{--dark:.45; --blur:4px}</style>'),
    kin('경비 자리도 / !20대!와 경쟁', '이십 대', y=150, size=124, mode='pop'),
]},
{'from': '오 위부터 보겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    intro30(), mgbg('dusk'),
    kin('*5위*부터', '+0.0', y=300, size=170, mode='pop', sfx='whoosh'),
]},
]
try:
    from plan_body import BODY
except ImportError:
    BODY = [{'from': '삼성전자에서 삼십이 년을', 'bg': None, 'items': [mgbg('teal')]}]   # 본문 작성 전 자리 표시
PLAN += BODY
