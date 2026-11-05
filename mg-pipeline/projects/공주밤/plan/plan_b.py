"""공주밤 편 — 3막(흔한 설명 확인) · 4막 원인 A·B (자막 79~178, 5:32~12:43)."""
from gen import (hook, flashhit, tag, stamp, big, cover, punch, glow, raw, stack, swapnum, card, article, bubble, donut, bars, flipcard)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

B = [
# ================= 3막 =================
{'from': '여기까지 확인한 건', 'enter': 'wipe', 'bg': 'ph_report_desk', 'items': [
    cover('+0.02'),
    *stack([('① 밤은 30년 동안 줄었다', '삼십 년', 'trending-down', 'dark'), ('이제 흔한 설명을 하나씩', '흔히', 'scan', 'red')], x=380, y=260, gap=180, size=60),
]},
{'from': '먼저 날씨입니다', 'enter': 'flash', 'bg': 'ph_dry_burr', 'cam': [('crash', '흉작이면', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    flipcard('날씨 때문?', '흉작이면 값은 올라야', '날씨 때문이구나', '흉작이면', y=300, size=80),
]},
{'from': '숫자를 보겠습니다', 'enter': 'zoom', 'bg': 'ph_wholesale_market', 'items': [
    cover('+0.02'),
    tag('9월 가락시장 밤 도매가 (상품 1kg)', '구월 서울', None, 150, icon='chart-bar', tone='dark', size=50),
    swapnum('6,105원', '5,061원', '구월 서울', '십칠', y=300, size=130, tone='bad'),
    tag('-17% · 추석 대목에도', '추석 대목', None, 600, icon='trending-down', tone='red', size=58),
]},
{'from': '날씨가 밤을 귀하게', 'enter': 'wipe', 'bg': 'ph_chestnut_trees', 'items': [
    BRIGHT,
    tag('공주는 수확이 늘었다', '공주는', 120, 140, icon='trending-up', tone='green', size=58),
    glow('날씨는 범인이 아니었다', '남부 농가', y=620, size=70),
]},
{'from': '두 번째 설명은 중국산', 'enter': 'flash', 'bg': 'ph_import_warehouse', 'items': [
    cover('+0.02'),
    tag('두 번째: 중국산 (일부 사실)', '중국산입니다', None, 150, icon='flag', tone='red', size=58),
    card('수입 1~9월 (생밤 환산)', '10,016톤', '만 톤', 220, 280, w=660, h=300, vat='만 톤을'),
    card('작년보다', '+11.7%', '십이', 1040, 280, w=640, h=300, vat='십이', hot=True),
    tag('저관세 의무 물량 2,170톤', '이천백칠십', None, 650, icon='file-invoice', tone='dark', size=52),
]},
{'from': '그런데 그 수입 밤의 얼굴', 'enter': 'zoom', 'bg': 'ph_frozen_peeled', 'items': [
    cover('+0.02'),
    donut(77, '여덟', label='냉동·조제 밤 = 공장으로', x=760, y=200, d=420, tone='bad'),
    tag('주원인 단정 어렵다 (밤 업계 신문)', '업계', None, 690, icon='file-invoice', tone='dark', size=50),
]},
{'from': '다만 중국산은 다른 곳에서', 'enter': 'wipe', 'bg': 'ph_japan_market', 'items': [
    BRIGHT,
    glow('중국산은 다른 곳에서 우리 밤을 밀어냈다', '밀어내고', y=600, size=60),
]},
{'from': '세 번째는 시장에서', 'enter': 'flash', 'bg': 'ph_basket_few', 'items': [
    BRIGHT,
    tag('세 번째: 중간에서 다 떼먹는다?', '떼먹는다는', 120, 140, icon='alert-triangle', tone='red', size=56),
    bubble('버린다면서, 내가 살 땐 왜 이렇게 비싸?', '버린다면서', 160, 520, size=50),
]},
{'from': '계산해 보겠습니다', 'enter': 'strips', 'bg': 'ph_wholesale_market', 'cam': [('push', '+0.1', 50, 50, 1.15)], 'items': [
    cover('+0.02'),
    bars([('산지 (산청 특대)', 2200 / 8350, '2,200원', '산청', True), ('도매 (가락)', 5061 / 8350, '5,061원', '오천', False),
          ('온라인 소매', 1.0, '8,000원+', '팔천', False)], top=220),
    tag('서너 배', '서너', None, 690, icon='trending-up', tone='red', size=64),
]},
{'from': '농산물 전체로 보면', 'enter': 'zoom', 'bg': 'ph_money_table', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'),
    tag('소비자 1,000원 → 농가', '천 원을', None, 150, icon='coin', tone='dark', size=58),
    big('508원', '오백팔', y=300, size=230, color='#ffd400'),
    glow('절반 가까이는 길 위에서', '길 위에서', y=640, size=66),
]},
{'from': '최근 밤 한 봉지를', 'enter': 'wipe', 'bg': 'ph_phone_shopping', 'items': [
    BRIGHT,
    tag('최근 밤 한 봉지, 얼마에 사셨나요?', '얼마에', 120, 140, icon='mail', tone='red', size=56),
    tag('댓글로 동네 시세를 남겨 주세요', '댓글로', 120, 300, icon='users', tone='dark', size=54),
]},
{'from': '공정하게 반대쪽 사정도', 'enter': 'zoom', 'bg': 'ph_sorting_packing', 'items': [
    BRIGHT,
    tag('반대쪽 사정', '공정하게', 120, 140, icon='scale', tone='dark', size=58),
    tag('선별·세척·저장·택배 + 썩는 밤', '골라내고', 120, 300, icon='home', tone='dark', size=54),
    tag('모두 폭리는 아니다', '폭리로', 120, 460, icon='alert-triangle', tone='green', size=56),
]},
{'from': '다만 이상한 점은 남습니다', 'enter': 'flash', 'bg': 'ph_money_table', 'items': [
    cover('+0.02'),
    tag('로켓과 깃털', '로켓과', None, 170, icon='trending-up', tone='red', size=72),
    tag('오를 땐 로켓처럼', '로켓처럼', 220, 400, tone='red', size=60),
    tag('내릴 땐 깃털처럼', '깃털처럼', 1020, 400, tone='green', size=60),
    tag('한국은행: 농가값·소비자값 격차 확대', '한국은행', None, 620, icon='file-invoice', tone='dark', size=48),
]},
{'from': '자, 이제 남은 설명은', 'enter': 'wipe', 'bg': 'ph_drone_spray', 'items': [
    BRIGHT,
    tag('네 번째: 일손 (일부 사실)', '일손 하나', 120, 140, icon='users', tone='dark', size=58),
    tag('일당 + 드론 방제 + 풀베기 = 계산 안 맞음', '드론', 120, 300, icon='coin', tone='red', size=50),
]},
{'from': '그런데 일손은 작년에도', 'enter': 'zoom', 'bg': 'ph_empty_slope', 'cam': [('crash', '작년 가을에서', 50, 50, 1.35)], 'items': [
    cover('+0.02'),
    hook('한 번에 40%를<br><strong>꺾은 힘은?</strong>', '그렇다면', y=180, size=120),
    punch('작년 가을', '작년 가을에서', y=560, size=150),
]},
# ================= 4막: 원인 A 창고 =================
{'from': '원인은 셋입니다', 'enter': 'flash', 'bg': 'ph_storage_sacks', 'items': [
    cover('+0.02'),
    *stack([('① 창고 (작년 재고)', '첫째,', 'home', 'red'), ('② 떠난 바다 건너 손님', '바다', 'flag', 'red'),
            ('③ 사라진 차례상', '셋째,', 'users', 'red')], x=440, y=220, gap=170, size=64),
]},
{'from': '첫째, 창고입니다', 'enter': 'zoom', 'bg': 'ph_storage_sacks', 'items': [
    cover('+0.02'),
    tag('기억해 두신 장면: 작년 가을 풍년', '앞에서', None, 150, icon='key', tone='dark', size=52),
    card('2025 밤 생산', '+5.9%', '육 퍼센트', 220, 290, w=660, h=300, vat='육 퍼센트'),
    card('2025 생산량', '약 39,000톤', '삼만', 1040, 290, w=660, h=300, vat='삼만'),
]},
{'from': '이상한 건 이 결과가', 'enter': 'wipe', 'bg': 'ph_report_desk', 'items': [
    cover('+0.02'),
    article('한국농촌경제연구원 (요약)', '2025.12', '밤 생산 증가… 이후 가격 하락 전망', '작년 십이월', mark='하락', x=460, y=150, rot=-2, until='올봄'),
    card('나무 늘린 농가', '4.8%', '늘렸다는', 260, 300, w=640, h=300, vat='늘렸다는'),
    card('줄인 농가', '1.9%', '줄였다는', 1020, 300, w=640, h=300, vat='줄였다는', hot=True),
]},
{'from': '팔리지 못한 작년 밤이', 'enter': 'zoom', 'bg': 'ph_storage_sacks', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'),
    tag('작년 재고 위에 올해 햇밤', '햇밤이', None, 170, icon='home', tone='dark', size=58),
    tag('연구원·농협: 전년산 재고 증가', '재고 증가', None, 330, icon='file-invoice', tone='red', size=56),
    tag('하동 농협: 416톤 · kg당 약 2,000원', '사백십육', None, 600, icon='coin', tone='dark', size=50),
]},
{'from': '밤처럼 꼭 필요한 만큼만', 'enter': 'wipe', 'bg': 'ph_kimchi_fridge', 'items': [
    BRIGHT,
    tag('작년 풍년이 올해 값을 눌렀다', '누른', 120, 140, icon='trending-down', tone='red', size=58),
    tag('우리 집 김치냉장고 = 시장의 창고', '김치냉장고', 120, 300, icon='home', tone='dark', size=54),
    tag('재고는 공개돼야 (밤 업계 신문)', '공개돼야', 120, 460, icon='file-invoice', tone='dark', size=52),
]},
# ================= 4막: 원인 B 바다 건너 손님 =================
{'from': '둘째, 바다 건너 손님', 'enter': 'flash', 'bg': 'ph_cargo_empty', 'items': [
    BRIGHT,
    card('수입 1~9월', '+11.7%', '십이 퍼센트', 220, 240, w=660, h=300, vat='십이 퍼센트'),
    card('수출 1~9월', '921톤', '구백이십일', 1040, 240, w=660, h=300, vat='구백이십일', hot=True),
    tag('평년의 절반도 안 됨', '절반에도', None, 610, icon='trending-down', tone='red', size=60),
]},
{'from': '앞에서 잠깐 보여 드린', 'enter': 'zoom', 'bg': 'ph_old_cargo_ship', 'cam': [('crash', '이만', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    swapnum('29,000톤', '1,000톤 ↓', '이만', '아래로', y=280, size=140, tone='bad'),
    tag('3톨 중 1톨 사 가던 손님이 떠났다', '세 톨', None, 600, icon='flag', tone='red', size=56),
]},
{'from': '연구원은 일본의 경기', 'enter': 'wipe', 'bg': 'ph_japan_market', 'items': [
    cover('+0.02'),
    *stack([('일본 경기 둔화 · 수요 감소', '경기', 'trending-down', 'dark'), ('중국산 경쟁력 ↑ (일본 시장)', '중국산', 'flag', 'red'),
            ('2024 가을 수출 물류비 지원 중단', '물류비', 'alert-triangle', 'red')], x=200, y=200, gap=170, size=54),
]},
{'from': '바다를 건너지 못한 밤은', 'enter': 'zoom', 'bg': 'ph_storage_sacks', 'items': [
    cover('+0.02'),
    glow('들어오는 밤 ↑ · 나가는 밤 ↓ → 산지값 ↓', '틈이', y=340, size=60),
]},
]
