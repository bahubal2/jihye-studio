"""카메라워크 데모 (2026-11-03): s02 = 줌아웃 공개 → 숫자 → 크래쉬줌, s04 = 전체 화면 → 1/5 액자 + 화살표·동그라미·밑줄 + 흔들기."""
from gen import tag, big, roll, cover, raw, shrink, arrow, circ, uline, rankbadge, foreshadow, flipcard, PAST, bubble
PLAN = [
{'from': '엄마, 나 회계사', 'bg': 'ph_phone_call_joy', 'items': []},
{'from': '이 직업은 아파트와', 'enter': 'flash', 'bg': 'ph_apartment_aerial',
 'cam': [('pull', '+0.05', 62, 58, 2.4), ('crash', '일곱은', 40, 62, 1.7)], 'items': [
    raw('<style>.bg{--dark:.9; --blur:0px}</style>'), rankbadge(7, '아파트 경비원', '+0.05'),
    tag('2018 서울시 전수조사', '전수조사했습니다', 120, 260, icon='file-invoice', tone='dark', size=60),
    roll(0, 4256, '사천이백오십육', y=420, size=200, suffix='개 단지', tone='good', dur=0.9),
    tag('10명 중 7명 용역 계약', '일곱은', 600, 680, icon='users', tone='red', size=62),
]},
{'from': '신혼집에 이삿짐', 'enter': 'wipe', 'bg': 'ph_moving_day', 'cam': [('push', '+0.1', 30, 40, 1.25)], 'items': [
    PAST, rankbadge(7, '아파트 경비원', '+0.05', still=True),
    tag('그 시절', '+0.1', 120, 260, icon='calendar', tone='dark', size=60),
    tag('이삿날 엘리베이터를 잡아 주던 분', '엘리베이터를', 120, 420, icon='heart-handshake', size=56),
    circ('엘리베이터를', 90, 395, 1320, 170, color='#ffd400'),
]},
{'from': '그런데 이천십팔 년,', 'bg': 'ph_bill_table', 'items': []},
{'from': '이쯤 되면 경비원 대량', 'enter': 'flash', 'bg': 'ph_guard_booth_dawn', 'cam': [('crash', '아닙니다', 50, 45, 1.4)], 'items': [
    cover('+0.02'), rankbadge(7, '아파트 경비원', '+0.05', still=True),
    flipcard('경비원 대량 해고', '감원 단지는 20곳 중 1곳', '대량', '아닙니다', y=300, size=80),
    foreshadow('305명', '삼백오', label='이 숫자, 기억해 두세요'),
]},
{'from': '삼백오 명이면', 'bg': 'ph_wedding_guests', 'items': []},
{'from': '서울 강서구의', 'enter': 'zoom', 'bg': 'ph_apartment_aerial', 'cam': [('shake', '칠만')], 'items': [
    cover('+0.02'), rankbadge(7, '아파트 경비원', '+0.05', still=True),
    shrink('ph_resident_meeting', '사십사', 1150, 150, 660, 372, cap='서울 강서구 한 아파트'),
    big('경비원 44명 해고', '사십사', y=200, size=110, color='#ff5a5a', x=110, center=False),
    arrow('결정됐습니다', 900, 300, 1140, 330, color='#ffd400'),
    tag('가구당 약 7만 원', '칠만', 110, 470, icon='coin', tone='red', size=62),
    circ('칠만', 30, 425, 1010, 200),
    tag('통합전자보안시스템 도입', '통합전자보안시스템을', 110, 700, icon='scan', tone='dark', size=54),
    uline('통합전자보안시스템을', 120, 830, 900),
]},
{'from': '훗날 법원은', 'bg': 'ph_resident_meeting', 'items': []},
]
