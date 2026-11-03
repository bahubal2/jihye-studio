"""5위 초등교사 (자막 137~194) · 4위 공인중개사 (195~247)."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, ranks, punch, glow, igrid, raw, stack, swapnum, card, article, rankbadge, bubble, bars, timeline, flow)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
def RB(n, name, first=False): return rankbadge(n, name, '+0.05', still=not first)

S2 = [
# ================= 5위 초등교사 =================
{'from': '잠깐 짚고 가겠습니다', 'enter': 'flash', 'bg': 'ph_teacher_waiting', 'items': [
    cover('+0.02'),
    tag('여기까지: 자리만 줄었다', '+0.1', 560, 200, icon='door-exit', tone='dark', size=62),
    hook('여기서부터는<br><strong>붙어도 기다린다</strong>', '오 위부터는', y=380, size=140),
]},
{'from': '이천이십육 년 일월,', 'enter': 'zoom', 'bg': 'ph_new_teachers', 'items': [
    RB(5, '초등교사', True),
    tag('2026.1 대전 유치원·초등 임용', '+0.1', 120, 260, icon='calendar', tone='dark', size=56),
    card('선발 예정', '', '선발', 260, 420, w=620, h=280, num=46, suffix='명', vat='사십육'),
    card('지원', '', '이백삼십일', 1040, 420, w=620, h=280, num=231, suffix='명', vat='이백삼십일'),
]},
{'from': '몇 명이 붙었을까요', 'enter': 'flash', 'bg': 'ph_new_teachers', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('최종 합격', '+0.1', 780, 220, icon='flag', tone='dark', size=62),
    roll(0, 41, '사십일', y=350, size=260, suffix='명', tone='good', dur=0.6),
]},
{'from': '합격자 사진 속', 'enter': 'wipe', 'bg': 'ph_parents_proud', 'items': [
    BRIGHT, RB(5, '초등교사'),
    tag('“언제 발령 나나” 걱정 없던 시절', '걱정은', 120, 260, icon='mood-sad', tone='dark', size=56),
]},
{'from': '교사는 오랫동안', 'enter': 'zoom', 'bg': 'ph_parents_proud', 'items': [
    BRIGHT, RB(5, '초등교사'),
    tag('안정의 대명사', '대명사였습니다', 120, 260, icon='lock', tone='green', size=64),
    tag('딸이 교대 붙으면 집안 잔치', '교대에', 120, 420, icon='home', size=58),
    bubble('선생님이래요!', '선생님', 1000, 560, size=58),
]},
{'from': '전북만 봐도', 'enter': 'strips', 'bg': 'ph_classroom_empty', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    card('전북 2015 초등 선발', '', '+0.1', 260, 260, w=640, h=300, num=312, suffix='명', vat='삼백십이'),
    card('2025학년도 전국 선발', '', '이천이십오학년도', 1020, 260, w=640, h=300, num=4272, suffix='명', vat='사천이백칠십이'),
]},
{'from': '그런데 아이가 줄었습니다', 'enter': 'zoom', 'bg': 'ph_classroom_empty', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('아이가 줄었다', '+0.05', 120, 200, icon='baby-carriage', tone='red', size=60),
    bars([('2025학년도', 1.0, '4,272명', '+0.3', True), ('2026학년도', 3113 / 4272, '3,113명', '삼천백십삼', False)], top=330),
    big('-27.1%', '이십칠', y=610, size=118, color='#ff5a5a'),
]},
{'from': '작년에 넷이 앉던', 'enter': 'wipe', 'bg': 'ph_training_hall', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('합격자 연수 강당', '+0.05', 700, 200, icon='users', tone='dark', size=60),
    igrid('user', 4, '+0.1', cols=4, y=360, size=180, tone='good', drop=1, dropat='셋이'),
]},
{'from': '이쯤 되면 이렇게 생각하시죠', 'enter': 'flash', 'bg': 'ph_calendar_wait', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('붙기만 하면 평생 철밥통?', '철밥통', None, 230, icon='lock', size=72, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=520, size=170),
]},
{'from': '이천십칠 년 봄 전북에선', 'enter': 'zoom', 'bg': 'ph_calendar_wait', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('2017년 봄 · 전북', '+0.05', 760, 160, icon='calendar', tone='dark', size=60),
    card('그해 합격자', '', '+0.1', 260, 280, w=640, h=300, num=152, suffix='명', vat='백오십이'),
    card('신학기 발령', '0명', '신학기에', 1020, 280, w=640, h=300, vat='한 명도', hot=True),
    tag('1년 전 합격자 261명도 대기', '명도 아직:명도', 500, 660, icon='clock', tone='red', size=58),
]},
{'from': '합격자 명부의 유효기간', 'enter': 'strips', 'bg': 'ph_list_paper', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    timeline([('합격', '명부 등록', '+0.1'), ('1년', '유효기간', '일 년입니다'), ('+2년', '연장 가능', '이 년'), ('3년', '못 받으면 취소', '취소될', 1)], y=330),
    tag('붙고도 달력을 넘기는 직업', '달력을', 540, 680, icon='calendar', tone='red', size=60),
]},
{'from': '그 소식은 다음 세대에게', 'enter': 'zoom', 'bg': 'ph_lecture_empty', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('전북 초등 임용 경쟁률', '경쟁률은', 640, 200, icon='chart-bar', tone='dark', size=60),
    big('2.2 : 1', '대 일까지:대', y=320, size=220, color='#ff5a5a'),
    tag('교대 자퇴생 증가', '자퇴생이', 680, 640, icon='door-exit', tone='red', size=62),
]},
{'from': '사람은 줄이 길면', 'enter': 'wipe', 'bg': 'ph_queue_line', 'items': [
    cover('+0.02'), RB(5, '초등교사'),
    tag('줄이 길면 따라 서고, 빈자리가 보이면 떠난다', '빈자리가', 220, 220, icon='users', tone='dark', size=52),
    big('사회적 증거', '사회적', y=360, size=180, color='#ffd400'),
    glow('대기 소식이 다음 해 원서를 바꾼다', '원서는', y=640, size=80),
]},
{'from': '환하게 웃던 합격자 사진', 'enter': 'zoom', 'bg': 'ph_list_paper', 'items': [
    BRIGHT, RB(5, '초등교사'),
    tag('사진 뒤엔 발령 대기 명부', '명부가', 120, 260, icon='file-invoice', tone='red', size=62),
]},
{'from': '이번 칸은 아이가', 'enter': 'flash', 'bg': 'ph_realty_closed', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=4, nowat='다음', opened={7: ('경비원', None), 6: ('콜센터', None), 5: ('초등교사', None)}, top=300),
    tag('손님이 직접 해 버려서 닫힌 문', '직접', 470, 680, icon='door-exit', tone='red', size=60),
]},
# ================= 4위 공인중개사 =================
{'from': '숫자 하나를 드리겠습니다', 'enter': 'zoom', 'bg': 'ph_realty_closed', 'items': [
    BRIGHT, RB(4, '공인중개사', True),
    roll(0, 14721, '만 사천칠백이십일:만', y=300, size=220, suffix='곳', tone='bad', dur=1.0),
    tag('2024년 문 닫거나 쉰 중개사무소', '공인중개사무소', 380, 580, icon='building-store', tone='red', size=58),
]},
{'from': '이걸 삼백육십오 일로', 'enter': 'strips', 'bg': 'ph_realty_window', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    big('하루 40곳', '마흔', y=180, size=180, color='#ff5a5a'),
    card('새로 연 곳', '', '새로', 260, 420, w=640, h=280, num=10308, suffix='곳', vat='만 삼백팔:만'),
    card('닫은 곳', '14,721곳', '닫는', 1020, 420, w=640, h=280, hot=True),
]},
{'from': '불과 몇 년 전,', 'enter': 'zoom', 'bg': 'ph_exam_crowd', 'items': [
    RB(4, '공인중개사'),
    tag('별명: 국민 자격증', '국민', 120, 260, icon='flag', tone='dark', size=62),
    roll(0, 278847, '이십칠만', y=380, size=170, suffix='명 응시', tone='good', dur=1.0),
    stamp('2021 역대 정점', '정점이었죠', x=980, y=630, size=90),
]},
{'from': '퇴직을 앞둔 가장들이', 'enter': 'wipe', 'bg': 'ph_night_study', 'items': [
    BRIGHT, RB(4, '공인중개사'),
    tag('퇴직 앞둔 가장 · 다 키운 어머니', '가장들이', 120, 260, icon='users', tone='dark', size=58),
    tag('노후 대비 1순위', '노후', 120, 420, icon='home', tone='red', size=62),
]},
{'from': '신혼집 구하러 가면', 'enter': 'zoom', 'bg': 'ph_realty_coffee', 'items': [
    BRIGHT, RB(4, '공인중개사'),
    tag('믹스커피부터 타 주던 시절', '믹스커피부터', 120, 260, icon='heart-handshake', size=60),
]},
{'from': '그런데 거래가 얼어붙었습니다', 'enter': 'flash', 'bg': 'ph_realty_window', 'items': [
    BRIGHT, RB(4, '공인중개사'),
    tag('거래 절벽', '얼어붙었습니다', 120, 260, icon='snowflake', tone='red', size=66),
    tag('전세 사기 이후 업계 전체 의심', '전세', 120, 430, icon='alert-triangle', tone='dark', size=58),
]},
{'from': '이천이십사 년 응시자는', 'enter': 'strips', 'bg': 'ph_exam_crowd', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    tag('공인중개사 시험 응시자', '+0.05', 600, 200, icon='users', tone='dark', size=60),
    bars([('2021년', 1.0, '27만 8,847명', '+0.2', True), ('2024년', 154669 / 278847, '15만 4,669명', '십오만', False)], top=330),
    tag('2017년 이후 처음 20만 명 아래', '이십만', None, 640, icon='trending-down', tone='red', size=58),
]},
{'from': '이쯤 되면 부동산 경기가', 'enter': 'zoom', 'bg': 'ph_night_study', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    tag('부동산 경기 탓?', '경기가', 640, 230, icon='trending-down', size=84, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=500, size=170),
    tag('경기만으론 설명 안 된다', '경기만으로는', None, 770, icon='alert-triangle', tone='dark', size=56),
]},
{'from': '같은 시기,', 'enter': 'wipe', 'bg': 'ph_phone_direct_deal', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    tag('중고거래 앱 부동산 직거래', '직거래가', 520, 180, icon='device-mobile', tone='red', size=60),
    bars([('2022년', 7094 / 34482, '7,094건', '칠천구십사', False), ('2023년', 23178 / 34482, '2만 3,178건', '이만', False), ('2024년 1~7월', 1.0, '3만 4,482건', '삼만', False)], top=320),
]},
{'from': '손님이 사라진 게 아니라', 'enter': 'zoom', 'bg': 'ph_phone_direct_deal', 'items': [
    BRIGHT, RB(4, '공인중개사'),
    hook('손님이<br><strong>직접 한다</strong>', '직접', y=300, size=170),
]},
{'from': '더 근본적인 숫자도', 'enter': 'strips', 'bg': 'ph_cert_drawer', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    card('자격증 보유', '', '+0.1', 260, 200, w=640, h=280, num=55, suffix='만 명+', vat='오십오만'),
    card('실제 개업', '', '실제로', 1020, 200, w=640, h=280, num=11, suffix='만 명', vat='십일만', hot=True),
    igrid('user', 5, '+0.2', lit=1, litat='하나만', cols=5, y=540, size=150, tone='good'),
]},
{'from': '동창회에 이 자격증', 'enter': 'zoom', 'bg': 'ph_reunion_cards', 'items': [
    BRIGHT, RB(4, '공인중개사'),
    tag('친구 5명 중 명함 1명', '한 명뿐인', 120, 260, icon='users', tone='red', size=62),
]},
{'from': '작년 시월 말엔', 'enter': 'wipe', 'bg': 'ph_reunion_cards', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    tag('2025년 10월 말 영업 중 중개사', '+0.05', 470, 200, icon='building-store', tone='dark', size=58),
    roll(0, 109979, '십만', y=320, size=200, suffix='명', tone='bad', dur=1.0),
    tag('5년 2개월 만에 11만 명 아래', '오 년', 520, 640, icon='trending-down', tone='red', size=58),
]},
{'from': '모두가 따니까', 'enter': 'zoom', 'bg': 'ph_cert_pile', 'items': [
    cover('+0.02'), RB(4, '공인중개사'),
    flow([('밴드왜건 효과', '모두가'), ('스놉 효과', '스놉')], y=260, size=96),
    tag('모두 가지면 특별하지 않다', '특별하지', 520, 480, icon='alert-triangle', tone='dark', size=58),
    stamp('장롱 자격증', '장롱', x=760, y=670, size=110),
]},
{'from': '동네 부동산에서 타 주던', 'enter': 'wipe', 'bg': 'ph_realty_coffee', 'items': [
    BRIGHT, RB(4, '공인중개사'),
    swapnum('믹스커피 한 잔', '채팅창 한 줄', '+0.1', '채팅창', y=230, size=110, tone='bad'),
    bubble('안녕하세요, 집 보러 가도 될까요?', '안녕하세요', 300, 560, size=50),
]},
]
