"""중산층몰락 본문 (0:57~17:35). 황학동 → 폐업 백만 → 잘나가던 시절 → 흔한 설명 3개 → 진짜 원인 3개(빈칸·빚·상가) → 끄떡없는 분들 → 결말.
화면: 레퍼런스(돈흐르네)처럼 실사 다큐 사진 + 키워드 팝업 + 숫자 그래픽. 그림은 input/그림_대본대조.json 의 문장과 1:1.
움직이는 영상은 글자 없는 장면만(ph_first_home · ph_retire_morning · ph_night_alley · ph_fridge_closeup · 황학동 재등장)."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, flipcard, bubble, group, raw, flow, igrid, punch, bars,
                 meter, timeline, chain, mgbg, qbadge, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.66; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.85; --blur:0px}</style>')
VID = raw('<style>.bg{--dark:.95; --blur:0px}</style>')
def P(n=50, m=50, z=1.1): return [('push', '+0.0', n, m, z)]
QB1 = qbadge('설명 ① 월급 빼고 다 올랐다'); QB2 = qbadge('설명 ② 다들 지갑을 닫았다'); QB3 = qbadge('설명 ③ 사장님이 너무 많다')
QC1 = qbadge('원인 ① 빈칸'); QC2 = qbadge('원인 ② 빚'); QC3 = qbadge('원인 ③ 상가')

BODY = [
# ================= 황학동 · 폐업 백만 (0:57~2:34) =================
{'from': '이 거리는 원래 돈이', 'enter': 'zoom', 'bg': [('ph_trade_truck', None)], 'cam': P(), 'items': [
    SOFT,
    kin('돈이 *빙글빙글* 도는 거리', '+0.1', y=110, size=100, mode='pop', until='한쪽에선'),
    group('끝나는 사람과', flow([('문 닫는 가게', '문 닫는'), ('집기', '집기를'), ('새로 여는 가게', '새로 여는')], y=140, size=70)),
    kin('끝과 시작이 / *손바닥을 맞대는* 자리', '끝나는 사람과', y=110, size=100, mode='drop'),
]},
{'from': '그런데 올여름, 이 거리', 'enter': 'flash', 'bg': [('ph_warehouse_pile', None)], 'cam': P(50, 55, 1.12), 'items': [
    SOFT,
    kin('올여름, 상인들 말이 *달라졌다*', '+0.05', y=110, size=96, mode='drop', until='물건은'),
    kin('들어오는 물건 *꾸역꾸역* / !나가는 속도!는 못 따라가', '물건은', y=110, size=96, mode='pop', until='고치고'),
    kin('안 팔리면 / !고스란히 손해!', '고치고', y=110, size=104, mode='drop', until='창업하겠다는'),
    kin('창업 문의도 / *부쩍* 줄었다', '창업하겠다는', y=110, size=104, mode='pop'),
]},
{'from': '평생 모은 돈을 지키는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('평생 모은 돈을 지키는 이야기', '+0.0', y=200, size=86, mode='drop'),
    kin('*구독* 눌러 두세요', '구독', y=360, size=150, mode='pop', sfx='ding'),
]},
{'from': '왜 이렇게 됐을까요', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    kin('왜 이렇게 됐을까?', '+0.0', y=150, size=96, mode='drop', until='이천이십사 년'),
    kin('2024년 폐업 신고 사업자', '이천이십사 년', y=150, size=80, mode='drop'),
    roll(0, 100, '백만 명', y=290, size=220, suffix='만 명+', tone='bad'),
    stamp('통계 작성 후 처음', '통계를 만든', x=1150, y=600, size=84, rot=-6),
]},
{'from': '그럼 이듬해는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('그럼 2025년은?', '+0.0', y=140, size=90, mode='drop'),
    swapnum('100만 명+', '97만 명대', '+0.3', '구십칠만', y=300, size=150, tone='good'),
    kin('그런데 *딱 한 연령대*만 / !거꾸로!', '숨통이', y=560, size=90, mode='pop'),
]},
{'from': '육십 세 이상입니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('*60세 이상*', '+0.0', y=110, size=130, mode='pop'),
    bars([('2023년 폐업자 중', 22.3 / 24.4 * 0.92, '22.3%', '이천이십삼 년', True), ('2025년 폐업자 중', 0.92, '24.4%', '이천이십오 년', False)], top=330),
    tag('폐업자가 줄곧 늘어난 유일한 연령대', '조사 기간', None, 720, tone='red', size=54),
]},
{'from': '어쩌면 그중 한 분이', 'enter': 'fade', 'bg': [('ph_reunion', None)], 'cam': P(50, 45, 1.08), 'items': [
    CLEAR,
    kin('그중 한 분이 / *우리 동창*일지도', '+0.1', y=110, size=100, mode='rise'),
]},
{'from': '다른 세대는 하나둘', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('다른 세대는 *하나둘* 접는데', '+0.0', y=220, size=96, mode='drop', until='왜 은퇴한'),
    kin('왜 은퇴 세대만 / !거꾸로! 뛰어들었나?', '왜 은퇴한', y=220, size=110, mode='pop', until='그 답은'),
    kin('답은 / *가장 잘나가던 시절*에', '그 답은', y=220, size=116, mode='pop'),
]},
# ================= 잘나가던 시절 · 허리 (2:34~4:56) =================
{'from': '기억하실 겁니다', 'enter': 'fade', 'bg': [('ph_first_home', None)], 'items': [VID]},         # 영상 (글자 없음)
{'from': '그 뒤로 월급은', 'enter': 'zoom', 'bg': [('ph_family_1990s', None)], 'cam': P(), 'items': [
    SOFT,
    clist([('월급은 *꼬박꼬박*', '월급은'), ('집값은 *야금야금*', '집값은'), ('학원비 · 부모님 용돈', '학원비')], x=110, y=150, size=68, until='이 세대가'),
    kin('대한민국 / *중산층의 허리*', '이 세대가', y=200, size=130, mode='pop'),
]},
{'from': '그 허리는 지금도', 'enter': 'zoom', 'bg': [('ph_sandwich', None)], 'cam': P(50, 45, 1.1), 'items': [
    SOFT,
    kin('위아래로 *짐*', '+0.05', y=110, size=110, mode='drop', until='한 조사에서'),
    group('자식 결혼', igrid('user', 10, '한 조사에서', lit=4, litat='넷 넘게', cols=10, y=130, size=100, tone='bad'),
          kin('60년대생 10명 중 4명+ / 부모님께 월 *73만 원*', '칠십삼만', y=330, size=90, mode='pop')),
    kin('자식 결혼 자금까지 / !휘청휘청!', '자식 결혼', y=110, size=110, mode='drop', until='내 노후'),
    kin('내 노후 통장보다 / *남의 통장* 먼저', '내 노후', y=110, size=110, mode='pop'),
]},
{'from': '성적표도 나쁘지 않습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    group('그대로 믿으면',
          kin('가구 순자산 (작년 3월 말)', '+0.0', y=130, size=72, mode='drop'),
          bars([('50대', 0.82, '5억 5,161만', '오억 오천', False), ('60대', 0.82 * 53000 / 55161, '5억 3천만+', '오억 삼천', False),
                ('39세 이하', 0.82 * 22000 / 55161, '2억 2천만 미만', '이억 이천', True)], top=290),
          stamp('1등', '일등', x=1480, y=620, size=100, rot=-8),
          tag('자식 세대보다 2배 넘게', '두 배', None, 760, tone='dark', size=56)),
    punch('그대로 믿으면 안 됩니다', '그대로 믿으면', y=380, size=110),
    kin('왜일까요?', '왜일까요', y=640, size=90, mode='pop'),
]},
{'from': '그런데 이 순자산엔', 'enter': 'zoom', 'bg': [('ph_apartment_evening', None)], 'cam': P(), 'items': [
    SOFT,
    kin('순자산 = *사는 집값* 포함', '+0.05', y=110, size=96, mode='drop', until='집이 아무리'),
    kin('안방을 썰어 / !반찬!을 살 순 없다', '집이 아무리', y=110, size=104, mode='pop', until='서류상'),
    flipcard('서류상 부자', '지갑 속 부자', '서류상', '지갑 속', y=330, size=88),
    kin('돈이 없는 게 아니라 / *꽁꽁 묶인* 것', '돈이 없는', y=110, size=100, mode='drop'),
]},
{'from': '이 차이가 드러나는 날', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('차이가 드러나는 날', '+0.0', y=220, size=90, mode='drop'),
    kin('*월급이 끊기는 날*', '바로 월급이', y=380, size=140, mode='pop'),
    kin('떠올려 보시죠', '이런 장면을', y=620, size=70, mode='rise'),
]},
{'from': '삼십 년 넘게 부장님', 'enter': 'fade', 'bg': [('ph_retire_morning', None)], 'items': [VID]},   # 영상 (글자 없음)
{'from': '이럴 때 사장님 소리라도', 'enter': 'zoom', 'bg': [('ph_empty_shop_rent', None)], 'cam': P(45, 50, 1.1), 'items': [
    SOFT,
    kin('*사장님* 소리라도 다시', '+0.05', y=110, size=100, mode='drop', until='놀면'),
    bubble('놀면 뭐 하나, 가게라도 하나 해 보자', '놀면', 380, 150, size=58),
    kin('그 마음을 *탓할 일*은 아닙니다', '그 마음을', y=700, size=80, mode='rise'),
]},
{'from': '문제는 시간표입니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('문제는 *시간표*', '+0.0', y=120, size=100, mode='drop'),
    card('법정 정년', '60세', '법정 정년', 260, 250, w=620, h=300, vsize=120),
    card('국민연금 (1969년생부터)', '65세', '육십오 세', 1040, 250, w=620, h=300, hot=True, vsize=120),
    kin('그 사이 / !텅 빈 5년!', '오 년입니다', y=620, size=120, mode='pop'),
]},
{'from': '그리고 그 오 년의 입구에서', 'enter': 'zoom', 'bg': [('ph_severance_envelope', None)], 'cam': [('crash', '퇴직금입니다', 50, 50, 1.25)], 'items': [
    SOFT,
    kin('5년의 입구에서 손에 쥐는 / *큰돈 하나*', '+0.1', y=110, size=90, mode='drop', until='퇴직금입니다'),
    kin('*퇴직금*', '퇴직금입니다', y=110, size=150, mode='pop', until='이 돈이'),
    kin('이 돈의 행방 = / *사건의 열쇠*', '이 돈이', y=110, size=110, mode='drop'),
]},
{'from': '여기까지 확인한 건', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('여기까지 확인한 것', '+0.0', y=170, size=80, mode='drop'),
    kin('무너지는 골목 한가운데 / *은퇴 세대*', '무너지는', y=320, size=110, mode='pop', until='이제 흔히'),
    kin('흔한 설명 *3가지*, / 하나씩 따져 봅니다', '이제 흔히', y=320, size=104, mode='pop'),
]},
# ================= 흔한 설명 ① 월급 빼고 다 올랐다 (4:56~5:41) =================
{'from': '첫 번째 설명은 제목 그대로', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), qbadge('설명 ① 월급 빼고 다 올랐다', '+0.0', pop=True),
    kin('설명 ①', '+0.0', y=170, size=90, mode='drop'),
    kin('"월급 빼고 / *다 올랐다*"', '월급 빼고', y=300, size=130, mode='pop'),
    stamp('숫자로도 맞다', '숫자로도', x=1250, y=640, size=90, rot=-6),
]},
{'from': '올해 사월부터 유월까지', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), QB1,
    kin('올해 2분기 · 물가 뺀 근로소득', '+0.0', y=170, size=80, mode='drop'),
    big('−2.1%', '이 점 일', y=320, size=220, color='#ff4b4b'),
    tag('두 분기 연속 뒷걸음질', '두 분기', None, 640, tone='red', size=56),
]},
{'from': '반대로 장바구니는', 'enter': 'zoom', 'bg': [('ph_supermarket_checkout', None)], 'cam': P(), 'items': [
    SOFT, QB1,
    kin('장바구니는 *무거워졌다*', '+0.05', y=110, size=96, mode='drop', until='팔월 소비자물가'),
    kin('8월 소비자물가 / !+3.1%!', '팔월 소비자물가', y=110, size=110, mode='pop'),
]},
{'from': '한국은행은 칠월과 팔월', 'enter': 'zoom', 'bg': [('ph_bank_window', None)], 'cam': P(), 'items': [
    SOFT, QB1,
    kin('기준금리 7월·8월 / *두 번 연속 인상*', '+0.05', y=110, size=100, mode='drop', until='삼 년 반'),
    kin('*3년 반* 만의 인상', '삼 년 반', y=110, size=110, mode='pop', until='월급봉투는'),
    flow([('월급봉투 ↓', '월급봉투는'), ('대출 이자 ↑', '대출 이자는')], y=150, size=80),
]},
{'from': '마트 계산대 앞에서', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), QB1,
    kin('영수증 보고 / 입이 *쩍*', '+0.05', y=200, size=110, mode='pop', until='그러니 이 설명은'),
    kin('이 설명은 *사실*', '그러니 이 설명은', y=200, size=110, mode='drop'),
    kin('다만 / !안 맞는 조각!이 있다', '다만 이것만으로는', y=420, size=110, mode='pop'),
]},
# ================= 흔한 설명 ② 다들 지갑을 닫았다 (5:41~6:54) =================
{'from': '두 번째 설명은 이렇습니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), qbadge('설명 ② 다들 지갑을 닫았다', '+0.0', pop=True),
    kin('설명 ②', '+0.0', y=170, size=90, mode='drop'),
    kin('"다들 / *지갑을 닫았다*"', '다들 지갑을', y=300, size=130, mode='pop'),
]},
{'from': '그런데 올해 일월부터 삼월까지', 'enter': 'zoom', 'bg': [('ph_car_showroom', None)], 'cam': P(), 'items': [
    SOFT, QB2,
    kin('1분기 가구당 소비지출', '+0.05', y=110, size=86, mode='drop', until='오 점 삼'),
    kin('*+5.3%* · 3년 만에 최대', '오 점 삼', y=110, size=110, mode='pop', until='자동차'),
    kin('자동차·가구가 / *쑥쑥*', '자동차', y=110, size=110, mode='drop', until='누가 샀을까요'),
    kin('누가 샀을까?', '누가 샀을까요', y=110, size=120, mode='pop'),
]},
{'from': '주식 시장이 후끈', 'enter': 'flash', 'bg': [('ph_stock_board', None)], 'cam': P(), 'items': [
    SOFT, QB2,
    kin('주식 시장 *후끈*', '+0.05', y=110, size=100, mode='drop', until='가진 자산의'),
    flow([('자산값 ↑', '가진 자산의'), ('부자 된 기분', '부자가 된'), ('지갑 열기', '지갑을 엽니다')], y=140, size=72),
    tag('자산 효과', '자산 효과', None, 700, tone='dark', size=64),
]},
{'from': '같은 시기, 소득 분배', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), QB2,
    kin('소득 분배 지표 / *6년 만에 최악*', '+0.05', y=150, size=100, mode='drop', until='쓰는 집은'),
    card('쓰는 집', '더 쓰고', '쓰는 집은', 260, 300, w=620, h=280, vsize=90),
    card('못 쓰는 집', '더 못 쓰고', '못 쓰는 집은', 1040, 300, w=620, h=280, hot=True, vsize=90),
    kin('지갑이 / !둘로 쩍!', '지갑이 둘로', y=640, size=110, mode='pop'),
]},
{'from': '처음에 말씀드린 그 이상한', 'enter': 'zoom', 'bg': [('ph_export_port', None)], 'cam': P(50, 50, 1.12), 'items': [
    SOFT, QB2,
    kin('처음 말씀드린 *그 숫자*', '+0.05', y=110, size=96, mode='drop', until='나라가 번'),
    kin('3분기 나라 실질 소득 / *+18.8%*', '나라가 번', y=110, size=104, mode='pop'),
    tag('반도체 몫이 컸다', '반도체가', None, 380, tone='dark', size=58),
]},
{'from': '그런데 같은 석 달', 'enter': 'flash', 'bg': [('ph_empty_wallet_table', None)], 'cam': P(), 'items': [
    SOFT, QB2,
    kin('같은 석 달 / 집집 씀씀이는 !줄었다!', '+0.05', y=110, size=100, mode='drop', until='파업 같은'),
    group('나라가 번 돈이', tag('파업 같은 일시적 요인도', '파업 같은', None, 380, tone='dark', size=52)),
    kin('나라 돈이 / 지갑까지 *안 내려왔다*', '나라가 번 돈이', y=110, size=104, mode='pop'),
]},
# ================= 흔한 설명 ③ 사장님이 너무 많다 (6:51~8:24) =================
{'from': '그럼 갈라진 아래쪽에는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('갈라진 *아래쪽*엔 / 누가?', '+0.0', y=250, size=120, mode='pop', until='우리나라엔'),
    qbadge('설명 ③ 사장님이 너무 많다', '우리나라엔', pop=True),
    kin('설명 ③ "우리나라엔 / *사장님이 너무 많다*"', '우리나라엔', y=250, size=104, mode='pop'),
    stamp('일부 사실', '이것도 일부', x=1250, y=620, size=90, rot=-6),
]},
{'from': '일하는 사람 중 자영업자', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), QB3,
    kin('일하는 사람 중 자영업자', '+0.0', y=130, size=80, mode='drop'),
    donut(19.8, '+0.2', label='자영업자 비중', x=760, y=250, d=380, tone='bad'),
    tag('OECD 회원국 중 8번째로 높다', '여덟 번째', None, 740, tone='dark', size=56),
]},
{'from': '그런데 그 사장님이 누구냐', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), QB3,
    kin('그 사장님이 *누구냐*', '+0.0', y=130, size=90, mode='drop'),
    bars([('60세+ · 10년 전', .8 * 184 / 270, '184만', '백팔십사만', True), ('60세+ · 작년', .8, '약 270만', '이백칠십만', False),
          ('39세 이하 · 10년 전', .8 * 112 / 270, '112만대', '백십이만', True), ('39세 이하 · 작년', .8 * 88 / 270, '88만대', '팔십팔만', False)], top=270),
    tag('자영업자 10명 중 4명 넘게 60세 이상', '열 명 중 네 명', None, 800, tone='red', size=50),
]},
{'from': '젊은 사장님이 빠져나간', 'enter': 'zoom', 'bg': [('ph_old_owners_alley', None)], 'cam': P(), 'items': [
    CLEAR, QB3,
    kin('젊은 사장님 나간 골목 / *은퇴한 가장들*이 채웠다', '+0.1', y=110, size=96, mode='drop'),
]},
{'from': '결과는 참담했습니다', 'enter': 'zoom', 'bg': [('ph_empty_restaurant', None)], 'cam': P(), 'items': [
    SOFT, QB3,
    kin('결과는 *참담*', '+0.05', y=110, size=110, mode='drop', until='육십 세 이상 새내기'),
    kin('60세 이상 새내기 사장님 / *셋 중 하나*', '육십 세 이상 새내기', y=110, size=90, mode='drop', until='한 달로'),
    kin('1년 영업이익 / !1천만 원 미만!', '천만 원도', y=360, size=110, mode='pop', until='한 달로'),
    kin('한 달 / !83만 원!도 안 된다', '한 달로', y=110, size=120, mode='pop'),
]},
{'from': '한 사람으로선 옳은', 'enter': 'zoom', 'bg': [('ph_same_shops', None)], 'cam': P(), 'items': [
    SOFT, QB3,
    kin('한 사람에겐 / *옳은 선택*', '+0.05', y=110, size=100, mode='drop', until='그런데 모두가'),
    kin('모두 같은 계산 → / 같은 골목에 !떼로!', '그런데 모두가', y=110, size=100, mode='pop', until='한 집에는'),
    kin('한 집엔 *약* / 모두에겐 !독!', '한 집에는', y=110, size=110, mode='pop', until='이런 걸'),
    tag('구성의 오류', '구성의 오류', None, 200, tone='dark', size=80),
]},
{'from': '그런데 아직 하나가', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('그런데 아직 / *하나가 안 맞는다*', '+0.0', y=140, size=100, mode='drop', until='작년에 오 년'),
    kin('5년 넘게 버티다 폐업', '작년에 오 년', y=140, size=84, mode='drop'),
    big('31만 7천 명+', '삼십일만', y=280, size=180, color='#ff4b4b'),
    tag('2005년 이후 가장 많다', '이천오 년', None, 540, tone='red', size=54),
    kin('왜 *접지도 못하고* / 버텼을까?', '왜 접지도', y=670, size=90, mode='pop'),
]},
# ================= 진짜 원인 ① 빈칸 (8:24~9:26) =================
{'from': '진짜 원인은 세 가지로', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    kin('진짜 원인 *3가지*', '+0.0', y=150, size=100, mode='drop'),
    clist([('첫째 *빈칸*', '첫째 빈칸'), ('둘째 *빚*', '둘째 빚'), ('셋째 *상가*', '셋째 상가')], x=660, y=330, size=86),
]},
{'from': '국민연금을 받는 분들의', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), qbadge('원인 ① 빈칸', '+0.0', pop=True),
    card('국민연금 월평균 (7월)', '65만 원', '육십오만', 220, 240, w=640, h=300, vsize=110),
    card('적정 노후 생활비 (부부)', '298만 원', '이백구십팔만', 1060, 240, w=640, h=300, vsize=110),
    kin('빈칸 / !233만 원!', '이백삼십삼만', y=600, size=120, mode='pop'),
]},
{'from': '이제 퇴직금을 꺼내 보죠', 'enter': 'zoom', 'bg': [('ph_severance_envelope', None)], 'cam': P(), 'items': [
    SOFT, QC1,
    kin('이제 *퇴직금*을 꺼내 보면', '+0.05', y=110, size=96, mode='drop', until='작년에 퇴직연금'),
    kin('퇴직연금 계좌 10개 중 *8개+* / 한 번에 받는 일시금', '작년에 퇴직연금', y=110, size=86, mode='drop', until='그 일시금'),
    kin('일시금 평균 / *1,833만 원*', '그 일시금', y=110, size=110, mode='pop', until='이 돈으로'),
    kin('이 돈으로 빈칸을 메우면?', '이 돈으로', y=110, size=100, mode='drop'),
]},
{'from': '여덟 달이 안 됩니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), QC1,
    kin('!8달!도 못 간다', '+0.0', y=140, size=130, mode='pop'),
    meter(20, 8 / 3, '앞에서 기억해', y=420, cap='버텨야 할 5년(60개월) 중 · 한 칸 = 3개월', capat='앞에서 기억해'),
]},
{'from': '게다가 그 오 년 동안은', 'enter': 'zoom', 'bg': [('ph_calculator', None)], 'cam': P(), 'items': [
    SOFT, QC1,
    kin('그 5년엔 65만 원도 / !안 나온다!', '+0.05', y=110, size=100, mode='drop', until='허리띠를'),
    kin('최소 생활비로 버텨도 / *1년 남짓*', '허리띠를', y=110, size=104, mode='pop', until='계산기'),
    kin('한숨만 *푹푹*', '계산기', y=110, size=120, mode='drop'),
]},
# ================= 진짜 원인 ② 빚 (9:26~10:56) =================
{'from': '두 번째, 빚입니다', 'enter': 'wipe', 'bg': [('ph_loan_desk', None)], 'cam': P(), 'items': [
    SOFT, qbadge('원인 ② 빚', '+0.0', pop=True),
    kin('원인 ② *빚*', '+0.0', y=110, size=120, mode='pop', until='올해 일분기'),
    kin('60세 이상 자영업자 금융권 대출', '올해 일분기', y=110, size=80, mode='drop'),
    roll(96, 405, '사백오조', y=240, size=200, suffix='조 원', tone='bad'),
    tag('전체 자영업자 대출의 37%', '삼십칠', None, 500, tone='dark', size=54),
    stamp('10년 새 4배+', '네 배', x=1260, y=620, size=96, rot=-6),
]},
{'from': '연체는 뒷목을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), QC2,
    kin('석 달 넘게 못 갚은 / 60세 이상 자영업자', '+0.05', y=120, size=80, mode='drop'),
    swapnum('1,598명', '21,883명', '천오백구십팔', '이만 천팔백', y=330, size=150),
    stamp('4년 새 14배', '십사 배', x=1260, y=540, size=100, rot=-6),
    kin('한 번 빠지면 / 10명 중 *8명* 못 나온다', '한 번 연체에', y=680, size=76, mode='rise'),
]},
{'from': '이제 아까 그 조각이', 'enter': 'zoom', 'bg': [('ph_dismantle_shop', None)], 'cam': P(), 'items': [
    SOFT, QC2,
    kin('이제 *조각이 맞는다*', '+0.05', y=110, size=100, mode='drop', until='폐업을 결심'),
    kin('폐업 결심 때 / 10명 중 7명은 *빚*', '폐업을 결심', y=110, size=96, mode='drop', until='평균 팔천'),
    kin('빚 평균 / !8,531만 원!', '평균 팔천', y=110, size=110, mode='pop', until='문 닫는 데'),
    kin('문 닫는 비용도 / !1,286만 원!', '문 닫는 데', y=110, size=110, mode='pop', until='장사를 접는'),
    kin('울며 겨자 먹기로 / *문을 열어 둔다*', '장사를 접는', y=110, size=100, mode='drop'),
]},
{'from': '한국은행에도 사정은', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('한국은행의 *사정*', '+0.0', y=140, size=96, mode='drop'),
    *chain([('chart-line', '물가 3%대', '물가가'), ('home', '서울 아파트값 ↑', '서울 아파트값'), ('alert-triangle', '더 큰 불 막기', '금리를 그대로', 'hot')], y=300),
    tag('이자 부담이 빚 많은 고령층에 쏠릴 수 있다는 걱정도', '다만 그 이자', None, 720, tone='red', size=48),
]},
# ================= 진짜 원인 ③ 상가 (10:56~13:13) =================
{'from': '이제 마지막이자 가장 큰', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('마지막이자 / *가장 큰 원인*', '+0.0', y=280, size=124, mode='pop'),
]},
{'from': '처음에 말씀드린 구조', 'enter': 'zoom', 'bg': [('ph_shutter_two_men', None)], 'items': [
    VID,
    kin('사장님도 건물주도 / *같은 또래*', '문 닫는 가게의', y=110, size=104, mode='pop'),
]},
{'from': '지금 서랍 속에 상가', 'enter': 'zoom', 'bg': [('ph_contract_drawer', None)], 'cam': P(), 'items': [
    SOFT, qbadge('원인 ③ 상가', '+0.0', pop=True),
    kin('서랍 속 / *상가 분양 계약서*', '+0.05', y=110, size=100, mode='drop', until='은퇴하면'),
    kin('*따박따박* 월세 받는 노후', '은퇴하면', y=110, size=104, mode='pop'),
]},
{'from': '숫자가 그 꿈의 크기를', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), QC3,
    kin('60세 이상 자영업자가 가장 많이 하는 일', '올해 사월', y=130, size=74, mode='drop'),
    donut(39.4, '부동산업이었습니다', label='부동산업', x=420, y=260, d=380, tone='bad'),
    donut(14.9, '도소매업은', label='도소매업', x=1120, y=260, d=380, tone='good'),
]},
{'from': '그럼 월세 받는 노후는', 'enter': 'zoom', 'bg': [('ph_vacant_building', None)], 'cam': P(), 'items': [
    SOFT, QC3,
    kin('월세 받는 노후는 / *안녕할까?*', '+0.05', y=110, size=100, mode='drop', until='임대업자'),
    kin('1년 월세가 이자의 1.5배도 안 되는 / 임대업자 *18.7%*', '임대업자', y=110, size=86, mode='pop', until='작아 보이지만'),
    kin('그런데 이분들 대출 = / 임대업 대출의 !59%!', '작아 보이지만', y=110, size=100, mode='pop', until='빚이 큰'),
    kin('빚 클수록 / 월세로 이자 막기도 *빠듯*', '빚이 큰', y=110, size=100, mode='drop'),
]},
{'from': '이 숫자들을 겹쳐서', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'), QC3,
    kin('한 장면으로 *재현*', '+0.0', y=120, size=90, mode='drop'),
    *chain([('cash', '퇴직금으로 가게', '은퇴한 사장님이'), ('key', '건물주도 빚낸 은퇴자', '그 가게를 빌려준'),
            ('door-exit', '손님 줄어 폐업', '손님이 줄어'), ('trending-down', '월세 뚝', '건물주의 월세', 'hot'),
            ('building-bank', '이자는 칼같이', '대출 이자는', 'hot')], y=330),
]},
{'from': '한쪽이 넘어지면', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), QC3,
    kin('한쪽이 넘어지면 / *같이 넘어진다*', '+0.05', y=130, size=100, mode='drop', until='둘 다'),
    kin('둘 다 지갑을 / !꽉!', '둘 다', y=130, size=110, mode='pop', until='골목 손님은'),
    igrid('building-store', 8, '골목 손님은', lit=8, litat='골목 손님은', cols=8, y=420, size=130, tone='good', drop=5, dropat='다음 가게가'),
    kin('노후 자금을 몰아 건 / !지옥행 열차!', '같은 골목에 노후', y=130, size=104, mode='pop'),
]},
{'from': '은행 문턱도 높았습니다', 'enter': 'zoom', 'bg': [('ph_savings_bank_street', None)], 'cam': P(), 'items': [
    SOFT,
    kin('은행 *문턱*도 높았다', '+0.05', y=110, size=100, mode='drop', until='육십 세 이상 자영업자 대출의'),
    kin('60세 이상 자영업자 대출 / *셋 중 하나+* 이자 비싼 곳', '육십 세 이상 자영업자 대출의', y=110, size=88, mode='pop', until='소득이 낮은'),
    kin('저소득 자영업 대출자 53만 명 / !절반 넘게! 60세 이상', '소득이 낮은', y=110, size=88, mode='pop', until='엎친 데'),
    kin('*엎친 데 덮친 격*', '엎친 데', y=110, size=120, mode='drop'),
]},
{'from': '평생 일해서 모은 돈이', 'enter': 'fade', 'bg': [('ph_night_alley', None)], 'items': [VID]},   # 영상 (글자 없음) — 담담하게
{'from': '다음 편에서는 은퇴 후', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    tag('다음 편 예고', '+0.0', None, 220, tone='dark', size=56),
    kin('상가 대신 / *월세 같은 돈* 만들기', '+0.1', y=340, size=110, mode='pop'),
]},
# ================= 끄떡없는 분들 (13:08~15:25) =================
{'from': '그런데 같은 은퇴 세대 안에서도', 'enter': 'zoom', 'bg': [('ph_happy_couple', None)], 'cam': P(), 'items': [
    CLEAR,
    kin('그런데 *끄떡없는 분들*', '+0.05', y=110, size=104, mode='drop', until='무엇이 달랐을까요'),
    kin('무엇이 달랐을까?', '무엇이 달랐을까요', y=110, size=116, mode='pop'),
]},
{'from': '첫 번째 차이는 퇴직금을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), qbadge('차이 ① 받는 방식', '+0.0', pop=True),
    kin('차이 ① 퇴직금 *받는 방식*', '+0.0', y=130, size=86, mode='drop'),
    card('일시금 평균', '1,833만 원', '+0.3', 220, 260, w=640, h=300, vsize=96),
    card('나눠 받는 연금 평균', '1억 4,891만 원', '일억 사천', 1060, 260, w=640, h=300, hot=True, vsize=96),
    stamp('8배', '팔 배', x=860, y=600, size=120, rot=-6),
    tag('금액 기준 연금 수령 처음 60% 넘어', '육십 퍼센트', None, 790, tone='dark', size=50),
]},
{'from': '공정하게 짚을 점도', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('공정하게 *짚을 점*', '+0.0', y=140, size=90, mode='drop'),
    flipcard('연금을 골라서 넉넉', '쪼갤 만큼 있어서 쪼갰다', '애초에', '연금을 골라서', y=320, size=80),
    kin('한 번에 받은 돈은 한 번에 / 나눠 받은 돈은 *오래 남는다*', '한 번에 받은', y=650, size=76, mode='rise'),
]},
{'from': '두 번째 차이는 연금을', 'enter': 'zoom', 'bg': [('ph_pension_mail', None)], 'cam': P(), 'items': [
    SOFT, qbadge('차이 ② 쌓은 시간', '+0.0', pop=True),
    kin('차이 ② 연금을 *쌓은 시간*', '+0.05', y=110, size=96, mode='drop', until='국민연금을 매달'),
    kin('월 200만 원 넘게 받는 분 / *11만 6천 명*+', '국민연금을 매달', y=110, size=100, mode='pop', until='월급이 끊기는'),
    kin('월급 끊기는 날을 늦춘 만큼 / 연금 통장 *두둑*', '월급이 끊기는', y=110, size=96, mode='drop'),
]},
{'from': '그래서 한국은행 연구진의', 'enter': 'zoom', 'bg': [('ph_reemployed', None)], 'cam': P(), 'items': [
    CLEAR,
    kin('한국은행 연구진의 *처방*', '+0.05', y=110, size=96, mode='drop', until='은퇴자가 골목'),
    kin('골목으로 몰리기 전에 / *월급 받는 일자리*에서 더 오래', '은퇴자가 골목', y=110, size=88, mode='drop', until='정년 뒤'),
    tag('정년 뒤 재고용', '정년 뒤', None, 140, tone='dark', size=76),
]},
{'from': '당장 쓸 수 있는 장치도', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('당장 쓸 수 있는 *장치*', '+0.0', y=120, size=90, mode='drop'),
    kin('국민연금 늦게 받기(연기)', '국민연금은 받기', y=240, size=70, mode='drop'),
    clist([('한 달 *+0.6%*', '영 점 육'), ('1년 *+7.2%*', '칠 점 이'), ('5년 *+36%*', '삼십육')], x=680, y=360, size=80),
    tag('문 닫을 땐 점포 철거비 지원 제도도', '점포 철거비', None, 800, tone='dark', size=48),
]},
{'from': '하지만 냉정하게 봐야 할', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('냉정하게 봐야 할 숫자', '+0.0', y=130, size=86, mode='drop'),
    kin('2차 베이비붐 세대 (1964~1974년생)', '천구백육십사', y=250, size=66, mode='drop'),
    big('954만 명', '구백오십사만', y=360, size=200, color='#ffd400'),
    tag('이제 차례로 60세', '차례로', None, 660, tone='red', size=56),
]},
{'from': '우리나라 노인 소득 빈곤율', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('노인 소득 빈곤율', '+0.0', y=130, size=86, mode='drop'),
    donut(39.7, '+0.2', label='OECD 1위', x=760, y=250, d=400, tone='bad'),
    stamp('평균의 2.7배', '이 점 칠', x=1250, y=600, size=90, rot=-6),
]},
{'from': '게다가 우리 노인들은', 'enter': 'zoom', 'bg': [('ph_senior_worker', None)], 'cam': P(), 'items': [
    SOFT,
    kin('생활비 *절반가량*을 / 아직도 일해서', '+0.05', y=110, size=100, mode='drop', until='연금이 받쳐'),
    kin('연금 대신 / *몸으로* 메운다', '연금이 받쳐', y=110, size=110, mode='pop'),
]},
{'from': '그 구백오십사만 명 안에', 'enter': 'zoom', 'bg': [('ph_crowd_boomers', None)], 'cam': P(), 'items': [
    SOFT,
    kin('954만 명 안에 / *동생과 후배들*', '+0.05', y=110, size=100, mode='drop', until='그분들이 또'),
    kin('또 같은 골목으로 / !우르르! 몰린다면?', '그분들이 또', y=110, size=104, mode='pop'),
]},
# ================= 결말 (15:25~17:35) =================
{'from': '다시 황학동 냉장고 앞으로', 'enter': 'fade', 'bg': [('ph_hwanghak_fridges', None)], 'items': [VID]},   # 영상 (처음 장면으로)
{'from': '나라는 마흔아홉 해 만에', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('나라는 49년 만에 가장 많이 벌었는데 / 왜 *우리 지갑만*?', '+0.05', y=300, size=96, mode='pop'),
]},
{'from': '답은 세 줄입니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    kin('답은 *세 줄*', '+0.0', y=120, size=96, mode='drop'),
    clist([('월급 빼고 다 오름 = *불씨*', '월급 빼고 다 오른'), ('진짜 문제 = 월급 끊긴 뒤 !빈칸!', '진짜 문제는'),
           ('빈칸을 퇴직금·빚으로 → *같은 골목*', '그 빈칸을 퇴직금')], x=120, y=270, size=80),
]},
{'from': '중산층을 무너뜨린 건', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('중산층을 무너뜨린 건 / 낮은 월급이 아니라', '+0.05', y=220, size=96, mode='drop'),
    kin('*월급이 끊긴 뒤의 빈칸*', '끊긴 뒤의', y=480, size=120, mode='pop', sfx='ding'),
]},
{'from': '그래서 오늘 딱 세 가지만', 'enter': 'wipe', 'bg': [('ph_phone_pension', None)], 'cam': P(), 'items': [
    SOFT,
    kin('오늘 할 일 *3가지*', '+0.0', y=100, size=96, mode='drop'),
    clist([('내 *예상 연금액* 확인 (국민연금공단 누리집·앱)', '국민연금공단'), ('퇴직금은 *연금 계좌로 나눠 받기*부터 검토', '퇴직금은 받기'),
           ('상가 계약 전 *월세 vs 이자* 나란히', '상가를 생각')], x=70, y=250, size=64),
    group('상가를 생각', tag('50세 이상 가입자 10명 중 8명+ 예상 연금 모른다', '오십 세 이상 가입자', None, 760, tone='red', size=48)),
    tag('월세가 이자의 1.5배가 안 되면 → 위험 신호', '월세가 이자의', None, 760, tone='red', size=48),
]},
{'from': '황학동의 그 냉장고는', 'enter': 'fade', 'bg': [('ph_fridge_closeup', None)], 'items': [VID]},   # 영상 (글자 없음)
{'from': '그 냉장고가 다음 주인을', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('다음 주인을 만날지는', '+0.1', y=260, size=90, mode='rise'),
    kin('그 *5년의 빈칸*을 / 어떻게 채우느냐에', '결국 우리가', y=420, size=110, mode='rise'),
]},
{'from': '여러분은 퇴직금을 어떻게', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('여러분은?', '+0.0', y=130, size=96, mode='drop'),
    card('A', '한 번에 받기', '한 번에 받기와', 260, 290, w=620, h=260, vsize=80),
    card('B', '나눠 받기', '나눠 받기', 1040, 290, w=620, h=260, hot=True, vsize=80),
    tag('댓글로 남겨 주세요', '댓글로', None, 660, tone='dark', size=60),
]},
{'from': '다음 이야기도 골라 주세요', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('다음 이야기 *투표*', '+0.0', y=120, size=96, mode='drop'),
    clist([('1번 · 주택연금으로 *노후 월급*', '일번'), ('2번 · 은퇴자 상가 투자 *진짜 수익률*', '은퇴자 상가 투자'),
           ('3번 · 자녀 증여 *언제* 해야 덜 손해', '삼번')], x=130, y=280, size=78),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('teal'),
    kin('숫자로 확인하고 / *사실로 말하는 곳*', '+0.05', y=220, size=104, mode='rise'),
    kin('지혜호수 경제연구소', '지혜호수', y=480, size=90, mode='pop'),
    kin('*구독*', '구독해', y=640, size=120, mode='pop', sfx='ding'),
]},
]
