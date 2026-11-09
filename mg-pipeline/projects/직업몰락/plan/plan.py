"""직업의 몰락 TOP7 (한국에서 가장 먼저 사라지는 직업) — 장면 계획.
2026-11-09 규칙: 인트로 30초 표준(kin·휙 전환), 교체 80%, 재탕 금지(asset_check 0건), 화면 기술(cardL/R 분할 카드·push·crash·shrink·polaroid),
레퍼런스(1NmjVFcxE4Q) 분할 카드 + 글자 나열."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, foreshadow, article, bubble, group, raw,
                 puppet, particles, mgbg, rankbadge, qbadge, polaroid, intro30, kin, cutsfx)
SOFT = raw('<style>.bg{--dark:.6; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')
R = lambda n, name, at: rankbadge(n, name, at)

PLAN = [
# ================= 인트로 (0:00~1:42) =================
{'from': '엘리베이터 문이 열리면', 'enter': 'flash', 'bg': [('i_elevator_notice', None), ('v:s_elevator', '경비용역'), ('i_guard_booth', '열두'), ('i_guard_protest', '경기도'), ('v:s_apartment', '한국에서'), ('v:s_snow', '엘리베이터 앞까지')],
 'cam': [('push', '+0.0', 50, 45, 1.2)], 'items': [
    intro30(), SOFT, cutsfx('경비용역', '열두', '경기도', '한국에서', '엘리베이터 앞까지'),
    kin('경비용역 변경안 / *주민 동의* 안내', '+0.1', y=170, size=92, mode='drop', until='열두', sfx='whoosh'),
    kin('경비원 *12명* → !6명!', '열두', y=330, size=150, mode='pop', until='한국에서', sfx='hit'),
    stamp('주민 투표', '투표입니다', x=1180, y=560, size=100),
    kin('한국에서 *가장 먼저* / 사라지는 직업', '한국에서', y=250, size=124, sfx='whoosh'),
]},
{'from': '올해 이월, 서울대학교 졸업식', 'enter': 'zoom', 'bg': [('i_snu_grad', None), ('v:s_grad', '학사모를'), ('v:s_interview', '문과'), ('i_seoul_jobs', '그 무렵')],
 'cam': [('push', '+0.0', 50, 50, 1.18)], 'items': [
    intro30(), SOFT, cutsfx('학사모를', '문과', '그 무렵'),
    kin('2026. 2 / *서울대* 졸업식', '+0.1', y=170, size=110, mode='drop', until='학사모를', sfx='whoosh'),
    kin('꽃다발보다 먼저 / *취업* 이야기', '학사모를', y=230, size=110, until='문과'),
    kin('취업? / !로스쿨?!', '문과', y=230, size=130, mode='pop', until='그 무렵'),
    kin('청년 취업자 / 한 달 새 !-17만!', '그 무렵', y=230, size=120, until='서울대를 나와도', sfx='hit'),
    kin('서울대를 나와도 / *갈 곳이 없다*', '서울대를 나와도', y=250, size=140, mode='pop', sfx='hit'),
]},
{'from': '그런데 정반대로 보이는', 'enter': 'wipe', 'bg': [('v:s_office_young', None), ('v:s_datacenter', '한국은행'), ('i_father_son', '흔히들')],
 'cam': [('cardL', '한국은행')], 'items': [
    CLEAR, cutsfx('한국은행', '흔히들'),
    kin('그런데 / *정반대* 숫자', '+0.1', y=250, size=130, mode='pop', until='한국은행', sfx='whoosh'),
    kin('한국은행 분석', '한국은행', x=1060, y=200, size=64, mode='slide', until='흔히들'),
    kin('AI 많이 쓰는 업종', '많이', x=1060, y=310, size=70, mode='slide', until='흔히들'),
    kin('청년 일자리 !급감!', '청년', x=1060, y=440, size=92, mode='pop', until='흔히들'),
    kin('50대 일자리 *증가*', '오십대', x=1060, y=590, size=92, mode='pop', until='흔히들', sfx='hit'),
    kin('숫자는 / *거꾸로*', '숫자는', x=1060, y=300, size=120, until='그렇다면 왜'),
    kin('아이의 첫 직장 / 아버지의 마지막 직장 / *한꺼번에?*', '그렇다면 왜', x=1060, y=250, size=80, mode='slide'),
]},
{'from': '자녀의 취업', 'enter': 'zoom', 'bg': [('v:s_typing', None), ('i_study_night', '그 끝에는'), ('v:s_seoul', '순서는'), ('v:s_grad', '나 자신에게')], 'items': [
    SOFT, cutsfx('그 끝에는', '순서는', '나 자신에게'),
    kin('사라지는 *7자리* / 그리고 남는 자리', '오늘은', y=220, size=116, until='그 끝에는', sfx='whoosh'),
    puppet('c_banker', '그 끝에는', 1260, 420, w=380, move='hand-stop', dx=-220, dur=7, until='순서는'),
    kin('은행 정년 *60대* / 세 번 떨어지고 다시 편 책', '그 끝에는', x=120, y=230, w=1100, size=80, until='순서는'),
    kin('순서 = *우리와의 거리*', '순서는', y=180, size=100, mode='slide'),
    *stack([('길 위', '길 위에서', 'car', 'dark'), ('동네', '동네와', 'home', 'dark'), ('가족', '가족을', 'users', 'dark'), ('나 자신', '나 자신에게', 'user', 'red')], x=760, y=310, gap=125, size=58),
    tag('이 영상의 판단 순위', '데이터 순위가', 1180, 790, tone='ghost', size=44),
]},
# ================= 7위 요금수납원 =================
{'from': '이천십구 년 추석', 'enter': 'flash', 'bg': [('i_toll_roof', None), ('v:s_tollgate', '상을 차린'), ('i_toll_booth', '대부분')], 'cam': [('push', '+0.0', 50, 40, 1.2)], 'items': [
    SOFT, cutsfx('상을 차린', '대부분'),
    kin('2019 추석 / 톨게이트 *지붕 위* 차례상', '+0.2', y=190, size=96, mode='drop', until='상을 차린', sfx='whoosh'),
    puppet('c_toll', '대부분', 1240, 420, w=360, move='enter', until='칠 위'),
    kin('우리 누님·아내 또래 / *어머니들*', '대부분', x=120, y=260, w=1000, size=88, until='칠 위'),
    R('7', '고속도로 요금수납원', '칠 위'),
    kin('7위 / *고속도로 요금수납원*', '칠 위', y=260, size=130, mode='pop', sfx='hit'),
]},
{'from': '그해 칠월 일일', 'enter': 'zoom', 'bg': [('v:s_highway', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    kin('2019.7.1', '+0.4', x=1060, y=190, size=80, mode='drop'),
    kin('요금수납원 *6,500명*', '육천오백여', x=1060, y=310, size=84, mode='slide'),
    kin('자회사 거부 / !1,500명! 일자리 잃음', '천오백', x=1060, y=450, size=84, sfx='hit'),
    kin('지붕 농성 *97일*', '구십칠', x=1060, y=700, size=96, mode='pop'),
]},
{'from': '도로공사가 내건 이유는', 'enter': 'wipe', 'bg': [('i_hipass', None)], 'cam': [('push', '+0.0', 60, 50, 1.25)], 'items': [
    SOFT,
    article('한국도로공사 입장', '2019', '하이패스 보급·수납 자동화 → 수납 인력 장기 유지 어렵다', '+0.3', mark='자동화', markat='자동화되면', x=420, y=200, rot=-2),
    stamp('자동화', '오래', x=1500, y=640, size=96),
]},
{'from': '지금 고속도로를 지나는', 'enter': 'zoom', 'bg': [('v:s_car_drive', None), ('v:s_cctv', '다음 단계는')], 'items': [
    SOFT, cutsfx('다음 단계는'),
    group('창문을', igrid('car', 10, '열 대 중', lit=9, litat='하이패스를', cols=10, y=300, size=120, tone='good')),
    kin('10대 중 *9대* 하이패스', '하이패스를', y=520, size=96, until='창문을'),
    kin('창문을 내리던 / *짧은 인사*', '창문을', y=260, size=116, until='다음 단계는'),
    kin('다음 단계 / *스마트톨링*', '다음 단계는', y=220, size=116, until='이게 깔리면'),
    kin('요금소 자체가 / !사라진다?!', '이게 깔리면', y=240, size=124, mode='pop', sfx='hit'),
]},
{'from': '물론 반론도 있습니다. 미납', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    group('사람을 빼는', swapnum('미납 262억', '994억', '미납 통행료가', '네 배', y=200, size=110, tone='bad'),
          kin('스마트톨링 *11년째* 제자리', '십일 년째', y=520, size=92, mode='slide')),
    kin('사람을 빼는 속도 = / 기계가 *돈을 받아 낼 수 있나*', '사람을 빼는', y=220, size=96, until='기계가 대신'),
    kin('첫 번째 단서 / *기계가 받을 수 있는 돈*', '기계가 대신', y=260, size=110, mode='pop', sfx='hit'),
    qbadge('<b>단서</b> ① 기계가 받는 돈', '첫 번째', pop=True),
]},
# ================= 6위 은행 창구 =================
{'from': '올해 사월 초, 제주의', 'enter': 'zoom', 'bg': [('i_bank_close', None), ('v:s_atm', '같은 달'), ('v:s_bank_hall', '육 위')], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    SOFT, cutsfx('같은 달', '육 위'),
    kin('2026. 4 / 제주 지점 *폐점*', '+0.2', y=200, size=104, mode='drop', until='같은 달', sfx='whoosh'),
    kin('광주 · 대전도 / !폐점 안내문!', '같은 달', y=230, size=104, until='육 위'),
    R('6', '은행 창구 직원', '육 위'),
    kin('6위 / *은행 창구 직원*', '육 위', y=260, size=130, mode='pop', sfx='hit'),
]},
{'from': '국내 은행 점포는', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    igrid('building-bank', 4, '네 곳 중', drop=1, dropat='사라졌습니다', cols=4, y=170, size=170),
    kin('10년 새 *4곳 중 1곳* 사라짐', '사라졌습니다', y=420, size=84, mode='slide', until='오대'),
    kin('5대 은행 5년 / !670곳+! 폐점', '육백칠십', y=420, size=100, mode='pop', sfx='hit'),
    tag('미국: 창구 직원 10년 -4만 명', '사만', None, 780, icon='world', tone='dark', size=52),
]},
{'from': '왜 이렇게 빠를까요', 'enter': 'zoom', 'bg': [('i_bank_1990', None), ('v:s_mobile_bank', '손님이 먼저')], 'cam': [('cardR', '한 시중은행')], 'items': [
    SOFT, cutsfx('손님이 먼저'),
    kin('왜 이렇게 / *빠를까?*', '+0.1', y=250, size=130, mode='pop', until='손님이 먼저'),
    kin('손님이 / *먼저 떠났다*', '손님이 먼저', y=250, size=130, until='한 시중은행', sfx='whoosh'),
    kin('업무량·손님 / !-30%!', '삼십 퍼센트', x=110, y=260, w=760, size=100, sfx='hit'),
    kin('10명 오던 창구 / *7명*도 안 온다', '열 명', x=110, y=560, w=760, size=74, mode='slide'),
]},
{'from': '정부가 이천이십삼 년', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('cream'),
    *stack([('2023 점포 폐쇄 규제 → 폐점 감소', '정부가', 'gavel', 'dark'), ('2024~ 다시 가팔라짐', '이천이십사', 'trending-up', 'red')], x=300, y=220, gap=150, size=62),
    kin('규제는 속도만 늦췄다 / 방향은 *그대로*', '규제는', y=560, size=92, sfx='hit'),
]},
{'from': '통장 정리하러 가던', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('dusk'),
    polaroid('i_bank_1990', '+0.1', 160, 170, w=660, rot=-5, cap='월급날 줄 서던 그 창구'),
    kin('앱이 서툰 / *부모님 세대*', '가장 불편해진', x=960, y=230, w=900, size=96, mode='slide'),
    kin('두 번째 단서 / *손님이 직접* 해도 되는 일', '손님이 직접', x=960, y=520, w=900, size=78, sfx='hit'),
    qbadge('<b>단서</b> ① 기계가 받는 돈 ② 손님이 직접', '두 번째', pop=True),
]},
# ================= 5위 콜센터 =================
{'from': '은행에 전화를 걸면', 'enter': 'flash', 'bg': [('i_mom_phone', None), ('v:s_callcenter', '오 위')], 'cam': [('push', '+0.0', 45, 45, 1.2)], 'items': [
    SOFT, cutsfx('오 위'),
    kin('사람보다 / *기계 목소리*가 먼저', '+0.2', y=200, size=104, until='말씀하시면'),
    kin('"말씀하시면 / 안내해 드리겠습니다"', '말씀하시면', y=230, size=100, mode='slide', until='오 위'),
    R('5', '콜센터 상담원', '오 위'),
    kin('5위 / *콜센터 상담원*', '오 위', y=260, size=130, mode='pop', sfx='hit'),
]},
{'from': '한 시중은행은 이천이십일 년', 'enter': 'zoom', 'bg': [('v:s_chatbot', None), ('i_callroom', '은행권 상담사')], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR, cutsfx('은행권 상담사'),
    group('은행권 상담사', donut(25, '사분의', label='AI가 처리', x=1180, y=200, d=380, tone='bad', cap='2021 한 시중은행')),
    kin('그만둔 자리 / !안 채웠다!', '채우지', x=1060, y=260, size=96, until='하청', sfx='hit'),
    kin('AI = 계약 해지의 / *그럴듯한 명분*', '하청', x=1060, y=260, size=84, until='자르기'),
    kin('"자르기 쉬운 자리부터"', '자르기', x=1060, y=300, size=84, mode='pop'),
]},
{'from': '그런데 여기서 반전이 있습니다', 'enter': 'flash', 'bg': [('v:s_old_phone', None), ('v:s_meeting', '일부 은행은'), ('v:s_bank_hall', '정해진 질문에')], 'items': [
    SOFT, cutsfx('일부 은행은', '정해진 질문에'),
    kin('그런데 / *반전*', '+0.1', y=250, size=150, mode='pop', until='AI 답변을', sfx='hit'),
    kin('챗봇 상담 / *오히려 감소*', 'AI 답변을', y=200, size=104, until='상담원 연결을'),
    kin('결국 / *"상담원 연결"*', '상담원 연결을', y=220, size=116, mode='pop', until='일부 은행은'),
    stamp('재채용', '다시 상담사를', x=1150, y=520, size=110),
    kin('정해진 답 → 기계 / 화난 사람 → *사람*', '정해진 질문에', y=230, size=100, mode='slide'),
]},
# ================= 4위 마트 계산원 =================
{'from': '매출은 사상 최고인데', 'enter': 'zoom', 'bg': [('v:s_supermarket', None)], 'cam': [('cardL', '국내 일 위')], 'items': [
    CLEAR, cutsfx('국내 일 위'),
    kin('매출 *최고* / 직원 !-5,000명!', '+0.1', y=240, size=124, mode='pop', until='국내 일 위', sfx='hit'),
    kin('국내 1위 대형마트 · 2021', '국내 일 위', x=1060, y=190, size=60, mode='slide'),
    kin('매출 *16조+*', '십육조', x=1060, y=300, size=96),
    swapnum('3만 명대', '2만 4천 명대', '삼만 명대', '이만 사천', x=1060, y=450, size=76, tone='bad'),
    R('4', '마트 계산원', '사 위'),
    kin('4위 *마트 계산원*', '사 위', x=1060, y=680, size=88, mode='pop', sfx='hit'),
]},
{'from': '그 빈자리를 채운 건', 'enter': 'wipe', 'bg': [('i_selfcheck', None)], 'cam': [('crash', '대구 지역', 50, 50, 1.3)], 'items': [
    SOFT,
    kin('빈자리 = *셀프계산대*', '+0.1', y=220, size=116, until='대구 지역'),
    roll(5, 54, '쉰네', y=160, size=220, suffix='대', tone='bad'),
    tag('대구 대형마트 5개 점포 · 3년 만에', '대구 지역', None, 680, tone='dark', size=50),
    kin('미국 계산원 10년 !-31만 개!', '삼십일만', y=820, size=72, sfx='hit'),
]},
{'from': '한때 대형마트 한 곳은', 'enter': 'fade', 'bg': [('i_mart_2000', None), ('v:s_carts', '물론 반론도')], 'items': [
    SOFT, cutsfx('물론 반론도'),
    kin('대형마트 1곳 = / 동네 일자리 *1,000개*', '+0.1', y=200, size=100, until='어머니는'),
    kin('엄마는 계산대 / 아들은 *카트 알바*', '어머니는', y=220, size=104, until='물론 반론도'),
    bubble('"저기요, 이거 잘 안 돼요"', '저기요', 640, 220, size=64, until='드렉셀대학교'),
    tag('드렉셀대: 사람 계산 → 재방문 ↑', '드렉셀대학교', None, 300, icon='bell-ringing', tone='dark', size=56),
    kin('그래도 / *방향은 그대로*', '그래도 방향은', y=500, size=110, sfx='hit'),
]},
{'from': '여기서 첫 번째 자가진단', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('자가진단 *①*', '+0.1', y=150, size=100, mode='drop', sfx='whoosh'),
    kin('내 일은 대부분 / *모니터 앞* · *같은 동작?*', '지금 내 일은', y=340, size=100),
    tag('채점은 마지막에', '채점하겠습니다', None, 720, icon='scan', tone='ghost', size=52),
]},
# ================= 3위 초등교사 =================
{'from': '이번엔 손주가 다닐', 'enter': 'zoom', 'bg': [('v:s_kids_school', None), ('v:s_exam', '전국 공립')], 'cam': [('cardR', '전국 공립')], 'items': [
    CLEAR, cutsfx('전국 공립'),
    kin('손주가 다닐 / *초등학교*', '+0.1', y=250, size=130, mode='pop', until='전국 공립'),
    kin('초등교사 선발', '전국 공립', x=110, y=200, w=780, size=64, mode='slide'),
    swapnum('4,272명', '2,821명', '사천이백칠십이', '이천팔백이십일', x=110, y=320, size=70, tone='bad'),
    kin('2년 새 *3할+* 감소', '이 년 사이', x=110, y=500, w=780, size=74),
    R('3', '초등학교 교사', '삼 위'),
    kin('3위 *초등학교 교사*', '삼 위', x=110, y=680, w=780, size=78, mode='pop', sfx='hit'),
]},
{'from': '지난 영상에 남겨 주신 댓글 중에는 교사', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('cream'),
    kin('지난 영상 댓글 / "교사 숫자가 *현실과 다르다*"', '+0.1', y=170, size=84, until='이천이십오 학년도는'),
    kin('교육부 공식 집계 · *불리한 숫자도*', '교육부', y=420, size=70, mode='slide', until='이천이십오 학년도는'),
    *stack([('2025: 늘봄 이동으로 일시 증원', '늘봄학교', 'bell-ringing', 'dark'), ('전년과 비교하면 감소 폭 작다', '그 전해와', 'chart-line', 'dark'), ('대구: 학생 -5%에도 선발 증가', '대구는', 'trending-up', 'green')], x=300, y=230, gap=150, size=58),
]},
{'from': '그래도 큰 흐름은 분명합니다', 'enter': 'zoom', 'bg': [('i_class_empty', None), ('v:s_classroom', '원인은'), ('v:s_chalk', '일자리는 기계')], 'cam': [('push', '+0.0', 50, 50, 1.2)], 'items': [
    SOFT, cutsfx('원인은', '일자리는 기계'),
    kin('제주 선발 / !-70%!', '칠십 퍼센트', y=220, size=130, mode='pop', until='원인은', sfx='hit'),
    kin('원인은 AI가 아니다 / *아이가 없다*', '원인은', y=220, size=110, until='일자리는 기계'),
    kin('세 번째 단서 / *사람 수가 줄어도* 사라진다', '사람 수가', y=240, size=100, sfx='hit'),
    qbadge('<b>단서</b> ①돈 ②손님 직접 ③인구', '세 번째', pop=True),
]},
# ================= 2위 신입 사무직 =================
{'from': '우리 때 신입사원은', 'enter': 'flash', 'bg': [('v:s_meeting', None), ('i_office_junior', '혼나면서')], 'items': [
    SOFT, cutsfx('혼나면서'),
    *stack([('회의록', '회의록을', 'file-invoice', 'dark'), ('자료 정리', '자료를', 'package', 'dark'), ('보고서 초안', '보고서', 'chart-bar', 'dark')], x=1200, y=200, gap=120, size=60),
    kin('혼나면서 배운 / 그 *계단*이 사라진다', '혼나면서', x=120, y=260, w=1000, size=88, until='이 위'),
    R('2', '신입 사무직', '이 위'),
    kin('2위 / *신입 사무직·초급 개발자*', '이 위', y=480, size=104, mode='pop', sfx='hit'),
]},
{'from': '한국은행 분석을 보면', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    donut(94, '구십사', label='AI 고노출 업종', x=160, y=210, d=440, tone='bad', cap='청년 일자리 감소분'),
    kin('청년 일자리 / !-28만 5천!', '이십팔만', x=760, y=220, w=1050, size=104, sfx='hit'),
    kin('신입 대신 *경력직*', '경력직을', x=760, y=520, w=1050, size=92, mode='slide'),
    tag('하버드: 신입 ↓ · 경력 ↑', '하버드대', 760, 720, icon='bell-ringing', tone='dark', size=56),
]},
{'from': '그리고 인트로의 그 숫자입니다', 'enter': 'zoom', 'bg': [('v:s_office_young', None), ('i_snu_grad', '서울대 졸업장')], 'items': [
    SOFT, cutsfx('서울대 졸업장'),
    kin('청년 *급감*', '같은 AI', x=150, y=260, w=760, size=110, until='경험과'),
    kin('50대 *증가*', '오십대', x=1010, y=260, w=760, size=110, until='경험과', sfx='hit'),
    kin('"연공편향 / *기술변화*"', '연공편향', y=500, size=96, mode='slide', until='경험과'),
    kin('숙련은 남고 / *처음 배우는 자리부터*', '경험과', y=230, size=104, until='서울대 졸업장'),
    kin('서울대 졸업장으로도 / *첫 계단*이 안 보인다', '서울대 졸업장', y=250, size=104, mode='pop'),
]},
{'from': '아버지 자리는 남았는데', 'enter': 'fade', 'bg': [('i_father_son', None), ('v:s_interview', '그럼 전부'), ('i_office_junior', '취업을 준비하는')], 'cam': [('push', '+0.0', 50, 45, 1.18)], 'items': [
    SOFT, cutsfx('그럼 전부', '취업을 준비하는'),
    kin('아버지 자리 *남고* / 아들 자리 !없다!', '+0.1', y=220, size=110, until='그럼 전부'),
    flipcard('전부 AI 탓?', 'AI는 흐름을 빠르게 했을 뿐', '그럼 전부', '코로나', y=200, size=74),
    tag('서류 탈락, 아이 탓만은 아니다', '아이 탓만은', None, 470, tone='ghost', size=54),
    kin('네 번째 단서 / *처음 배우는 사람의 일*', '네 번째', y=560, size=92, sfx='hit'),
    qbadge('<b>단서</b> ①돈 ②손님 ③인구 ④신입 일', '네 번째', pop=True),
]},
# ================= 1위 아파트 경비원 =================
{'from': '서울 강서구의 한 아파트', 'enter': 'flash', 'bg': [('i_guard_protest', None), ('v:s_apartment', '통합전자')], 'cam': [('push', '+0.0', 50, 50, 1.2)], 'items': [
    SOFT, cutsfx('통합전자'),
    kin('6~70대 경비원 30여 명 / *침묵의 삭발식*', '+0.3', y=190, size=96, until='통합전자', sfx='whoosh'),
    kin('통합보안 도입 / !44명 해고!', '마흔네', y=220, size=116, until='일 위', sfx='hit'),
    R('1', '아파트 경비원', '일 위'),
    kin('1위 / *아파트 경비원*', '일 위', y=260, size=150, mode='pop', sfx='hit'),
]},
{'from': '이 일은 오랫동안', 'enter': 'zoom', 'bg': [('v:s_cctv', None), ('i_guard_booth', 'CCTV와')], 'cam': [('cardL', '그런데 지금')], 'items': [
    CLEAR, cutsfx('CCTV와'),
    kin('은퇴자의 / *마지막 일자리*', '+0.1', y=250, size=130, mode='pop', until='그런데 지금'),
    kin('서울 단지당 경비원', '그런데 지금', x=1060, y=200, size=64, mode='slide'),
    swapnum('9.5명', '8.7명', '아홉 점', '여덟 점', x=1060, y=310, size=96, tone='bad'),
    kin('단지마다 *1명씩* 사라짐', '단지마다', x=1060, y=480, size=76),
    kin('고양 34명 중 !11명! 감축', '서른네', x=1060, y=660, size=76, sfx='hit'),
]},
{'from': '삭발식에 나온 한 경비원은', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('dusk'),
    puppet('c_guard', '+0.2', 180, 360, w=440, move='hand-stop', dx=160, dur=10),
    kin('"하루아침에 / *쓸모없는 사람*"', '쓸모없는', x=760, y=250, w=1080, size=100),
    kin('관리비 몇만 원 / *투표 한 번*으로', '관리비', x=760, y=560, w=1080, size=80, mode='slide', sfx='hit'),
]},
{'from': '반대 숫자도 공정하게', 'enter': 'wipe', 'bg': [('v:s_snow', None), ('i_guard_snow', '눈은 누가')], 'items': [
    SOFT, cutsfx('눈은 누가'),
    kin('무인 경비 / *큰 이득 없다*', '유인 경비와', y=220, size=110, until='눈은 누가'),
    kin('"눈은 / *누가 치우나*"', '눈은 누가', y=220, size=124, mode='pop', until='한 경비원은'),
    *stack([('재활용 정리', '재활용', 'package', 'dark'), ('시설 관리', '시설', 'key', 'dark'), ('교통 정리', '교통', 'car', 'dark')], x=1200, y=220, gap=120, size=60),
    kin('지켜보기 → 카메라 / 고치고 책임지기 → *사람*', '지켜보는', x=120, y=560, w=1000, size=72, sfx='hit'),
]},
# ================= 정리 · 남는 자리 =================
{'from': '일곱 자리를 정리해 보겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    *stack([('요금소 · 기계가 받는 돈', '요금소', 'car', 'dark'), ('창구·계산대 · 손님이 직접', '창구와 계산대', 'building-store', 'dark'), ('콜센터 · 정해진 답', '콜센터', 'device-mobile', 'dark'),
            ('교단 · 아이가 줄어', '교단', 'bell-ringing', 'dark'), ('신입 책상 · 정해진 일', '신입의 책상', 'building-skyscraper', 'dark'), ('순찰 · 카메라가 지켜봄', '순찰', 'scan', 'dark')], x=420, y=110, gap=115, size=48),
    kin('기계 + 인구 = *두 개의 파도*', '두 개의 파도', y=810, size=80, sfx='hit'),
]},
{'from': '여기서 두 번째 자가진단', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('자가진단 *②*', '+0.1', y=150, size=100, mode='drop', sfx='whoosh'),
    kin('내가 그만둬도 / 서류상 *아무 문제 없다?*', '내가 오늘', y=340, size=100),
    tag('= 법에 내 이름이 걸린 자리가 아니다', '내 이름이', None, 720, tone='ghost', size=50),
]},
{'from': '그럼 끝까지 남는 자리는', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('cream'),
    kin('끝까지 *남는 자리?*', '+0.1', y=140, size=116, mode='drop', sfx='whoosh'),
    *stack([('① 법이 사람 이름을 요구', '법이 사람', 'scale', 'green'), ('② 몸이 그 자리에 있어야', '몸이 그 자리에', 'hand-stop', 'green'), ('③ 쉰 넘어서도 뽑아 준다', '쉰 넘어서도', 'user', 'green')], x=420, y=340, gap=150, size=66),
    qbadge('<b>남는 자리</b> ① 법 ② 몸 ③ 50+', '세 가지', pop=True),
]},
{'from': '먼저 몸이 있어야 하는', 'enter': 'zoom', 'bg': [('i_construct', None), ('v:s_construction', '다만 최근'), ('v:s_forklift', '지게차운전기능사'), ('i_forklift', '로봇 지게차'), ('v:s_robot_wh', '큰 물류센터')], 'items': [
    SOFT, cutsfx('다만 최근', '지게차운전기능사', '로봇 지게차', '큰 물류센터'),
    kin('건설 기능인력 / 평균 *52세*', '쉰둘', y=200, size=110, until='한 현장소장'),
    kin('일당 40만 원에도 / 젊은 기능공 !없다!', '사십만', y=200, size=104, until='다만 최근'),
    tag('사망자 10명 중 4명 = 60세+', '사망자', None, 220, icon='alert-triangle', tone='red', size=60, until='위험한 건'),
    kin('위험한 건 나이가 아니라 / *처음 6개월*', '위험한 건', y=220, size=104, until='지게차운전기능사', sfx='hit'),
    kin('지게차 시험 / *11만 명+*', '십일만', y=220, size=116, until='로봇 지게차'),
    kin('로봇 지게차 = *큰 곳부터* / 작은 공장은 한참 뒤', '로봇 지게차', y=220, size=96, until='삼 톤'),
    kin('3톤 이상 = *면허 필수*', '삼 톤', y=240, size=116, mode='pop'),
]},
{'from': '다음은 법이 사람을 앉히라고', 'enter': 'wipe', 'bg': [('i_mgmt_office', None), ('v:s_senior_study', '오십대'), ('i_elevator_notice', '경비원은 줄어도')], 'cam': [('cardL', '주택관리사입니다')], 'items': [
    CLEAR, cutsfx('오십대', '경비원은 줄어도'),
    kin('5060이 가장 따고 싶은 자격증 / *법전 공부*', '+0.1', y=230, size=96, until='주택관리사입니다'),
    kin('*주택관리사*', '주택관리사입니다', x=1060, y=190, size=120, mode='pop', sfx='hit'),
    kin('합격자 50대+ / *10명 중 7명*', '열 명 중 일곱', x=1060, y=370, size=80),
    kin('법이 정한 자리 / *관리사무소장*', '관리사무소장으로', x=1060, y=370, size=80, mode='slide'),
    kin('평균 연봉 *4,500만*', '사천오백만', x=1060, y=590, size=84),
    tag('상대평가 · 민원 폭탄', '상대평가', 1040, 780, icon='alert-triangle', tone='red', size=44),
]},
{'from': '마지막 자가진단입니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('자가진단 *③*', '+0.1', y=150, size=100, mode='drop', sfx='whoosh'),
    kin('은퇴 후 쓸 *자격증·기술* / 서랍에 없다?', '은퇴 후에', y=340, size=100),
]},
{'from': '금융기관에서 정년퇴직한', 'enter': 'zoom', 'bg': [('i_study_night', None), ('v:s_exam', '왜 그렇게까지')], 'cam': [('push', '+0.0', 40, 50, 1.15)], 'items': [
    SOFT, cutsfx('왜 그렇게까지'),
    puppet('c_banker', '+0.2', 1380, 380, w=420, move='hand-stop', dx=-260, dur=9),
    kin('은행 정년퇴직 *60대*', '+0.2', x=120, y=170, w=1100, size=92, until='왜 그렇게까지'),
    kin('*3번* 떨어지고 / 다시 책을 폈다', '세 번 도전한', x=120, y=360, w=1100, size=100, until='왜 그렇게까지', sfx='hit'),
    *stack([('일흔 넘어서도 일한다', '일흔이', 'clock', 'green'), ('건강보험료 부담 ↓', '건강보험료', 'heart-handshake', 'green')], x=120, y=220, gap=130, size=60),
    kin('그가 딴 자격증 = *전기기사*', '전기기사입니다', y=560, size=110, mode='pop', sfx='hit'),
]},
{'from': '이 길에 사람이 몰리고', 'enter': 'wipe', 'bg': [('v:s_electrician', None), ('v:s_e_panel', '월급이')], 'cam': [('cardR', '+0.3')], 'items': [
    CLEAR, cutsfx('월급이'),
    kin('전기기능사 50대+ 합격 / *+40%*', '사십 퍼센트', x=110, y=210, w=780, size=78, sfx='hit'),
    kin('시험이 쉬워서? / !아니다!', '시험이 쉬워서', x=110, y=470, w=780, size=72, until='월급이'),
    kin('월급이 많아서? / !아니다!', '월급이', x=110, y=470, w=780, size=72),
    tag('강남 빌딩 · 월 330만 원', '삼백삼십만', 110, 730, icon='building-skyscraper', tone='dark', size=54),
]},
{'from': '남는 이유는 법과 몸입니다', 'enter': 'zoom', 'bg': [('i_electric_room', None), ('v:s_powerline', '경비원 순찰은')], 'cam': [('push', '+0.0', 55, 50, 1.2)], 'items': [
    SOFT, cutsfx('경비원 순찰은'),
    kin('남는 이유 = *법* + *몸*', '+0.1', y=190, size=116, mode='pop', until='전기안전관리법'),
    article('전기안전관리법', '법률', '일정 규모 이상 전기설비 → 전기안전관리자 선임 의무', '전기안전관리법', mark='선임', markat='선임하도록', x=420, y=180, rot=-2, until='그 빌딩'),
    kin('매달 *4번 이상* 점검', '네 번', y=240, size=116, until='경비원 순찰은'),
    kin('순찰 → 카메라 / 점검표 → *사람 이름*', '경비원 순찰은', y=240, size=104, sfx='hit'),
]},
{'from': '마지막 조각은 AI 그 자체', 'enter': 'flash', 'bg': [('v:s_datacenter', None), ('i_datacenter', '미국 노동통계국'), ('v:s_code', 'AI가 우리')], 'cam': [('crash', '팔 배', 50, 50, 1.3)], 'items': [
    SOFT, cutsfx('미국 노동통계국', 'AI가 우리'),
    group('미국 노동통계국', roll(1, 8, '팔 배', y=200, size=230, suffix='배', tone='good'),
          tag('데이터센터 전기 신청 2023→2027', '데이터센터', None, 520, tone='dark', size=56)),
    kin('미국 전기기술자 / 매년 *8만 명+* 신규', '팔만', y=230, size=104, until='AI가 우리'),
    kin('AI가 커질수록 / *전기를 지키는 자리* 증가', 'AI가 우리', y=230, size=100, until='물론 자격증만'),
    tag('자격 · 경력 · 현장경험이 필요', '물론 자격증만', None, 300, tone='ghost', size=58),
]},
{'from': '지난 영상에 남겨 주신 댓글 중 가장', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    kin('지난 영상 *최다 댓글*', '+0.1', y=150, size=84, mode='drop'),
    kin('"판사·국회의원부터 / *AI로 바꾸자*"', '판사와', y=310, size=104, mode='pop'),
    kin('끝까지 남는 자리 = / *책임지는 자리*', '책임을 지는', y=600, size=92, sfx='hit'),
]},
{'from': '왜 아이의 첫 직장과 아버지의 마지막 직장이 한꺼번에 흔들릴까요', 'enter': 'zoom', 'bg': [('i_seoul_jobs', None), ('v:s_powerline', '그리고 그 파도가'), ('i_electric_room', '보고서는')], 'items': [
    SOFT, cutsfx('그리고 그 파도가', '보고서는'),
    kin('겉으로는 AI / 실제로는 *기계 + 인구*', '겉으로는', y=220, size=104, until='그리고 그 파도가'),
    *stack([('법이 이름을 요구', '법이 사람', 'scale', 'green'), ('몸이 현장에', '몸이 그 자리에', 'hand-stop', 'green'), ('숙련이 쌓인다', '숙련이', 'trending-up', 'green')], x=600, y=160, gap=120, size=58),
    kin('*모라벡의 역설*', '모라벡의', y=540, size=104, mode='pop'),
    tag('보고서는 AI · 차단기는 사람', '보고서는', None, 720, tone='red', size=52),
]},
{'from': '이제 채점하겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('cream'),
    *stack([('같은 동작으로 끝나는 일', '정해진 자리에서', 'scan', 'dark'), ('내 이름 없는 자리', '내 이름이', 'scan', 'dark'), ('텅 빈 서랍', '텅 빈', 'scan', 'dark')], x=120, y=260, gap=150, size=50),
    tag('0개 · 안심', '하나도 없다면', 1180, 240, tone='green', size=52),
    tag('1개 · 지켜볼 만', '하나라면', 1180, 380, tone='dark', size=52),
    tag('2개 · 움직이는 중', '둘이라면', 1180, 520, tone='red', size=52),
    tag('3개 · 다음 명단', '셋 모두라면', 1180, 660, tone='red', size=58),
]},
{'from': '희망도 숫자로 확인됩니다', 'enter': 'zoom', 'bg': [('v:s_senior_study', None), ('v:s_electrician', '준비도 멀지')], 'items': [
    SOFT, cutsfx('준비도 멀지'),
    puppet('c_electrician', '+0.3', 1320, 400, w=400, move='hand-stop', dx=-240, dur=9),
    kin('정진광 씨 / 쉰 중반에 *기전기사*', '정진광', x=120, y=200, w=1050, size=92, until='준비도 멀지'),
    kin('*7년째* 현장', '칠 년째', x=120, y=470, w=1050, size=100, until='준비도 멀지', sfx='hit'),
    *stack([('국민내일배움카드 · 만 75세 미만', '국민내일배움카드', 'ticket', 'green'), ('중장년내일센터 상담', '중장년내일센터', 'mail', 'green')], x=120, y=260, gap=150, size=58),
]},
{'from': '다시 그 엘리베이터 앞입니다', 'enter': 'fade', 'bg': [('v:s_elevator', None), ('v:s_e_panel', '건물 지하에는'), ('i_guard_snow', '한쪽은 사라지는'), ('v:s_seoul', '은퇴 후 여러분의')], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    SOFT, cutsfx('건물 지하에는', '한쪽은 사라지는', '은퇴 후 여러분의'),
    kin('경비원 줄이자는 공고 / 그 지하엔 *전기실*', '건물 지하에는', y=220, size=96, until='한쪽은 사라지는'),
    kin('사라지는 이름 / *남는 이름*', '한쪽은 사라지는', y=230, size=116, mode='pop', until='은퇴 후 여러분의'),
    kin('어느 종이에 적힐지는 / *지금부터의 준비*', '은퇴 후 여러분의', y=240, size=100, sfx='hit'),
]},
{'from': '여러분이라면 정년 없는', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    group('숫자로 확인하고', card('1번', '정년 없는 관리소장', '관리소장과', 220, 230, w=680, h=300),
          card('2번', '일흔까지 전기 기술', '전기 기술', 1020, 230, w=680, h=300, hot=True),
          kin('번호로 *댓글* 주세요', '우리 가족이', y=640, size=84)),
    kin('숫자로 확인하고 / *사실로 말하는 곳*', '숫자로 확인하고', y=260, size=110, mode='pop'),
    tag('지혜호수_경제연구소', '지혜호수', None, 600, tone='ghost', size=60),
]},
]

# 순위 배지(왼쪽 위, 칸 내내) — 순위 공개 장면은 각자 넣었다. 나머지 장면에 still 배지.
RANKS = [('그해 칠월 일일', '7', '고속도로 요금수납원'), ('국내 은행 점포는', '6', '은행 창구 직원'), ('한 시중은행은', '5', '콜센터 상담원'),
         ('그 빈자리를 채운 건', '4', '마트 계산원'), ('지난 영상에 남겨 주신 댓글 중에는 교사', '3', '초등학교 교사'), ('한국은행 분석을 보면', '2', '신입 사무직'),
         ('이 일은 오랫동안', '1', '아파트 경비원'), ('일곱 자리를 정리', None, None)]
STOP = ('여기서 첫 번째 자가진단',)
rk = None
for sc in PLAN:
    f = sc['from']
    for k, r, n in RANKS:
        if f.startswith(k): rk = (r, n) if r else None; break
    if rk and not f.startswith(STOP) and not any(getattr(i, '__name__', '') == 'rb' for i in sc['items']):
        if not any(f.startswith(k) for k in ('올해 사월 초', '은행에 전화를', '매출은 사상', '이번엔 손주가', '우리 때 신입사원', '서울 강서구의')):
            sc['items'].append(rankbadge(rk[0], rk[1], '+0', still=True))
# 단서 배지: 한 번 뜬 뒤 다음 단서까지 유지
QB = [('올해 사월 초', '<b>단서</b> ① 기계가 받는 돈'), ('은행에 전화를', '<b>단서</b> ① 기계가 받는 돈 ② 손님이 직접'), ('우리 때 신입사원', '<b>단서</b> ①돈 ②손님 직접 ③인구'),
      ('서울 강서구의', '<b>단서</b> ①돈 ②손님 ③인구 ④신입 일'), ('일곱 자리를 정리', None), ('먼저 몸이 있어야', '<b>남는 자리</b> ① 법 ② 몸 ③ 50+'), ('지난 영상에 남겨 주신 댓글 중 가장', None)]
q = None
for sc in PLAN:
    for k, v in QB:
        if sc['from'].startswith(k): q = v; break
    has = any('qbadge' in str(getattr(i, '__qualname__', '')) for i in sc['items'])
    if q and not has: sc['items'].append(qbadge(q))
