"""휴양지몰락 본문 (0:48~18:52). 5위 태국 / 4위 필리핀 / 3위 괌 / 2위 캄보디아 / 1위 사이판 / 정리·결말.
그림은 input/그림_대본대조.json 의 자막 문장과 1:1. 사람이 숨진 이야기(필리핀 통계·괌 총격·보코산)는 담담하게: 도장·쿵 없음."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, flipcard, bubble, group, raw, flow, igrid, rankbadge,
                 puppet, mgbg, qbadge, kin, cutsfx, clist, droppile)
SOFT = raw('<style>.bg{--dark:.6; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')
VID = raw('<style>.bg{--dark:.62; --blur:0px}</style>')
def RB(rank, name, first=False): return rankbadge(rank, name, '+0.05', still=not first)
def Q(n, text, note='마지막에 함께 매겨 봅니다', at='마지막에'): return [mgbg('teal'), kin(f'오늘의 질문 *{n}*', '+0.0', y=170, size=90, mode='drop'),
                        kin(text, '+0.3', y=320, size=96, mode='pop'), tag(note, at, None, 640, tone='dark', size=50)]

BODY = [
# ================= 5위 태국 (0:48~3:15) =================
{'from': '비행기는 그대로 뜨는데', 'enter': 'zoom', 'bg': [('g_plane_sky', None)], 'cam': [('cardL', '올해 상반기')], 'items': [
    CLEAR,
    kin('비행기는 뜨는데 / *사람만* 빠진다', '+0.1', y=240, size=124, mode='pop', until='올해 상반기'),
    clist([('인천 → 이 도시 운항 *−10%*', '열 편'), ('승객은 !−17%!', '여섯 중'), ('빈자리 *숭숭*', '빈자리가')], size=60),
]},
{'from': '이 도시는 방콕입니다', 'enter': 'flash', 'bg': [('v:s_bangkok', None)], 'items': [
    VID, RB(5, '태국', True),
    kin('5위 / *태국 방콕*', '+0.0', y=260, size=150, mode='pop', sfx='whoosh'),
]},
{'from': '나라 전체로 넓히면', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), RB(5, '태국'),
    kin('태국 찾은 한국인', '+0.1', y=120, size=84, mode='drop'),
    swapnum('180만', '140만', '백팔십만', '백사십만', y=230, size=170),
    igrid('user', 5, '다섯이', lit=5, litat='다섯이', drop=1, dropat='넷도', cols=5, y=560, size=120, tone='bad'),
]},
{'from': '올겨울 휴가지를 고르고', 'enter': 'zoom', 'bg': [('g_couple_brochure', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT, RB(5, '태국'),
    kin('올겨울 *휴가지* 고르신다면', '+0.1', y=140, size=100, mode='drop', until='같은 돈'),
    kin('편히 *쉬다* 올까 / 내내 !가슴 졸일까!', '같은 돈', y=150, size=110, mode='pop'),
]},
{'from': '이런 숫자 이야기가', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('숫자로 짚는 여행 이야기', '+0.0', y=200, size=90, mode='drop'),
    kin('*구독* 눌러 두세요', '구독', y=360, size=150, mode='pop', sfx='ding'),
]},
{'from': '줄은 이렇게 세웠습니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'),
    kin('순위 기준', '+0.0', y=110, size=90, mode='drop'),
    card('기준 ①', '전성기 대비 감소폭', '가장 많이', 200, 260, w=720, h=280, vsize=64),
    card('기준 ②', '현지가 입은 타격', '현지가', 1000, 260, w=720, h=280, hot=True, vsize=64),
    tag('이 영상의 판단', '판단', None, 640, tone='dark', size=52),
]},
{'from': '방콕 물가가 갑자기', 'enter': 'zoom', 'bg': [('g_bkk_market', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT, RB(5, '태국'),
    kin('방콕 물가가 / *하늘로*?', '+0.0', y=150, size=120, mode='pop', until='그보다'),
    kin('눈에 띄는 건 / !바로 옆 나라!', '그보다', y=160, size=120, mode='drop'),
]},
{'from': '태국과 캄보디아 국경에서', 'enter': 'flash', 'bg': [('g_border_map', None)], 'cam': [('cardR', '+0.2')], 'items': [
    CLEAR, RB(5, '태국'),
    clist([('25년 여름 국경 *무력 충돌*', '+0.3'), ('접경 지역 *여행경보 ↑*', '여행경보'), ('가을, 캄보디아 대학생 사건', '그해 가을'), ('"태국·베트남도 위험?" !문의!', '문의')], x=110, y=250, size=54),
]},
{'from': '방콕에서 일어난 일이 아닌데', 'enter': 'zoom', 'bg': [('g_agency_phone', None)], 'cam': [('shake', '덜컥', 50, 50, 1.0)], 'items': [
    SOFT, RB(5, '태국'),
    kin('방콕 일이 아닌데', '+0.0', y=150, size=110, mode='drop'),
    stamp('예약 덜컥', '덜컥', x=1150, y=520, size=120, rot=-8),
]},
{'from': '사람은 위험을 확률보다', 'enter': 'wipe', 'bg': [('g_news_memory', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR, RB(5, '태국'),
    clist([('위험은 확률보다 *기억*으로', '+0.3'), ('뉴스 장면 → *내 일처럼*', '뉴스에서'), ('이름: !가용성 휴리스틱!', '가용성')], size=58),
]},
{'from': '올겨울 방콕 패키지를', 'enter': 'zoom', 'bg': [('g_laptop_package', None)], 'cam': [('push', '+0.0', 50, 55, 1.15)], 'items': [
    SOFT, RB(5, '태국'),
    kin('손이 *멈칫*했다면', '멈칫', y=150, size=130, mode='pop'),
    tag('바로 그 마음', '바로 그', None, 620, tone='dark', size=54),
]},
{'from': '물론 태국 관광 전체가', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), RB(5, '태국'),
    card('태국 관광 전체', '−7%', '+0.1', 200, 240, w=720, h=300, vsize=120),
    card('한국인', '−22%', '다만', 1000, 240, w=720, h=300, hot=True, vsize=120),
    kin('*세 배* 가까이', '세 배', y=640, size=96, mode='pop'),
    tag('옆집 불안이 담장을 훌쩍', '옆집', None, 800, tone='red', size=50),
]},
{'from': '그런데 태국은 사건이 남의 동네', 'enter': 'zoom', 'bg': [('g_neighbor_smoke', None)], 'cam': [('push', '+0.0', 40, 45, 1.1)], 'items': [
    SOFT, RB(5, '태국'),
    kin('사건은 / *남의 동네*', '+0.0', y=150, size=120, mode='drop', until='사건이 내 동네'),
    kin('내 동네에서 / !10년 내내!라면?', '사건이 내 동네', y=150, size=120, mode='pop'),
]},
{'from': '본론 전에 오늘의 첫 번째', 'enter': 'flash', 'bg': None, 'items':
    Q(1, '최근 한국인 노린 / *사건*이 이어졌나?')},
# ================= 4위 필리핀 (3:15~5:46) =================
{'from': '지금 베란다 창고에 골프백', 'enter': 'zoom', 'bg': [('g_golfbag_tag', None)], 'cam': [('push', '+0.0', 45, 40, 1.12)], 'items': [
    SOFT,
    kin('베란다 창고 *골프백*', '+0.1', y=140, size=110, mode='drop', until='필리핀입니다'),
    kin('4위 / *필리핀*', '필리핀입니다', y=230, size=150, mode='pop', sfx='whoosh'),
]},
{'from': '필리핀을 찾는 외국인 다섯 중', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), RB(4, '필리핀', True),
    kin('외국인 5명 중 1명 = *한국인*', '+0.0', y=120, size=88, mode='drop'),
    igrid('user', 5, '+0.2', lit=1, litat='+0.4', cols=5, y=300, size=150, tone='good'),
    stamp('미국·일본 제치고 1위', '떡하니', x=1180, y=560, size=80, rot=-6),
    tag('그 1위가 쑥쑥 줄고 있다', '쑥쑥', None, 780, tone='red', size=56),
]},
{'from': '필리핀 관광부 집계로 작년', 'enter': 'zoom', 'bg': [('g_manila_arrival', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR, RB(4, '필리핀'),
    clist([('작년 한국인 약 *125만 명*', '+0.3'), ('전년보다 !−20%!↑', '이십 퍼센트'), ('코로나 전의 *6할* 남짓', '열이')], size=60),
]},
{'from': '필리핀 관광부의 설명은', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(4, '필리핀'),
    flipcard('보복 여행 끝나 제자리', '일본은 코로나 전보다 +70%', '보복', '그런데 같은', y=300, size=78),
    kin('꺾이기는커녕 *쭉*', '꺾이기는커녕', y=680, size=96, mode='pop'),
]},
{'from': '남는 단서는 안전입니다', 'enter': 'wipe', 'bg': [('g_manila_night', None)], 'cam': [('cardR', '외교부')], 'items': [
    CLEAR, RB(4, '필리핀'),
    kin('남는 단서 = *안전*', '+0.0', y=240, size=124, mode='drop', until='외교부'),
    clist([('2015~ 필리핀 한국인 피살 *38명*', '외교부'), ('아시아·태평양의 *절반 가까이*', '절반'), ('작년 앙헬레스 관광객 총격', '앙헬레스에서'), ('마닐라 납치 · 20일 만에 석방', '마닐라에서는')], x=110, y=240, size=50, sfx='tick'),
]},
{'from': '클라크와 앙헬레스로 주말 골프', 'enter': 'zoom', 'bg': [('g_golf_group', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT, RB(4, '필리핀'),
    bubble('밤엔 숙소 밖에 나가지 말자', '밤에는', 380, 160, size=56),
    kin('숫자가 생활 속으로 / *슬금슬금*', '숫자가', y=560, size=96, mode='pop'),
]},
{'from': '필리핀 정부도 손을 놓고', 'enter': 'flash', 'bg': [('g_help_desk', None)], 'cam': [('cardL', '관광부는')], 'items': [
    CLEAR, RB(4, '필리핀'),
    kin('정부도 *손 놓진 않았다*', '+0.0', y=240, size=116, mode='drop', until='관광부는'),
    clist([('한국인 노린 범죄 *무관용*', '관광부는'), ('한국인 *도움 창구* 설치', '도움 창구'), ('효과 확인은 !아직!', '손님 숫자로')], size=58),
]},
{'from': '여기에 엎친 데 덮친', 'enter': 'zoom', 'bg': [('g_won_weak', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT, RB(4, '필리핀'),
    kin('*엎친 데 덮친* 격 / !원화 약세!', '+0.0', y=150, size=116, mode='pop', until='정리하면'),
    flow([('쌓인 사건', '정리하면'), ('회복의 발목', '발목을')], y=360, size=110),
]},
{'from': '그런데 일 위 섬에는 이런 사건이', 'enter': 'flash', 'bg': [('g_island_teaser', None)], 'cam': [('push', '+0.0', 50, 60, 1.1)], 'items': [
    raw('<style>.bg{--dark:.5; --blur:6px}</style>'), RB(4, '필리핀'),
    kin('1위 섬은 *사건 없이* / 더 크게 비었다', '+0.0', y=150, size=110, mode='pop', until='그 전에'),
    kin('그 전에 / 비행기가 !늘어난! 섬', '그 전에', y=170, size=116, mode='drop'),
]},
{'from': '두 번째 질문입니다', 'enter': 'flash', 'bg': None, 'items':
    Q(2, '더 가깝고 편한 / *대체지*가 생겼나?')},
# ================= 3위 괌 (5:46~8:49) =================
{'from': '석 비행기에 손님 삼 명', 'enter': 'zoom', 'bg': [('g_empty_cabin', None)], 'cam': [('cardL', '처음에')], 'items': [
    CLEAR, RB(3, '괌', True),
    kin('3위 / *괌*', '+0.0', y=240, size=150, mode='pop', sfx='whoosh', until='처음에'),
    clist([('작년 11월 *괌 → 부산*', '작년 십일월'), ('180석에 손님 *3명*', '기장과'), ('직원 6명 = 손님의 *2배*', '두 배'), ('별명 !눕코노미!', '눕코노미')], size=56),
]},
{'from': '빛바랜 신혼여행 앨범을', 'enter': 'wipe', 'bg': [('g_honeymoon_album', None)], 'cam': [('cardR', '이천십구')], 'items': [
    CLEAR, RB(3, '괌'),
    kin('괌 = *신혼여행* 1번지', '+0.0', y=240, size=116, mode='drop', until='이천십구'),
    clist([('2019 한국인 약 *75만 명*', '이천십구'), ('괌 관광객의 *절반 이상*', '절반이'), ('2024 약 37만 → !반토막!', '반토막')], x=110, y=280, size=58),
]},
{'from': '올해는 더 내려갑니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(3, '괌'),
    kin('올해 1~7월 한국인', '+0.0', y=150, size=90, mode='drop'),
    roll(0, 30, '삼십', y=290, size=230, suffix='%↓', tone='bad', dur=1.2),
]},
{'from': '그럼 그 비행기는 왜', 'enter': 'zoom', 'bg': [('g_guam_planes', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT, RB(3, '괌'),
    kin('왜 비어서 날았나?', '+0.0', y=140, size=110, mode='drop', until='손님은 줄었는데'),
    kin('손님 *↓* · 비행기 !↑!', '손님은 줄었는데', y=140, size=130, mode='pop'),
    roll(0, 25, '이십오', y=380, size=170, prefix='+', suffix='%', tone='bad', dur=1.2),
    tag('작년 한국–괌 운항', '이십오', None, 620, tone='dark', size=50),
]},
{'from': '대한항공과 아시아나가 합칠 때', 'enter': 'flash', 'bg': [('g_rule_doc', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR, RB(3, '괌'),
    clist([('합병 조건: 좌석 *코로나 전 90%↑*', '공정거래위원회'), ('항공사 "70%로 낮춰 달라"', '칠십'), ('심사관 !"받아들이기 어렵다"!', '심사관')], size=54),
]},
{'from': '이쯤 되면 비행기가 이렇게', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'), RB(3, '괌'),
    flipcard('비행기 많으니 손님도 곧', '수요가 아니라 규칙이 띄웠다', '+0.1', '그런데 아닙니다', y=330, size=84),
]},
{'from': '손님이 떠난 첫째 이유는', 'enter': 'flash', 'bg': [('v:s_exchange', None)], 'items': [
    VID, RB(3, '괌'),
    kin('첫째 이유 = *달러값*', '+0.0', y=150, size=116, mode='pop'),
    tag('괌 = 미국 땅 · 밥값도 호텔값도 달러', '미국 땅', None, 360, size=54),
    roll(0, 1500, '천오백', y=470, size=190, suffix='원 선', tone='bad', dur=1.3),
]},
{'from': '다녀온 분들 후기엔', 'enter': 'zoom', 'bg': [('g_tip_bill', None)], 'cam': [('push', '+0.0', 35, 45, 1.15)], 'items': [
    SOFT, RB(3, '괌'),
    bubble('팁이 붙었는데 팁 칸이 또?', '+0.3', 640, 160, size=56, tone='red'),
    stamp('눈이 휘둥그레', '휘둥그레', x=1180, y=480, size=100, rot=-7),
    tag('낯선 팁 문화 = 바가지 느낌', '미국식', None, 700, tone='dark', size=52),
]},
{'from': '둘째는 신뢰입니다', 'enter': 'wipe', 'bg': [('g_guam_dusk', None)], 'cam': [('push', '+0.0', 50, 50, 1.06)], 'items': [
    SOFT, RB(3, '괌'),
    kin('둘째 = *신뢰*', '+0.0', y=150, size=120, mode='drop', until='이천이십사'),
    kin('2024년 1월 / 은퇴 기념 여행 중 총격', '이천이십사', y=170, size=96, mode='drop'),
    tag('현지에서도 "치안 구멍" 비판', '현지에서도', None, 620, tone='dark', size=50),
]},
{'from': '결과는 상가에서 먼저', 'enter': 'zoom', 'bg': [('g_dfs_closed', None), ('g_dutyfree_packing', '롯데면세점도')], 'cam': [('push', '+0.0', 60, 50, 1.1)], 'items': [
    SOFT, RB(3, '괌'), cutsfx('롯데면세점도'),
    kin('시내 면세점 / 3월 *폐점*', '괌 시내', y=150, size=116, mode='pop', until='롯데면세점도'),
    kin('공항 면세점도 / 13년 만에 *짐을 싼다*', '롯데면세점도', y=150, size=110, mode='drop'),
]},
{'from': '여기서 단서를 모아 보겠습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('단서 모으기', '+0.0', y=90, size=84, mode='drop'),
    clist([('태국 · *옆집 사건*', '태국은'), ('필리핀 · *쌓인 사건*', '필리핀은'), ('괌 · 달러값에 지갑 *꽁꽁*', '괌은'), ('공통점 = !불안 + 부담!', '공통점은')], x=420, y=230, size=64),
]},
{'from': '그런데 맞지 않는 조각이', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('dusk'),
    qbadge('맞지 않는 조각', '+0.0', pop=True),
    card('괌', '비행기 넘침', '비행기가 넘치는', 200, 270, w=720, h=280, vsize=88),
    card('1위 섬', '비행기 사라짐', '사라진 섬', 1000, 270, w=720, h=280, hot=True, vsize=88),
    kin('더 크게 빈 곳은 → *1위 섬*', '훨씬', y=660, size=84, mode='pop'),
]},
{'from': '참고로 이 다섯 곳과 정반대로', 'enter': 'wipe', 'bg': [('g_crowded_town', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT,
    tag('다음 이야기 예고', '+0.0', None, 120, tone='red', size=56),
    kin('한국인 몰려 / *값 뛴 곳*', '한국인이 몰려', y=260, size=130, mode='pop'),
]},
{'from': '그 섬으로 가기 전에', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('지금까지 = 손님이 *스스로* 떠남', '지금까지는', y=220, size=92, mode='drop'),
    kin('다음 = 정부가 !막았다!', '다음 나라는', y=400, size=120, mode='pop'),
]},
# ================= 2위 캄보디아 (8:49~11:57) =================
{'from': '십육 일 자정', 'enter': 'zoom', 'bg': [('g_ban_map', None)], 'cam': [('cardR', '+0.4')], 'items': [
    CLEAR, RB(2, '캄보디아', True),
    clist([('25.10.16 자정 *여행금지* 3곳', '+0.5'), ('여행경보 *최고 단계*', '가장 높은'), ('보코산 = 대학생이 숨진 곳', '보코산')], x=110, y=290, size=58, sfx='tick'),
]},
{'from': '불과 몇 년 전만 해도', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(2, '캄보디아'),
    kin('캄보디아 간 한국인', '+0.0', y=120, size=88, mode='drop'),
    swapnum('6천 명', '19만 명', '육천', '십구만', y=260, size=170, tone='good'),
    stamp('3년 만에 30배↑', '삼십 배', x=1180, y=560, size=100, rot=-6),
]},
{'from': '앙코르와트 새벽 일출은', 'enter': 'zoom', 'bg': [('v:s_angkor', None)], 'items': [
    VID, RB(2, '캄보디아'),
    kin('앙코르와트 일출 = / *효도여행* 단골', '+0.0', y=180, size=116, mode='pop'),
    tag('25년 1~7월에도 10만 명 넘게', '사건 직전', None, 600, size=56),
]},
{'from': '이 나라를 찾는 이유도', 'enter': 'wipe', 'bg': [('g_cambodia_tour', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR, RB(2, '캄보디아'),
    clist([('유적 + 휴양 = *꿩 먹고 알 먹고*', '문화유산'), ('대체지 일본 *급성장*', '비행시간이'), ('매력 ↓ 에 !사건!', '매력이')], size=56),
]},
{'from': '그러다 한 계절 만에', 'enter': 'zoom', 'bg': [('g_empty_agency', None)], 'cam': [('cardR', '캄보디아 전문')], 'items': [
    CLEAR, RB(2, '캄보디아'),
    kin('한 계절 만에 / 발길 *뚝*', '+0.0', y=240, size=124, mode='pop', until='캄보디아 전문'),
    clist([('성수기 예약 *씨가 말랐다*', '캄보디아 전문'), ('픽업 기사 "한국인이세요?"', '픽업'), ('한인회 "관광업 !90% 멈춤!"', '한인회는')], x=110, y=290, size=56),
]},
{'from': '앙코르 유적 매표소의 숫자', 'enter': 'flash', 'bg': [('g_angkor_ticket', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT, RB(2, '캄보디아'),
    kin('1분기 앙코르 입장권', '+0.1', y=120, size=88, mode='drop'),
    roll(0, 27, '이십칠만', y=240, size=190, suffix='만 명', tone='bad', dur=1.2),
    stamp('−1/3', '삼분의', x=1200, y=520, size=130, rot=-8),
]},
{'from': '물론 이 숫자를 모두 한국인 탓으로', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), RB(2, '캄보디아'),
    card('태국인 손님', '−96%', '태국인', 200, 260, w=720, h=300, vsize=120),
    card('한국인 쪽', '여행사·한인회 같은 방향', '다만', 1000, 260, w=720, h=300, hot=True, vsize=58),
    tag('국경 분쟁 탓도 크다', '국경 분쟁', None, 640, tone='dark', size=54),
]},
{'from': '정부의 경보도 한 번에', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(2, '캄보디아'),
    flow([('12월 경보 하향', '그해 십이월'), ('길은 열렸다', '길은'), ('이름표는 늦게', '이름표는')], y=330, size=66),
    kin('"위험 국가" 이름표는 / *늦게* 떨어진다', '이름표는', y=560, size=84, mode='pop'),
]},
{'from': '여기서 짚을 점이 있습니다', 'enter': 'zoom', 'bg': [('g_scam_compound', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    SOFT, RB(2, '캄보디아'),
    kin('바가지 이야기 *아님*', '이 사건은', y=140, size=110, mode='drop', until='고수익'),
    kin('고수익 취업 공고 → / !범죄단지 감금!', '고수익', y=150, size=104, mode='pop'),
    tag('피해자 대부분 젊은 층', '피해자', None, 640, tone='dark', size=52),
]},
{'from': '혹시 우리 아이 휴대폰에', 'enter': 'wipe', 'bg': [('g_phone_scam', None)], 'cam': [('push', '+0.0', 45, 45, 1.12)], 'items': [
    SOFT, RB(2, '캄보디아'),
    bubble('해외 단기 고수익 근무!', '+0.4', 780, 170, size=56, tone='red'),
    kin('원인 = 가격 ✕ / *신뢰*', '그래서', y=520, size=110, mode='pop', until='사람이 사라질'),
    kin('싼 가격표도 / *힘을 잃는다*', '사람이 사라질', y=520, size=104, mode='drop'),
]},
{'from': '다행히 이 나라에는 바뀌는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    tag('바뀌는 숫자 → 마지막에', '+0.0', None, 120, tone='green', size=56),
    card('캄보디아', '정부가 막았다', '캄보디아는 정부가', 200, 260, w=720, h=280, vsize=80),
    card('1위 섬', '아무도 안 막았다', '아무도', 1000, 260, w=720, h=280, hot=True, vsize=80),
    kin('하늘이 먼저 · *하늘길*이 뒤따라', '하늘이', y=650, size=84, mode='pop'),
]},
{'from': '세 번째 질문입니다', 'enter': 'flash', 'bg': None, 'items':
    Q(3, '그곳 *직항*이 / 줄고 있나?', '이제 1위 섬으로', '이제 처음에')},
# ================= 1위 사이판 (12:00~15:36) =================
{'from': '북마리아나 제도의 사이판', 'enter': 'zoom', 'bg': [('v:s_island_aerial', None)], 'items': [
    VID, RB(1, '사이판', True),
    kin('1위 / *사이판*', '+0.0', y=180, size=160, mode='pop', sfx='whoosh', until='이 섬의'),
    donut(50, '둘 중', label='2019 외국인 손님 중 한국인', x=760, y=220, d=420, tone='good'),
    tag('그해 약 24만 명', '그해', None, 720, size=56),
]},
{'from': '올해 칠월 한 달', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(1, '사이판'),
    swapnum('11,015명', '1,574명', '+0.3', '천오백칠십사', y=180, size=150),
    igrid('user', 7, '일곱이', lit=7, litat='일곱이', drop=6, dropat='하나만', cols=7, y=520, size=120, tone='bad'),
    kin('섬이 *썰렁*', '썰렁', y=760, size=80, mode='pop'),
]},
{'from': '바가지 때문일까요', 'enter': 'zoom', 'bg': [('g_korean_resort', None)], 'cam': [('cardL', '+0.2')], 'items': [
    CLEAR, RB(1, '사이판'),
    clist([('바가지? → 리조트 주인 *한국 기업*', '이 섬의'), ('호구 취급 = *제 발등 찍기*', '호구'), ('사건? → 보도 *찾기 어렵다*', '사건 때문'), ('그럼 !남는 건?!', '남는 건')], size=52),
]},
{'from': '첫 번째는 하늘입니다', 'enter': 'flash', 'bg': [('v:s_typhoon', None)], 'cam': [('shake', '휩쓸고', 50, 50, 1.0)], 'items': [
    VID, RB(1, '사이판'),
    kin('첫째 = *하늘*', '+0.0', y=150, size=124, mode='drop', until='사월'),
    kin('4월 중순 / !슈퍼태풍!', '사월', y=160, size=130, mode='pop', until='정전이'),
    kin('정전 · 공항 폐쇄 / 국제선 *6월까지 멈춤*', '정전이', y=160, size=104, mode='drop'),
]},
{'from': '그 석 달 동안 한국인', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'), RB(1, '사이판'),
    kin('그 석 달 한국인', '+0.0', y=140, size=90, mode='drop'),
    roll(0, 99, '구십구', y=280, size=230, prefix='−', suffix='%', tone='bad', dur=1.4),
    tag('7월 초 태풍 또', '칠월 초', None, 640, tone='red', size=56),
]},
{'from': '그런데 태풍은 지나갑니다', 'enter': 'wipe', 'bg': [('g_saipan_airport', None)], 'cam': [('cardR', '진짜 문제는')], 'items': [
    CLEAR, RB(1, '사이판'),
    kin('태풍은 *지나간다*', '+0.0', y=240, size=124, mode='drop', until='진짜 문제는'),
    clist([('진짜 문제 = *하늘길*', '진짜 문제는'), ('2019 하루 최대 *5편*', '하루 최대'), ('지금 !주 4번!', '지금은'), ('아시아나 정기편·사무소 *철수*', '아시아나는')], x=110, y=250, size=56),
]},
{'from': '남은 항공사도 운항을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(1, '사이판'),
    kin('작년 한국–사이판 운항 *−1/3*', '작년 한 해', y=120, size=86, mode='drop'),
    igrid('user', 3, '셋이', lit=3, litat='셋이', drop=1, dropat='둘만', cols=3, y=300, size=150, tone='bad'),
    kin('방문객 *−32%*', '삼십이', y=560, size=110, mode='pop'),
    tag('태풍 오기 전 숫자', '태풍이 오기', None, 760, tone='red', size=54),
]},
{'from': '괌과 나란히 놓으면', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'), RB(1, '사이판'),
    card('괌', '비행기 ↑ · 손님 −30%', '괌 노선은', 200, 240, w=720, h=300, vsize=72),
    card('사이판', '비행기 ↓ · 손님 −80%↑', '사이판은', 1000, 240, w=720, h=300, hot=True, vsize=72),
    kin('차이는 *비행기*', '비행기가 남은', y=650, size=110, mode='pop'),
]},
{'from': '괌에서 빈 비행기를 만든', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(1, '사이판'),
    kin('빈 비행기 만든 규칙이 / *괌을 붙잡았다*', '+0.0', y=130, size=100, mode='pop'),
    flow([('손님 ↓', '손님이 줄자'), ('비행기 ↓', '비행기가 빠졌고'), ('손님 더 ↓', '더 줄었습니다')], y=470, size=110),
]},
{'from': '사람 마음도 같은 쪽으로', 'enter': 'zoom', 'bg': [('g_cancel_sms', None)], 'cam': [('cardL', '한 번')], 'items': [
    CLEAR, RB(1, '사이판'),
    clist([('결항 문자 한 번 → 노선 *쓱* 삭제', '한 번'), ('작년 여름 감편·결항 *발 동동*', '작년 여름'), ('짧은 연차 여행이면 *더*', '짧은 연차')], size=54),
]},
{'from': '여기에 달러값까지 올랐습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), RB(1, '사이판'),
    tag('항공권·호텔·렌터카 모두 달러', '사이판도', None, 130, size=56),
    swapnum('1,364원', '1,480원대', '천삼백', '천사백', y=300, size=160),
]},
{'from': '환갑 기념으로 가족끼리', 'enter': 'zoom', 'bg': [('g_family_planning', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT, RB(1, '사이판'),
    kin('날짜보다 / *비행기 시간표*부터', '날짜보다', y=150, size=116, mode='pop'),
]},
{'from': '지금 이 섬의 모습이 그렇습니다', 'enter': 'wipe', 'bg': [('g_resort_reopen', None)], 'cam': [('cardR', '리조트는')], 'items': [
    CLEAR, RB(1, '사이판'),
    clist([('7월부터 리조트 *하나둘 불*', '리조트는'), ('연말까지 대형 *3곳* 복귀', '연말까지'), ('비행기는 !주 4번뿐!', '주 네 번뿐'), ('관광청 "항공편 없인 정상화 불가"', '마리아나'), ('27년 3월까지 *주 4회* 유지', '이천이십칠')], x=110, y=200, size=50),
]},
# ================= 정리·결말 (15:36~18:52) =================
{'from': '그럼 다섯 곳을 한 줄로', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('한 줄로 꿰면', '+0.0', y=80, size=84, mode='drop'),
    clist([('5위 태국 · *옆 나라 사건*', '오 위'), ('4위 필리핀 · *쌓인 사건*', '사 위'), ('3위 괌 · *달러값*', '삼 위'), ('2위 캄보디아 · *신뢰*', '이 위'), ('1위 사이판 · !하늘길!', '그리고 일 위')], x=380, y=200, size=60),
]},
{'from': '처음 질문으로 돌아가', 'enter': 'zoom', 'bg': [('g_split_japan_island', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    SOFT,
    kin('일본은 *바글바글*', '이중 가격은', y=140, size=100, mode='drop', x=80, w=820),
    kin('다섯 곳은 !휑!', '휑하게', y=140, size=100, mode='pop', x=1000, w=820),
]},
{'from': '반대편 숫자가 답을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('반대편 숫자', '+0.0', y=80, size=84, mode='drop'),
    clist([('일본 · 코로나 전보다 *+70%*', '일본을'), ('중국 무비자 · *+37%*', '중국은'), ('장가계 · *+150%*', '장가계는'), ('베트남 · *430만 명*↑', '베트남은')], x=420, y=210, size=62),
    tag('다낭 속사정 → 지난 영상', '다낭 속사정', None, 720, tone='dark', size=48),
]},
{'from': '동네 미용실을 떠올려', 'enter': 'zoom', 'bg': [('g_barbershop', None)], 'cam': [('cardL', '커트값이')], 'items': [
    CLEAR,
    kin('*동네 미용실*', '+0.0', y=260, size=140, mode='pop', until='커트값이'),
    clist([('커트값 조금 ↑ → *꼬박꼬박*', '커트값이'), ('길 위험·노선 끊김 → !그날로!', '가는 길이'), ('옆에 괜찮은 집 → *더 빨리*', '바로 옆에')], size=54),
]},
{'from': '결론은 짧습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    flipcard('바가지', '불안한 길 · 끊긴 길', '겉으로', '실제로', y=320, size=100),
]},
{'from': '이 명단에 없는 곳은', 'enter': 'zoom', 'bg': [('g_domestic_town', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT,
    kin('명단에 없으면 *안전*?', '+0.0', y=140, size=110, mode='drop', until='이 기준은'),
    kin('국내 관광지도 / *같은 기준*', '이 기준은', y=150, size=120, mode='pop'),
]},
{'from': '이제 세 가지 질문을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('세 가지 질문', '+0.0', y=90, size=84, mode='drop'),
    clist([('① 한국인 노린 *사건*', '최근 한국인을'), ('② 더 가깝고 편한 *대체지*', '더 가깝고'), ('③ 줄어드는 *직항*', '직항이')], x=480, y=240, size=70),
]},
{'from': '하나도 없으면 안심', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('dusk'),
    tag('0개 → 안심', '+0.0', None, 220, tone='green', size=64),
    tag('1개 → 지켜볼 만', '하나면', None, 360, size=64),
    tag('2개 → 손님 이동 중', '둘이면', None, 500, tone='red', size=64),
    tag('3개 → 다음 순위표 후보', '셋이면', None, 640, tone='red', size=72),
]},
{'from': '희망도 있습니다', 'enter': 'wipe', 'bg': [('g_cambodia_hope', None)], 'cam': [('cardL', '캄보디아는')], 'items': [
    CLEAR,
    kin('*희망*도 있다', '+0.0', y=260, size=140, mode='pop', until='캄보디아는'),
    clist([('캄보디아 범죄 조직 *단속*', '캄보디아는'), ('감금 피해 신고 *−94%*', '구십사'), ('7월 9일 여행금지 !해제!', '칠월 구'), ('안전 돌아오면 *길도 열린다*', '안전이')], size=52),
]},
{'from': '괌 투몬 거리로 돌아가', 'enter': 'zoom', 'bg': [('g_tumon_empty', None)], 'cam': [('push', '+0.0', 60, 50, 1.1)], 'items': [
    SOFT,
    kin('셔터는 *아직* 내려가 있다', '시내 면세점의', y=140, size=100, mode='drop', until='다시 셔터가'),
    tag('공항 면세점 12/20 마지막 영업', '공항의', None, 330, tone='red', size=56, until='다시 셔터가'),
    kin('셔터를 올릴 열쇠 = / *비행기* · *안전*', '다시 셔터가', y=160, size=104, mode='pop'),
]},
{'from': '여러분이라면 다음 휴가지를', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('다음 휴가지는?', '+0.0', y=110, size=96, mode='drop'),
    card('1번', '비싸도 가깝고 편한 곳', '일 번', 200, 270, w=720, h=300, vsize=68),
    card('2번', '불편해도 값싼 곳', '이 번', 1000, 270, w=720, h=300, hot=True, vsize=68),
    tag('댓글에 번호로', '번호로', None, 680, tone='dark', size=56),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'zoom', 'bg': [('g_ending_suitcase', None)], 'cam': [('push', '+0.0', 50, 45, 1.08)], 'items': [
    SOFT,
    kin('숫자로 확인하고 / *사실로* 말합니다', '+0.0', y=180, size=110, mode='pop'),
    tag('지혜호수 경제연구소', '+0.5', None, 460, tone='dark', size=56),
    kin('*구독*해 두세요', '구독', y=600, size=110, mode='pop', sfx='ding'),
]},
]
