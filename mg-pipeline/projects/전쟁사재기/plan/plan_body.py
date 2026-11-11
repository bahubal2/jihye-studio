"""전쟁사재기 본문 (0:35~15:38). 1막 불씨(애기봉·영국·일본) / 2막 사재기 정점 / 3막 흔한 설명·반전(스타링크 반값) /
4막 우리 집 대비 기준 / 5막 같은 모양의 사재기(마스크·계엄·봉투) / 결말. 그림은 input/그림_대본대조.json 의 자막 문장과 1:1."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, flipcard, bubble, group, raw, flow,
                 puppet, mgbg, qbadge, kin, cutsfx, clist, droppile)
SOFT = raw('<style>.bg{--dark:.6; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')
DIM = raw('<style>.bg{--dark:.45; --blur:0px}</style>')
VID = raw('<style>.bg{--dark:.62; --blur:0px}</style>')

BODY = [
# ================= 1막: 불씨 (0:35~1:59) =================
{'from': '시월 하순, 경기도 김포', 'enter': 'zoom', 'bg': [('v:s_river_fog', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    VID, kin('10월 하순 / 김포 *애기봉 전망대*', '+0.1', y=230, size=124, mode='drop'),
]},
{'from': '강 건너 북한 개풍군', 'enter': 'flash', 'bg': [('g_scope_view', None)], 'cam': [('cardL', '일 점')], 'items': [
    CLEAR,
    kin('강 건너 / *자주포 세 대*', '+0.1', y=240, size=130, mode='pop', until='일 점'),
    clist([('개풍군 해안 *자주포 3대*', '일 점'), ('북한 땅까지 *1.5km*', '킬로미터'), ('북한군 *10여 명* · 포신 움직임', '북한군'), ('미국 겨냥 !선전 문구!', '선전')], size=54),
]},
{'from': '이렇게 가까이에서 자주포가', 'enter': 'zoom', 'bg': [('g_range_map', None)], 'cam': [('push', '+0.0', 45, 40, 1.12)], 'items': [
    SOFT,
    kin('이렇게 가까이는 / *이례적*', '+0.1', y=150, size=116, mode='drop', until='이 포의'),
    kin('사거리 → / !경기 북부! 사정권', '이 포의', y=170, size=124, mode='pop'),
    tag('언론 분석', '이 포의', None, 620, tone='dark', size=50),
]},
{'from': '영상은 눈 깜짝할 새', 'enter': 'flash', 'bg': [('v:s_phone_scroll', None)], 'items': [
    VID, kin('영상은 / *눈 깜짝할 새*', '+0.0', y=230, size=140, mode='pop'),
]},
{'from': '주말이 되자 접경지', 'enter': 'zoom', 'bg': [('g_aegibong_crowd', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT,
    kin('주말 전망대에 / *시민들이 몰렸다*', '+0.1', y=150, size=110, mode='drop', until='전쟁 나는 건가'),
    kin('"전쟁 나는 건가" / *수군수군*', '전쟁 나는 건가', y=170, size=120, mode='pop'),
]},
{'from': '이런 돈과 불안 이야기', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('돈과 불안 이야기', '+0.0', y=200, size=96, mode='drop'),
    kin('*구독* 눌러 두세요', '구독', y=360, size=150, mode='pop', sfx='ding'),
]},
{'from': '같은 무렵,', 'enter': 'wipe', 'bg': [('g_news_tv', None)], 'cam': [('push', '+0.0', 60, 40, 1.1)], 'items': [
    SOFT,
    kin('김여정 부장', '김여정', y=140, size=100, mode='drop'),
    kin('전 국경선 / *새로운 대응 수단* / 임무 대기', '국경선에', y=300, size=104, mode='pop'),
]},
{'from': '바다 건너 소식도 겹쳤습니다', 'enter': 'zoom', 'bg': [('g_uk_home', None), ('g_japan_home', '일본 방재')], 'cam': [('cardR', '시월 이십이')], 'items': [
    CLEAR, cutsfx('일본 방재'),
    kin('바다 건너 / *소식*도', '+0.0', y=240, size=130, mode='pop', until='시월 이십이'),
    clist([('10.22 영국 *사흘 버틸 물자*', '시월 이십이'), ('집집마다 갖추라 · *캠페인*', '캠페인을'), ('일본 장관 *최소 사흘~일주일*', '일본 방재')], x=110, y=280, size=54),
]},
{'from': '엎친 데 덮친 격으로', 'enter': 'flash', 'bg': [('g_phone_night', None)], 'cam': [('push', '+0.0', 30, 45, 1.12), ('shake', '철렁했을', 50, 50, 1.0)], 'items': [
    SOFT,
    kin('*엎친 데 덮친* 격', '+0.0', y=150, size=120, mode='drop', until='뉴스를'),
    kin('뉴스 켤 때마다 / !가슴이 철렁!', '뉴스를', y=160, size=116, mode='pop', until='마음이'),
    kin('마음이 / *뒤숭숭*', '마음이', y=170, size=130, mode='drop'),
]},
# ================= 2막: 사재기의 정점 (1:56~4:03) =================
{'from': '그리고 십일월 초, 불안은', 'enter': 'zoom', 'bg': [('g_cart_full', None)], 'cam': [('cardL', '한 사람은')], 'items': [
    CLEAR,
    kin('불안은 / *장바구니*가 됐다', '+0.1', y=240, size=124, mode='pop', until='한 사람은'),
    clist([('11월 초 불안 → *장바구니*', '한 사람은'), ('생수 *36병* + 햇반 *80개*', '햇반'), ('5식구 재난 가방 !400만 원!', '다섯 식구')], size=54),
]},
{'from': '방독면, 안전모, 정수 알약까지', 'enter': 'flash', 'bg': [('g_bag_items', None), ('g_bathroom_tank', '욕실에')], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR, cutsfx('욕실에'),
    clist([('*방독면* · 안전모', '방독면'), ('*정수 알약*까지', '알약까지'), ('목록이 *줄줄이*', '줄줄이'), ('욕실엔 !대형 물통!', '욕실에')], x=110, y=260, size=72),
]},
{'from': '사백만 원이면 어느 정도일까요', 'enter': 'zoom', 'bg': [('g_ledger', None)], 'cam': [('cardL', '은퇴한')], 'items': [
    CLEAR,
    kin('400만 원이면?', '+0.0', y=260, size=150, mode='pop', until='은퇴한'),
    clist([('= 은퇴 부부 *몇 달 생활비*', '은퇴한'), ('가방 몇 개에 *고스란히*', '고스란히'), ('지갑은 !홀쭉!', '홀쭉해졌습니다')], size=57, until='다시 말씀드립니다'),
    big('400만 원', '사백만 원입니다', x=1010, y=380, size=150, color='#ff5a5a'),
]},
{'from': '이런 장면을 한번 떠올려', 'enter': 'fade', 'bg': [('g_wife_phone', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    raw('<style>.bg{--dark:.4; --blur:0px}</style>'),
    tag('재현 장면', '+0.1', 80, 60, tone='dark', size=44),
    bubble('여보, 옆 동 김 씨네는 생수를 한 트럭 들였대', '여보,', 420, 140, size=48),
    bubble('호들갑 떨지 마, 그 포 다 고물이래', '호들갑', 140, 330, size=52, tone='red'),
]},
{'from': '그러고는 잠자리에 누워서', 'enter': 'flash', 'bg': [('g_bed_app', None)], 'cam': [('push', '+0.0', 45, 50, 1.15)], 'items': [
    SOFT, tag('재현 장면', '+0.1', 80, 60, tone='dark', size=44),
    kin('잠자리에서 / *몰래 마트 앱*', '+0.1', y=150, size=120, mode='pop', until='남의 이야기'),
    kin('남의 이야기 / *같지 않으시죠?*', '남의 이야기', y=170, size=116, mode='drop'),
]},
{'from': '거실마다 비슷한 말다툼도', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    kin('거실마다 *말다툼*', '+0.0', y=110, size=100, mode='drop'),
    card('한쪽', '"지금 쟁여 둬야"', '한쪽은', 200, 260, w=720, h=280, vsize=72),
    card('한쪽', '"유난 떨지 말라"', '유난', 1000, 260, w=720, h=280, hot=True, vsize=72),
    tag('비상용품 챙기다 부부 싸움 글도', '비상용품을', None, 640, tone='dark', size=52),
]},
{'from': '전쟁 나면 길이 막힌다며', 'enter': 'zoom', 'bg': [('g_motorcycle', None)], 'cam': [('push', '+0.0', 50, 55, 1.12)], 'items': [
    SOFT, kin('길 막힌다며 / *중고 오토바이*까지', '+0.1', y=150, size=116, mode='pop'),
]},
{'from': '인공지능으로 만든 가짜 사진도', 'enter': 'flash', 'bg': [('g_fake_photo', None), ('g_comments', '글마다')], 'cam': [('cardL', '접경지')], 'items': [
    CLEAR, cutsfx('글마다'),
    kin('AI로 만든 / *가짜 사진*', '+0.0', y=240, size=130, mode='pop', until='접경지'),
    clist([('카페 창밖에 *북한 포?*', '접경지'), ('진짜 영상과 *나란히*', '나란히'), ('"사실 확인 좀" 댓글 *줄줄이*', '글마다'), ('이미 !반쯤 믿었다!', '반쯤'), ('가짜+진짜 = *등골 오싹*', '등골이')], size=54),
]},
{'from': '옆집이 생수를 쌓는 사진을', 'enter': 'zoom', 'bg': [('g_neighbor_stack', None)], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR,
    clist([('옆집은 *생수 탑*', '옆집이'), ('우리 집만 비면 !불안!', '불안해집니다'), ('"남들이 하니 맞겠지"', '남들이'), ('= *사회적 증거*', '사회적'), ('남의 행동이 *답안지*', '답안지로')], x=110, y=240, size=72),
]},
{'from': '혹시 우리 단톡방에도', 'enter': 'flash', 'bg': [('g_groupchat', None)], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    SOFT,
    kin('우리 *단톡방*에도?', '+0.0', y=150, size=124, mode='pop', until='그 사진을'),
    kin('마트 앱을 열었다면 / *그게 이 마음*', '그 사진을', y=170, size=110, mode='drop'),
]},
# ================= 3막: 흔한 설명 확인 · 반전 (4:03~7:38) =================
{'from': '자, 그럼 흔히 듣는 설명을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('흔한 설명 / *하나씩* 짚기', '+0.0', y=260, size=130, mode='pop', sfx='whoosh'),
    qbadge('무엇이 비웠나?', '+0.2', pop=True),
]},
{'from': '첫째, 북한이 정말 쳐들어올', 'enter': 'zoom', 'bg': [('g_old_gun', None)], 'cam': [('cardL', '불씨는 맞습니다')], 'items': [
    CLEAR,
    kin('① 북한이 / *쳐들어올 기세?*', '+0.0', y=240, size=116, mode='pop', until='불씨는 맞습니다'),
    clist([('불씨는 *맞다*', '불씨는 맞습니다'), ('포·위협은 *실제*', '실제로 왔고'), ('가까이 보면 *그림이 다르다*', '그림이'), ('언론: !오래된 122mm 구형!', '오래된')], size=54),
]},
{'from': '국방부는 보이는 곳에', 'enter': 'flash', 'bg': [('g_briefing', None)], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR,
    clist([('국방부 "보이는 배치 = *전술상 안 맞다*"', '국방부는'), ('쏠 포라면 *숨긴다*', '숨겨'), ('합참 "구형 노출 = !보여주기식!"', '합참도'), ('군 대비 태세는 *굳게 유지*', '대비 태세를')], x=110, y=250, size=54, until='불씨는 맞았습니다'),
    kin('불씨만으로 / 진열대는 *텅텅* 안 빈다', '불씨는 맞았습니다', x=110, y=300, w=820, size=84),
]},
{'from': '둘째, 물건이 정말 모자랐을까요', 'enter': 'zoom', 'bg': [('g_shelf_full', None)], 'cam': [('cardL', '이건 근거가')], 'items': [
    CLEAR,
    kin('② 물건이 / *모자랐다?*', '+0.0', y=240, size=124, mode='pop', until='이건 근거가'),
    clist([('근거 *약함*', '이건 근거가'), ('생수 바닥 발표 *없음*', '바닥났다고'), ('2026.3에도 "수급 *문제없다*"', '수급에'), ('소문이 !불안에 부채질!', '부채질을')], size=54),
]},
{'from': '셋째, 영국과 일본이 비상물자를', 'enter': 'zoom', 'bg': [('g_quake_drill', None)], 'cam': [('cardR', '여기에도')], 'items': [
    CLEAR,
    kin('③ 영국·일본 권고 = / *큰일?*', '+0.0', y=240, size=110, mode='pop', until='여기에도'),
    clist([('두 나라 "당장 위협 *없다*"', '두 나라'), ('영국: *정전·단수·통신 두절* 가정', '영국 캠페인은'), ('일본: *대지진* 대비', '대지진이었습니다'), ('일본은 !사재기 자제! 당부', '사재기를 하지')], x=110, y=260, size=54),
]},
{'from': '일본 정부의 설명은 이랬습니다', 'enter': 'flash', 'bg': [('g_japan_home', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT,
    kin('스스로 버티는 집 ↑ / → 도움은 *꼭 필요한 사람*에게', '스스로', y=150, size=96, mode='drop', until='겁을'),
    kin('겁주기 !아닌! / *평소 준비* 당부', '겁을', y=170, size=116, mode='pop'),
]},
{'from': '지진과 정전 대비 목록이 바다를', 'enter': 'zoom', 'bg': [('g_label_swap', None)], 'cam': [('push', '+0.0', 50, 45, 1.12)], 'items': [
    SOFT,
    kin('지진·정전 목록 → / *전쟁 목록*으로 / 이름표만 바꿨다', '+0.1', y=140, size=100, mode='pop'),
]},
{'from': '그렇다면 보도로 확인된 품절은', 'enter': 'flash', 'bg': [('v:s_cart_water', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    VID,
    kin('보도로 확인된 / *품절*은 어디?', '+0.0', y=160, size=116, mode='pop', until='여기서 반전이'),
    kin('반전', '여기서 반전이', y=200, size=180, mode='pop', sfx='whoosh', until='생수 매대가'),
    kin('생수 매대 !아님!', '생수 매대가', y=200, size=140, mode='drop', until='위성'),
    kin('→ *스타링크* 매장', '위성', y=220, size=150, mode='pop'),
]},
{'from': '스타링크는 하늘의 위성에서', 'enter': 'zoom', 'bg': [('v:s_satellite', None), ('g_starlink', '땅의')], 'cam': [('cardL', '땅의')], 'items': [
    CLEAR, cutsfx('땅의'),
    kin('하늘의 위성 → / *인터넷*', '+0.0', y=240, size=124, mode='pop', until='땅의'),
    clist([('땅 통신망 끊겨도', '땅의'), ('*하늘만 보이면* 연결', '하늘만'), ('정전·통신 대비 *인증 글*', '인증')], size=65),
]},
{'from': '그런데 그 주,', 'enter': 'flash', 'bg': [('g_electronics_rush', None)], 'cam': [('cardR', '스타링크는 국내에서')], 'items': [
    CLEAR,
    kin('그런데 / *그 주*', '+0.0', y=240, size=140, mode='pop', until='스타링크는 국내에서'),
    clist([('장비·요금 *반값 행사*', '스타링크는 국내에서'), ('미니 !32만 → 16만 원!', '십육만'), ('불안 ↑ + 값 ↓', '불안은 커졌고'), ('*같은 주, 같은 매장*', '두 힘이')], x=110, y=260, size=63),
]},
{'from': '여기서 그림이 한 번 더', 'enter': 'zoom', 'bg': [('g_sale_2024', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT,
    kin('2년 전 11월 / *연중 최대 할인*', '이 년 전', y=150, size=110, mode='drop', until='텅 빈'),
    bubble('"여기 무슨 전쟁이라도 났나요?"', '여기 무슨', 520, 200, size=60, tone='red'),
    stamp('품절 = 할인', '품절의', x=1100, y=600, size=110),
]},
{'from': '다만 이것 하나는 기억해 두세요', 'enter': 'flash', 'bg': [('g_bankbook', None)], 'cam': [('cardL', '이런 장비는')], 'items': [
    CLEAR,
    kin('이것 하나는 / *기억*해 두세요', '+0.0', y=240, size=116, mode='pop', until='이런 장비는'),
    clist([('한 번 사고 끝? !아니다!', '이런 장비는'), ('매달 *요금* 자동 이체', '매달 요금이'), ('섬·산골·낚시·캠핑엔 *쓸모*', '섬이나'), ('덜컥 약정 = *매달 고지서*', '덜컥')], size=61),
]},
{'from': '돌다리도 두들겨 보고', 'enter': 'zoom', 'bg': [('g_stone_bridge', None)], 'cam': [('push', '+0.0', 50, 55, 1.12)], 'items': [
    SOFT, kin('*돌다리도* / 두들겨 보고', '+0.0', y=160, size=140, mode='pop'),
]},
{'from': '다음 편에서는 이렇게 불안할 때', 'enter': 'flash', 'bg': [('g_gold_dollar', None)], 'cam': [('push', '+0.0', 50, 50, 1.12)], 'items': [
    SOFT,
    kin('다음 편', '+0.0', y=130, size=90, mode='drop'),
    kin('불안할 때 *금·달러* / 은퇴자 통장은?', '+0.4', y=280, size=110, mode='pop'),
]},
# ================= 4막: 우리 집은 얼마나 (7:38~11:42) =================
{'from': '자, 이제 진짜 궁금한 질문으로', 'enter': 'zoom', 'bg': [('g_couple_check', None)], 'cam': [('push', '+0.0', 40, 60, 1.12)], 'items': [
    SOFT,
    kin('*우리 집*은 / 얼마나?', '우리 집은', y=150, size=130, mode='pop', until='사백만'),
    kin('400만 원 가방 / !꼭 필요?!', '사백만', y=170, size=116, mode='drop', until='답은'),
    kin('답은 *정부 안내*에', '답은', y=200, size=124, mode='pop'),
]},
{'from': '영국 정부가 권한 물의 양은', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('1인 하루 *3리터*', '+0.0', y=110, size=104, mode='drop', until='사흘이면'),
    kin('3일 = *9리터*', '사흘이면', y=110, size=110, mode='pop', until='부부'),
    droppile('c_bottle', '부부', 9, 9, 560, 520, w=78, gap=10, every=0.12),
    kin('부부 = *2리터 9병*', '부부', y=110, size=116, mode='pop'),
]},
{'from': '다시 말씀드리겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    big('9병', '부부 두 분, 생수', y=250, size=300, color='#ffd400'),
    tag('36병 쌓은 집의 4분의 1', '베란다에', None, 640, tone='dark', size=60),
]},
{'from': '손주와 함께 사는 세 식구라면', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    kin('3식구 = 27리터 = *14병*', '+0.0', y=100, size=100, mode='pop'),
    droppile('c_bottle', '+0.3', 14, 7, 620, 560, w=74, gap=10, every=0.1),
    kin('식구 수 × *9리터*', '식구 수에', y=840, size=90, mode='drop'),
]},
{'from': '그리고 한꺼번에 많이 사면', 'enter': 'flash', 'bg': [('g_expiry', None)], 'cam': [('cardR', '생수에도')], 'items': [
    CLEAR,
    kin('한꺼번에 사면 / *숨은 비용*', '+0.0', y=240, size=116, mode='pop', until='생수에도'),
    clist([('생수에도 *유통기한*', '생수에도'), ('대개 *반년~2년*', '반년에서'), ('36병 → 유통기한도 *한 번에*', '유통기한도'), ('!하수구!로 흘러가는 돈', '하수구에'), ('햇반 80개도 *마찬가지*', '햇반')], x=110, y=240, size=56),
]},
{'from': '영국 캠페인의 목록을 보면', 'enter': 'zoom', 'bg': [('g_uk_list', None)], 'cam': [('cardL', '마실 물')], 'items': [
    CLEAR,
    kin('영국 목록은 / *더 반갑다*', '+0.0', y=240, size=124, mode='pop', until='마실 물'),
    clist([('마실 물 · *3일 치 식량*', '마실 물'), ('약간의 *현금* · 담요', '담요'), ('구급상자 · 손전등 · *라디오*', '라디오'), ('대부분 !이미 집에! 있다', '대부분'), ('새로 사기보다 *한곳에 모으기*', '한곳에')], size=54),
]},
{'from': '일본 장관이 꼽은 목록에는', 'enter': 'flash', 'bg': [('g_toilet_kit', None)], 'cam': [('push', '+0.0', 50, 50, 1.12)], 'items': [
    SOFT,
    kin('일본 목록엔 / *휴대용 화장실*', '+0.0', y=150, size=120, mode='pop', until='단수가'),
    kin('단수되면 / 물보다 먼저 *화장실*', '단수가', y=170, size=110, mode='drop'),
]},
{'from': '그리고 우리 세대에게 꼭 필요한', 'enter': 'zoom', 'bg': [('g_meds', None)], 'cam': [('cardR', '매일 드시는')], 'items': [
    CLEAR,
    kin('우리 세대에게 / *꼭 필요한 것*', '+0.0', y=240, size=116, mode='pop', until='매일 드시는'),
    clist([('*매일 드시는 약*', '매일 드시는'), ('혈압약·당뇨약 = !생수보다 귀함!', '혈압약'), ('처방 때 *일주일 치 여유*', '처방받을'), ('400만 원 가방에도 *없는 대비*', '가장 값진')], x=110, y=260, size=54),
]},
{'from': '우리 세대 가방에 꼭 넣을 것이', 'enter': 'flash', 'bg': [('g_drawer_kit', None)], 'cam': [('cardL', '여분 안경')], 'items': [
    CLEAR,
    kin('가방에 *꼭 넣을 것*', '+0.0', y=260, size=124, mode='pop', until='여분 안경'),
    clist([('여분 *안경·돋보기*', '여분 안경'), ('*보청기 건전지*', '보청기를'), ('신분증 사본 · *연락처 종이*', '신분증'), ('휴대폰 꺼지면 !번호가 안 떠오른다!', '휴대폰이'), ('서랍 한 칸이면 *충분*', '서랍')], size=54),
]},
{'from': '우리 행정안전부도 기준을', 'enter': 'zoom', 'bg': [('g_two_bags', None)], 'items': [
    raw('<style>.bg{--dark:.72; --blur:0px}</style>'),
    kin('행정안전부 기준', '+0.0', y=110, size=96, mode='drop'),
    card('들고 나갈 배낭', '2~3일분', '대피할 때', 200, 250, w=720, h=280, vsize=96),
    card('집에 둘 물자', '30일분', '삼십 일분', 1000, 250, w=720, h=280, hot=True, vsize=96),
    kin('나갈 건 *가볍게* / 둘 건 *넉넉하게*', '들고 나갈 것은', y=620, size=90, mode='pop'),
]},
{'from': '그렇다면 집에 둘 것은 어떻게', 'enter': 'flash', 'bg': [('g_norway', None)], 'cam': [('cardR', '노르웨이는')], 'items': [
    CLEAR,
    kin('본보기는 / *북유럽*', '+0.0', y=240, size=130, mode='pop', until='노르웨이는'),
    clist([('노르웨이 2024 *3일 → 1주일*', '노르웨이는'), ('스웨덴도 *1주일*', '스웨덴도'), ('뉴스 보고 허겁지겁 !X!', '허겁지겁'), ('평소에 *조금씩*', '평소에 조금씩')], x=110, y=260, size=54),
]},
{'from': '방법은 간단합니다', 'enter': 'zoom', 'bg': [('g_checkout', None)], 'cam': [('cardL', '평소 장 볼 때')], 'items': [
    CLEAR,
    kin('방법은 *간단*', '+0.0', y=260, size=140, mode='pop', until='평소 장 볼 때'),
    clist([('장 볼 때 *한 묶음 더*', '평소 장 볼 때'), ('산 날짜 적고 *먹으며 채우기*', '산 날짜를'), ('서울시·행안부: *유통기한 교체*', '서울시와'), ('버림 X · !목돈! X', '목돈이')], size=54),
]},
{'from': '비상시 국민행동요령에는', 'enter': 'flash', 'bg': [('g_sweep', None)], 'cam': [('push', '+0.0', 45, 50, 1.12)], 'items': [
    SOFT,
    kin('국민행동요령 / "생활필수품 *사재기 금지*"', '+0.0', y=140, size=100, mode='drop', until='내가'),
    kin('내가 쓸어 담으면 / *이웃 몫*이 사라진다', '내가', y=160, size=110, mode='pop'),
]},
{'from': '평소 장 볼 때 생수 한 묶음을 더 얹는 집과', 'enter': 'wipe', 'bg': [('v:s_coins_count', None)], 'items': [
    raw('<style>.bg{--dark:.7; --blur:0px}</style>'),
    card('장 볼 때 한 묶음 더', '통장 그대로', '평소 장 볼 때', 200, 220, w=720, h=280, vsize=72),
    card('하루에 400만 원', '통장에 구멍', '사백만', 1000, 220, w=720, h=280, hot=True, vsize=72),
    kin('*하늘과 땅* 차이', '하늘과', y=600, size=124, mode='pop'),
]},
{'from': '돈 한 푼 안 드는 대비도', 'enter': 'zoom', 'bg': [('g_meeting_point', None)], 'cam': [('push', '+0.0', 50, 50, 1.12)], 'items': [
    SOFT,
    kin('돈 한 푼 *안 드는* 대비', '+0.0', y=150, size=116, mode='pop', until='전화가'),
    kin('전화 안 될 때 / *어디서 만날지*', '전화가', y=170, size=116, mode='drop'),
]},
# ================= 5막: 같은 모양의 사재기 (11:42~13:37) =================
{'from': '그런데 이런 사재기, 이번이', 'enter': 'flash', 'bg': [('v:s_city_night2', None)], 'cam': [('pull', '+0.0', 50, 50, 1.12)], 'items': [
    VID, kin('이번이 / *처음*이었을까?', '+0.0', y=230, size=140, mode='pop', sfx='whoosh'),
]},
{'from': '이천이십 년 봄을 기억하실', 'enter': 'zoom', 'bg': [('g_mask_line', None)], 'cam': [('cardR', '마스크 한 장')], 'items': [
    CLEAR,
    kin('*2020년 봄*', '+0.0', y=260, size=150, mode='pop', until='마스크 한 장'),
    clist([('약국 앞 *마스크 줄*', '마스크 한 장'), ('출생 연도 끝자리 *요일제*', '출생'), ('일주일에 *2장*', '두 장씩'), ('불안이 번지는 속도를 !몸으로!', '몸으로')], x=110, y=260, size=59),
]},
{'from': '이천이십사 년 십이월 삼 일 밤에는', 'enter': 'flash', 'bg': [('g_conv_night', None)], 'cam': [('cardL', '대형마트는')], 'items': [
    CLEAR,
    kin('2024.12.3 밤', '+0.0', y=260, size=140, mode='pop', until='대형마트는'),
    clist([('마트는 이미 *문 닫음*', '대형마트는'), ('밤샘 편의점으로 *부랴부랴*', '부랴부랴'), ('한 편의점 집계', '한 편의점'), ('통조림 판매 !+337%!', '삼백삼십칠')], size=65),
]},
{'from': '누가 먼저 움직였을까요', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('누가 *먼저*?', '+0.0', y=110, size=104, mode='drop', until='현장에서는'),
    kin('현장: *50·60대* 손님', '현장에서는', y=110, size=104, mode='pop', until='비상 상황을'),
    kin('비상을 / *몸으로 기억하는* 세대', '비상 상황을', y=300, size=110, mode='drop', until='바로 우리'),
    kin('바로 / *우리 세대*', '바로 우리', y=300, size=180, mode='pop', sfx='ding'),
    tag('6시간 뒤 해제 · 다음 날 주문 취소도', '여섯 시간', None, 700, tone='dark', size=52),
]},
{'from': '올해 삼월에도 비슷한 일이', 'enter': 'zoom', 'bg': [('g_trash_bags', None)], 'cam': [('push', '+0.0', 50, 50, 1.12)], 'items': [
    SOFT,
    kin('2026년 3월 / *종량제 봉투*', '+0.0', y=140, size=110, mode='drop', until='서울의'),
    kin('하루 판매 / !5배!', '서울의', y=160, size=150, mode='pop', until='유통업계는'),
    tag('유통업계: 물량 충분', '유통업계는', None, 620, tone='dark', size=56),
]},
{'from': '마스크, 통조림, 종량제 봉투', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('마스크 · 통조림 · 봉투 · 생수', '+0.0', y=110, size=86, mode='drop'),
    flow([('불안', '불안이'), ('우르르', '우르르'), ('가라앉음', '가라앉습니다')], y=360, size=110),
    kin('남는 건 / *생수 탑 + 카드 명세서*', '남는 건', y=560, size=96, mode='pop'),
]},
{'from': '냉정하게 말씀드릴 것도', 'enter': 'fade', 'bg': [('g_calm_window', None)], 'cam': [('push', '+0.0', 45, 45, 1.08)], 'items': [
    SOFT,
    kin('이 영상은 / 전쟁 가능성을 *판단하지 않습니다*', '이 영상은', y=150, size=96, mode='drop', until='대비는'),
    kin('대비는 *필요* / 문제는 언제·얼마나', '대비는', y=170, size=104, mode='pop'),
]},
# ================= 결말 (13:37~15:38) =================
{'from': '다시 처음 질문입니다', 'enter': 'zoom', 'bg': [('g_empty_shelf', None)], 'cam': [('push', '+0.0', 45, 45, 1.12)], 'items': [
    SOFT,
    kin('다시 처음 질문', '+0.0', y=140, size=96, mode='drop'),
    kin('무엇이 / *진열대*를 비웠나?', '무엇이', y=280, size=120, mode='pop'),
]},
{'from': '답은 세 줄입니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('답은 *세 줄*', '+0.0', y=110, size=100, mode='drop'),
    clist([('① 포는 *불씨* · 진열대는 안 비웠다', '하나,'), ('② 지진 목록에 *전쟁 이름표*', '둘,'), ('③ 먼저 동난 곳 = !반값 가격표 앞!', '셋,')], x=200, y=320, size=72),
]},
{'from': '불안할 때 무언가를 사면', 'enter': 'zoom', 'bg': [('g_card_moment', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT,
    kin('사면 / 마음이 *잠시 놓인다*', '+0.0', y=150, size=116, mode='drop', until='평생'),
    kin('가족 지켜 온 분일수록 / *먼저 움직인다*', '평생', y=150, size=104, mode='pop', until='다만 그 마음이'),
    kin('그 마음이 / *노후 통장*을 축내지 않도록', '다만 그 마음이', y=150, size=104, mode='drop'),
]},
{'from': '하나, 우리 집 물을 세어', 'enter': 'flash', 'bg': [('g_veranda', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR,
    clist([('① 물 세기: *식구 × 9리터*', '하나,'), ('베란다에서 *1분*', '베란다에서'), ('② 매일 먹는 약 *일주일 치*', '둘,'), ('③ 비싼 장비 앞 !한 번 멈춤!', '셋,'), ('안내로 확인 · *약정 조건*', '약정')], size=54),
]},
{'from': '그리고 불안한 소식을 들으면', 'enter': 'zoom', 'bg': [('g_phone_family', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT,
    kin('불안한 소식엔 / 가족에게 *전화 한 통*', '+0.0', y=150, size=110, mode='pop', until='그게'),
    kin('가장 싸고 / *가장 든든한* 대비', '그게', y=170, size=116, mode='drop'),
]},
{'from': '여러분 댁 베란다에는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('베란다 생수, *몇 병?*', '+0.0', y=110, size=100, mode='drop'),
    card('1번', '이미 넉넉하다', '일 번', 200, 270, w=720, h=300, vsize=80),
    card('2번', '오늘 세어 보겠다', '이 번', 1000, 270, w=720, h=300, hot=True, vsize=80),
    tag('댓글로 번호를 남겨 주세요', '댓글로', None, 680, tone='dark', size=56),
]},
{'from': '다음에 다룰 이야기도', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('다음 이야기 *투표*', '+0.0', y=110, size=100, mode='drop'),
    clist([('1번 불안할 때 *금·달러*', '일 번,'), ('2번 은퇴 후 *집 한 채*', '이 번,'), ('3번 자식에게 돈 줄 때 *실수*', '삼 번,')], x=330, y=320, size=72),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'fade', 'bg': [('g_calm_window', None)], 'cam': [('pull', '+0.0', 50, 50, 1.1)], 'items': [
    raw('<style>.bg{--dark:.6; --blur:0px}</style>'),
    kin('*지혜호수 경제연구소*', '지혜호수', y=200, size=116, mode='pop'),
    tag('숫자로 확인하고 사실로 말합니다', '숫자로', None, 420, tone='ghost', size=60),
    kin('*구독*해 두세요', '구독해', y=600, size=96, mode='pop'),
]},
]
