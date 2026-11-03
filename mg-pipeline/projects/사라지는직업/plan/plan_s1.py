"""7위 아파트 경비원 (자막 31~84) · 6위 콜센터 상담사 (85~136)."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, ranks, punch, glow, igrid, raw, stack, swapnum, card, article, logo, rankbadge, bubble)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
def RB(n, name, first=False): return rankbadge(n, name, '+0.05', still=not first)

S1 = [
# ================= 7위 아파트 경비원 =================
{'from': '한겨울 새벽 다섯 시', 'enter': 'flash', 'bg': 'ph_guard_booth_dawn', 'items': [
    BRIGHT, RB(7, '아파트 경비원', True),
    tag('한겨울 새벽 5시', '다섯', 120, 260, icon='snowflake', tone='dark', size=60),
]},
{'from': '창밖에선 신문 뭉치가', 'enter': 'zoom', 'bg': 'ph_guard_snow_shovel', 'items': [
    BRIGHT, RB(7, '아파트 경비원'),
    tag('주민보다 먼저 길을 낸다', '먼저', 120, 260, icon='home', size=60),
]},
{'from': '이 직업은 아파트와', 'enter': 'strips', 'bg': 'ph_apartment_aerial', 'items': [
    RB(7, '아파트 경비원'),
    tag('2018 서울시 전수조사', '전수조사했습니다', 120, 260, icon='file-invoice', tone='dark', size=60),
    roll(0, 4256, '사천이백오십육', y=420, size=200, suffix='개 단지', tone='good', dur=0.9),
]},
{'from': '그 단지마다 경비원이', 'bg': 'ph_apartment_aerial', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    tag('경비원 10명 중', '+0.1', 640, 220, icon='users', tone='dark', size=60),
    igrid('user', 10, '+0.2', lit=7, litat='일곱은', cols=10, y=400, size=130, tone='bad'),
    tag('7명은 용역 계약', '용역', 680, 640, icon='file-invoice', tone='red', size=62),
]},
{'from': '신혼집에 이삿짐', 'enter': 'wipe', 'bg': 'ph_moving_day', 'items': [
    BRIGHT, RB(7, '아파트 경비원'),
    tag('이삿날 엘리베이터를 잡아 주던 분', '엘리베이터를', 120, 260, icon='heart-handshake', size=56),
]},
{'from': '자녀 수능 날 아침', 'enter': 'zoom', 'bg': 'ph_exam_morning', 'items': [
    BRIGHT, RB(7, '아파트 경비원'),
    bubble('잘 보고 와라!', '잘', 900, 330, size=60),
    tag('동네 어른', '어른이었죠', 120, 600, icon='home', tone='dark', size=62),
]},
{'from': '그런데 이천십팔 년,', 'enter': 'flash', 'bg': 'ph_bill_table', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    tag('2018 최저임금', '+0.05', 640, 200, icon='coin', tone='dark', size=62),
    big('+16.4%', '십육', y=330, size=230, color='#ff5a5a'),
    tag('관리비 고지서가 움직였다', '고지서가', 520, 640, icon='receipt', tone='red', size=60),
]},
{'from': '이쯤 되면 경비원 대량', 'enter': 'zoom', 'bg': 'ph_guard_booth_dawn', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    tag('경비원 대량 해고?', '대량', 560, 230, icon='user-x', size=84, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=520, size=170),
]},
{'from': '같은 조사에서 감원이', 'enter': 'strips', 'bg': 'ph_bill_table', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    card('감원한 단지', '', '+0.1', 260, 200, w=640, h=300, num=171, suffix='곳', vat='백칠십일'),
    card('줄어든 경비원', '', '줄어든', 1020, 200, w=640, h=300, num=305, suffix='명', vat='삼백오', hot=True),
    tag('20단지 중 1곳', '스무', 300, 600, icon='home', tone='dark', size=58),
    tag('단지당 0.1명', '영 점', 1060, 600, icon='user', tone='red', size=58),
]},
{'from': '삼백오 명이면', 'enter': 'wipe', 'bg': 'ph_wedding_guests', 'items': [
    BRIGHT, RB(7, '아파트 경비원'),
    tag('305명 = 결혼식 하객 한 무리', '하객', 120, 260, icon='users', tone='red', size=60),
    tag('대부분은 근무시간 조정으로 지켰다', '대부분', 120, 600, icon='clock', tone='green', size=56),
]},
{'from': '그런데 왜 순위에', 'enter': 'zoom', 'bg': 'ph_guard_snow_shovel', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    hook('한꺼번에가 아니라<br><strong>한 단지씩</strong>', '한꺼번에가', y=300, size=150),
]},
{'from': '서울 강서구의', 'enter': 'strips', 'bg': 'ph_resident_meeting', 'items': [
    RB(7, '아파트 경비원'),
    tag('서울 강서구 한 아파트', '+0.05', 120, 260, icon='map-pin', tone='dark', size=58),
    big('경비원 44명 해고', '사십사', y=380, size=140, color='#ff5a5a'),
    tag('가구당 약 7만 원 아끼려고', '칠만', 120, 600, icon='coin', tone='red', size=58),
    tag('통합전자보안시스템 도입', '통합전자보안시스템을', 120, 740, icon='scan', tone='dark', size=50),
]},
{'from': '훗날 법원은', 'enter': 'zoom', 'bg': 'ph_resident_meeting', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    article('판결 요약', '훗날', '법원, 경비원 해고 결의는 무효', '+0.1', mark='무효', markat='무효로', x=460, y=190),
    tag('다른 단지에서도 반복', '반복됐습니다', 640, 680, icon='alert-triangle', tone='red', size=58),
]},
{'from': '사람은 처음 본 숫자를', 'enter': 'wipe', 'bg': 'ph_bill_hand', 'items': [
    cover('+0.02'), RB(7, '아파트 경비원'),
    tag('지난달 고지서 = 잣대', '기준이', 560, 220, icon='receipt', tone='dark', size=62),
    tag('7만 원 = 손해로만 보인다', '손해로만', 560, 380, icon='trending-down', tone='red', size=62),
    big('기준점 효과', '기준점', y=520, size=150, color='#ffd400'),
]},
{'from': '고지서엔 금액이', 'enter': 'zoom', 'bg': 'ph_snow_path', 'items': [
    BRIGHT, RB(7, '아파트 경비원'),
    glow('새벽 눈삽의 온기는 찍히지 않는다', '온기는', y=560, size=86),
]},
{'from': '이제 어떤 경비실엔', 'enter': 'strips', 'bg': 'ph_guard_booth_monitor', 'items': [
    RB(7, '아파트 경비원'),
    swapnum('주황 난로', '푸른 모니터', '+0.1', '푸른', y=300, size=120, tone='bad'),
    tag('길을 먼저 내던 사람이 없다', '먼저', 520, 620, icon='user-x', tone='red', size=60),
]},
{'from': '경비원은 기계가 들어와도', 'enter': 'flash', 'bg': 'ph_snow_path', 'items': [
    cover('+0.02'),
    tag('주민이 막아선 직업', '+0.05', 600, 140, icon='hand-stop', tone='dark', size=62),
    ranks('+0.05', n=7, now=6, nowat='다음', opened={7: ('경비원', None)}, top=320),
    tag('다음 칸은 정반대', '정반대입니다', 640, 700, icon='arrows-exchange', tone='red', size=60),
]},
# ================= 6위 콜센터 상담사 =================
{'from': '"상담원 연결을', 'enter': 'flash', 'bg': 'ph_phone_ars', 'items': [
    BRIGHT, RB(6, '콜센터 상담사', True),
    tag('“상담원 연결은 0번”', '+0.1', 120, 260, icon='microphone', tone='dark', size=60),
    tag('또 메뉴…', '또', 120, 420, icon='alert-triangle', size=60),
    tag('“다시 말씀해 주세요”', '다시 말씀해', 120, 580, icon='robot', tone='red', size=60),
]},
{'from': '예전엔 달랐습니다', 'enter': 'wipe', 'bg': 'ph_card_lost_night', 'items': [
    BRIGHT, RB(6, '콜센터 상담사'),
    tag('카드 잃어버린 밤', '카드를', 120, 260, icon='coin', tone='dark', size=60),
    tag('전화 너머 사람이 받았다', '사람이', 120, 420, icon='user', tone='green', size=60),
]},
{'from': '접촉사고가 난', 'enter': 'zoom', 'bg': 'ph_car_accident_call', 'items': [
    BRIGHT, RB(6, '콜센터 상담사'),
    tag('사고 현장 위치도 사람이', '위치를', 120, 260, icon='car', tone='dark', size=58),
    tag('마지막엔 사람의 목소리', '목소리가', 120, 600, icon='microphone', tone='green', size=62),
]},
{'from': '이천십구 년 말', 'enter': 'strips', 'bg': 'ph_callcenter_floor', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    tag('2019년 말 · 카드사 8곳 콜센터', '+0.05', 470, 200, icon='microphone', tone='dark', size=58),
    roll(0, 12000, '상담사가 만:만', y=330, size=220, prefix='약 ', suffix='명', tone='good', dur=0.9),
    tag('회사의 얼굴 = 비대면 영업점', '얼굴', 540, 650, icon='building-store', size=58),
]},
{'from': '그런데 이천이십 년 이후', 'enter': 'zoom', 'bg': 'ph_callcenter_dark', 'items': [
    BRIGHT, RB(6, '콜센터 상담사'),
    tag('2020~ AI 컨택센터', '컨택센터가', 120, 260, icon='robot', tone='red', size=62),
    tag('2022~ 그만둔 자리 안 채움', '채우지', 120, 420, icon='user-x', tone='dark', size=60),
]},
{'from': '카드사 콜센터만 해도', 'enter': 'wipe', 'bg': 'ph_callcenter_floor', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    tag('카드사 콜센터 5년 새', '+0.05', 600, 180, icon='trending-down', tone='dark', size=60),
    igrid('user', 5, '+0.1', cols=5, y=320, size=150, tone='bad', drop=1, dropat='하나가'),
    logo('keis', '한국고용정보원도', 420, 620, h=64),
    tag('AI 대체 고위험군', '고위험군으로', 1000, 610, icon='robot', tone='red', size=60),
]},
{'from': '이쯤 되면 상담원은', 'enter': 'flash', 'bg': 'ph_ai_office', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    tag('상담원은 이미 다 사라졌다?', '사라졌다고', None, 230, icon='user-x', size=70, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=520, size=170),
]},
{'from': '콜 대응이 어려워지자', 'enter': 'zoom', 'bg': 'ph_callcenter_rehire', 'items': [
    RB(6, '콜센터 상담사'),
    tag('은행, 상담원 다시 충원', '충원하고', 120, 260, icon='users', tone='green', size=62),
    article('세계일보 (요약)', '2026.4', '챗봇 상담, 오히려 줄었다', '챗봇', mark='줄었다', markat='줄었다는', x=640, y=440, rot=2),
]},
{'from': '결국 사람을 다시 뽑는', 'enter': 'strips', 'bg': 'ph_angry_call', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    tag('다시 뽑으니 괜찮다?', '괜찮은', 520, 260, icon='users', size=80, strike='그런데'),
    tag('대부분 도급 인력', '도급', 600, 520, icon='file-invoice', tone='red', size=70),
]},
{'from': '그리고 다시 생긴 자리는', 'enter': 'zoom', 'bg': 'ph_angry_call', 'items': [
    BRIGHT, RB(6, '콜센터 상담사'),
    tag('AI가 못 푼 불만 콜부터', '불만', 120, 260, icon='alert-triangle', tone='red', size=60),
    bubble('왜 뺑뺑이만 시켜요!', '뺑뺑이만', 960, 520, size=58, tone='red'),
]},
{'from': '앞으로는 어떨까요', 'enter': 'wipe', 'bg': 'ph_callcenter_dark', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    logo('gartner', '가트너는', 820, 130, h=70),
    tag('2029년 · 흔한 고객 문의', '이천이십구', None, 250, icon='calendar', tone='dark', size=52),
    roll(0, 80, '퍼센트를 AI가:퍼센트를', y=380, size=230, suffix='%', tone='bad', dur=0.8),
    tag('AI가 사람 없이 처리', '사람', 640, 640, icon='robot', tone='red', size=60),
]},
{'from': '콜센터 한 층에', 'enter': 'strips', 'bg': 'ph_desks_row', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    tag('책상 10개라면', '+0.05', 700, 180, icon='users', tone='dark', size=60),
    igrid('user', 10, '+0.1', cols=10, y=340, size=130, tone='good', drop=8, dropat='여덟'),
    tag('남은 2자리 = 가장 어려운 전화', '남은', 420, 640, icon='alert-triangle', tone='red', size=60),
]},
{'from': '흔할 때는 아무도', 'enter': 'zoom', 'bg': 'ph_phone_ars', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    tag('흔하면 값이 없고, 귀하면 값이 붙는다', '귀해지고', 300, 220, icon='coin', tone='dark', size=56),
    big('희소성 효과', '희소성', y=360, size=180, color='#ffd400'),
    glow('사람의 목소리 = 서비스', '서비스가', y=640, size=84),
]},
{'from': '예전엔 영 번을', 'enter': 'wipe', 'bg': 'ph_card_lost_night', 'items': [
    cover('+0.02'), RB(6, '콜센터 상담사'),
    swapnum('0번 = 기본', '0번 뒤 사람 = 행운', '+0.1', '행운이', y=360, size=110, tone='good'),
]},
{'from': '여기까지는 기계에 밀린', 'enter': 'flash', 'bg': 'ph_desks_row', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=5, nowat='다음', opened={7: ('경비원', None), 6: ('콜센터', None)}, top=300),
    tag('아이들이 줄어서 닫힌 문', '아이들이', 520, 680, icon='baby-carriage', tone='red', size=60),
]},
]
