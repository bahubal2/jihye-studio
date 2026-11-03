"""사라지는 직업 TOP7 — 인트로 0:00~1:22 (자막 1~30). 화풍 A 다큐.
2026-11-02 인트로 화면 규칙: 첫 0.3초 쾅 글자 · 2~4초 컷 · 반전마다 번쩍 · 움직이는 클립 · 숫자 roll · 첫 1초 비우지 않기."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, ranks, punch, glow, igrid, inset, raw, stack, swapnum)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

INTRO = [
# 0:00 "엄마, 나 회계사 붙었어." — 기뻐 소리치는 딸 (클립)
{'from': '엄마, 나 회계사', 'enter': 'flash', 'bg': 'ph_phone_call_joy', 'items': [
    BRIGHT,
    hook('“엄마, 나 <strong>붙었어!</strong>”', '+0.05', y=600, size=170),
]},
# 0:02 온 집안 잔치 (클립)
{'from': '그 전화 한 통에', 'enter': 'zoom', 'bg': 'ph_family_party', 'items': [
    BRIGHT,
    tag('공인회계사 최종 합격', '+0.1', 120, 140, icon='flag', tone='green', size=64),
    flashhit('잔치를'),
]},
# 0:06 그런데 몇 달이 지나도 출근할 곳이 없다 (클립)
{'from': '그런데 몇 달이', 'enter': 'strips', 'bg': 'ph_waiting_alone', 'items': [
    BRIGHT,
    tag('몇 달 뒤', '+0.05', 120, 140, icon='calendar', tone='dark', size=62),
    hook('합격했는데<br><strong>출근할 곳이 없다</strong>', '아이는', y=280, size=150),
]},
# 0:10 한국에서 가장 먼저 사라지는 직업 — 일곱 사람 줄 세우기
{'from': '한국에서 가장 먼저', 'enter': 'flash', 'bg': 'th_lineup_shutter', 'items': [
    BRIGHT,
    hook('한국에서 가장 먼저<br><strong>사라지는 직업 TOP7</strong>', '+0.05', y=600, size=118),
    flashhit('사라지는'),
]},
# 0:14 2025년 공인회계사 합격자 1,200명
{'from': '이천이십오 년, 공인회계사', 'enter': 'zoom', 'bg': 'ph_accounting_firm', 'items': [
    cover('+0.02'),
    tag('2025 공인회계사 시험', '+0.05', 560, 140, icon='file-invoice', tone='dark', size=64),
    roll(0, 1200, '천이백', y=330, size=230, suffix='명 합격', tone='good', dur=0.9),
]},
# 0:19 수습처 등록 338명 → 넷 중 셋은 첫 출근 못 함
{'from': '그해 가을까지', 'enter': 'strips', 'bg': 'ph_empty_new_desk', 'items': [
    cover('+0.02'),
    tag('가을까지 수습처 등록', '+0.05', 560, 120, icon='calendar', tone='dark', size=60),
    roll(0, 338, '삼백삼십팔', y=250, size=190, suffix='명', tone='good', dur=0.8),
    igrid('user', 4, '+0.3', lit=1, litat='삼백삼십팔', cols=4, y=520, size=170, tone='good', drop=3, dropat='셋은'),
]},
# 0:28 AI 탓? → 절반만 맞습니다
{'from': '다들 AI가', 'enter': 'zoom', 'bg': 'ph_ai_office', 'items': [
    BRIGHT,
    tag('AI가 일자리를 뺏어서?', 'AI가', None, 220, icon='robot', size=74, strike='절반만'),
    punch('절반만 맞습니다', '절반만', y=520, size=160),
]},
# 0:34 예고 ① 붙고도 교단에 못 서는 사람들
{'from': '오늘 순위표에는', 'enter': 'wipe', 'bg': 'ph_teacher_waiting', 'items': [
    BRIGHT,
    tag('오늘의 순위표', '+0.05', 120, 130, icon='flag', tone='dark', size=60),
    hook('붙고도<br><strong>교단에 못 선다</strong>', '임용시험에', y=300, size=150, sfx='pop'),
]},
# 0:42 예고 ② 다섯 중 넷이 장롱에 잠든 자격증
{'from': '한때 국민 자격증이었는데', 'enter': 'strips', 'bg': 'ph_cert_drawer', 'items': [
    tag('한때 국민 자격증', '+0.05', 120, 130, icon='key', tone='dark', size=60),
    igrid('user', 5, '+0.1', lit=0, cols=5, y=330, size=170, tone='bad', drop=4, dropat='넷이'),
    stamp('장롱 자격증', '장롱에', x=1080, y=620, size=110),
]},
# 0:47 예고 ③ 13년 새 2,300곳 넘게 꺼진 창구
{'from': '십삼 년 사이', 'enter': 'flash', 'bg': 'ph_bank_dark_counter', 'items': [
    BRIGHT,
    tag('13년 사이', '+0.05', 120, 130, icon='building-bank', tone='dark', size=60),
    roll(0, 2300, '이천삼백', y=300, size=220, prefix='-', suffix='곳', tone='bad', dur=0.9),
    flashhit('꺼진'),
]},
# 0:51 그리고 1위 — 평생 걱정 없다던 그 기술
{'from': '그리고 일 위', 'enter': 'zoom', 'bg': 'ph_kid_coding_class', 'items': [
    cover('+0.02'),
    ranks('+0.02', n=7, now=1, nowat='일 위', top=180),
    glow('“이것만 배우면 평생 걱정 없다”', '이것만', y=600, size=80),
]},
# 0:59 지금 자녀가, 혹은 내가 준비하는 그 자격증 / 자식한테 권해도 될까
{'from': '지금 자녀가', 'enter': 'wipe', 'bg': 'ph_parent_worry', 'items': [
    BRIGHT,
    tag('내 자녀 · 내 자격증', '+0.05', 120, 140, icon='users', tone='dark', size=62),
    hook('자식한테<br><strong>권해도 될까?</strong>', '자식한테', y=330, size=160),
]},
# 1:08 끝까지 보면 두 가지
{'from': '끝까지 들으시면', 'enter': 'strips', 'bg': 'th_lineup_office', 'items': [
    cover('+0.02'),
    tag('끝까지 보시면', '+0.05', 640, 150, icon='key', tone='dark', size=62),
    *stack([('① 일곱 직업을 꿰는 마음의 법칙', '마음의', 'heart-handshake', 'red'), ('② 내 일자리 30초 자가진단', '자가진단법', 'clock', 'red')], x=150, y=320, gap=170, size=58),
]},
# 1:20 덜 무너진 7위부터
{'from': '덜 무너진 칠 위부터', 'enter': 'flash', 'bg': 'th_lineup_shutter', 'items': [
    cover('+0.02'),
    ranks('+0.02', n=7, now=7, nowat='칠', top=300),
]},
]
