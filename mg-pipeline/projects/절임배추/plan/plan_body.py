"""절임배추 본문 (0:36~16:44) — 분할 카드 체크리스트(clist) 본문 40%+, 재탕 0, 쿵 최소."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, igrid, flipcard, bubble, group, raw,
                 puppet, mgbg, qbadge, polaroid, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.6; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')

BODY = [
# ================= 1막: 상자의 정체 =================
{'from': '상자를 연 그 집으로', 'enter': 'zoom', 'bg': [('i_salting', None), ('v:s_wash_veg', '왜 하필'), ('v:s_slice', '이십 킬로그램')], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR, cutsfx('왜 하필', '이십 킬로그램'),
    clist([('소금물에 *담그고*', '소금물에 담갔다가'), ('*씻고*', '씻고'), ('물기를 빼면 = *절임배추*', '물기를')], until='왜 하필'),
    kin('왜 *소금물*? / 물을 빼야 양념이 밴다', '왜 하필', x=1030, y=300, w=860, size=76, until='이십 킬로그램'),
    clist([('20kg 한 상자 = *6~8포기*', '이십 킬로그램'), ('가장 고된 *반나절*이 사라진다', '반나절이')]),
]},
{'from': '그런데 이 상자는 정체가', 'enter': 'wipe', 'bg': [('i_two_docs', None)], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    SOFT,
    kin('이 상자, / 정체가 *두 개*', '+0.1', y=170, size=110, mode='pop', until='파는 사람'),
    card('이름 ①', '농산물', '농산물로도', 220, 300, w=680, h=280),
    card('이름 ②', '절임식품', '절임식품으로도', 1020, 300, w=680, h=280, hot=True),
    kin('*기억해 두세요*', '기억해', y=680, size=84),
]},
{'from': '상자 안에는 보통 안내문', 'enter': 'zoom', 'bg': [('i_leaflet', None)], 'cam': [('crash', '수돗물로', 45, 40, 1.35)], 'items': [
    SOFT,
    kin('상자 속 *안내문*', '+0.1', y=200, size=110, until='수돗물로'),
    kin('"수돗물로 / *다시 씻지 마세요*"', '수돗물로', y=220, size=116, mode='pop', sfx='paper'),
]},
{'from': '상자 하나는 우리 집', 'enter': 'fade', 'bg': [('i_kimchi_fridge', None), ('v:s_delivery', '그 무게를'), ('i_invoice', '송장에는')], 'cam': [('cardR', '송장에는')], 'items': [
    SOFT, cutsfx('그 무게를', '송장에는'),
    kin('김치냉장고 *한 칸* / 손주가 먹을 김치', '+0.1', y=200, size=100, until='그 무게를'),
    kin('그 무게를 / *송장 한 장*으로 믿는다', '그 무게를', y=220, size=104, until='송장에는'),
    clist([('보낸 날짜 → *찍힘*', '보낸'), ('절인 날짜 → !있기도 없기도!', '절였는지는')], x=110, y=330, size=64),
]},
# ================= 2막: 전성기 =================
{'from': '이 상자는 어떻게 열 집 중', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('어떻게 *10집 중 6집*을 / 차지했을까?', '+0.1', y=300, size=104, mode='pop', sfx='whoosh'),
]},
{'from': '천구백구십사 년, 한국식품연구원', 'enter': 'zoom', 'bg': [('i_lab_1994', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    clist([('*1994* 한국식품연구원', '천구백구십사'), ('절인 배추를 *따로* 보관', '따로'), ('상품화 질문은 *그때 이미*', '이미')]),
]},
{'from': '혹시 기억나십니까', 'enter': 'fade', 'bg': [('i_yard_kimjang', None), ('i_bathtub', '아파트로')], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    SOFT, cutsfx('아파트로'),
    kin('그 시절 마당 / *고무 함지*', '+0.2', y=190, size=104, until='아파트로'),
    kin('아파트에선 *욕조*', '아파트로', y=200, size=110, until='허리는'),
    kin('끊어질 듯한 *허리* / 소금물에 *튼 손*', '허리는', y=210, size=100),
]},
{'from': '그러니 상자 하나로', 'enter': 'zoom', 'bg': [('v:s_cooking', None)], 'items': [
    SOFT,
    kin('몇만 원 더 내고 산 것 = / *하루치 허리*', '몇만', y=240, size=104, mode='pop'),
]},
{'from': '얼마나 늘었을까요', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('절임배추 사는 집', '+0.1', y=120, size=80, mode='drop'),
    clist([('2012년 *42%*', '사십이'), ('2016년 *51%* · 절반 돌파', '오십일'), ('2025년 !59%!', '오십구')], x=540, y=260, size=84),
    kin('10집 중 4집 → *6집*', '열 집 중 넷', y=760, size=80),
]},
{'from': '그런데 절반을 넘긴', 'enter': 'zoom', 'bg': [('v:s_documents', None)], 'cam': [('cardR', '+0.3')], 'items': [
    CLEAR,
    clist([('2016년 *같은 조사*', '같은 조사에는'), ('안 사는 집에 *이유*를 물으니', '이유를'), ('!"비위생적이라 못 믿어"!', '비위생적이라'), ('*10명 중 3명*', '열 명 중 셋이')], x=110, y=280, size=56),
]},
{'from': '그래도 흐름은 멈추지', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('4인 가족 김장 배추', '+0.1', y=140, size=80, mode='drop'),
    swapnum('24포기+', '18포기', '스물네', '열여덟', y=280, size=140, tone='good'),
    kin('적게, 대신 *편하게*', '적게', y=600, size=100),
]},
{'from': '유통가 풍경도', 'enter': 'zoom', 'bg': [('i_preorder', None), ('v:s_phone_shop', '가을이'), ('i_elevator_boxes', '아파트 엘리베이터')], 'items': [
    SOFT, cutsfx('가을이', '아파트 엘리베이터'),
    kin('2022 사전예약 / *역대 최대* 물량', '이천이십이', y=200, size=100, until='가을이'),
    kin('도착 날짜를 고르는 / *달력*', '가을이', y=210, size=104, until='아파트 엘리베이터'),
    kin('상자가 쌓이는 날 = / *그 동네 김장 날*', '아파트 엘리베이터', y=220, size=100),
]},
{'from': '하지만 그보다 앞선', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('불만 신고 / 한 해 !500여 건!', '오백여', y=200, size=120, mode='pop', sfx='ding'),
    tag('2016 · 시민단체 집계', '시민단체', None, 520, tone='ghost', size=48),
    kin('잘 팔리는 만큼 / *금*도 함께', '잘 팔리는', y=650, size=76),
]},
# ================= 3막: 의심 확인 =================
{'from': '그 금은 무엇이었을까요', 'enter': 'flash', 'bg': [('i_lab_test', None)], 'cam': [('crash', '직접', 50, 50, 1.3)], 'items': [
    SOFT,
    kin('2018 / 공공기관이 *상자를 열다*', '+0.1', y=230, size=110, mode='pop', sfx='whoosh'),
]},
{'from': '한국소비자원이 온라인에서', 'enter': 'zoom', 'bg': [('v:s_microscope', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    clist([('온라인 절임배추 *15개* 검사', '십오'), ('!1개! 대장균 기준 초과', '대장균이'), ('분변 오염 → *비위생* 우려', '분변을')], size=60),
]},
{'from': '소비자원은 접수된', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('피해 사례 *19건*', '십구', y=150, size=110, mode='pop'),
    *stack([('부패', '부패', 'alert-triangle', 'red'), ('변질', '변질', 'alert-triangle', 'red'), ('이물질', '이물질', 'alert-triangle', 'red'), ('악취', '악취였습니다', 'alert-triangle', 'red')], x=800, y=360, gap=120, size=60),
]},
{'from': '역시 중국산 때문이구나', 'enter': 'zoom', 'bg': [('i_suspect', None)], 'cam': [('push', '+0.0', 40, 50, 1.15)], 'items': [
    SOFT,
    kin('역시 *중국산?*', '+0.1', y=190, size=130, mode='pop', until='유명 산지'),
    tag('커뮤니티 후기', '유명 산지', 1180, 220, tone='ghost', size=44),
    bubble('"다른 배추 같았다"', '유명 산지', 1020, 320, size=58),
]},
{'from': '이 의심은 일부 사실', 'enter': 'zoom', 'bg': [('i_kimchi_factory', None)], 'cam': [('cardR', '이천이십사')], 'items': [
    CLEAR,
    kin('일부는 *사실*', '+0.1', y=240, size=130, mode='pop', until='이천이십사'),
    clist([('2024 *전북 김치공장*', '전북의'), ('중국산 섞고 *국산* 표시', '국산으로'), ('!입건!', '입건됐습니다'), ('산지 거짓 표시도 *단속 대상*', '이름난')], x=110, y=260, size=56),
]},
{'from': '그런데 숫자를 보겠습니다', 'enter': 'wipe', 'bg': [('i_market_inspect', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    clist([('2024 김장철 *4만 9천 곳* 점검', '사만'), ('위반 185건 중', '백팔십오'), ('배추김치 !143건!', '백사십삼'), ('배추 *13건*', '열세')], size=56),
]},
{'from': '지난해도 비슷합니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    donut(76, '백팔', label='식당', x=160, y=200, d=440, tone='bad', cap='적발 142곳 중 108곳'),
    kin('위반 146건 중 / 배추김치 *119건*', '백십구', x=760, y=230, w=1080, size=90),
    kin('둔갑 = 주로 / *식당 김치 접시*', '둔갑은', x=760, y=520, w=1080, size=86),
]},
{'from': '허술하게 찾은 것도', 'enter': 'zoom', 'bg': [('v:s_market', None), ('v:s_restaurant', '그물을')], 'items': [
    SOFT, cutsfx('그물을'),
    kin('특별사법경찰 · 명예감시원 / *유통이력*으로 표적 단속', '특별사법경찰', y=220, size=76, until='그물을'),
    kin('그래도 걸리는 건 / *김치 접시*', '그물을', y=240, size=104),
]},
{'from': '그럼 소금은 어떨까요', 'enter': 'zoom', 'bg': [('i_salt_farm', None), ('i_salt_sacks', '두 배')], 'cam': [('cardR', '이천십육')], 'items': [
    CLEAR, cutsfx('두 배'),
    kin('그럼 *소금*은?', '+0.1', y=240, size=130, mode='pop', until='이천십육'),
    clist([('국산 천일염 *175원*/kg', '백칠십오'), ('수입 천일염 !70원!', '칠십 원'), ('두 배 차이 → *바꿔치기*', '두 배'), ('수입 소금 쓰고 국산 표시 !적발!', '잇달아')], x=110, y=260, size=54),
]},
{'from': '틀린 말은 아닙니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    flipcard('소금이 범인?', '정직의 문제일 뿐, 무르는 이유는 아니다', '+0.1', '정직의', y=170, size=70),
    tag('수입 소금도 검사 통과해야 수입 (식약처)', '검사를', None, 520, tone='dark', size=52),
    tag('호주산 천일염 섞었다고 밝힌 제품도', '호주산', None, 660, tone='green', size=52),
]},
{'from': '우리는 김치에 들어간 소금이', 'enter': 'fade', 'bg': [('v:s_saltpan', None), ('i_wilted', '중국산도')], 'items': [
    SOFT, cutsfx('중국산도'),
    kin('소금 원산지, / 물어본 적 *없다*', '+0.1', y=210, size=104, until='그보다'),
    kin('그보다 먼저 / *물어야 할 것*', '그보다', y=210, size=104, until='중국산도'),
    kin('그 *시큼한 냄새*는 / 어디서?', '중국산도', y=230, size=120, mode='pop', sfx='whoosh'),
]},
# ================= 4막: 진짜 원인 =================
{'from': '남은 조각은 세 가지', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('남은 조각 *3개*', '+0.1', y=130, size=96, mode='drop'),
    *stack([('① 달력', '달력', 'ticket', 'dark'), ('② 하루', '하루', 'clock', 'dark'), ('③ 이름', '이름입니다', 'file-invoice', 'red')], x=760, y=300, gap=175, size=78),
]},
{'from': '달력이 왜 중요할까요', 'enter': 'zoom', 'bg': [('i_peak_season', None), ('v:s_boxes', '일 년 내내')], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR, cutsfx('일 년 내내'),
    clist([('11월 하순 *10집 중 3집*', '십일월'), ('12월 상순 *또 3집*', '십이월'), ('→ 6집이 !3주!에 몰림', '삼 주'), ('1년 내내 파는 곳 *몇 곳뿐*', '일 년 내내')], size=54, until='사람도'),
    kin('사람·물·소금물 / *쉴 틈 없이*', '사람도', x=1030, y=300, w=860, size=84),
    tag('위생이 흔들릴 가능성 ↑', '위생이', 1030, 620, tone='red', size=50),
]},
{'from': '올해도 다르지 않습니다', 'enter': 'wipe', 'bg': [('v:s_supermarket', None)], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR,
    clist([('A 마트 물량 *+50%*', '오십 퍼센트'), ('B 마트 *+20%*', '이십 퍼센트'), ('절이는 날은 여전히 !몇 주!', '절이는 날은')], x=110, y=300, size=62),
]},
{'from': '둘째는 하루입니다', 'enter': 'flash', 'bg': [('i_box_overnight', None)], 'cam': [('push', '+0.0', 50, 50, 1.2)], 'items': [
    SOFT,
    kin('② *하루*', '+0.1', y=200, size=150, mode='drop', sfx='whoosh', until='우리는 보통'),
    kin('상한 채 왔다? / 순서가 *거꾸로*?', '우리는 보통', y=220, size=104),
]},
{'from': '식약처가 절임배추를 산', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    igrid('user', 5, '다섯 명 중', lit=1, litat='하루 이상', cols=5, y=170, size=160, tone='bad'),
    kin('구매자 500명 중 / *22.4%*가 하루 넘게 보관', '하루 이상', y=470, size=82),
    tag('상온 하루 → 대장균군 증가 가능 (식약처 실험)', '상온에서', None, 720, tone='red', size=48),
]},
{'from': '그래서 식약처는 하루를', 'enter': 'zoom', 'bg': [('i_rinse', None), ('v:s_tap', '온라인 후기')], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR, cutsfx('온라인 후기'),
    clist([('하루 넘기면 *씻어서*', '씻어'), ('3번 세척 → 세균 !-95%!', '구십오'), ('대장균군 !-93%!', '구십삼')], size=62),
    tag('후기: 미끈거려 다시 씻었다', '물엿을', 1030, 720, tone='ghost', size=40),
]},
{'from': '첫머리에서 기억해', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    card('판매자', '"씻지 마세요"', '판매자는', 220, 230, w=680, h=280),
    card('식약처', '"하루 넘기면 3번"', '식약처는', 1020, 230, w=680, h=280, hot=True),
    kin('문제는 *하루 넘긴 5집 중 1집*', '문제는', y=650, size=80),
]},
{'from': '판매자 쪽 사정도', 'enter': 'zoom', 'bg': [('v:s_wash_veg', None)], 'items': [
    SOFT,
    kin('너무 많이 씻으면 / *물러진다*', '너무 많이', y=210, size=104, until='식약처도'),
    kin('식약처도 *3번 이하*', '식약처도', y=230, size=116, until='씻지 말라는'),
    kin('씻지 말라는 안내에도 / *이유*가 있었다', '씻지 말라는', y=220, size=96),
]},
{'from': '편하자고 산 상자인데', 'enter': 'fade', 'bg': [('v:s_rain_window', None), ('v:s_clock', '여러분 댁은')], 'items': [
    SOFT, cutsfx('여러분 댁은'),
    kin('다시 씻기는 *귀찮고*', '+0.2', y=220, size=104, until='안내문이'),
    kin('안내문은 *씻지 말라*', '안내문이', y=220, size=104, until='그 하루가'),
    kin('그 *하루*가 / 김장을 망쳤다면?', '그 하루가', y=220, size=110, until='여러분 댁은'),
    kin('바로 쓰나요? / *하루 두나요?*', '여러분 댁은', y=220, size=110, mode='pop'),
    tag('댓글로 알려 주세요', '댓글로', None, 560, tone='ghost', size=52),
]},
{'from': '이제 가장 큰 조각이', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('③ *이름*', '셋째는', y=200, size=150, mode='drop', sfx='whoosh'),
    card('기억하시죠?', '이름이 두 개', '이 상자의', 610, 480, w=700, h=260),
]},
{'from': '절임배추를 사는 집은 열 집 중 여섯입니다', 'enter': 'zoom', 'bg': [('i_two_docs', None)], 'cam': [('cardR', '그런데 이천십팔')], 'items': [
    CLEAR,
    kin('10집 중 *6집*이 사는데', '+0.1', y=240, size=110, until='그런데 이천십팔'),
    kin('2018 조사 당시', '그런데 이천십팔', x=110, y=200, w=780, size=60, mode='slide'),
    clist([('절임식품 → 기준 *있음*', '절임식품으로'), ('농산물 → 기준 !없음!', '농산물로 등록하면')], x=110, y=330, size=66),
]},
{'from': '기준만 없던 게 아닙니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('정확한 *통계조차 없다*', '통계조차', y=220, size=116, mode='pop'),
    tag('2016 · 농촌경제연구원 연구원 지적', '농촌경제연구원의', None, 470, tone='ghost', size=48),
    kin('그 수를 / *아는 사람이 없다*', '그 수를', y=610, size=84),
]},
{'from': '점검 숫자도 견줘 보겠습니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    card('위생 점검 (2022)', '135곳', '백삼십오', 220, 200, w=680, h=280, hot=True),
    card('원산지 점검', '수만 곳', '수만 곳을', 1020, 200, w=680, h=280),
    tag('깐마늘·곶감·시래기까지 합친 숫자', '깐마늘', None, 540, tone='ghost', size=46, until='촘촘한'),
    kin('원산지는 *촘촘한 그물* / 위생은 !성긴 그물!', '촘촘한', y=560, size=80),
]},
{'from': '물론 손을 놓고', 'enter': 'zoom', 'bg': [('v:s_lab', None), ('v:s_documents', '다만 그 가이드라인')], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR, cutsfx('다만 그 가이드라인'),
    clist([('식약처 *위생관리 가이드라인*', '가이드라인을 만들어'), ('원료 · 세척수 · *작업자 위생*', '작업자'), ('지켰는지는 상자에 !안 적힌다!', '적히지')], size=58),
]},
{'from': '그 사이 사는 사람이', 'enter': 'wipe', 'bg': [('i_door_boxes', None)], 'cam': [('cardR', '+0.3')], 'items': [
    CLEAR,
    clist([('언제 절였는지 *?*', '언제 절였는지'), ('어느 물로 씻었는지 *?*', '어느 물로'), ('소금물 몇 번 썼는지 *?*', '소금물은')], x=110, y=260, size=62),
    kin('파는 사람만 *안다*', '파는 사람은', x=110, y=640, w=780, size=78),
]},
{'from': '경제학 교과서는', 'enter': 'flash', 'bg': [('i_seller_buyer', None), ('i_lemon', '그러면 정직하게')], 'items': [
    SOFT, cutsfx('그러면 정직하게'),
    kin('*레몬 시장*', '레몬', y=190, size=150, mode='pop', until='파는 쪽만'),
    kin('파는 쪽만 속을 안다 / 사는 쪽은 *못 가린다*', '파는 쪽만', y=210, size=96, until='그러면 정직하게'),
    kin('정직한 집까지 / !의심!받는다', '그러면 정직하게', y=220, size=110),
]},
{'from': '그 정보 차이의 값은', 'enter': 'zoom', 'bg': [('v:s_money', None)], 'items': [
    SOFT,
    kin('정보 차이의 값 = *우리 지갑*', '+0.1', y=160, size=96),
    *stack([('버린 배추 세 상자', '버린', 'alert-triangle', 'red'), ('급히 다시 산 배추', '급히', 'shopping-cart', 'red'), ('하루 더 쓴 허리', '하루 더', 'clock', 'red')], x=620, y=360, gap=130, size=60),
]},
{'from': '그런데 같은 시장, 같은 배추로도', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('탈 없이 끝낸 집이 / *훨씬 많다*', '+0.1', y=220, size=110),
    kin('그 상자는 / *무엇이 달랐을까?*', '그 집 상자에는', y=540, size=96, mode='pop', sfx='whoosh'),
]},
# ================= 5막: 믿어도 되는 상자 =================
{'from': '다시 이천십팔 년 검사로', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    igrid('package', 15, '십오 개', lit=14, litat='나머지', cols=15, y=230, size=90, tone='good'),
    kin('15개 중 *14개* 정상', '나머지', y=470, size=100),
    kin('대부분의 상자는 *멀쩡했다*', '대부분의 상자는', y=660, size=78),
]},
{'from': '멀쩡한 상자는 뭐가', 'enter': 'zoom', 'bg': [('i_good_box', None)], 'cam': [('cardL', '앞에서 말씀드린')], 'items': [
    CLEAR,
    kin('겉면을 보면 *보인다*', '+0.1', y=240, size=120, mode='pop', until='앞에서 말씀드린'),
    clist([('해썹 시설 *5번* 세척', '해썹'), ('주문 *당일* 절임', '당일'), ('소비기한 *5일*', '소비기한은'), ('받는 날짜 *선택*', '받는 날짜는')], size=60),
]},
{'from': '다른 온라인몰의 한 제품은', 'enter': 'wipe', 'bg': [('v:s_phone_shop', None)], 'cam': [('cardR', '+0.3')], 'items': [
    CLEAR,
    clist([('원재료 칸에 *소금까지*', '원재료'), ('국산 + !호주산! 천일염', '호주산'), ('숨기지 않은 표시 = *믿을 근거*', '믿을')], x=110, y=300, size=60),
]},
{'from': '정리하면 이렇습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('상자 겉면 *4줄*', '+0.1', y=110, size=90, mode='drop'),
    clist([('① 언제 *절였는지*', '언제 절였는지'), ('② 어디 *배추*인지', '어디 배추인지'), ('③ 어떤 *소금*인지', '어떤 소금인지'), ('④ 언제 *받는지*', '언제 받는지')], x=600, y=240, size=76),
    kin('정보의 벽에 낸 *창문*', '창문을', y=800, size=72),
]},
{'from': '차이도 짚어야 합니다', 'enter': 'zoom', 'bg': [('i_price_tags', None), ('i_lab_test', '냉정하게')], 'items': [
    SOFT, cutsfx('냉정하게'),
    kin('늘 *싼 건 아니다*', '+0.1', y=200, size=110, until='천사백구십'),
    kin('kg당 *1,490원* ~ !3,490원!', '천사백구십', y=220, size=100, until='냉정하게'),
    kin('표시가 있다고 / *다 안전하진 않다*', '냉정하게', y=220, size=100),
]},
{'from': '어디서 사느냐도', 'enter': 'zoom', 'bg': [('i_farm_direct', None), ('v:s_field', '얼굴을 아는')], 'items': [
    SOFT, cutsfx('얼굴을 아는'),
    kin('산지 직구 / *10집 중 3집*', '산지에서', y=210, size=104, until='얼굴을 아는'),
    kin('아는 농가라면 / 날짜·소금 *물어보기 쉽다*', '얼굴을 아는', y=220, size=96),
]},
{'from': '직접 절이는 쪽으로', 'enter': 'fade', 'bg': [('i_family_salting', None), ('v:s_slice', '다만 직접')], 'items': [
    SOFT, cutsfx('다만 직접'),
    kin('"올해는 / *직접* 절이겠다"', '온라인 후기에는', y=210, size=104, until='다만 직접'),
    kin('직접 절이는 이유 1위 = *간*', '다만 직접', y=220, size=100),
    tag('10명 중 4명: 절임배추 간이 안 맞는다', '열 명 중 넷이', None, 520, tone='dark', size=52),
]},
{'from': '올해 사정은 조금', 'enter': 'zoom', 'bg': [('v:s_market', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    clist([('배추 1포기 *4천 원 미만*', '사천'), ('1년 전보다 *-13%*', '십삼'), ('김장재료 할인 *640억*', '육백사십억'), ('원산지 집중 단속 ~12월 초', '집중 단속')], size=56),
]},
{'from': '올해는 오 킬로그램', 'enter': 'wipe', 'bg': [('i_elevator_boxes', None)], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    SOFT,
    kin('*5kg* 작은 상자까지', '+0.1', y=210, size=116, until='김장이'),
    kin('작아질수록 / 상자 하나에 거는 *기대*는 커진다', '김장이', y=220, size=88),
]},
{'from': '배춧값이 싼 해에는', 'enter': 'zoom', 'bg': [('v:s_kimchi', None)], 'items': [
    SOFT,
    kin('싼 해엔 / 섞을 이유도 *줄어든다*', '+0.1', y=200, size=100, until='올해 더'),
    kin('올해 볼 것 = / 원산지보다 *날짜·위생*', '올해 더', y=210, size=100, until='올겨울'),
    kin('상자 겉면 *몇 줄*에서 갈린다', '올겨울', y=230, size=100),
]},
# ================= 결말 =================
{'from': '이제 처음 그 현관', 'enter': 'flash', 'bg': [('v:s_apartment', None)], 'items': [
    SOFT,
    kin('다시 *그 현관 앞*', '+0.1', y=210, size=110, until='열 집 중'),
    kin('10집 중 6집이 믿는데 / 왜 *해마다* 망쳤나?', '열 집 중', y=220, size=96, until='답은'),
    kin('답은 *세 줄*', '답은', y=240, size=140, mode='pop', sfx='whoosh'),
]},
{'from': '첫째, 중국산 둔갑은', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    clist([('① 둔갑은 주로 *식당 김치 접시*', '첫째'), ('② 김장은 *몇 주*에 · 받고 *하루* 넘김', '둘째'), ('③ 가장 큰 몫 = !알 길 없는 시장!', '셋째')], x=180, y=260, size=64),
]},
{'from': '우리는 상자를 살 때', 'enter': 'fade', 'bg': [('i_family_dinner', None), ('v:s_dinner', '망친 건')], 'items': [
    SOFT, cutsfx('망친 건'),
    kin('배추가 아니라 / 파는 사람의 *하루*를 산다', '그런데 실은', y=210, size=96, until='망친 건'),
    kin('망친 건 배추가 아니라 / *몰랐던 날짜*', '망친 건', y=220, size=110, mode='pop', sfx='hit'),
]},
{'from': '주문 전에 세 가지만', 'enter': 'zoom', 'bg': [('i_good_box', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    clist([('날짜·산지·소금 *확인*', '하나'), ('없으면 *물어보기*', '없으면'), ('받는 날 = *김장 전날·당일*', '둘'), ('하루 넘기면 *3번까지만* 세척', '셋')], size=54),
]},
{'from': '냄새가 이상하면', 'enter': 'zoom', 'bg': [('i_hotline', None)], 'items': [
    SOFT,
    kin('냄새가 이상하면 / *쓰지 말고 사진부터*', '+0.1', y=200, size=96, until='원산지가 의심되면'),
    kin('원산지 신고 / *1588-8112*', '원산지가 의심되면', y=220, size=124, mode='pop', sfx='ding'),
]},
{'from': '다시 그 현관 앞입니다', 'enter': 'fade', 'bg': [('v:s_delivery', None)], 'items': [
    SOFT,
    kin('올해는 상자보다 / *송장 날짜*부터', '+0.2', y=230, size=110, mode='pop'),
]},
{'from': '여러분은 올해 어느 쪽', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    card('1번', '절임배추를 산다', '일 번', 220, 220, w=680, h=280),
    card('2번', '직접 절인다', '이 번', 1020, 220, w=680, h=280, hot=True),
    tag('다음 이야기: 새우젓 · 고춧가루 · 포장김치', '다음 이야기도', None, 620, tone='dark', size=50),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'fade', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('숫자로 확인하고 / *사실로 말하는 곳*', '+0.1', y=250, size=110, mode='pop'),
    tag('지혜호수_경제연구소', '지혜호수', None, 600, tone='ghost', size=60),
]},
]

# 기억·조각 추적 배지 (오른쪽 위)
QB = [('그런데 이 상자는 정체가', '<b>기억</b> ① 이름 두 개'), ('상자 안에는 보통', '<b>기억</b> ① 이름 두 개 ② "씻지 마세요"'),
      ('남은 조각은', '<b>남은 조각</b> ①달력 ②하루 ③이름'), ('첫머리에서 기억해', '<b>남은 조각</b> ①달력 ✔ ②하루 ✔ ③이름'),
      ('그 정보 차이의', '<b>남은 조각</b> ①✔ ②✔ ③이름 ✔'), ('다시 이천십팔 년 검사로', None)]
q = None
for sc in BODY:
    for k, v in QB:
        if sc['from'].startswith(k): q = v; first = True; break
    else: first = False
    if q: sc['items'].append(qbadge(q, pop=first))
