"""삼성알박기 — 강남역 삼성타운 사이 6층 빌딩 (VREW 오디오, 16:41). 화풍 A 다큐.
새 기법: 스포트라이트(spot) · 가로 연표(timeline) · 전환 strips/wipe/zoom · 앞 레이어(빛 번짐·먼지·비네팅) · 진행 바.
글자 배율 1.4 (55세+ 77.5%)."""
from gen import (hook, flashhit, landmap, tag, logo, stamp, roll, split, side, big, cover, punch, pictos, line, raw, flow, glow, article, inset,
                 rankbadge, swapnum, igrid, donut, bubble, timeline, spot, card)

from gen import A, E
def CH(n, name, first=False):   # 상단 고정 배지 '이유 1 · 상대의 시계' (순위가 아니므로 '위'를 붙이지 않는다)
    return lambda sc: f'<div class="rankbadge{"" if first else " still"}" {A(sc, "+0.05")}><b>이유 {n}</b>{E(name)}</div>'
TL = raw('<style>.tline .tp b{font-size:76px; height:88px} .tline .tp span{font-size:52px} .tline .tp{width:300px; margin-left:-150px}</style>')

PLAN = [
# ================= 인트로 (0:00~1:03) — 2026-11-02 담당자 "후킹이 없다" → 다시 짬: 2~3초 컷, 초대형 쾅 글자, 번쩍, 밝은 화면, 움직이는 클립 위주
{'from': '삼성이 20년 동안', 'enter': 'flash', 'bg': [('ph_samsung_town_aerial', None), ('ph_small_building_street', '못한')], 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'),
    hook('삼성도<br><strong>못 산 땅</strong>', '+0.05', y=250, size=210),
    flashhit('못한'),
]},
{'from': '강남역 사거리', 'enter': 'zoom', 'bg': [('ph_gangnam_crosswalk', None), ('ph_glass_facade', '삼성타운')], 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'),
    tag('강남역 사거리', '강남역', 120, 140, icon='map-pin', tone='red', size=72, until='삼성타운'),
    hook('삼성타운 <em>유리 빌딩 3동</em>', '삼성타운', y=330, size=130),
]},
{'from': '여섯 층짜리', 'enter': 'strips', 'bg': 'ph_small_building_street', 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'),
    spot('겨우 6층', '+0.2', 720, 290, 440, 620),
    tag('신발 속 돌멩이', '돌멩이처럼', 60, 520, icon='alert-triangle', tone='red', size=64),
    flashhit('돌멩이처럼'),
]},
{'from': '삼성은 이 일대', 'enter': 'zoom', 'bg': 'ph_skyline_gangnam', 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'), cover('+0.02'),
    landmap(100, '+0.05', '사들였습니다', holes=(57, 58), holeat='필지', cols=20, y=150, cell=62),
    roll(0, 7600, '사들였습니다', y=470, size=150, suffix='평 매입', prefix='', tone='good', dur=1.0),
    stamp('130평만 못 샀다', '130여', x=700, y=690, size=96),
]},
{'from': '백 칸짜리 바둑판', 'enter': 'strips', 'bg': 'ph_skyline_gangnam', 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'), cover('+0.02'),
    landmap(100, '+0.02', '+0.05', holes=(44, 45), holeat='두', cols=10, x=140, y=95, cell=62, sfx=None),
    tag('100칸 중 단 2칸', '두', 960, 380, icon='map-pin', tone='red', size=64),
]},
{'from': '그리고 2009년', 'enter': 'flash', 'bg': 'ph_cash_count', 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'),
    tag('2009년', '+0.1', 120, 120, icon='calendar', tone='dark', size=66),
    roll(0, 230, '230억', y=330, size=260, suffix='억 원', tone='good', dur=0.9),
    flashhit('팔렸습니다'),
]},
{'from': '산 사람은 삼성이', 'enter': 'zoom', 'bg': 'ph_mystery_buyer', 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'),
    logo('samsung', '+0.05', 120, 150, h=110),
    stamp('X', '아니었습니다', x=420, y=40, size=300, rot=-6),
    swapnum('???', '성형외과 원장', '+0.6', '원장이었습니다', y=520, size=150, tone='good'),
]},
{'from': '다들 끝까지 버텨서', 'enter': 'strips', 'bg': 'ph_small_building_street', 'items': [
    raw('<style>.bg{--dark:.86; --blur:0px}</style>'), cover('+0.02'),
    hook('끝까지 버틴 <strong>알박기?</strong>', '+0.05', y=170, size=140, sfx='pop'),
    *[tag(t, '숫자를', x, y, icon=i, tone=tn, size=58) for t, x, y, i, tn in
      (('6억/월', 300, 400, 'clock', 'dark'), ('+67억?', 1040, 400, 'trending-up', 'green'), ('163억', 300, 540, 'coin', 'dark'), ('1.5~3배', 1040, 540, 'scale', 'dark'))],
    glow('전혀 다른 그림', '그림이', y=710, size=90),
]},
{'from': '재벌도 이기지 못한', 'enter': 'zoom', 'bg': 'ph_gangnam_rain', 'items': [
    hook('재벌도 못 이긴 땅<br><em>왜 쓸쓸할까?</em>', '재벌도', y=230, size=150),
]},
{'from': '이 질문은 강남', 'enter': 'wipe', 'bg': 'ph_city_bokeh', 'items': [
    cover('+0.02'),
    inset('ph_small_building_street', '+0.1', 70, 170, w=560, h=420, cap='강남 6층 빌딩'),
    inset('ph_church_ruins', '500억', 680, 170, w=560, h=420, cap='500억 날린 교회'),
    inset('ph_samik_apartment', '아파트', 1290, 170, w=560, h=420, cap='아파트 한 동'),
    stamp('500억', '500억', x=760, y=660, size=120),
]},
{'from': '오늘은 그 이유를', 'enter': 'zoom', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    *[tag(t, a, 520, y, icon='key', tone=tn, size=82) for t, a, y, tn in
      (('이유 1', '+0.1', 150, 'dark'), ('이유 2', '세', 340, 'dark'), ('이유 3', '벗겨', 530, 'red'))],
    stamp('무릎을 친다', '무릎을', x=1150, y=640, size=110),
]},
# ================= 알박기란 (1:03~2:20) =================
{'from': '먼저 알박기라는', 'enter': 'wipe', 'bg': 'ph_dictionary', 'items': [
    tag('알박기', '알박기라는', 140, 150, icon='file-invoice', tone='red', size=80),
    article('국립국어원 풀이 (요약)', '표준국어대사전', '주요한 택지의 일부를 남보다 앞서 사 두는 일', '주요한', mark='앞서 사 두는 일', markat='앞서', x=560, y=330, rot=-1.5),
]},
{'from': '요즘은 개발 예정지', 'bg': 'ph_dev_field', 'items': [
    tag('요즘 뜻: 개발 예정지 땅 쥐고 값 크게 부르기', '요즘은', 120, 170, icon='alert-triangle', tone='dark', size=54),
]},
{'from': '큰 건물이나 아파트', 'bg': 'ph_loan_site', 'items': [
    flow([('땅 다 모아야', '모여야'), ('대부분 빌린 돈', '빌려서'), ('매달 이자', '이자가')], y=200, size=66),
]},
{'from': '실제 판례에 나온', 'enter': 'strips', 'bg': 'ph_loan_site', 'items': [
    cover('+0.02'),
    tag('실제 판례 · 땅 몇 필지 못 사서 승인 지연', '실제', 300, 130, icon='gavel', tone='dark', size=54),
    big('한 달 6억 원', '6억', y=280, size=170, color='#ff5a5a'),
    tag('하루 2,000만 원', '하루로', 640, 560, icon='clock', tone='red', size=66),
]},
{'from': '웬만한 새 경차', 'bg': 'ph_small_car', 'items': [
    tag('= 매일 새 경차 한 대', '경차', 120, 180, icon='car', tone='red', size=70),
]},
{'from': '이 한 달 6억 원', 'bg': 'ph_taxi_meter', 'items': [
    cover('+0.02'),
    glow('한 달 6억 원', '6억', y=300, size=140),
    tag('오늘 이야기의 열쇠', '열쇠입니다', 660, 560, icon='key', tone='dark', size=62),
]},
{'from': '사업자에게도 무기가', 'enter': 'zoom', 'bg': 'st_court', 'items': [
    cover('+0.02'),
    *split('+0.05'),
    side('l', '매도', tag('무기 ① 매도청구', '매도', 0, 0, icon='gavel', tone='red', size=56), tag('땅 모으면 법원 통해 매도 요구', '모으면', 0, 0, size=40)),
    side('r', '제척입니다', tag('무기 ② 제척', '제척입니다', 0, 0, icon='hand-stop', tone='red', size=56), tag('그 땅을 구역에서 빼기', '빼', 0, 0, size=40)),
]},
{'from': '낯선 단어죠', 'bg': 'st_court', 'items': [
    cover('+0.02'),
    stamp('제척', '두', x=760, y=260, size=180),
    tag('수백억 원의 운명을 가른다', '수백억', 520, 600, icon='coin', tone='dark', size=62),
]},
# ================= 윤빌딩 연표 (2:16~4:24) =================
{'from': '그렇다면 삼성타운 앞', 'enter': 'wipe', 'bg': 'ph_building_entrance', 'items': [
    spot('어떻게 여기에?', '작은', 720, 290, 440, 620),
]},
{'from': '시간을 반세기쯤', 'enter': 'zoom', 'bg': 'ph_gangnam_1970s', 'items': [
    tag('반세기 전 강남: 논밭과 흙길', '논밭과', 120, 160, icon='map-pin', tone='dark', size=58),
]},
{'from': '건물주 윤 모 씨는', 'bg': 'ph_scrivener_office', 'items': [
    tag('건물주 윤 모 씨 · 법무사 출신', '건물주', 120, 150, icon='user', size=58),
    tag('땅 취득 1970년대 초 (등기부 보도)', '1970년대로', 120, 290, icon='calendar', tone='dark', size=54),
]},
{'from': '한때는 시외버스 터미널', 'bg': 'ph_city_blueprint', 'items': [
    tag('시외버스터미널 예정 부지로 묶였다는 이야기', '터미널', 120, 150, icon='bus', tone='dark', size=52),
    tag('땅에 대한 애착이 유난', '애착이', 120, 300, icon='heart-handshake', tone='red', size=58),
]},
{'from': '1993년, 삼성이', 'enter': 'strips', 'bg': 'ph_glass_facade', 'items': [
    cover('+0.02'),
    TL,
    timeline([('1970s', '윤 씨 땅 취득', '+0.1'), ('1993', '삼성 매입 시작', '1993년,'), ('1998', '외환위기·윤빌딩 착공', '1998년,'),
              ('1999', '윤빌딩 완공', '이듬해', 1)], y=330),
    tag('그룹의 새 심장', '심장을', 760, 130, icon='building-skyscraper', tone='dark', size=54),
]},
{'from': '이름은 자기 성을 딴', 'bg': 'ph_new_building_1999', 'items': [
    tag('윤빌딩 · 지하 2층 지상 6층', '윤빌딩이었습니다', 120, 160, icon='building-store', size=62),
    tag('2004 · 삼성타운 착공', '마침내', 120, 310, icon='building-skyscraper', tone='red', size=62),
]},
{'from': '삼성은 윤빌딩의 왼쪽과', 'enter': 'zoom', 'bg': 'ph_construction_surround', 'items': [
    tag('왼쪽 · 오른쪽 · 뒤쪽을 둘러싸고 공사', '둘러싸고', 120, 140, icon='building-skyscraper', tone='red', size=56),
]},
{'from': '2005년, 한 시사주간지', 'bg': 'ph_construction_surround', 'items': [
    article('시사주간지 현장 (요약)', '2005', '거대한 공사장 한가운데 홀로 선 윤빌딩', '+0.1', mark='홀로 선', markat='한가운데', x=120, y=120, rot=-2),
    tag('인부들은 그 편의점 단골', '인부들은', 900, 600, icon='shopping-cart', size=50),
]},
{'from': '건물주는 그때', 'bg': 'ph_old_man_window', 'items': [
    tag('그때 건물주 82세', '여든두', 120, 160, icon='user', tone='dark', size=66),
]},
{'from': '삼성은 이후에도', 'bg': 'ph_glass_facade', 'items': [
    cover('+0.02'),
    tag('2006 · 2007 두 차례 매입 타진설', '+0.1', 360, 150, icon='mail', size=58),
    big('평당 약 1억 2,000만 원', '거론된', y=290, size=110, color='#ffd166'),
    tag('일부 보도 추정치', '거론된', 760, 470, icon='alert-triangle', tone='ghost', size=48),
    stamp('윤 씨는 안 팔았다', '팔지', x=980, y=610, size=90),
]},
{'from': '2008년, 삼성타운이', 'enter': 'strips', 'bg': 'ph_tower_crane_2004', 'items': [
    TL,
    timeline([('2004', '삼성타운 착공', '+0'), ('2008', '삼성타운 완공', '+0.2', 1)], y=150),
    tag('핵심 계열사 입주', '입주했습니다', 700, 470, icon='building-skyscraper', tone='green', size=60),
]},
{'from': '강남역을 오가던', 'bg': 'ph_passersby', 'items': [
    bubble('저 작은 건물은 대체 뭐길래?', '저', 560, 220, size=62),
]},
{'from': '삼성을 못 이긴 건물', 'bg': 'ph_gangnam_dusk', 'items': [
    glow('삼성도 못 이긴 건물', '삼성을', y=300, size=110),
    tag('강남의 전설', '전설이', 700, 540, icon='flag', tone='dark', size=66),
]},
{'from': '그런데 이상한 신호는', 'enter': 'wipe', 'bg': 'ph_tower_crane_2004', 'items': [
    cover('+0.02'),
    tag('이상한 신호', '신호는', 700, 200, icon='alert-triangle', tone='red', size=72),
    line('삼성타운이 다 지어졌다는 것 자체', '다', x=None, y=420, cls='say', size=74, center=True),
]},
# ================= 2009년 매각과 첫 반전 (4:24~6:11) =================
{'from': '2009년, 윤 씨가', 'enter': 'zoom', 'bg': 'ph_funeral_flowers', 'items': [
    tag('2009 · 윤 씨 별세', '+0.1', 120, 160, icon='calendar', tone='dark', size=60),
]},
{'from': '유족들은 상속세', 'bg': 'ph_tax_bill', 'items': [
    tag('상속세 마련하려 매각', '상속세', 120, 160, icon='receipt', size=60),
    big('230억 원', '230억', y=380, size=170, color='#ffd166'),
]},
{'from': '역시 버틴 사람이', 'bg': 'st_calc', 'items': [
    cover('+0.02'),
    bubble('역시 버틴 사람이 이겼구나!', '역시', 520, 180, size=60),
    flow([('1억 2,000만 × 136평', '136평이면'), ('약 163억', '163억')], y=380, size=70),
    tag('+67억 더 받은 셈?', '67억', 640, 600, icon='trending-up', tone='green', size=66),
]},
{'from': '그런데 숫자를 들여다보니', 'enter': 'strips', 'bg': 'ph_remodeled_building', 'items': [
    cover('+0.02'),
    tag('이상한 점 ① 산 사람이 삼성 아님', '먼저', 200, 170, icon='alert-triangle', tone='red', size=58),
    tag('삼성은 이미 그 땅 없이 다 지음', '없이', 200, 320, icon='building-skyscraper', tone='dark', size=56),
    tag('이상한 점 ② 새 주인도 7년 만에 매물로', '그다음은', 200, 470, icon='alert-triangle', tone='red', size=56),
    tag('임대수익이 안 나와서', '임대', 200, 620, icon='trending-down', size=52),
]},
{'from': '그리고 결정적인 사실이', 'enter': 'zoom', 'bg': 'ph_old_man_window', 'items': [
    cover('+0.02'),
    punch('알박기가 아니었다', '알박기가', y=330, size=140),
]},
{'from': '2005년 윤 씨의', 'bg': 'ph_scrivener_office', 'items': [
    bubble('삼성이 직접 사려 한 적 없다 (가족)', '삼성이', 200, 200, size=52),
    bubble('삼성인 줄도 몰랐다 (관리인)', '개인이', 300, 470, size=52, tone='red'),
]},
{'from': '법원의 기준도', 'enter': 'wipe', 'bg': 'ph_supreme_court', 'items': [
    article('대법원 판결 취지 (요약)', '2009. 1', '개발 계획 모른 채 산 땅을 비싸게 파는 건 부당이득 아니다', '+0.3', mark='부당이득 아니다', markat='부당이득이', x=200, y=130),
    tag('1.5~3배 받았지만 무죄', '무죄였습니다', 820, 600, icon='scale', tone='green', size=60),
]},
{'from': '그러니까 윤빌딩은', 'bg': 'ph_building_entrance', 'items': [
    cover('+0.02'),
    swapnum('알박기 건물', '팔기 싫었던 사람의 건물', '+0.1', '그냥', y=280, size=100, tone='good'),
    stamp('첫 번째 반전', '첫', x=760, y=560, size=110),
]},
{'from': '그렇다면 질문은', 'bg': 'ph_sunset_skyline', 'items': [
    cover('+0.02'),
    tag('법도 문제 삼지 않았고', '법도', 520, 200, icon='scale', size=62),
    tag('삼성도 이기지 못했는데', '삼성도', 520, 340, icon='building-skyscraper', size=62),
    line('왜 이렇게 쓸쓸할까?', '쓸쓸할까요', x=None, y=520, cls='head', size=110, center=True, color='#ffd166'),
]},
# ================= 세 가지 이유 예고 (6:11~6:35) =================
{'from': '자, 그런데 여기서부터가', 'enter': 'flash', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    tag('버틴 땅의 운명을 가르는 세 가지', '버틴', 400, 110, icon='key', tone='dark', size=60),
    tag('① 버티는 힘은 상대의 시계에서', '첫째,', 200, 260, icon='clock', size=58),
    tag('② 처음 부른 큰 숫자가 발목을', '둘째,', 200, 400, icon='coin', size=58),
    tag('③ 땅값은 혼자서 생기지 않는다', '셋째,', 200, 540, icon='users', tone='red', size=58),
]},
# ================= 이유 1: 상대의 시계 (6:33~8:25) =================
{'from': '첫째부터 보겠습니다', 'enter': 'zoom', 'bg': 'ph_taxi_meter', 'items': [
    CH(1, '상대의 시계', first=True),
    glow('한 달 6억 원', '6억', y=300, size=130),
    tag('땅 주인의 진짜 무기', '무기는', 660, 540, icon='key', tone='red', size=62),
]},
{'from': '택시 미터기를', 'bg': 'ph_city_bokeh', 'items': [
    CH(1, '상대의 시계'),
    tag('상대의 미터기가 도는 동안 = 하루하루가 돈', '미터기가', 120, 180, icon='clock', tone='dark', size=52),
    tag('그래서 비싸게라도 산다', '비싸게라도', 120, 330, icon='coin', tone='green', size=58),
]},
{'from': '그런데 미터기가 꺼지는', 'enter': 'strips', 'bg': 'ph_crane_up', 'items': [
    CH(1, '상대의 시계'),
    tag('미터기가 꺼지는 순간 = 비켜 짓기로 결정할 때', '꺼지는', 120, 160, icon='hand-stop', tone='red', size=52),
    stamp('삼성 미터기 OFF', '꺼졌습니다', x=1100, y=560, size=100),
]},
{'from': '2009년 유족이', 'bg': 'ph_tax_bill', 'items': [
    CH(1, '상대의 시계'),
    tag('2009년 매물 → 삼성은 급하지 않았다', '급하지', 120, 170, icon='clock', tone='dark', size=56),
]},
{'from': '여기엔 마음의 이유도', 'enter': 'wipe', 'bg': 'st_money', 'items': [
    CH(1, '상대의 시계'),
    cover('+0.02'),
    *split('+0.05'),
    side('l', '잃는', tag('잃는 고통', '잃는', 0, 0, icon='trending-down', tone='red', size=66), big('×2', '잃는', y=0, size=150, color='#ff5a5a')),
    side('r', '얻는', tag('얻는 기쁨', '얻는', 0, 0, icon='trending-up', tone='green', size=66), big('×1', '얻는', y=0, size=150, color='#3fe08a')),
    glow('손실 회피', '손실', y=640, size=90),
]},
{'from': '버티는 쪽은 상대의', 'bg': 'st_money', 'items': [
    CH(1, '상대의 시계'),
    swapnum('두려움', '살 사람도 사라짐', '+0.1', '사라지면', y=320, size=110),
]},
{'from': '잠깐, 그럼 끝까지', 'enter': 'zoom', 'bg': 'ph_dev_field', 'items': [
    CH(1, '상대의 시계'),
    bubble('끝까지 버티면 결국 이기는 거 아닌가요?', '잠깐', 300, 200, size=58),
    tag('반대 사례: 충남 천안', '천안의', 600, 500, icon='map-pin', tone='red', size=62),
]},
{'from': '사업 승인이 막혀', 'bg': 'ph_redevelop_fence', 'items': [
    CH(1, '상대의 시계'),
    cover('+0.02'),
    big('시세의 약 36배', '서른여섯', y=180, size=140, color='#ff5a5a'),
    tag('부당이득 약 25억 2,800만 원', '부당', 420, 400, icon='coin', tone='dark', size=58),
    stamp('징역 10월 · 집행유예 2년', '징역', x=560, y=610, size=80),
]},
{'from': '2006년 헌법재판소는', 'bg': 'ph_courtroom', 'items': [
    CH(1, '상대의 시계'),
    tag('2006 헌재: 처벌 조항 합헌', '헌법재판소는', 120, 170, icon='gavel', size=58),
    tag('대법원: 삶의 터전 내놓는 사람엔 충분한 보상', '대법원은', 120, 330, icon='scale', tone='green', size=52),
]},
{'from': '결국 가르는 기준은', 'enter': 'strips', 'bg': 'ph_courtroom', 'items': [
    CH(1, '상대의 시계'),
    cover('+0.02'),
    tag('가르는 기준 두 가지', '기준은', 600, 130, icon='scale', tone='dark', size=60),
    tag('① 언제 그 땅을 샀나', '언제', 300, 300, icon='calendar', size=62),
    tag('② 상대의 다급함을 노렸나', '다급함을', 300, 460, icon='alert-triangle', tone='red', size=62),
]},
# ================= 이유 2: 처음 부른 숫자 (8:25~10:27) =================
{'from': '둘째. 처음 부른', 'enter': 'zoom', 'bg': 'ph_church_ruins', 'items': [
    CH(2, '처음 부른 숫자', first=True),
    tag('서울 성북구 장위10구역', '장위10구역', 120, 180, icon='map-pin', size=60),
]},
{'from': '2008년 정비 구역으로', 'bg': 'ph_church_gate', 'items': [
    CH(2, '처음 부른 숫자'),
    TL,
    timeline([('2008', '정비구역 지정', '+0'), ('2017', '관리처분 인가', '2017년'), ('90%+', '철거', '아홉')], y=180),
    tag('허허벌판에 교회 하나만', '교회', 560, 560, icon='building-bank', tone='red', size=60),
]},
{'from': '교회는 보상금으로', 'enter': 'strips', 'bg': 'ph_church_gate', 'items': [
    CH(2, '처음 부른 숫자'),
    cover('+0.02'),
    big('563억 원 요구', '563억', y=180, size=140, color='#ff5a5a'),
    tag('조합 첫 제시액의 2배+', '두', 600, 420, icon='trending-up', tone='dark', size=60),
    tag('조합은 명도소송 승소 · 강제집행은 난항', '명도', 360, 570, icon='gavel', size=52),
]},
{'from': '결국 양쪽은', 'bg': 'ph_redevelop_fence', 'items': [
    CH(2, '처음 부른 숫자'),
    stamp('500억 원 합의', '500억', x=200, y=200, size=110),
    tag('그런데 교회가 이전 안 하겠다고', '입장을', 120, 480, icon='alert-triangle', tone='red', size=56),
    tag('교회 측: 알박기 보도 탓에 옮겨갈 땅 못 사', '교회', 120, 620, icon='file-invoice', tone='ghost', size=46),
]},
{'from': '그러자 조합은', 'enter': 'wipe', 'bg': 'ph_union_vote', 'items': [
    CH(2, '처음 부른 숫자'),
    stamp('제척', '제척입니다', x=1200, y=180, size=160),
    tag('2023. 5 총회 · 422명 중 323명 찬성', '총회에서', 120, 460, icon='users', size=56),
    igrid('user', 10, '422명', lit=8, litat='323명이', cols=10, y=600, size=80, tone='bad'),
]},
{'from': '교회를 빼고 짓겠다는', 'bg': 'ph_excavators_2026', 'items': [
    CH(2, '처음 부른 숫자'),
    swapnum('보상 약 600억', '물거품', '+0.4', '물거품이', y=150, size=110),
    tag('조합: 100억대 손해배상 예고', '100억', 120, 420, icon='gavel', tone='red', size=52),
    tag('교회 측: 조합원 손해 2,800억 주장', '2,800억', 120, 550, icon='alert-triangle', tone='ghost', size=50),
]},
{'from': '2025년 6월, 성북구는', 'enter': 'strips', 'bg': 'ph_excavators_2026', 'items': [
    CH(2, '처음 부른 숫자'),
    TL,
    timeline([('2025.6', '교회 뺀 계획 인가', '+0'), ('2026', '실제 착공', '2026년'), ('17년', '지정부터 걸린 시간', '17년', 1)], y=180),
]},
{'from': '왜 500억 원을', 'enter': 'zoom', 'bg': 'ph_cash_stack', 'items': [
    CH(2, '처음 부른 숫자'),
    cover('+0.02'),
    tag('왜 500억을 받고 떠나지 않았나?', '왜', 360, 130, icon='alert-triangle', size=60),
    glow('기준점 효과', '기준점', y=300, size=120),
    swapnum('563억', '500억 = 깎인 돈?', '563억', '깎인', y=520, size=100),
]},
{'from': '여기서 두 번째 반전', 'bg': 'ph_eviction_gate', 'items': [
    CH(2, '처음 부른 숫자'),
    cover('+0.02'),
    stamp('두 번째 반전', '두', x=700, y=150, size=110),
    line('미터기가 꺼지면 숫자는 0', '미터기가', x=None, y=420, cls='head', size=100, center=True, color='#ff5a5a'),
    tag('여러분이라면 500억 합의, 받아들였을까요?', '여러분이라면', 300, 620, icon='heart-handshake', tone='dark', size=50),
]},
# ================= 이유 3: 이웃과 맞물려야 (10:27~11:57) =================
{'from': '이제 마지막 퍼즐', 'enter': 'zoom', 'bg': 'ph_puzzle', 'items': [
    CH(3, '이웃과 맞물려야', first=True),
    tag('사실 이게 가장 아프다', '아픕니다', 120, 200, icon='mood-sad', tone='red', size=62),
]},
{'from': '서울 강동구 명일동', 'bg': 'ph_old_apartment', 'items': [
    CH(3, '이웃과 맞물려야'),
    tag('강동구 명일동 삼익맨숀', '명일동', 120, 180, icon='home', size=60),
    tag('넓은 평형 5동의 주장', '5동이었습니다', 120, 320, icon='users', tone='dark', size=58),
    bubble('우리 동은 대지가 넓다, 같은 조건 안 돼', '우리', 260, 500, size=50),
]},
{'from': '계산만 보면', 'bg': 'ph_old_apartment', 'items': [
    CH(3, '이웃과 맞물려야'),
    tag('나름 일리 있는 주장', '일리', 120, 180, icon='scale', size=58),
    tag('협상 결렬 → 토지분할 소송', '협상은', 120, 330, icon='gavel', tone='red', size=58),
]},
{'from': '2026년 7월, 서울시', 'enter': 'strips', 'bg': 'ph_old_apartment', 'items': [
    CH(3, '이웃과 맞물려야'),
    cover('+0.02'),
    tag('2026. 7 서울시 통합심의 통과', '+0.1', 420, 130, icon='calendar', size=58),
    stamp('5동 빼고 C자 단지', 'C자', x=720, y=300, size=110),
    flow([('768가구', '768가구가'), ('최고 39층 990가구', '990가구로')], y=540, size=70),
]},
{'from': '그럼 빠진 5동은', 'bg': 'ph_apartment_fence', 'items': [
    CH(3, '이웃과 맞물려야'),
    cover('+0.02'),
    tag('빠진 5동 146㎡', '+0.1', 520, 130, icon='home', size=60),
    big('17억 7,000만 원 거래', '17억', y=260, size=110, color='#ffd166'),
    tag('82㎡ 최고 호가도 18억 5,000만', '17억', 300, 480, icon='alert-triangle', tone='red', size=50),
    tag('넓이 2배인데 몸값은 비슷', '17억', 520, 620, icon='scale', tone='dark', size=58),
]},
{'from': '퍼즐 조각을 떠올려', 'enter': 'wipe', 'bg': 'ph_puzzle', 'items': [
    CH(3, '이웃과 맞물려야'),
    tag('조각 하나는 그림이 아니다', '한', 120, 170, icon='package', size=58),
    tag('맞물릴 때만 그림의 일부', '맞물릴', 120, 320, icon='users', tone='green', size=58),
]},
{'from': '땅도 같습니다', 'bg': 'ph_site_model', 'items': [
    CH(3, '이웃과 맞물려야'),
    cover('+0.02'),
    tag('개발 가치 = 이웃과 합쳐질 때', '개발', 380, 150, icon='home', tone='green', size=60),
    swapnum('내 몫 지키기', '나 혼자 섬', '내', '섬으로', y=330, size=110),
    glow('구성의 오류', '구성의', y=580, size=100),
]},
{'from': '다만 아직 결론은', 'bg': 'ph_apartment_fence', 'items': [
    CH(3, '이웃과 맞물려야'),
    tag('5동 안에서도 의견 갈림: 함께 vs 따로', '5동', 120, 180, icon='users', tone='dark', size=54),
    tag('다시 합칠 가능성도 거론', '합칠', 120, 330, icon='heart-handshake', tone='green', size=56),
]},
# ================= 끝까지 웃는 쪽 (11:57~13:46) =================
{'from': '그렇다면 버텨서', 'enter': 'zoom', 'bg': 'ph_aus_suburb', 'items': [
    tag('버텨서 끝까지 웃는 쪽은?', '그렇다면', 120, 150, icon='alert-triangle', tone='dark', size=60),
    stamp('있습니다', '있습니다', x=1200, y=300, size=120),
]},
{'from': '호주 시드니 외곽', 'bg': 'ph_aus_driveway', 'items': [
    tag('호주 시드니 더 폰즈 · 자밋 가족', '호주', 120, 150, icon='map-pin', size=56),
    tag('약 2만㎡ = 축구장 3개', '축구장', 120, 290, icon='flag', tone='green', size=56),
    tag('진입로 200m', '200미터짜리', 120, 430, icon='car', size=56),
]},
{'from': '그사이 이웃들은', 'bg': 'ph_aus_suburb', 'items': [
    spot('초록 잔디 섬', '초록', 560, 230, 820, 500),
    tag('개발업자 5,000만 호주달러 제시 보도', '5,000만', 120, 790, icon='coin', tone='dark', size=50),
]},
{'from': '다만 가족은 제안', 'bg': 'ph_aus_driveway', 'items': [
    tag('가족은 액수를 밝힌 적 없음', '다만', 120, 160, icon='lock', tone='dark', size=56),
    bubble('막다른 골목이라 아이들 안전 (이웃)', '덕분에', 260, 400, size=50),
]},
{'from': '미국 시애틀에도', 'enter': 'wipe', 'bg': 'ph_seattle_house', 'items': [
    tag('시애틀 이디스 메이스필드 할머니', '이디스', 120, 150, icon='user', size=56),
    tag('2006 · 100만 달러 제안 거절', '100만', 120, 290, icon='hand-stop', tone='red', size=58),
    tag('영화 「업」의 영감으로 알려짐', '업의', 120, 430, icon='home', tone='dark', size=54),
]},
{'from': '이들과 앞의 사례는', 'enter': 'zoom', 'bg': 'ph_city_bokeh', 'items': [
    cover('+0.02'),
    *split('+0.05'),
    side('l', '팔려고', tag('팔려고 버팀', '팔려고', 0, 0, icon='coin', tone='red', size=62), tag('시간은 상대 편', '돈이면', 0, 0, icon='clock', size=50)),
    side('r', '살려고', tag('살려고 버팀', '살려고', 0, 0, icon='home', tone='green', size=62), tag('시간은 내 편', '삶이면', 0, 0, icon='clock', size=50)),
]},
{'from': '물론 그대로 판박이는', 'bg': 'ph_funeral_flowers', 'items': [
    tag('호주 동네는 지금도 개발 수요', '호주의', 120, 160, icon='trending-up', size=54),
    tag('상속이 일어나는 순간 순서가 뒤집힌다', '상속이', 120, 310, icon='arrows-exchange', tone='red', size=54),
    swapnum('삶의 터전', '세금 고지서', '땅은', '고지서가', y=480, size=100),
]},
{'from': '그럼 거인은', 'enter': 'strips', 'bg': 'ph_corp_lobby', 'items': [
    cover('+0.02'),
    logo('samsung', '+0.1', 820, 110, h=70),
    swapnum('2018 · 7,484억 매각', '2024 · 약 1조 1,000억 재매입', '2018년', '1조', y=320, size=80, tone='good'),
    tag('거인에게 건물은 끝까지 숫자', '거인에게', 520, 560, icon='coin', tone='dark', size=58),
]},
{'from': '정부도 움직이고', 'bg': 'st_contract', 'items': [
    cover('+0.02'),
    tag('2026. 4 국토부 지역주택조합 제도 개선', '+0.1', 300, 130, icon='building-bank', size=54),
    swapnum('토지 확보 95%', '80%', '95%에서', '80%로', y=270, size=130, tone='good'),
    igrid('home', 5, '다섯', lit=4, litat='네', cols=5, y=500, size=120, tone='good'),
]},
{'from': '업무대행사 같은 쪽이', 'bg': 'ph_document_sign', 'items': [
    tag('업무대행사 보유 땅: 보유 기간 무관 매도청구', '업무대행사', 120, 170, icon='gavel', tone='red', size=50),
    tag('법 개정·시행 시점은 지켜봐야', '다만', 120, 320, icon='clock', tone='dark', size=54),
]},
# ================= 정리 (14:39~16:41) =================
{'from': '오늘 처음에 여쭤봤던', 'enter': 'zoom', 'bg': 'ph_sunset_skyline', 'items': [
    cover('+0.02'),
    line('재벌도 이기지 못한 땅', '재벌도', x=None, y=180, cls='head', size=100, center=True),
    line('왜 승리처럼 보이지 않았을까?', '승리처럼', x=None, y=330, cls='say', size=76, center=True, color='#ffd166'),
]},
{'from': '답은 세 줄입니다', 'bg': 'ph_gangnam_rain', 'items': [
    cover('+0.02'),
    tag('① 버티는 힘은 상대가 급할 때만', '버티는', 200, 170, icon='clock', size=58),
    tag('② 처음 부른 숫자는 나를 묶는 밧줄', '처음', 200, 320, icon='coin', size=58),
    tag('③ 땅값은 이웃과 맞물릴 때', '이웃과', 200, 470, icon='users', tone='green', size=58),
]},
{'from': '한 문장으로 줄이면', 'enter': 'strips', 'bg': 'ph_narrow_gap', 'items': [
    cover('+0.02'),
    line('버티기는 몸값을 올려 줄 뿐', '몸값을', x=None, y=230, cls='head', size=96, center=True),
    line('값을 치를 사람까지 붙잡지는 못한다', '치를', x=None, y=400, cls='head', size=86, center=True, color='#ff8a8a'),
]},
{'from': '이건 땅만의 이야기가', 'bg': 'ph_negotiation', 'items': [
    tag('연봉 협상 · 가게 권리금 · 집 매매', '연봉', 120, 170, icon='heart-handshake', size=56),
    swapnum('내 물건에서?', '상대의 조급함에서?', '내', '조급함에서', y=380, size=90),
]},
{'from': '오늘 해 보실 수 있는', 'enter': 'wipe', 'bg': 'ph_negotiation', 'items': [
    cover('+0.02'),
    tag('오늘 해 볼 일 세 가지', '오늘', 600, 100, icon='key', tone='dark', size=58),
    tag('□ 지주택 권유 → 토지 소유권 몇 % 서류 확인', '하나,', 140, 250, icon='file-invoice', size=52),
    tag('□ 재개발 구역 → 우리 땅 제척 가능성 질문', '둘,', 140, 400, icon='home', size=52),
    tag('□ 처음 들은 호가를 잣대로 삼지 않기', '셋,', 140, 550, icon='alert-triangle', tone='red', size=52),
]},
{'from': '강남역 사거리, 유리 빌딩', 'enter': 'zoom', 'bg': 'ph_samsung_town_aerial', 'items': [
    spot('지금도 서 있는 작은 건물', '세', 860, 500, 230, 340),
]},
{'from': '삼성은 그 땅을 끝내', 'bg': 'ph_gangnam_rain', 'items': [
    cover('+0.02'),
    line('삼성은 끝내 갖지 못했고', '삼성은', x=None, y=230, cls='say', size=84, center=True),
    line('지킨 사람도 끝까지 머물지 못했다', '머물지는', x=None, y=380, cls='say', size=84, center=True, color='#ffd166'),
]},
{'from': '여러분이 윤 씨였다면', 'enter': 'flash', 'bg': 'ph_narrow_gap', 'items': [
    cover('+0.02'),
    tag('여러분이 윤 씨였다면?', '여러분이', 600, 60, icon='heart-handshake', tone='dark', size=54),
    raw('<style>.side{top:280px}</style>'),
    *split('1번'),
    side('l', '1번', tag('1번 판다', '판다,', 0, 0, icon='coin', tone='green', size=80)),
    side('r', '2번', tag('2번 버틴다', '버틴다로', 0, 0, icon='hand-stop', tone='red', size=80)),
]},
{'from': '다음 이야기도 골라', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    tag('다음 이야기 투표', '다음', 640, 100, icon='flag', tone='dark', size=58),
    tag('1번 동네 목욕탕은 왜 사라졌을까', '1번,', 160, 250, icon='droplet', size=54),
    tag('2번 분양가보다 싼 신도시 상가', '2번,', 160, 400, icon='building-store', size=54),
    tag('3번 권리금 수억이 0원 되는 순간', '3번,', 160, 550, icon='coin', tone='red', size=54),
]},
{'from': '숫자 뒤에 숨은', 'enter': 'zoom', 'bg': 'ph_skyline_gangnam', 'items': [
    cover('+0.02'),
    line('숫자 뒤에 숨은 사람의 마음', '숫자', x=None, y=300, cls='say', size=80, center=True),
    line('지혜호수 경제연구소', '지혜호수', x=None, y=440, cls='head', size=120, center=True),
]},
]
