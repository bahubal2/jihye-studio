"""공주밤 편 — 4막 원인 C · 5막 · 결말 (자막 179~288, 12:43~20:59). 담당자 규칙: 뒤쪽은 돈을 쓰지 않는다 → 그림 재사용, 장면 단순."""
from gen import (hook, tag, big, cover, glow, raw, stack, card, bars, split, side)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

C = [
{'from': '셋째, 가장 큰 이유입니다', 'enter': 'flash', 'bg': 'ph_basket_few', 'items': [
    cover('+0.02'),
    hook('셋째<br><strong>가장 큰 이유</strong>', '+0.05', y=280, size=140),
]},
{'from': '한국농촌경제연구원이 올 추석', 'enter': 'zoom', 'bg': 'ph_simple_table', 'items': [
    cover('+0.02'),
    tag('추석 차례 지낼 집 (KREI 조사)', '천 가구에', None, 140, icon='users', tone='dark', size=52),
    bars([('2016년', 1.0, '74.4%', '이천십육', False), ('2025년', 40.4 / 74.4, '40.4%', '작년만', False), ('2026년', 27.3 / 74.4, '27.3%', '이십칠', True)], top=250),
]},
{'from': '다른 조사도 같은 방향', 'enter': 'wipe', 'bg': 'ph_simple_table', 'items': [
    BRIGHT,
    tag('한국리서치 2026 설: 차례·제사 35%', '한국리서치', 120, 140, icon='file-invoice', tone='dark', size=52),
    tag('상을 차려도 절반은 간소하게', '간소하게', 120, 300, icon='home', tone='dark', size=54),
    glow('손이 많이 가는 밤 접시가 먼저 빠진다', '손이 많이', y=640, size=60),
]},
{'from': '세대 차이는 더 큽니다', 'enter': 'zoom', 'bg': 'ph_ancestral_table', 'items': [
    cover('+0.02'),
    card('70세 이상 “차례 필요”', '54%', '일흔', 260, 240, w=640, h=300, vat='일흔'),
    card('30대 이하', '약 1/3', '삼십 대', 1020, 240, w=640, h=300, vat='삼십 대', hot=True),
    glow('하나하나는 효도, 모이니 밤 산의 손님이 줄었다', '효도인데', y=640, size=56),
]},
{'from': '그럼 사람들은 밤을 아예', 'enter': 'wipe', 'bg': 'ph_peeled_pack', 'items': [
    BRIGHT,
    tag('먹는 방식이 바뀌었다: 깐 밤', '먹는 방식', 120, 140, icon='building-store', tone='dark', size=58),
    tag('그 자리는 수입 밤이 먼저', '수입 밤이 먼저', 120, 300, icon='flag', tone='red', size=58),
]},
{'from': '정리하겠습니다', 'enter': 'flash', 'bg': 'ph_storage_sacks', 'items': [
    cover('+0.02'),
    *stack([('올해: 작년 재고', '창고였습니다', 'home', 'red'), ('30년: 차례상·일본 손님 감소', '두 손님', 'users', 'red'),
            ('일손: 남부의 포기를 앞당김', '일손 부족은', 'user-x', 'dark')], x=300, y=220, gap=170, size=58),
]},
# ================= 5막 =================
{'from': '그런데 같은 조건에서', 'enter': 'zoom', 'bg': 'ph_loading_container', 'items': [
    cover('+0.02'),
    hook('그런데<br><strong>버틴 곳</strong>', '버틴', y=300, size=140),
]},
{'from': '시월 삼십 일, 공주', 'enter': 'flash', 'bg': 'ph_loading_container', 'items': [
    BRIGHT,
    tag('10.30 사곡농협 알밤 20톤 → 미국', '사곡농협', 120, 140, icon='flag', tone='dark', size=54),
    tag('처음 그 컨테이너', '처음에', 120, 300, icon='key', tone='red', size=58),
]},
{'from': '공주시는 현지 수입상을', 'enter': 'zoom', 'bg': 'ph_us_grocery', 'items': [
    cover('+0.02'),
    tag('공주 밤 미국 수출', '+0.1', None, 150, icon='flag', tone='dark', size=58),
    bars([('2025년', 25 / 44, '25톤', '이십오', False), ('2026년 전망', 1.0, '44톤 (+77%)', '사십사', True)], top=290),
]},
{'from': '시작은 작았습니다', 'enter': 'wipe', 'bg': 'ph_roast_festival', 'items': [
    BRIGHT,
    tag('미국 군밤축제와 함께 길을 텄다', '군밤 축제', 120, 140, icon='heart-handshake', tone='dark', size=56),
    glow('손님 앞으로 밤을 들고 갔다', '손님 앞으로', y=620, size=66),
]},
{'from': '남부와 비교하면', 'enter': 'zoom', 'bg': 'ph_orchard_aerial', 'items': [
    cover('+0.02'),
    card('경남 (연평균)', '-7%', '칠 퍼센트', 140, 240, w=520, h=280, vat='칠 퍼센트', hot=True),
    card('전남 (연평균)', '-11%', '십일', 700, 240, w=520, h=280, vat='십일', hot=True),
    card('충남 (연평균)', '+2.2%', '이 퍼센트', 1260, 240, w=520, h=280, vat='이 퍼센트'),
]},
{'from': '농가 한 집의 크기도', 'enter': 'flash', 'bg': 'ph_orchard_aerial', 'items': [
    cover('+0.02'),
    card('공주 농가당', '16.5톤', '십육', 260, 240, w=640, h=300, vat='십육'),
    card('남부 농가당', '1.5톤', '일 점', 1020, 240, w=640, h=300, vat='일 점', hot=True),
    tag('10배 · 수매량 정안 +10% / 산청 -30%', '열 배', None, 610, icon='chart-bar', tone='dark', size=48),
]},
{'from': '공주가 버틴 이유는', 'enter': 'wipe', 'bg': 'ph_gongju_town', 'items': [
    BRIGHT,
    tag('공주알밤 4년 연속 대표 브랜드 대상', '대표', 120, 140, icon='flag', tone='dark', size=54),
    tag('밤 수집기·수확 인력 지원', '수집기', 120, 300, icon='users', tone='dark', size=56),
]},
{'from': '그렇다고 공주 농가가', 'enter': 'zoom', 'bg': 'ph_farmers_rally', 'items': [
    BRIGHT,
    tag('9.23 사곡농협 수매장 앞 집회', '이십삼일', 120, 140, icon='calendar', tone='red', size=56),
    tag('수매가 인상 · 농민 목소리를', '수매가를', 120, 300, icon='users', tone='dark', size=56),
]},
{'from': '공정하게 짚을 것도', 'enter': 'wipe', 'bg': 'ph_us_grocery', 'items': [
    cover('+0.02'),
    tag('2022 부여 > 공주 · 2024 공주 재역전', '부여가', None, 170, icon='chart-bar', tone='dark', size=50),
    big('44톤 = 0.5%', '사십사', y=330, size=150, color='#ff5a5a'),
    tag('백 톨 중 반 톨', '반 톨', None, 620, icon='alert-triangle', tone='red', size=58),
]},
{'from': '고향 산에 아버님이', 'enter': 'wipe', 'bg': 'ph_hometown_mountain', 'items': [
    BRIGHT,
    glow('산의 값은 누가 사 주느냐에 달렸다', '누가 새로', y=620, size=62),
]},
# ================= 결말 =================
{'from': '이제 처음 그 저울', 'enter': 'flash', 'bg': 'th_scale_chestnut', 'items': [
    cover('+0.02'),
    big('2,200원', '이천이백', y=200, size=180, color='#ff5a5a'),
    tag('= 공주가 아니라 경남 수매장', '경남의', None, 500, icon='map-pin', tone='red', size=60),
    tag('“썩는다”는 말은 절반만 맞다', '절반만', None, 660, icon='scale', tone='dark', size=54),
]},
{'from': '처음 질문에 답하겠습니다', 'enter': 'zoom', 'bg': 'ph_chestnut_ground', 'items': [
    cover('+0.02'),
    *stack([('① 올해 값: 작년 재고', '첫째,', 'home', 'red'), ('② 30년: 차례상·일본 손님', '둘째,', 'users', 'red'),
            ('③ 일손·중국산: 일부 사실', '셋째,', 'scan', 'dark')], x=300, y=220, gap=170, size=58),
]},
{'from': '장바구니 앞에서 화가', 'enter': 'wipe', 'bg': 'ph_basket_few', 'items': [
    BRIGHT,
    glow('내 돈의 절반은 길 위에서, 내릴 땐 깃털처럼', '절반 가까이가', y=620, size=54),
]},
{'from': '밤이 썩은 게 아니라', 'enter': 'flash', 'bg': 'ph_ancestral_table', 'items': [
    cover('+0.02'),
    hook('밤이 썩은 게 아니라<br><strong>사 줄 상이 사라졌다</strong>', '+0.05', y=300, size=110),
]},
{'from': '이번에는 우리 손에', 'enter': 'wipe', 'bg': 'ph_label_check', 'items': [
    cover('+0.02'),
    *stack([('① 포장의 수확 연도', '첫째,', 'calendar', ''), ('② 1kg당 값으로 비교 (KAMIS)', '둘째,', 'scan', ''),
            ('③ 깐 밤·군밤 원산지', '셋째,', 'flag', '')], x=300, y=220, gap=170, size=58),
]},
{'from': '이 이야기는 밤에서', 'enter': 'zoom', 'bg': 'ph_ancestral_table', 'items': [
    BRIGHT,
    glow('상이 바뀌면 산이 바뀐다', '상이 바뀌면', y=620, size=74),
]},
{'from': '구월 말 그 저울 위에는', 'enter': 'flash', 'bg': 'th_scale_chestnut', 'items': [
    BRIGHT,
    tag('다시, 그 저울 앞', '+0.1', 120, 140, icon='map-pin', tone='dark', size=60),
]},
{'from': '여러분은 올 추석', 'enter': 'zoom', 'bg': 'ph_simple_table', 'items': [
    cover('+0.02'),
    *split('올렸다면', vs=True),
    side('l', '올렸다면', tag('1번', '올렸다면', 0, 0, tone='red', size=80), tag('밤 올렸다', '올렸다면', 0, 0, size=54)),
    side('r', '뺐다면', tag('2번', '뺐다면', 0, 0, tone='green', size=80), tag('이번엔 뺐다', '뺐다면', 0, 0, size=54)),
]},
{'from': '다음 이야기도 골라', 'enter': 'wipe', 'bg': 'ph_wholesale_market', 'items': [
    cover('+0.02'),
    *stack([('1번 한우: 산지 소값 vs 식당 고깃값', '일 번', 'chart-bar', ''), ('2번 양파: 소비자값 70%가 유통비', '이 번', 'chart-bar', ''),
            ('3번 차례상의 다음 차례, 곶감', '삼 번', 'home', '')], x=160, y=220, gap=170, size=50),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'flash', 'bg': 'ph_chestnut_trees', 'items': [
    BRIGHT,
    hook('지혜호수<br><strong>경제연구소</strong>', '지혜호수', y=260, size=150, sfx='ding'),
    tag('숫자로 확인하고 사실로 말합니다', '+0.3', None, 620, tone='dark', size=56),
]},
]
