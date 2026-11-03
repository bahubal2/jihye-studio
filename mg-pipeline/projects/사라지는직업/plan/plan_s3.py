"""3위 은행원 (자막 248~301) · 2위 공인회계사 (302~358)."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, ranks, punch, glow, igrid, raw, stack, swapnum, card, article, logo, rankbadge, bubble, donut, flow, split, side)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
def RB(n, name, first=False): return rankbadge(n, name, '+0.05', still=not first)
OPEN4 = {7: ('경비원', None), 6: ('콜센터', None), 5: ('초등교사', None), 4: ('공인중개사', None)}

S3 = [
# ================= 3위 은행원 =================
{'from': '이제부터는 듣다 보면', 'enter': 'flash', 'bg': 'ph_bank_shutter', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=3, nowat='이제부터는', opened=OPEN4, top=260),
    glow('여기서부터는 사람의 마음이 보인다', '마음이', y=640, size=78),
]},
{'from': '어느 은행 지점 유리문에', 'enter': 'zoom', 'bg': 'ph_bank_notice', 'items': [
    BRIGHT, RB(3, '은행원', True),
    tag('“인근 지점과 통합됩니다”', '통합됩니다', 120, 260, icon='building-bank', tone='red', size=60),
]},
{'from': '그 앞에서 한 어르신이', 'enter': 'strips', 'bg': 'ph_elder_phone', 'items': [
    BRIGHT, RB(3, '은행원'),
    tag('인증번호… 누르고, 지우고, 다시', '누르고', 120, 260, icon='device-mobile', tone='dark', size=60),
]},
{'from': '시간을 삼십 년쯤', 'enter': 'wipe', 'bg': 'ph_bank_1990s', 'items': [
    BRIGHT, RB(3, '은행원'),
    tag('30년 전 월급날', '월급날', 120, 260, icon='calendar', tone='dark', size=60),
    tag('번호표 기계 · 통장 정리기 줄', '번호표', 120, 420, icon='ticket', size=58),
]},
{'from': '예물 반지를 맞추려고', 'enter': 'zoom', 'bg': 'ph_loan_stamp', 'items': [
    BRIGHT, RB(3, '은행원'),
    tag('적금 깨고 대출 도장 찍던 곳', '도장을', 120, 260, icon='home', size=58),
    tag('은행원 = 신랑감 1순위', '신랑감', 120, 420, icon='heart-handshake', tone='red', size=62),
]},
{'from': '이천십이 년,', 'enter': 'flash', 'bg': 'ph_bank_1990s', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    tag('2012 국내 은행 점포', '+0.05', 640, 200, icon='building-bank', tone='dark', size=60),
    roll(0, 7836, '개로 정점을:개로', y=330, size=220, suffix='곳', tone='good', dur=0.9),
    stamp('역대 정점', '정점을', x=1180, y=620, size=100),
]},
{'from': '그런데 스마트폰이', 'enter': 'zoom', 'bg': 'ph_mobile_bank', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    tag('은행이 주머니 속으로', '+0.05', 620, 160, icon='device-mobile', tone='dark', size=60),
    donut(81.3, '팔십일', label='한 달 안 모바일 금융', x=760, y=280, d=400, tone='good'),
    tag('3년 전엔 3명 중 2명', '셋 중', 600, 720, icon='users', tone='dark', size=56),
]},
{'from': '입출금 거래의', 'enter': 'strips', 'bg': 'ph_mobile_bank', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    tag('입출금 인터넷뱅킹 비중 86.5%', '+0.05', 470, 200, icon='percentage', tone='dark', size=58),
    igrid('building-bank', 10, '+0.2', lit=8, litat='팔십육', half=True, cols=10, y=360, size=130, tone='good'),
    tag('10번 중 9번 가까이 창구 밖', '열 번', 520, 620, icon='door-exit', tone='red', size=58),
]},
{'from': '이천이십오 년 구월 말', 'enter': 'flash', 'bg': 'ph_bank_shutter', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    tag('2025년 9월 말 점포', '+0.05', 680, 180, icon='building-bank', tone='dark', size=60),
    swapnum('7,836곳', '5,534곳', '+0.2', '오천오백삼십사', y=320, size=140, tone='bad'),
    big('-2,302곳', '이천삼백두', y=560, size=150, color='#ff5a5a'),
]},
{'from': '오대 은행만 보면', 'enter': 'zoom', 'bg': 'ph_bank_dark_counter', 'items': [
    BRIGHT, RB(3, '은행원'),
    tag('5대 은행 5년 사이 676곳 폐쇄', '육백칠십육', 120, 260, icon='building-bank', tone='red', size=58),
    tag('일주일에 2~3곳씩 셔터', '셔터가', 120, 420, icon='lock', tone='dark', size=60),
]},
{'from': '이쯤 되면 점포는 시골부터', 'enter': 'flash', 'bg': 'ph_seoul_bank_street', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    tag('시골부터 사라진다?', '시골부터', None, 230, icon='map-pin', size=76, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=520, size=170),
]},
{'from': '이천이십 년부터 이천이십오 년', 'enter': 'zoom', 'bg': 'ph_seoul_bank_street', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    card('2020~2025.6 문 닫은 점포', '', '+0.1', 120, 260, w=700, h=300, num=937, suffix='곳', vat='구백삼십칠'),
    donut(67, '육백이십구', label='서울·경기 629곳', x=1100, y=210, d=420, tone='bad'),
    tag('임대료·인건비 비싼 곳부터', '임대료와', 140, 640, icon='coin', tone='red', size=58),
]},
{'from': '부아가 치미는 대목은', 'enter': 'strips', 'bg': 'ph_elder_phone', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    tag('고령층 모바일뱅킹 이용률', '고령층의', 560, 180, icon='user', tone='dark', size=60),
    igrid('user', 10, '+0.2', lit=3, litat='넷도', half=True, cols=10, y=330, size=130, tone='bad'),
    tag('평균이 10이면 4도 안 된다', '넷도', 560, 560, icon='trending-down', tone='red', size=58),
    glow('닫히는 속도 > 배우는 속도', '빠릅니다', y=720, size=76),
]},
{'from': '비교할 길이 없을 땐', 'enter': 'wipe', 'bg': 'ph_teller_warm', 'items': [
    cover('+0.02'), RB(3, '은행원'),
    swapnum('정', '계산', '+0.2', '계산으로', y=230, size=170, tone='bad'),
    big('대안의 등장', '대안의', y=470, size=160, color='#ffd400'),
    tag('손님이 계산하자 은행도 계산', '은행도', 520, 700, icon='scale', tone='dark', size=58),
]},
{'from': '번호표 기계가 종이를', 'enter': 'zoom', 'bg': 'ph_ticket_machine', 'items': [
    BRIGHT, RB(3, '은행원'),
    tag('꺼진 기계와 안내문 한 장', '꺼진', 120, 260, icon='ticket', tone='red', size=60),
]},
# ================= 2위 공인회계사 =================
{'from': '여기까지는 손님이 떠나서', 'enter': 'flash', 'bg': 'ph_ticket_machine', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=2, nowat='다음', opened={**OPEN4, 3: ('은행원', None)}, top=260),
    tag('손님은 그대로인데 신입만 안 뽑는다', '신입만', 360, 660, icon='user-x', tone='red', size=58),
]},
{'from': '이천이십오 년 늦가을', 'enter': 'zoom', 'bg': 'ph_seminar', 'items': [
    RB(2, '공인회계사', True),
    tag('2025 늦가을 · 여의도 세미나', '여의도의', 120, 260, icon='map-pin', tone='dark', size=58),
    tag('토론석에 앉은 합격자', '합격자', 120, 420, icon='user', tone='red', size=62),
]},
{'from': '이 자리가 마련된 이유는', 'enter': 'strips', 'bg': 'ph_seminar', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    hook('합격하고도<br><strong>첫 출근을 못 했다</strong>', '첫 출근을:첫', y=300, size=150),
]},
{'from': '회계사는 오래도록', 'enter': 'wipe', 'bg': 'ph_holiday_family', 'items': [
    BRIGHT, RB(2, '공인회계사'),
    tag('합격 = 곧 취업', '합격이', 120, 260, icon='flag', tone='green', size=64),
    bubble('회계사 붙었대!', '붙었대', 1000, 420, size=58),
    tag('어디든 골라 가던 시절', '골라', 120, 600, icon='building-skyscraper', tone='dark', size=58),
]},
{'from': '그런데 회계업계에 불황이', 'enter': 'flash', 'bg': 'ph_ai_ledger', 'items': [
    BRIGHT, RB(2, '공인회계사'),
    tag('회계업계 불황', '불황이', 120, 260, icon='trending-down', tone='red', size=62),
    tag('AI가 장부를 읽는다', '장부를', 120, 420, icon='robot', tone='dark', size=62),
]},
{'from': '수습처를 못 찾는 합격자가', 'enter': 'zoom', 'bg': 'ph_ai_ledger', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    hook('수습처 못 찾는 합격자<br><strong>해마다 증가</strong>', '해마다', y=260, size=120),
    logo('fsc', '금융위원회의', 820, 620, h=72),
]},
{'from': '회계사는 합격만으로', 'enter': 'strips', 'bg': 'ph_accounting_firm', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    flow([('합격', '합격만으로'), ('1년 실무수습', '실무수습을'), ('정식 등록', '등록이')], y=330, size=84),
    stamp('막혔다', '막혔습니다', x=780, y=560, size=150),
]},
{'from': '이쯤 되면 그래도 몇 달', 'enter': 'flash', 'bg': 'ph_empty_new_desk', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    tag('몇 달 기다리면 다 들어간다?', '몇 달', None, 230, icon='clock', size=70, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=520, size=170),
]},
{'from': '이천이십오 년 합격자 천이백 명 중', 'enter': 'zoom', 'bg': 'ph_waiting_alone', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    tag('2025 합격자 1,200명 중 10월 하순 수습 등록', '+0.05', None, 170, icon='file-invoice', tone='dark', size=46),
    roll(0, 338, '삼백삼십팔', y=300, size=200, suffix='명', tone='good', dur=0.8),
    igrid('user', 4, '+0.2', lit=1, litat='넷 중', cols=4, y=540, size=150, tone='good'),
]},
{'from': '전년도 합격자 중에도', 'enter': 'strips', 'bg': 'ph_resume_stack', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    card('전년도 합격자 미취업', '', '+0.1', 260, 220, w=640, h=300, num=171, suffix='명', vat='명이 여전히:명이'),
    card('협회 추산 실질 미지정', '', '협회는', 1020, 220, w=640, h=300, num=592, suffix='명', vat='오백구십이', hot=True),
    tag('그해 합격자의 절반', '절반', 640, 640, icon='users', tone='red', size=62),
]},
{'from': '스터디 동기 넷이', 'enter': 'wipe', 'bg': 'ph_friends_dinner', 'items': [
    BRIGHT, RB(2, '공인회계사'),
    tag('스터디 동기 4명 합격', '+0.1', 120, 260, icon='users', tone='dark', size=60),
    igrid('user', 4, '+0.2', lit=1, litat='한 명뿐', cols=4, x=1000, y=560, size=120, tone='good', drop=3, dropat='나머지'),
]},
{'from': '결국 이천이십육 년 오월', 'enter': 'zoom', 'bg': 'ph_gov_briefing', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    logo('fsc', '+0.1', 760, 170, h=80),
    tag('2026.5 수습 안정화 방안', '오월', 560, 330, icon='file-invoice', tone='dark', size=60),
    tag('2년 넘게 못 구하면 협회가 배정', '배정하는', 380, 520, icon='hand-stop', tone='red', size=60),
]},
{'from': '수습기관도 국회', 'enter': 'strips', 'bg': 'ph_gov_briefing', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    tag('수습기관 확대', '+0.05', 700, 160, icon='building-bank', tone='dark', size=60),
    tag('국회', '국회', 200, 330, icon='flag', size=66),
    tag('법원', '법원', 620, 330, icon='gavel', size=66),
    tag('국민연금공단', '국민연금공단', 1040, 330, icon='building-bank', size=66),
    stamp('2004년 이후 처음 바뀐다', '이천사', x=560, y=560, size=96),
]},
{'from': '정부가 합격자에게', 'enter': 'zoom', 'bg': 'ph_resume_stack', 'items': [
    BRIGHT, RB(2, '공인회계사'),
    hook('정부가 자리를<br><strong>찾아 주겠다</strong>', '찾아', y=300, size=150),
]},
{'from': '사람은 이득보다 손해를', 'enter': 'wipe', 'bg': 'ph_scale_balance', 'items': [
    cover('+0.02'), RB(2, '공인회계사'),
    big('손실 회피', '손실', y=50, size=105, color='#ffd400'),
    *split('비용입니다'),
    side('l', '비용입니다', tag('확실한 비용', '비용입니다', 0, 0, icon='coin', tone='red', size=60), tag('신입 교육 1년', '비용입니다', 0, 0, size=50)),
    side('r', '불확실한', tag('불확실한 이득', '불확실한', 0, 0, icon='trending-up', tone='green', size=60), tag('10년 뒤 성과', '불확실한', 0, 0, size=50)),
    glow('미래의 선배를 통째로 놓친다', '선배를', y=720, size=76),
]},
{'from': '그 세미나장 토론석에', 'enter': 'zoom', 'bg': 'ph_empty_seat_panel', 'items': [
    BRIGHT, RB(2, '공인회계사'),
    tag('원래 앉았어야 할 자리 = 회계법인 신입 책상', '신입', 120, 260, icon='user', tone='red', size=54),
]},
]
