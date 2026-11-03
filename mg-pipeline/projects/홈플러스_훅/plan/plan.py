"""홈플러스 콜드 오픈 (약 12초, 승인 대본 2026-10-30). 뒤에 홈플러스_v2 본편을 붙인다.
2~3초마다 컷, 장면마다 배경 영상 교체. 효과음은 숫자·도장·법원 세 군데 위주로만."""
from gen import (raw, tag, logo, stamp, roll, split, side, article, glow, cover)

PLAN = [
# 0:00 하루 11억을 판 1등 매장 (번쩍 열기, 재개장 인파 클립)
{'from': '하루 11억을', 'enter': 'flash', 'bg': 'ph_reopen_crowd', 'items': [
    logo('homeplus', '+0.05', 120, 150, h=64),
    tag('하루 매출', '+0.05', 730, 200, icon='trending-up', tone='green', size=66),
    roll(0, 11, '+0.15', y=340, size=300, suffix='억', tone='good', dur=1.0),
    stamp('전국 1등', '매장', x=1260, y=640, size=120),
]},
# 0:02 그런데 매일 11억이 — 좌우 대비 (돈 스톡)
{'from': '그런데 매일', 'enter': 'slide', 'bg': 'st_money', 'items': [
    raw('<style>.side{top:250px} .side{gap:40px}</style>'),
    *split('+0.02', vs=True),
    side('l', '+0.05', tag('하루 매출', '+0.05', 0, 0, icon='trending-up', tone='green', size=58),
         roll(11, 11, '+0.05', y=150, size=250, suffix='억', tone='good', dur=.1)),
    side('r', '매일', tag('매일 나가는 돈', '매일', 0, 0, icon='receipt', tone='red', size=58),
         roll(0, 11, '매일', y=150, size=250, suffix='억', tone='bad', dur=.9)),
]},
# 0:04 문 열기도 전에 월세로 (셔터 클립)
{'from': '문 열기도', 'enter': 'mask', 'bg': 'ph_shutter', 'items': [
    cover('+0.02'),
    tag('문 열기도 전에', '문', 560, 230, icon='lock', tone='dark', size=70),
    glow('월세로 나갔다', '월세로', y=520, size=130),
]},
# 0:07 매출은 늘었는데 왜 법원으로? (법원 계단 + 다시 쓴 기사 카드)
{'from': '매출은 늘었는데', 'enter': 'slide', 'bg': 'ph_court_steps', 'items': [
    article('파이낸셜뉴스', '2025. 3. 4', '홈플러스, 기업회생 신청… 법원 같은 날 개시 결정', '+0.05', mark='기업회생', markat='법원으로', x=520, y=150),
    tag('매출은 늘었는데', '매출은', 120, 640, icon='trending-up', tone='green', size=62),
    tag('왜 법원으로?', '법원으로', 1000, 760, icon='gavel', tone='red', size=72),
]},
# 0:09 범인은 쿠팡이 아닙니다 (가리개 + 쿠팡 로고 + 도장)
{'from': '범인은', 'enter': 'flash', 'bg': 'st_phone_order', 'items': [
    cover('+0.02'),
    tag('범인은?', '범인은', 160, 200, icon='alert-triangle', tone='dark', size=66),
    logo('coupang', '쿠팡이', 560, 330, h=130),
    stamp('범인 아님', '아닙니다', x=700, y=620, size=130),
]},
]
