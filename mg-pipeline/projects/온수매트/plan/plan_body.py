"""온수매트 단독 다큐 본문 (0:38.6~16:18). 1막 등 밑 추위·물병 / 2막 건너간 길·나비엔 / 3막 흔한 설명 /
4막 안전·가격·생활 방식 / 5막 같은 기술의 다른 길·전기 / 결말. 제작 그림(Gemini) + 실사 + 모션그래픽, clist 40%+, 재탕 0."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, flipcard, bubble, group, raw, flow,
                 puppet, mgbg, qbadge, kin, cutsfx, clist)
SOFT = raw('<style>.bg{--dark:.6; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')
DIM = raw('<style>.bg{--dark:.45; --blur:0px}</style>')

BODY = [
# ================= 1막: 등 밑의 추위 (0:38~2:52) =================
{'from': '침낭을 세 겹 덮었는데', 'enter': 'zoom', 'bg': [('v:s_frost_window', None)], 'cam': [('cardL', '싸구려였다면')], 'items': [
    CLEAR,
    kin('침낭 3겹인데 / 왜 등이 !얼음장?!', '+0.1', y=230, size=116, mode='pop', until='싸구려였다면'),
    clist([('싸구려? → *배·가슴*도', '싸구려였다면'), ('바람? → *얼굴*이 먼저', '바람이'), ('실제 후기: !등·엉덩이!', '엉덩이입니다')], size=70),
]},
{'from': '침낭이 따뜻한 건', 'enter': 'wipe', 'bg': [('g_sleepbag_cut', None)], 'cam': [('push', '+0.0', 50, 55, 1.1), ('crash', '납작하게', 50, 65, 1.3)], 'items': [
    SOFT,
    kin('솜 사이 *공기*가 / 따뜻함', '+0.1', y=150, size=104, until='누우면'),
    kin('누우면 등 밑 솜이 / !납작!', '누우면', y=150, size=110, mode='pop', until='위를 세 겹'),
    kin('열은 / *밑으로* 다 샌다', '위를 세 겹', y=150, size=116, mode='drop'),
]},
{'from': '현관문을 세 번', 'enter': 'flash', 'bg': [('g_door_locks', None)], 'cam': [('shake', '구멍을', 50, 60, 1.0)], 'items': [
    SOFT,
    kin('자물쇠 *3개* / 바닥엔 !구멍!', '+0.1', y=150, size=120, mode='pop'),
]},
{'from': '평생 가족을 위해', 'enter': 'fade', 'bg': [('v:s_snow_walk', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    raw('<style>.bg{--dark:.65; --blur:0px}</style>'),
    kin('평생 가족 위해 / 일하신 분들께', '+0.1', y=200, size=96, until='놓치지'),
    kin('놓치지 마세요 / *구독* 눌러 두세요', '놓치지', y=220, size=110, mode='pop', sfx='ding'),
]},
{'from': '그래서 미국 캠퍼들은 침낭보다', 'enter': 'zoom', 'bg': [('g_pad_layers', None)], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR,
    clist([('침낭보다 *깔개*부터', '깔개를'), ('냉기 차단 겨울 *5 이상*', '오 이상을'), ('추위는 !밑에서! 온다', '밑에서')], x=110, y=260, size=67),
    stamp('단서 ①', '기억해', x=1250, y=640, size=90),
]},
{'from': '우리 집도 다르지', 'enter': 'flash', 'bg': [('g_korean_living', None)], 'cam': [('push', '+0.0', 40, 60, 1.12)], 'items': [
    SOFT,
    kin('우리 집도 / 요 한 장 + *두꺼운 이불*', '+0.1', y=150, size=100, until='새벽에'),
    kin('새벽 / !허리!부터 시리다', '새벽에', y=170, size=124, mode='pop'),
]},
{'from': '미국 캠퍼들에게는 이 추위를', 'enter': 'zoom', 'bg': [('v:s_kettle', None), ('g_bottle_pour', '단단한'), ('g_bottle_hug', '양말로')], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT, cutsfx('단단한', '양말로'),
    kin('미국 캠퍼의 / *오래된 요령*', '+0.1', y=200, size=110, until='단단한'),
    kin('플라스틱 물병에 / *끓는 물*', '단단한', y=160, size=110, until='양말로'),
    kin('양말로 감싸 / *끌어안고* 잔다', '양말로', y=160, size=110),
]},
{'from': '미국 등산 블로그', 'enter': 'wipe', 'bg': [('v:s_mountain_snow', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR,
    clist([('미국 등산 블로그 *단골 요령*', '블로그'), ('2025.11 *행정안전부*', '행정안전부도'), ('텐트에선 *물주머니*로 체온', '물주머니로')], size=57),
]},
{'from': '요령은 꽤 꼼꼼합니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('요령은 *꼼꼼*하다', '+0.0', y=130, size=96, mode='drop'),
    clist([('끓는 물 되는 병인지 *확인*', '끓는 물을'), ('거꾸로 들어 *새는지*', '거꾸로'), ('발치 = 발 · 배 쪽 = *온몸*', '발치에')], x=330, y=330, size=72),
]},
{'from': '한 등산객은 침낭 속에', 'enter': 'zoom', 'bg': [('g_bottle_spill', None), ('v:s_suburb_snow', '영하 근처의')], 'cam': [('shake', '쏟아', 50, 50, 1.0)], 'items': [
    SOFT, cutsfx('영하 근처의'),
    kin('침낭 속에 / !물을 쏟은! 밤', '+0.1', y=170, size=116, mode='pop', until='영하 근처의'),
    kin('가벼운 침낭 + / *물병 하나*로 버텼다', '영하 근처의', y=200, size=104),
]},
{'from': '미국 캠퍼들은 이미 알고', 'enter': 'flash', 'bg': [('g_bottle_dawn', None), ('g_mat_boiler', '온수매트는')], 'cam': [('push', '+0.0', 50, 50, 1.1), ('crash', '온수매트는', 55, 55, 1.25)], 'items': [
    SOFT, cutsfx('온수매트는'),
    kin('물은 / *열을 오래 품는다*', '물은', y=160, size=110, mode='drop', until='문제는'),
    stamp('단서 ②', '물은', x=1300, y=640, size=90),
    kin('문제: 새벽이면 / !식는다!', '문제는', y=170, size=116, mode='pop', until='온수매트는'),
    kin('온수매트 = / 밤새 *식지 않는 물병*', '온수매트는', y=160, size=110),
]},
# ================= 2막: 어떻게 건너갔나 (2:52~4:47) =================
{'from': '그렇다면 이 물건은 어떻게', 'enter': 'zoom', 'bg': [('v:s_port', None)], 'cam': [('pull', '+0.0', 50, 50, 1.15)], 'items': [
    raw('<style>.bg{--dark:.6; --blur:0px}</style>'),
    kin('어떻게 / *미국 텐트*까지?', '+0.1', y=200, size=124, mode='pop', until='시작은'),
    kin('시작은 / 캠핑장이 !아니었다!', '시작은', y=220, size=110, mode='drop'),
    qbadge('어떻게 건너갔나?', '건너갔을까요', pop=True),
]},
{'from': '한인 마트의 진열대', 'enter': 'wipe', 'bg': [('g_hmart', None)], 'cam': [('cardL', '이천십육')], 'items': [
    CLEAR,
    kin('*한인 마트* 진열대', '+0.0', y=240, size=124, mode='pop', until='이천십육'),
    clist([('2016 *나비엔 메이트* 북미', '이천십육'), ('한인 마트·*공식 쇼핑몰*', '공식'), ('첫 손님 = *고국 잠자리*', '첫 손님은')], size=57),
]},
{'from': '그다음 길은 더 넓었습니다', 'enter': 'zoom', 'bg': [('g_costco', None), ('v:s_warehouse', '당시')], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT, cutsfx('당시'),
    kin('다음 길은 / *더 넓었다*', '+0.1', y=200, size=110, until='아쿠아라는'),
    kin('아쿠아 매트 / *캐나다 코스트코* → 미국', '아쿠아라는', y=170, size=100, until='당시'),
    tag('당시 미·캐나다 전기 안전 인증 = 이것 하나', '당시', None, 620, tone='dark', size=50),
]},
{'from': '지금 미국 아마존에는', 'enter': 'flash', 'bg': [('g_online_shop', None)], 'cam': [('push', '+0.0', 50, 45, 1.15)], 'items': [
    SOFT,
    kin('미국 아마존 상품명 / *"Onsu Mat"*', '+0.1', y=160, size=116, mode='drop'),
    stamp('한국 발음 그대로', '한국 발음을', x=1150, y=620, size=84),
]},
{'from': '이 대목에서 떠오르는', 'enter': 'fade', 'bg': [('g_postoffice', None)], 'cam': [('push', '+0.0', 45, 55, 1.1)], 'items': [
    SOFT,
    kin('자녀에게 / *온수매트* 부쳐 본 집', '자녀에게', y=160, size=104, until='무거운'),
    kin('"거기도 겨울은 / *춥겠지*"', '무거운', y=170, size=110, until='그 상자들이'),
    kin('그 상자가 이제 / *현지 진열대*에', '그 상자들이', y=170, size=110, mode='pop'),
]},
{'from': '그 뒤에는 한국 보일러', 'enter': 'zoom', 'bg': [('g_boiler_factory', None)], 'cam': [('cardR', '이천이십오 년 매출')], 'items': [
    CLEAR,
    kin('그 뒤엔 / *한국 보일러 회사*', '+0.1', y=240, size=116, mode='pop', until='이천이십오 년 매출'),
    clist([('2025 매출 *1조 5,022억*', '이천이십오 년 매출'), ('북미 비중 !58%!', '오십팔')], x=110, y=300, size=54),
]},
{'from': '다시 말씀드리면, 열 개를', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    donut(58, '+0.1', label='북미 매출 비중', x=760, y=200, d=420),
    kin('10개 팔면 / *6개 가까이* 북미', '+0.3', y=700, size=84),
]},
{'from': '그리고 미국 가스 순간온수기', 'enter': 'zoom', 'bg': [('g_plumber_install', None)], 'cam': [('push', '+0.0', 40, 45, 1.15)], 'items': [
    SOFT,
    kin('미국 가스 *순간온수기* / 점유율', '+0.1', y=150, size=104, until='일 위입니다'),
    stamp('미국 1위', '일 위입니다', x=1180, y=560, size=120),
]},
{'from': '하루아침에 된 일이', 'enter': 'wipe', 'bg': [('g_expo', None)], 'cam': [('cardL', '북미 최대')], 'items': [
    CLEAR,
    kin('하루아침에 / !된 일이 아니다!', '+0.0', y=240, size=110, mode='pop', until='북미 최대'),
    clist([('북미 최대 *냉난방 전시회*', '북미 최대'), ('국내 업계 *처음*', '처음으로'), ('2025년까지 !16년 연속!', '십육 년')], size=61),
]},
{'from': '우리 집 베란다 보일러로', 'enter': 'zoom', 'bg': [('g_veranda_boiler', None)], 'cam': [('push', '+0.0', 35, 45, 1.15)], 'items': [
    SOFT,
    kin('우리 집 / *베란다 보일러* 그 회사', '+0.1', y=150, size=104, until='지금은 매출의'),
    kin('매출 절반 넘게 / !미국·캐나다!', '지금은 매출의', y=170, size=116, mode='pop'),
]},
{'from': '그런데 숫자 하나는 아직', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('북미에서 / 몇 장 팔렸나?', '+0.1', y=200, size=116, until='공개된'),
    big('?', '온수매트가', y=420, size=240),
    tag('공개 통계 없음', '공개된', None, 720, tone='red', size=64),
]},
{'from': '그래도 우리말 이름 그대로', 'enter': 'zoom', 'bg': [('v:s_city_night', None)], 'cam': [('pull', '+0.0', 50, 50, 1.12)], 'items': [
    raw('<style>.bg{--dark:.62; --blur:0px}</style>'),
    kin('우리말 이름 그대로 / *미국 쇼핑몰*에', '+0.1', y=170, size=104, until='그 자체가'),
    kin('우리 바닥 문화가 / *바다를 건넜다*', '그 자체가', y=180, size=116, mode='pop'),
]},
# ================= 3막: 흔한 설명 확인 (4:47~6:12) =================
{'from': '그렇다면 이 물건은 왜 통했을까요', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('왜 *통했을까?*', '+0.0', y=130, size=110, mode='pop'),
    clist([('① 한인 *입소문*', '입소문을'), ('② 한국 *기술*', '기술이'), ('③ 값이 *싸서*', '싸서')], x=640, y=340, size=72),
    qbadge('왜 통했나?', '+0.2'),
]},
{'from': '입소문은 일부 사실입니다', 'enter': 'zoom', 'bg': [('g_neighbors', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR,
    clist([('입소문 = *일부 사실*', '입소문은'), ('광고보다 *옆집 추천*', '옆집이'), ('코스트코·아마존은 !한인만! X', '코스트코와'), ('출발점이지 *전부는 아님*', '출발점이었지')], size=57),
]},
{'from': '그럼 기술일까요', 'enter': 'zoom', 'bg': [('g_12v_pad', None)], 'cam': [('cardR', '미국 캠핑 동호회')], 'items': [
    CLEAR,
    kin('그럼 / *기술*일까?', '+0.0', y=240, size=130, mode='pop', until='미국 캠핑 동호회'),
    clist([('미국에도 *같은 발상*', '미국 캠핑 동호회'), ('12V 패드 · 해발 *3,000m*', '해발'), ('단, 몸 밑으로 !전선!', '전선이')], x=110, y=280, size=54),
]},
{'from': '물로 침대를 데우는 회사도', 'enter': 'flash', 'bg': [('g_smartbed', None)], 'cam': [('push', '+0.0', 45, 60, 1.1), ('crash', '구조만', 45, 62, 1.3)], 'items': [
    SOFT,
    kin('뉴욕 / *에이트 슬립*', '뉴욕의', y=150, size=120, mode='drop', until='매트리스'),
    kin('물관 덮개 + / *머리맡 기계*', '매트리스', y=150, size=110, until='구조만'),
    stamp('구조는 거의 같다', '구조만', x=1100, y=600, size=84),
]},
{'from': '미국은 이 기술을 몰랐던', 'enter': 'wipe', 'bg': [('v:s_money_count', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    raw('<style>.bg{--dark:.62; --blur:0px}</style>'),
    kin('미국은 / !이미 만들어 팔고! 있었다', '+0.1', y=200, size=104, until='그렇다면'),
    kin('그럼 / *무엇이* 달랐나?', '그렇다면', y=220, size=120, mode='pop'),
]},
# ================= 4막: 남은 이유 셋 (6:04~11:05) =================
{'from': '남은 이유는 셋입니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('남은 이유 *셋*', '+0.0', y=150, size=110, mode='drop'),
    flow([('안전', '첫째는'), ('가격', '둘째는'), ('생활 방식', '셋째는')], y=420, size=96),
    tag('가장 큰 것은 마지막', '가장 큰', None, 640, tone='red', size=60),
]},
{'from': '이천이십삼 년 봄', 'enter': 'zoom', 'bg': [('g_recall_blankets', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR, qbadge('첫째: 안전', '+0.1', pop=True),
    clist([('2023 봄 *미국 소비자안전위*', '미국 소비자제품안전위원회가'), ('전기담요·패드 !35만 개! 리콜', '삼십오만'), ('조절기 고장 → *불·화상*', '온도 조절기가')], size=54),
]},
{'from': '한 번의 일이 아닙니다', 'enter': 'zoom', 'bg': [('g_blanket_smoke', None)], 'cam': [('cardR', '미국 전기안전재단은')], 'items': [
    CLEAR,
    kin('한 번의 일이 / !아니다!', '+0.0', y=240, size=120, mode='pop', until='미국 전기안전재단은'),
    clist([('화재 해마다 *약 500건*', '미국 전기안전재단은'), ('대부분 *10년 넘은* 담요', '대부분은'), ('수칙: !잠든 동안 쓰지 말라!', '잠든')], x=110, y=280, size=59),
]},
{'from': '온수매트는 구조가 다릅니다', 'enter': 'flash', 'bg': [('g_mat_cutaway', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    SOFT,
    kin('열은 / *매트 밖 보일러*에', '열을', y=140, size=104, until='몸 밑으로는'),
    kin('몸 밑엔 / *데운 물만*', '몸 밑으로는', y=140, size=116, mode='pop', until='미국에서 팔리는'),
    tag('상품명에 "No Electric Wire"', '전선 없음이라는', None, 640, tone='dark', size=56),
]},
{'from': '그렇다면 온수매트는 무조건', 'enter': 'zoom', 'bg': [('g_mat_leak', None)], 'cam': [('cardL', '한국소비자원에')], 'items': [
    CLEAR,
    kin('무조건 안전? / !아닙니다!', '+0.0', y=240, size=120, mode='pop', until='한국소비자원에'),
    clist([('2020~ 5년 난방용품 사고', '한국소비자원에'), ('그중 온수매트 *684건*', '육백팔십사'), ('10건 중 6 = *누수·조절기*', '열 건 중')], size=54),
]},
{'from': '더 무서운 건 불입니다', 'enter': 'flash', 'bg': [('g_van_danger', None)], 'cam': [('push', '+0.0', 50, 50, 1.1), ('shake', '+0.2', 50, 50, 1.0)], 'items': [
    SOFT,
    kin('더 무서운 건 / !불!', '+0.0', y=200, size=150, mode='pop', until='전북 군산에서는'),
    kin('부탄가스로 데우는 매트 / 캠핑카 부부 *사망*', '전북 군산에서는', y=160, size=92, until='불을 때서'),
    kin('불을 때면 / = *이미 난로*', '불을 때서', y=180, size=120, mode='pop'),
]},
{'from': '한국가스안전공사 실험에서는', 'enter': 'zoom', 'bg': [('g_tent_co', None)], 'cam': [('push', '+0.0', 50, 55, 1.12)], 'items': [
    SOFT,
    kin('밀폐 텐트 + / *휴대용 가스 난방기*', '+0.1', y=140, size=96, until='십오분'),
    tag('15분 만에', '십오분', None, 330, tone='dark', size=60),
    roll(0, 1600, '천육백', y=420, size=200, suffix='ppm', tone='bad'),
    kin('2시간 안에 / !목숨!을 잃는 농도', '두 시간', y=160, size=100, until='소방청'),
    tag('일산화탄소 신고 5건 중 1건 = 텐트', '소방청', None, 700, tone='red', size=54),
]},
{'from': '이천이십삼 년 시월에는', 'enter': 'fade', 'bg': [('g_reservoir', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    DIM,
    kin('2023.10 광주 저수지 / *60대 부부*', '+0.1', y=170, size=100, until='우리 또래의'),
    kin('우리 또래의 / *이야기*', '우리 또래의', y=200, size=124),
]},
{'from': '그러니 첫째 이유는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('완벽해서가 / !아니다!', '온수매트가', y=170, size=116, mode='pop', until='전기로'),
    kin('불과 전선을 / 몸에서 *한 걸음*', '전기로', y=200, size=116),
    stamp('이유 ① 안전', '+0.2', x=1250, y=640, size=90),
]},
{'from': '텐트나 차에서 난방기구', 'enter': 'zoom', 'bg': [('v:s_campfire_snow', None)], 'cam': [('pull', '+0.0', 50, 50, 1.1)], 'items': [
    raw('<style>.bg{--dark:.6; --blur:0px}</style>'),
    kin('텐트·차에서 / *아찔했던* 경험?', '+0.1', y=180, size=110, mode='pop'),
    tag('댓글로 나눠 주세요 → 누군가의 안전 수칙', '댓글로', None, 600, tone='dark', size=54),
]},
{'from': '둘째는 가격표입니다', 'enter': 'zoom', 'bg': [('g_price_scale', None)], 'cam': [('cardL', '에이트 슬립은')], 'items': [
    CLEAR, qbadge('둘째: 가격', '+0.1', pop=True),
    kin('둘째 / *가격표*', '+0.0', y=240, size=140, mode='pop', until='에이트 슬립은'),
    clist([('에이트 슬립 *$2,300~2,800+*', '에이트 슬립은'), ('= *300만 원+* · 월 구독료', '우리 돈'), ('나비엔 매트(2019) *$399*', '삼백구십구'), ('→ !6개 가까이! 산다', '여섯 개')], size=54),
]},
{'from': '물론 두 물건이 똑같지는', 'enter': 'wipe', 'bg': [('g_price_tags', None)], 'items': [
    raw('<style>.bg{--dark:.75; --blur:0px}</style>'),
    kin('똑같지는 *않다*', '+0.0', y=110, size=100, mode='drop'),
    card('에이트 슬립', '몸 재고 자동 조절', '에이트 슬립은', 200, 250, w=720, h=280, vsize=74),
    card('온수매트', '물 데워 돌리기', '온수매트는', 1000, 250, w=720, h=280, vsize=74),
    kin('뼈대는 같고 / 가격은 !6배!', '같은 뼈대에', y=620, size=96, mode='pop'),
]},
{'from': '부자들이 삼백만 원 넘게', 'enter': 'flash', 'bg': [('v:s_money_count', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    raw('<style>.bg{--dark:.68; --blur:0px}</style>'),
    kin('300만 원 물 침대 / vs *몇십만 원*', '+0.1', y=160, size=104, until='먼저 본'),
    kin('*기준점 효과*', '기준점', y=240, size=150, mode='pop', sfx='ding'),
    tag('처음 들은 값 = 머릿속 기준', '처음 들은', None, 560, tone='dark', size=58),
]},
{'from': '다음 편에서는 은퇴 후', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('다음 편', '+0.0', y=150, size=90, mode='drop'),
    kin('은퇴 후 *겨울 난방비* / 어디서 새나', '+0.3', y=320, size=110, mode='pop'),
]},
{'from': '그런데 풀리지 않은 질문이', 'enter': 'zoom', 'bg': [('v:s_suburb_snow', None)], 'cam': [('pull', '+0.0', 50, 50, 1.12)], 'items': [
    raw('<style>.bg{--dark:.65; --blur:0px}</style>'),
    kin('미국 = *300만 원* 첨단 침대', '미국은', y=180, size=96, until='한국은'),
    kin('한국 = *몇십만 원* 생활 가전', '한국은', y=330, size=96, until='답은'),
    kin('답은 / !지하실!에', '답은', y=220, size=150, mode='pop', sfx='whoosh'),
    qbadge('셋째: 생활 방식', '답은', pop=True),
]},
{'from': '미국 집 지하실에는 대개', 'enter': 'zoom', 'bg': [('g_furnace_house', None)], 'cam': [('cardL', '+0.3')], 'items': [
    CLEAR,
    clist([('*퍼네스* = 온풍 난방기', '퍼네스라는'), ('북미 집 난방 *가장 많이*', '가장 많이'), ('공기 데워 *바람구멍*으로', '바람구멍으로'), ('미국 = !공기!를 데운다', '공기를 데우며')], size=65),
]},
{'from': '전기담요가 태어난 장면도', 'enter': 'flash', 'bg': [('g_1912', None), ('g_1936', '천구백삼십육')], 'cam': [('push', '+0.0', 45, 45, 1.12)], 'items': [
    SOFT, cutsfx('천구백삼십육'),
    kin('1912 *시드니 러셀* / 결핵 환자용 전기 패드', '시드니', y=150, size=92, until='당시'),
    kin('바깥에서 자는 환자 / *위에서 덮어* 주는 물건', '당시', y=150, size=96, until='천구백삼십육'),
    kin('1936 *자동 온도* 전기담요 / → 미국 안방', '천구백삼십육', y=150, size=96),
]},
{'from': '한국은 반대입니다', 'enter': 'zoom', 'bg': [('g_ondol_cut', None), ('g_apt_pipes', '아파트로'), ('g_mat_bedroom', '그 바닥을')], 'cam': [('push', '+0.0', 50, 55, 1.1)], 'items': [
    SOFT, cutsfx('아파트로', '그 바닥을'),
    kin('한국은 / *바닥*을 데운다', '+0.0', y=160, size=124, mode='pop', until='아궁이에'),
    kin('아궁이 · 구들장 / *아랫목*', '아궁이에', y=160, size=110, until='아파트로'),
    kin('아파트 바닥 밑 / *따뜻한 물*', '아파트로', y=160, size=110, until='그 바닥을'),
    kin('바닥을 이불 크기로 = / *온수매트*', '그 바닥을', y=160, size=104, mode='pop'),
]},
{'from': '앞에서 나온 두 단서를', 'enter': 'flash', 'bg': [('g_clue_merge', None)], 'cam': [('push', '+0.0', 50, 50, 1.12), ('crash', '둘을', 50, 55, 1.3)], 'items': [
    raw('<style>.bg{--dark:.7; --blur:0px}</style>'),
    kin('단서 ① *물은 열을 품는다*', '물은', y=120, size=84, until='둘을'),
    kin('단서 ② *추위는 밑에서*', '추위는', y=260, size=84, until='둘을'),
    kin('둘을 합친 물건 / *바닥을 데우는 나라*에서', '둘을', y=160, size=100, mode='pop'),
]},
{'from': '순서를 보면 더 분명해집니다', 'enter': 'zoom', 'bg': [('g_air_vs_floor', None)], 'cam': [('cardR', '+0.3')], 'items': [
    CLEAR,
    clist([('미국: 공기 데움 → *덮는 담요*', '미국은 공기를'), ('한국: 바닥 데움 → *까는 매트*', '한국은 바닥을'), ('!기술!보다 *집 데우는 방식*', '기술이 먼저가')], x=110, y=280, size=54),
]},
{'from': '목욕탕 온탕을 떠올려', 'enter': 'fade', 'bg': [('g_bathhouse', None)], 'cam': [('push', '+0.0', 50, 45, 1.12)], 'items': [
    SOFT,
    kin('목욕탕 *온탕*', '+0.1', y=160, size=130, mode='drop', until='밑에서부터'),
    kin('밑에서 데우면 / *위는 따라온다*', '밑에서부터', y=160, size=110, until='바닥 난방을'),
    kin('공기 데우던 사람에겐 / *새로운 경험*', '바닥 난방을', y=160, size=100),
]},
{'from': '우리 어머니들이 겨울밤', 'enter': 'fade', 'bg': [('g_rice_bowl', None), ('g_family_araetmok', '평생')], 'cam': [('push', '+0.0', 45, 50, 1.1)], 'items': [
    SOFT, cutsfx('평생'),
    kin('아랫목 이불 밑 / *밥그릇*', '+0.2', y=160, size=116, until='평생'),
    kin('바닥 난방 = / 기술 아닌 *생활*', '평생', y=160, size=116, until='그 생활이'),
    kin('바다 건너선 / *신기한 발명품*', '그 생활이', y=170, size=116, mode='pop'),
]},
# ================= 5막: 같은 기술, 다른 길 (12:19~14:11) =================
{'from': '같은 물 기술은 미국에서', 'enter': 'zoom', 'bg': [('g_investors', None)], 'cam': [('cardL', '에이트 슬립은 지금까지')], 'items': [
    CLEAR,
    kin('미국에선 / *첨단 수면 기술*', '+0.1', y=240, size=116, mode='pop', until='에이트 슬립은 지금까지'),
    clist([('투자 *3억 달러+*', '삼억'), ('2026.3 기업 가치 !15억 달러!', '십오억'), ('13~43℃ *냉·온* 조절', '섭씨')], size=54),
]},
{'from': '그쪽 사정도 공정하게', 'enter': 'zoom', 'bg': [('g_bad_review', None)], 'cam': [('cardR', '+0.3')], 'items': [
    CLEAR,
    clist([('"*비싼 물침대*일 뿐"', '비싼'), ('누수·기계 멈춤 *후기*', '물이 새거나'), ('물 돌리는 침대 = *같은 숙제*', '숙제를'), ('!기술 부족! 아닌 습관 차이', '기술이 모자랐던')], x=110, y=260, size=56),
]},
{'from': '한국 쪽은 지금 어떨까요', 'enter': 'flash', 'bg': [('v:s_factory', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    raw('<style>.bg{--dark:.62; --blur:0px}</style>'),
    kin('2025 *관세 부담* 속에도', '경동나비엔은', y=150, size=100, until='그해'),
    kin('3분기 해외 매출 / !+11%!', '그해', y=170, size=124, mode='pop', until='두 차례'),
    kin('값 2번 올려도 / 판매 *그대로*', '두 차례', y=170, size=110, until='값이 아니라'),
    stamp('값이 아니라 실력', '값이 아니라', x=1150, y=640, size=90),
]},
{'from': '냉정한 한계도 있습니다', 'enter': 'zoom', 'bg': [('g_car_camping', None)], 'cam': [('cardL', '국내 비교')], 'items': [
    CLEAR,
    kin('냉정한 한계 / !전기!', '+0.0', y=240, size=124, mode='pop', until='국내 비교'),
    clist([('1인용 시간당 *약 100Wh*', '국내 비교'), ('전기장판의 *2배*', '두 배입니다'), ('1kWh 배터리 → *10시간 안팎*', '휴대용'), ('하룻밤 OK · 이틀 !무리!', '하룻밤은')], size=54, until='은퇴 후 차박을'),
    kin('차박이라면 / *배터리 용량*부터', '은퇴 후 차박을', x=1030, y=360, w=820, size=84),
]},
{'from': '집 안방이라면 계산이', 'enter': 'flash', 'bg': [('g_bill', None), ('g_thermostat', '보일러 온도를')], 'items': [
    raw('<style>.bg{--dark:.72; --blur:0px}</style>'), cutsfx('보일러 온도를'),
    kin('2인용 · 하루 8시간 · 한 달', '이인용', y=110, size=80, until='보일러 온도를'),
    card('온수매트 (한 달)', '+8,000원', '팔천', 200, 240, w=720, h=280, hot=True, vsize=96),
    card('전기장판 (한 달)', '+5,000원', '오천', 1000, 240, w=720, h=280, vsize=96),
    kin('보일러 한두 칸 ↓ / *3,000원 차이*는 절약 쪽', '보일러 온도를', y=580, size=80, until='집마다'),
    tag('집마다 다름 · 내 고지서로 계산', '집마다', None, 640, tone='dark', size=56),
]},
# ================= 결말 (14:11~16:18) =================
{'from': '다시 처음 질문입니다', 'enter': 'zoom', 'bg': [('v:s_snow_camp_night', None)], 'cam': [('pull', '+0.0', 50, 50, 1.12)], 'items': [
    raw('<style>.bg{--dark:.62; --blur:0px}</style>'),
    kin('전기담요 만든 나라가 / 왜 *놀랐을까?*', '전기담요를', y=200, size=110, mode='pop'),
]},
{'from': '답은 세 줄입니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('답은 *세 줄*', '+0.0', y=110, size=100, mode='drop'),
    clist([('① 불·전선을 뗀 *구조*', '하나,'), ('② 첨단 침대의 *5분의 1도 안 되는* 값', '둘,'), ('③ !바닥을 데워 온 습관!', '공기 대신')], x=230, y=300, size=72),
    tag('한국 기술도 좋다 · 다만 미국에도 있었다', '한국 기술이 좋았다는', None, 760, tone='dark', size=50),
]},
{'from': '한 줄로 줄이겠습니다', 'enter': 'zoom', 'bg': [('g_agungi', None)], 'cam': [('push', '+0.0', 60, 55, 1.15)], 'items': [
    raw('<style>.bg{--dark:.7; --blur:0px}</style>'),
    kin('놀라게 한 건 / 기술이 !아니라!', '미국 캠퍼를', y=150, size=110, until='밑에서부터'),
    kin('*밑에서부터 데우는* / 우리의 습관', '밑에서부터', y=170, size=124, mode='pop', sfx='ding'),
]},
{'from': '그렇다면 우리 집 잠자리는', 'enter': 'zoom', 'bg': [('g_yo_more', None)], 'cam': [('cardL', '하나, 이불은')], 'items': [
    CLEAR,
    kin('우리 집 잠자리 / *오늘 확인할 3가지*', '+0.1', y=240, size=104, mode='pop', until='하나, 이불은'),
    clist([('① 바닥은 *비워 두나?*', '하나, 이불은'), ('→ 이불 말고 *요 한 장 더*', '바닥에 요')], size=57),
]},
{'from': '둘, 텐트나 차 안에서 불', 'enter': 'wipe', 'bg': [('g_co_alarm', None)], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR,
    clist([('② 불 때는 난방기 *켜고 자나?*', '둘,'), ('→ 자기 전 !반드시 끄기!', '잠들기'), ('→ 차박엔 *CO 경보기*', '경보기')], x=110, y=280, size=54),
]},
{'from': '셋, 온수매트 호스가', 'enter': 'zoom', 'bg': [('g_hose_check', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR,
    clist([('③ 호스 꺾임 · *물 교체*', '셋,'), ('사고 10건 중 6 = *누수·조절기*', '사고의'), ('올겨울 *호스부터 펴기*', '호스부터')], size=54),
]},
{'from': '다시 그 겨울 캠핑장입니다', 'enter': 'fade', 'bg': [('g_split_contrast', None), ('g_ship', '아궁이에서 시작한')], 'cam': [('push', '+0.0', 72, 45, 1.15)], 'items': [
    raw('<style>.bg{--dark:.75; --blur:0px}</style>'), cutsfx('아궁이에서 시작한'),
    kin('텐트 밑엔 / *물 한 통 + 작은 보일러*', '반팔', y=140, size=100, until='그 물을'),
    kin('그 생각은 / 아버지 세대의 *아궁이*에서', '그 물을', y=150, size=100, until='아궁이에서 시작한'),
    kin('우리 생활 방식이 / *미국 텐트 바닥*까지', '아궁이에서 시작한', y=150, size=104, until='다음에'),
    kin('다음에 바다를 건널 / *우리 습관*은?', '다음에', y=170, size=110, mode='pop'),
]},
{'from': '여러분은 온수매트파이십니까', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('여러분은?', '+0.0', y=110, size=100, mode='drop'),
    card('1번', '온수매트파', '온수매트파이십니까', 200, 270, w=720, h=300, hot=True),
    card('2번', '전기장판파', '전기장판파이십니까', 1000, 270, w=720, h=300),
    tag('댓글로 번호를 남겨 주세요', '댓글로', None, 680, tone='dark', size=56),
]},
{'from': '다음 이야기도 골라', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('다음 이야기 *투표*', '+0.0', y=110, size=100, mode='drop'),
    clist([('1번 해외에서 잘 팔리는 *한국 가전*', '일 번,'), ('2번 *차박 캠핑* 노후 비용', '이 번,'), ('3번 *한국 보일러* 미국 생존기', '삼 번,')], x=230, y=300, size=72),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'fade', 'bg': [('g_camp_blizzard', None)], 'cam': [('pull', '+0.0', 50, 50, 1.12)], 'items': [
    raw('<style>.bg{--dark:.6; --blur:0px}</style>'),
    kin('*지혜호수 경제연구소*', '지혜호수', y=200, size=116, mode='pop'),
    tag('숫자로 확인하고 사실로 말합니다', '숫자로', None, 420, tone='ghost', size=60),
    kin('*구독*해 두세요', '구독해', y=600, size=96, mode='pop'),
]},
]
