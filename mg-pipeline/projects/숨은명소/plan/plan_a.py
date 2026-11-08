"""숨은명소 TOP5 — 인트로 · 5위 영양 자작나무숲 · 4위 화순 적벽 (자막 1~91). 실사 스톡 + 플랫 일러스트 + 모션그래픽."""
from gen import (hook, flashhit, tag, stamp, big, cover, glow, raw, stack, swapnum, card, bars, flipcard, foreshadow,
                 puppet, particles, mgbg, rankbadge, intro30, kin, cutsfx)
BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
SOFT = raw('<style>.bg{--dark:.7; --blur:0px}</style>')
A = [
# ---- 인트로 30초 표준: 2~3초마다 컷 교체 + 모든 문장 움직이는 글자 ----
{'from': '이천이십육 년 시월 십칠 일', 'enter': 'flash', 'bg': [('i_iron_gate', None), ('v:s_seoul_night', '서울'), ('i_iron_gate', '철문')], 'cam': [('push', '+0.0', 50, 50, 1.25)], 'items': [
    intro30(), SOFT, particles('leaf', '+0.0', n=12), cutsfx('서울', '철문'),
    kin('2026. 10. 17 / 오전 *9시*', '+0.1', y=150, size=96, mode='drop', until='철문', sfx='whoosh'),
    kin('*철문이* !열렸다!', '열렸습니다', y=430, size=190, mode='pop', sfx='hit'),
]},
{'from': '죽기 전에 꼭 가 봐야 할', 'enter': 'zoom', 'bg': [('v:s_seoul_night', None), ('i_jeodo_island', '+2.0'), ('i_seoul_1968', '닫히던'), ('i_reunion', '쉰아홉')], 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    intro30(), SOFT, cutsfx('+2.0', '닫히던', '쉰아홉'),
    kin('죽기 전에 꼭 가 봐야 할 / *숨은* *국내* *명소*', '죽기', y=200, size=118, until='닫히던', sfx='whoosh'),
    kin('그해 태어난 아이', '닫히던', y=240, size=100, mode='slide'),
    kin('올해 !59살!', '쉰아홉', y=420, size=200, mode='pop', sfx='hit'),
]},
{'from': '그 철문은 오십구 년 동안', 'enter': 'flash', 'bg': [('i_iron_gate', None), ('i_fortress_fence', '+1.8'), ('i_waterfall_gorge', '그런데 이상한'), ('v:s_mountain_peak', '오늘 소개할'), ('v:s_bus_road', '내 차로는'), ('v:s_hike_deck', '몇백'), ('i_villa_gate', '절반만')], 'cam': [('push', '+0.0', 50, 50, 1.2)], 'items': [
    intro30(), SOFT, cutsfx('+1.8', '그런데 이상한', '오늘 소개할', '내 차로는', '몇백', '절반만'),
    kin('*59년* / 닫혀 있던 철문', '오십구', y=170, size=170, mode='drop', until='그런데 이상한', sfx='hit'),
    kin('그런데 / !이상한! 일', '이상한', y=300, size=150, mode='pop', until='오늘 소개할', sfx='whoosh'),
    kin('문은 열렸는데…', '오늘 소개할', y=150, size=96, mode='slide'),
    kin('내 차로는 !못! 들어간다', '내 차로는', y=330, size=92, mode='slide'),
    kin('하루 *몇백* 명만', '몇백', y=480, size=92, mode='slide'),
    kin('*절반만* 보여 준다', '절반만', y=630, size=92, mode='slide'),
]},
{'from': '흔히들 오래 닫힌 곳은', 'enter': 'zoom', 'bg': [('v:s_seoul_wall', None), ('i_redcliff', '+2.4'), ('i_villa_gate', '다섯'), ('v:s_island_ferry', '넷은'), ('i_geumseong', '열쇠를'), ('v:s_mountain_peak', '문을 연')], 'cam': [('push', '+0.0', 50, 50, 1.15)], 'items': [
    intro30(), cover('+0.02'), cutsfx('+2.4', '다섯', '넷은', '열쇠를', '문을 연'),
    flipcard('길이 험해서? 너무 귀해서?', '누군가 열쇠를 쥐고 있었다', '흔히들', '열쇠를', y=230, size=70),
    kin('다섯 곳 중 !넷은!', '다섯', y=500, size=110, mode='pop', until='문을 연', sfx='whoosh'),
    kin('문을 연 건 / 정말 *세월이었을까?*', '세월이었을까요', y=540, size=104, mode='mix', sfx='hit'),
]},
{'from': '내년 봄, 어디로 갈지', 'enter': 'wipe', 'bg': [('v:s_cherry', None), ('i_birch_forest', '+2.8'), ('v:s_island_ferry', '이 질문이'), ('i_geumseong', '오늘 명단에는'), ('i_landmine', '땅속부터'), ('i_iron_gate', '그리고 첫'), ('i_fortress_fence', '마지막에'), ('v:s_hike_deck', '이 영상은'), ('i_deck_peak', '긴 곳')], 'items': [
    intro30(), SOFT, cutsfx('+2.8', '이 질문이', '오늘 명단에는', '땅속부터', '그리고 첫', '마지막에', '이 영상은', '긴 곳'),
    kin('내년 봄, / *어디로* 가실 건가요?', '내년', y=170, size=110, mode='drop', until='오늘 명단에는', sfx='whoosh'),
    kin('!땅속부터! 뒤진 산', '땅속부터', y=380, size=130, mode='pop', until='그리고 첫', sfx='hit'),
    foreshadow('땅속부터 뒤진 산', '땅속부터', label='뒤에서 공개'),
    kin('첫 장면의 철문은 / *어디였을까?*', '철문이', y=300, size=110, mode='mix', until='이 영상은', sfx='whoosh'),
    kin('순위 기준 / 문이 닫혀 있던 *세월*', '이 영상은', y=260, size=104, mode='slide'),
    kin('짧은 곳 → !긴 곳!', '짧은 곳부터', y=560, size=96, mode='pop'),
]},
# ================= 5위 =================
{'from': '결혼식장에서 양가', 'enter': 'fade', 'bg': 'i_wedding_candle', 'cam': [('push', '+0.1', 50, 50, 1.15)], 'items': [
    BRIGHT, particles('ember', '+0.2', n=12),
    tag('화촉 = 자작나무 껍질 불?', '화촉을', 120, 140, icon='heart-handshake', tone='dark', size=56),
]},
{'from': '오 위는 그 자작나무가', 'enter': 'flash', 'bg': [('v:s_birch', None), ('i_birch_forest', '원래')], 'items': [
    SOFT, rankbadge('5', '영양 자작나무숲', '오 위는'),
    tag('경북 영양 죽파리', '죽파리', 120, 200, icon='map-pin', tone='dark', size=56),
    tag('솔잎혹파리로 망가진 산에서 시작', '솔잎혹파리', 120, 360, icon='alert-triangle', tone='red', size=52),
]},
{'from': '천구백구십삼 년, 산림청이', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('cream'),
    swapnum('30cm 묘목', '20m 숲', '삼십 센티미터', '이십 미터', y=240, size=110, tone='good'),
    tag('1993년부터 26년을 숨어 자랐다', '이십육', None, 500, icon='clock', tone='dark', size=54),
    tag('아파트 7층 높이', '아파트', None, 640, icon='building-store', tone='green', size=54),
]},
{'from': '숲이 일반에 알려진 건', 'enter': 'wipe', 'bg': [('v:s_birch', None), ('i_birch_forest', '+7')], 'items': [
    cover('+0.02'),
    card('2019 공개 · 면적', '30.6ha', '삼십 점', 220, 220, w=660, h=300, vat='삼십 점'),
    card('축구장', '42개', '사십이', 1040, 220, w=660, h=300, vat='사십이'),
    tag('인제 원대리 숲의 3배', '세 배', None, 620, icon='trending-up', tone='green', size=58),
]},
{'from': '그런데 이 숲은 누가 일부러', 'enter': 'zoom', 'bg': 'i_birch_forest', 'items': [
    BRIGHT,
    tag('막은 게 아니라, 아무도 몰랐다', '아무도', 120, 140, icon='scan', tone='dark', size=56),
    tag('2023 산림청 명품숲 100', '명품숲', 120, 300, icon='flag', tone='green', size=54),
    puppet('c_bus', '전기차를', -700, 520, w=640, move='walk', dx=1500, dur=9, step=0.7, tilt=1, sfx=None),
]},
{'from': '전기차에서 내려 삼십 분쯤', 'enter': 'wipe', 'bg': [('v:s_birch', None), ('v:s_hike_deck', '+7')], 'items': [
    BRIGHT,
    tag('산책로 3km · 전망 데크', '삼 킬로미터', None, 140, icon='map-pin', tone='dark', size=56),
    tag('가을 평일 300명 · 주말 600명', '평일', None, 300, icon='users', tone='dark', size=54),
    puppet('c_couple', '+0.5', -440, 480, w=420, move='walk', dx=1100, dur=11, step=0.6),
]},
{'from': '이 동네는 밤에도', 'enter': 'fade', 'bg': 'v:s_stars', 'items': [
    BRIGHT,
    tag('2015 · 아시아 최초 국제 밤하늘 보호공원', '아시아에서', None, 150, icon='flag', tone='dark', size=52),
    glow('낮에는 하얀 숲, 밤에는 쏟아지는 별', '쏟아지는', y=600, size=68),
]},
{'from': '결혼식 날 켠 그 촛불의', 'enter': 'flash', 'bg': 'i_birch_forest', 'cam': [('crash', '지금부터는', 50, 50, 1.3)], 'items': [
    cover('+0.02'), flashhit('지금부터는'),
    tag('5위는 아무도 문을 잠그지 않았다', '아무도', None, 150, icon='key', tone='dark', size=54),
    hook('지금부터는<br><strong>누군가 문을 잠갔던 곳</strong>', '지금부터는', y=320, size=110),
]},
{'from': '여기서 하나 여쭤 보겠습니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    tag('질문 ①', '여쭤', None, 160, icon='scan', tone='red', size=64),
    big('내 차로 바로 갈 수 있나?', '내 차를', y=330, size=96, color='#ffcf4a'),
]},
# ================= 4위 =================
{'from': '천구백팔십오 년, 전남 화순에', 'enter': 'fade', 'bg': [('i_dam_village', None), ('v:s_lake_dam', '그리고')], 'items': [
    BRIGHT,
    tag('1985 전남 화순 · 동복댐', '동복댐이', 120, 140, icon='calendar', tone='dark', size=56),
    tag('마을 10여 개가 물 아래로', '십여', 120, 300, icon='alert-triangle', tone='red', size=54),
]},
{'from': '사 위는 화순 적벽입니다', 'enter': 'flash', 'bg': [('v:s_redcliff', None), ('i_redcliff', '김삿갓이')], 'items': [
    SOFT, rankbadge('4', '화순 적벽', '사 위는'),
    tag('동복천 상류 7km 붉은 절벽', '칠 킬로미터', 120, 200, icon='map-pin', tone='dark', size=54),
]},
{'from': '삼십 년 동안 아무도', 'enter': 'zoom', 'bg': 'i_redcliff', 'items': [
    cover('+0.02'),
    card('출입 통제', '30년', '삼십 년', 220, 200, w=660, h=300, vat='삼십 년'),
    card('개방', '2014.10', '이천십사', 1040, 200, w=660, h=300, vat='이천십사'),
    tag('광주시 · 화순군 상생 협약', '협약을', None, 560, icon='file-invoice', tone='green', size=56),
    tag('망향정 = 고향을 바라보는 정자', '망향정', None, 690, icon='home', tone='dark', size=50),
]},
{'from': '적벽은 한 덩어리가', 'enter': 'wipe', 'bg': [('v:s_redcliff', None), ('v:s_bus_road', '+9')], 'items': [
    cover('+0.02'),
    *stack([('물염적벽', '물염적벽', 'map-pin', 'dark'), ('창랑적벽', '창랑적벽', 'map-pin', 'dark'), ('보산적벽', '보산적벽', 'map-pin', 'dark'),
            ('장항적벽 (노루목)', '장항적벽', 'map-pin', 'red')], x=200, y=150, gap=125, size=54),
    tag('지금은 국가 명승 · 해설사가 기다린다', '명승으로', None, 680, icon='flag', tone='green', size=50),
]},
{'from': '물에 잠긴 마을에서', 'enter': 'fade', 'bg': [('i_redcliff', None), ('v:s_lake_dam', '+12'), ('i_dam_village', '+21')], 'items': [
    BRIGHT,
    tag('경치보다 사연이 먼저 남는 곳', '사연이', 120, 140, icon='heart-handshake', tone='dark', size=54),
    glow('저 물 밑이 우리 집 마당이었다', '마당이었다고요', y=600, size=66),
    puppet('c_hiker', '명절마다', 1500, 480, w=360, move='idle', sfx=None),
]},
{'from': '그렇다고 활짝 열린 건', 'enter': 'zoom', 'bg': [('v:s_bus_road', None), ('v:s_redcliff', '+12')], 'items': [
    cover('+0.02'),
    *stack([('개인 차량 ✕ · 정해진 버스만', '개인 차량', 'user-x', 'red'), ('2026년부터 사전 예약', '예약해야', 'calendar', 'dark'),
            ('개방 초기 하루 360명', '삼백육십', 'users', 'dark')], x=200, y=170, gap=150, size=52),
    tag('그래도 2015년 한 해 3만 명+', '삼만', None, 670, icon='trending-up', tone='green', size=54),
]},
{'from': '여기서 앞뒤가 안 맞는 소식이', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    tag('2026 여름 · 동복댐 둑 높이기 검토 보도', '검토하고', None, 120, icon='file-invoice', tone='red', size=50),
    bars([('지금 둑', 44.7 / 59.7, '44.7m', '사십사', False), ('검토안', 1.0, '59.7m', '오십구', True)], top=260),
    tag('저수량 2배 이상 · 공업용수 하루 30만 톤', '두 배', None, 690, icon='trending-up', tone='red', size=48),
]},
{'from': '둑이 높아지면 물도', 'enter': 'zoom', 'bg': [('v:s_redcliff', None), ('i_redcliff', '+8')], 'items': [
    cover('+0.02'),
    tag('절벽 아랫부분이 또 잠길 수도', '잠길', None, 150, icon='alert-triangle', tone='red', size=56),
    tag('아직은 검토 단계', '검토 단계', None, 300, icon='scan', tone='dark', size=54),
    glow('한 번 열린 문이 영원하다는 보장은 없다', '보장은', y=600, size=58),
]},
{'from': '두 번째 질문입니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    tag('질문 ②', '두 번째', None, 160, icon='scan', tone='red', size=64),
    big('하루 입장 인원이 정해져 있나?', '하루에', y=330, size=90, color='#ffcf4a'),
]},
]
