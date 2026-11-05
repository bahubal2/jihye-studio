"""공주밤 편 — 인트로 · 1막 · 2막 (자막 1~78, 0:00~5:32). 앞쪽 집중: 짧은 컷, 카메라, 복선, 세피아 회상. 3:24 반전(29,000톤→1,000톤 아래)."""
from gen import (hook, flashhit, tag, stamp, big, cover, punch, glow, raw, stack, swapnum, card, bubble, donut, bars,
                 shrink, foreshadow, flipcard, PAST)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

A = [
# ================= 인트로 =================
{'from': '구월 말, 밤 수매장의', 'enter': 'flash', 'bg': 'th_scale_chestnut', 'cam': [('push', '+0.1', 50, 55, 1.15)], 'items': [
    BRIGHT,
    tag('9월 말 · 밤 수매장 저울 앞', '+0.2', 120, 140, icon='calendar', tone='dark', size=58),
]},
{'from': '특대 밤 일 킬로그램에', 'enter': 'zoom', 'bg': 'th_scale_chestnut', 'cam': [('crash', '이천이백', 50, 50, 1.35)], 'items': [
    cover('+0.02'),
    tag('특대 밤 1kg', '+0.05', None, 170, icon='scale', tone='dark', size=64),
    big('2,200원', '이천이백', y=300, size=230, color='#ff5a5a'),
]},
{'from': '공주 밤이 산에서 썩어', 'enter': 'wipe', 'bg': 'ph_chestnut_ground', 'items': [
    BRIGHT,
    hook('“공주 밤이<br><strong>산에서 썩는다”</strong>', '썩어', y=300, size=150),
]},
{'from': '작년보다 사십 퍼센트', 'enter': 'flash', 'bg': 'th_scale_chestnut', 'items': [
    cover('+0.02'),
    tag('작년보다', '+0.05', None, 170, tone='dark', size=64),
    big('-40%', '사십', y=300, size=240, color='#ff5a5a'),
]},
{'from': '그런데 같은 달 국책연구원', 'enter': 'flash', 'bg': 'ph_report_desk', 'cam': [('crash', '오히려', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    flashhit('오히려'),
    tag('같은 달 국책연구원 조사', '+0.1', None, 170, icon='file-invoice', tone='dark', size=56),
    big('공주 수확 ↑', '오히려', y=330, size=170, color='#2ee66b'),
]},
{'from': '온라인의 공주 밤은', 'enter': 'zoom', 'bg': 'ph_phone_shopping', 'items': [
    BRIGHT,
    tag('온라인 공주 밤 1kg', '+0.1', 120, 140, icon='device-mobile', tone='dark', size=58),
    big('8,000원+', '팔천', y=520, size=170, color='#ffd400'),
]},
{'from': '값은 폭락했다는데', 'enter': 'strips', 'bg': 'ph_basket_few', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'),
    hook('산지는 폭락<br><strong>내 장바구니는 그대로?</strong>', '장바구니', y=280, size=120),
]},
{'from': '흔히들 일손 탓이라고', 'enter': 'wipe', 'bg': 'ph_empty_slope', 'items': [
    BRIGHT,
    tag('흔한 설명: 일손 부족', '일손', 120, 140, icon='users', tone='red', size=60),
    tag('틀린 말은 아니다', '틀린', 120, 300, tone='dark', size=56),
    glow('한 해 만에 꺾인 데는 다른 손이', '다른', y=640, size=66),
]},
{'from': '실마리는 엉뚱하게도', 'enter': 'zoom', 'bg': 'ph_container_port', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    BRIGHT,
    tag('실마리: 미국행 컨테이너', '컨테이너', 120, 140, icon='flag', tone='dark', size=58),
    foreshadow('공주 밤 20톤', '이십', label='이 컨테이너, 뒤에서 다시'),
]},
{'from': '그 저울은 공주에', 'enter': 'flash', 'bg': 'th_scale_chestnut', 'cam': [('crash', '산청군', 50, 50, 1.35)], 'items': [
    cover('+0.02'),
    stamp('공주 아님', '않았습니다', x=1150, y=200, size=110),
    flashhit('산청군'),
    tag('경남 산청군 농협 수매장', '산청군', None, 560, icon='map-pin', tone='red', size=66),
]},
{'from': '산청 농협은 특대 밤을', 'enter': 'strips', 'bg': 'ph_buying_station', 'items': [
    cover('+0.02'),
    card('산청 특대 1kg', '2,200원', '이천이백', 220, 220, w=660, h=300, vat='이천이백', hot=True),
    card('하동 특대 1kg', '3,800→2,200원', '삼천팔백', 1040, 220, w=680, h=300, vat='이천이백 원으로', hot=True),
]},
{'from': '가뭄과 폭염으로', 'enter': 'wipe', 'bg': 'ph_dry_burr', 'items': [
    BRIGHT,
    tag('가뭄·폭염 → 수확 감소 (남부)', '가뭄과', 120, 140, icon='alert-triangle', tone='dark', size=56),
    bubble('주워 봐야 일당도 안 나와요', '주워', 160, 560, size=50),
]},
{'from': '그럼 공주는 어땠을까요', 'enter': 'zoom', 'bg': 'ph_report_desk', 'items': [
    cover('+0.02'),
    tag('한국농촌경제연구원 밤 관측 (10월)', '한국농촌경제연구원', None, 150, icon='file-invoice', tone='dark', size=50),
    card('공주 이른 밤 수확', '+5.7%', '오 퍼센트', 220, 290, w=660, h=300, vat='오 퍼센트'),
    card('수확 포기 농가', '남부', '남부', 1040, 290, w=660, h=300, vat='남부', hot=True),
]},
# ================= 1막 =================
{'from': '지금 냉장고 야채 칸에', 'enter': 'zoom', 'bg': 'ph_fridge_chestnut', 'cam': [('push', '+0.1', 50, 55, 1.2)], 'items': [
    BRIGHT,
    tag('내 냉장고 속 밤 한 봉지, 어느 산에서?', '냉장고', 120, 140, icon='home', tone='dark', size=54),
]},
{'from': '열 톨 중 여섯 톨은', 'enter': 'flash', 'bg': 'ph_orchard_aerial', 'items': [
    cover('+0.02'),
    donut(63, '여섯', label='중부(충청 중심) 63%', x=300, y=230, d=420, tone='good'),
    card('공주 2024', '8,380톤', '팔천', 1040, 250, w=620, h=280, vat='팔천'),
    tag('전국 5톨 중 1톨+', '다섯', 1060, 590, icon='map-pin', tone='red', size=50),
]},
{'from': '밤은 논밭이 아니라', 'enter': 'wipe', 'bg': 'ph_chestnut_trees', 'cam': [('push', '+0.1', 50, 50, 1.15)], 'items': [
    BRIGHT,
    tag('밤은 산비탈에서', '산비탈', 120, 140, icon='map-pin', tone='dark', size=58),
    tag('한 번 심으면 수십 년', '수십', 120, 300, icon='clock', tone='dark', size=58),
    tag('값이 내려도 열매는 그대로', '덜', 120, 460, icon='alert-triangle', tone='red', size=58),
]},
{'from': '열린 밤은 사람이', 'enter': 'zoom', 'bg': 'ph_picking_bent', 'items': [
    BRIGHT,
    tag('하나하나 허리 굽혀 줍는다', '허리를', 120, 140, icon='users', tone='dark', size=58),
    foreshadow('2025 가을, 밤 풍년', '작년'),
]},
# ================= 2막 =================
{'from': '이 구조를 머리에 두고', 'enter': 'flash', 'bg': 'ph_orchard_aerial', 'cam': [('pull', '+0.05', 50, 50, 1.6)], 'items': [
    cover('+0.02'),
    hook('그 많던 밤은<br><strong>어디로 갔을까</strong>', '그 많던', y=300, size=130),
]},
{'from': '천구백구십오 년, 전국', 'enter': 'strips', 'bg': 'ph_orchard_aerial', 'items': [
    cover('+0.02'),
    tag('전국 밤 생산', '+0.1', None, 150, icon='chart-bar', tone='dark', size=58),
    bars([('1995년', 1.0, '93,654톤', '구만', False), ('2024년', 37010 / 93654, '37,010톤', '삼만', True)], top=290),
]},
{'from': '그 시절 밤은 산에만', 'enter': 'zoom', 'bg': 'ph_old_cargo_ship', 'items': [
    PAST, cover('+0.02'),
    tag('1995년 밤 수출', '+0.1', None, 150, icon='flag', tone='dark', size=58),
    big('29,000톤', '이만', y=290, size=200, color='#ffd400'),
    tag('3톨 중 1톨이 바다 건너로', '세 톨', None, 600, icon='flag', tone='red', size=60),
]},
{'from': '지금도 한국 밤의 주요', 'enter': 'wipe', 'bg': 'ph_japan_market', 'items': [
    BRIGHT,
    tag('주요 수출 시장 = 일본', '일본입니다', 120, 140, icon='flag', tone='dark', size=60),
    tag('일본 밤은 줄고 → 한국에서 사 갔다', '모자란', 120, 300, icon='trending-down', tone='dark', size=54),
]},
{'from': '그런데 그 큰 손님', 'enter': 'flash', 'bg': 'ph_cargo_empty', 'cam': [('crash', '천 톤도', 50, 50, 1.35)], 'items': [
    BRIGHT,
    flashhit('천 톤도'),
    tag('그 큰 손님, 지금은?', '큰 손님', None, 150, icon='flag', tone='dark', size=60),
    swapnum('29,000톤', '1,000톤 ↓', '이만 구천 톤이', '아래로', y=300, size=140, tone='bad'),
    tag('이 숫자, 뒤에서 따라갑니다', '조금 뒤에', None, 620, icon='key', tone='red', size=56),
]},
{'from': '산 아래 풍경도', 'enter': 'wipe', 'bg': 'ph_village_women_past', 'items': [
    PAST,
    tag('가을이면 밤 줍는 아낙들', '아낙들', 120, 140, icon='users', tone='dark', size=58),
    shrink('ph_roasted_vendor', '군밤', 1150, 170, 660, 372, cap='신문지 봉투의 군밤'),
]},
{'from': '그리고 제삿날 전날', 'enter': 'zoom', 'bg': 'ph_peeling_hands', 'cam': [('push', '+0.1', 50, 55, 1.25)], 'items': [
    PAST,
    tag('제삿날 전날 밤, “밤을 친다”', '친다고들', 120, 140, icon='heart-handshake', tone='red', size=58),
]},
{'from': '대추, 곶감과 함께', 'enter': 'strips', 'bg': 'ph_ancestral_table', 'items': [
    BRIGHT,
    tag('상 앞줄 = 빠지면 안 되는 자리', '앞줄에', 120, 140, icon='home', tone='dark', size=58),
    glow('먹고 싶어서가 아니라, 꼭 올려야 해서', '올려야', y=640, size=62),
]},
{'from': '그 시절 밤 농사는', 'enter': 'wipe', 'bg': 'ph_orchard_aerial', 'items': [
    PAST, cover('+0.02'),
    tag('2008년 전업 밤 농가 평균', '이천팔', None, 150, icon='chart-bar', tone='dark', size=56),
    big('5ha+', '오 헥타르', y=290, size=200, color='#ffd400'),
    tag('축구장 7개가 넘는 산비탈', '축구장', None, 560, icon='map-pin', tone='dark', size=56),
    glow('자식 등록금이 나온 산', '등록금', y=700, size=58),
]},
{'from': '공주는 그 중심에', 'enter': 'zoom', 'bg': 'ph_gongju_town', 'items': [
    cover('+0.02'),
    *stack([('2006 정안밤 지리적표시 4호', '정안', 'flag', 'dark'), ('2010 공주 알밤 특구', '이천십', 'map-pin', 'dark'),
            ('2016 차례 지낼 집 74.4%', '이천십육', 'users', 'red')], x=200, y=200, gap=170, size=56),
    foreshadow('차례 74.4% (2016)', '기억해'),
]},
{'from': '그런데 정점에서 이미', 'enter': 'flash', 'bg': 'ph_cargo_empty', 'items': [
    BRIGHT,
    tag('정점에서 시작된 균열', '+0.05', None, 150, icon='trending-down', tone='dark', size=58),
    bars([('1995년 수출', 1.0, '28,860톤', '이만', False), ('2000년 수출', 15615 / 28860, '15,615톤', '만 오천', True)], top=290),
    tag('배가 반쯤 빈 채로', '반쯤', None, 640, icon='alert-triangle', tone='red', size=58),
]},
{'from': '그래도 산 아래에선', 'enter': 'wipe', 'bg': 'ph_ancestral_table', 'items': [
    BRIGHT,
    tag('그래도 차례상이 남은 밤을 받아 줬다', '차례상이', 120, 140, icon='home', tone='dark', size=54),
]},
{'from': '남부의 밤 산에서는', 'enter': 'zoom', 'bg': 'ph_old_tree', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'),
    tag('늙은 나무 · 베어 낸 자리', '늙은', None, 170, icon='trending-down', tone='dark', size=58),
    hook('생산이 줄었는데<br><strong>값은 왜 내렸나?</strong>', '이상하지', y=330, size=120),
]},
]
