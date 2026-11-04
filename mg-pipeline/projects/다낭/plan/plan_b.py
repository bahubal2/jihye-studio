"""다낭 편 — 3막(흔한 설명 확인) · 4막 앞부분(가격·환율) (자막 76~158, 5:16~11:54). 아직 앞쪽: 카메라·긋기·카드 유지."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, punch, glow, raw, stack, swapnum, card, article, bubble, donut, bars,
                 shrink, arrow, circ, uline, flipcard)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

B = [
# ================= 3막 흔한 설명 확인 =================
{'from': '여기까지 확인한 것을', 'enter': 'wipe', 'bg': 'ph_report_documents', 'items': [
    cover('+0.02'),
    *stack([('① 다낭은 한국인이 키웠다', '키웠고', 'flag', 'dark'), ('② 비중은 정점에서 흔들렸다', '흔들리고', 'trending-down', 'dark'),
            ('이제 흔한 설명을 하나씩 확인', '이유들을', 'scan', 'red')], x=380, y=230, gap=170, size=58),
]},
{'from': '이천이십사 년 십이월, 무안공항', 'enter': 'fade', 'bg': 'ph_memorial_quiet', 'items': [
    tag('2024.12 무안공항 제주항공 참사', '+0.2', 120, 140, icon='calendar', tone='dark', size=56),
    tag('179명 희생', '백칠십구', 120, 300, tone='dark', size=58),
]},
{'from': '그 뒤 한국발 항공편', 'bg': 'ph_canceled_board', 'items': [
    BRIGHT,
    tag('한국발 취소 · 여행 연기', '취소와', 120, 140, icon='alert-triangle', tone='red', size=58),
    tag('2025.1 다낭시: 한국인 감소 공식 확인', '공식적으로', 120, 300, icon='file-invoice', tone='dark', size=52),
    tag('하필 성수기 12~4월', '성수기', 120, 460, icon='calendar', tone='dark', size=56),
]},
{'from': '역시 그 사고 때문이구나', 'enter': 'zoom', 'bg': 'ph_canceled_board', 'items': [
    cover('+0.02'),
    flipcard('참사 때문에 끝났다', '절반만 맞다', '역시', '절반은', y=280, size=80),
    glow('그 충격이 오래갔다면?', '오래갔다면', y=620, size=70),
]},
{'from': '이천이십오 년 팔월 일일, 다낭시는', 'enter': 'flash', 'bg': 'ph_ceremony_stage', 'cam': [('push', '+0.1', 50, 45, 1.2)], 'items': [
    BRIGHT,
    tag('7개월 만에 100만 번째 한국인', '일곱', 120, 140, icon='users', tone='green', size=60),
    tag('베트남항공 왕복 항공권 2장', '항공권', 120, 300, icon='flag', tone='dark', size=56),
    glow('반년 남짓 만에 회복', '반년', y=640, size=74),
]},
{'from': '두 번째로 흔한 설명은', 'enter': 'zoom', 'bg': 'th_beach_full', 'cam': [('crash', '아닙니다', 50, 55, 1.35)], 'items': [
    cover('+0.02'),
    tag('사람이 줄었다?', '줄었다', None, 230, icon='user-x', size=80, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=500, size=170),
]},
{'from': '이천이십오 년 다낭의 외국인 손님은', 'enter': 'strips', 'bg': 'ph_tourists_mixed', 'items': [
    cover('+0.02'),
    card('2025 외국인 손님', '+25%', '+0.1', 260, 220, w=640, h=300, vat='이십오 퍼센트:이십오', hot=False),
    card('2026 1~5월 숙박객', '+20%↑', '일월부터', 1020, 220, w=640, h=300, vat='이십 퍼센트'),
    glow('쇠락이 아니라 호황', '호황입니다', y=640, size=80),
]},
{'from': '세 번째 설명은', 'enter': 'wipe', 'bg': 'ph_nhatrang_beach', 'cam': [('pull', '+0.05', 50, 50, 1.8)], 'items': [
    cover('+0.02'),
    tag('한국인이 나트랑으로?', '나트랑으로', 600, 140, icon='map-pin', tone='red', size=62),
    bars([('카인호아(나트랑) 2024', 1.0, '240만 명+', '이백사십만', False), ('다낭 2024', 168 / 240, '168만 명', '다낭보다', True)], top=300),
    tag('2025 여름 검색: 나트랑 > 도쿄', '도쿄를', None, 660, icon='scan', tone='dark', size=48),
]},
{'from': '그런데 이 설명에는', 'enter': 'zoom', 'bg': 'ph_vietnam_coast_map', 'cam': [('push', '+0.1', 50, 50, 1.3)], 'items': [
    BRIGHT,
    tag('구멍: 다낭 한국인은 줄지 않았다', '구멍이', 120, 140, icon='alert-triangle', tone='red', size=56),
    glow('나트랑은 판을 넓혔다', '넓힌', y=620, size=80),
]},
{'from': '마지막은 처음에 꺼낸', 'enter': 'flash', 'bg': 'ph_fake_goods', 'items': [
    cover('+0.02'),
    tag('2025 상반기 다낭시 단속', '상반기', 640, 150, icon='scan', tone='dark', size=58),
    card('점검', '', '삼백구십', 260, 290, w=640, h=280, num=390, suffix='건', vat='삼백구십'),
    card('위반 적발', '', '이백사십구', 1020, 290, w=640, h=280, num=249, suffix='건', vat='이백사십구', hot=True),
    tag('대부분 가짜 상품', '가짜', 700, 650, icon='alert-triangle', tone='red', size=56),
]},
{'from': '택시도 마찬가지입니다', 'enter': 'zoom', 'bg': 'ph_airport_taxi_night', 'items': [
    cover('+0.02'),
    article('VnExpress (요약)', '2018', '다낭 택시 기사, 한국인 승객 요금 부풀려 해고', '+0.2', mark='해고', x=460, y=190, rot=-2, until='이천이십삼'),
    article('VnExpress (요약)', '2023', '무면허 운전자, 한국인 관광객 바가지로 벌금 1,100만 동', '이천이십삼', mark='벌금', x=460, y=190, rot=2),
]},
{'from': '여행 커뮤니티에도 택시', 'enter': 'wipe', 'bg': 'ph_taxi_meter_night', 'items': [
    cover('+0.02'),
    tag('다낭 이미지는 깎였다', '이미지를', 640, 160, icon='trending-down', tone='red', size=62),
    hook('바가지는<br><strong>그때도 있었다</strong>', '그때도', y=330, size=150),
    tag('2018 = 한국인이 가장 몰려가던 해', '몰려가던', 460, 680, icon='calendar', tone='dark', size=54),
]},
{'from': '공정하게 하나 더', 'enter': 'zoom', 'bg': 'ph_seoul_taxi_airport', 'items': [
    BRIGHT,
    tag('서울도 2025 상반기 공항 택시 부당요금 139건', '백삼십구', 120, 140, icon='alert-triangle', tone='dark', size=50),
    glow('줄어든 건 한국인 비중뿐', '비중뿐', y=620, size=80),
]},
{'from': '그렇다면 남은 질문은', 'enter': 'flash', 'bg': 'th_hanmarket_street', 'items': [
    cover('+0.02'),
    hook('도시는 커졌는데<br><strong>왜 한국인이 안 보일까</strong>', '느낄까요', y=300, size=120),
]},
# ================= 4막 앞부분: 가격 · 환율 =================
{'from': '첫째는 가격', 'enter': 'zoom', 'bg': 'ph_hotel_room_luxury', 'items': [
    cover('+0.02'),
    *stack([('① 가격', '가격,', 'coin', 'red'), ('② 환율', '환율,', 'currency-won', 'red'), ('③ 비중의 정체', '비중의', 'chart-bar', 'red')], x=640, y=230, gap=160, size=70),
]},
{'from': '다낭 호텔 방값은', 'enter': 'strips', 'bg': 'ph_hotel_room_luxury', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'),
    card('4·5성 객실가 (2026 1분기)', '+10%', '십 퍼센트', 220, 250, w=660, h=300, vat='십 퍼센트', hot=True),
    donut(85, '팔십오', label='객실 점유율 85%+', x=1140, y=210, d=420, tone='bad'),
]},
{'from': '그 방은 누가 채웠을까요', 'enter': 'flash', 'bg': 'ph_russian_family_checkin', 'items': [
    BRIGHT,
    tag('러시아인 다낭 숙소 예약 (얀덱스, 상반기)', '얀덱스', 120, 140, icon='users', tone='dark', size=50),
    big('+155%', '백오십오', y=420, size=230, color='#2ee66b'),
]},
{'from': '온라인에서는 호텔비가', 'enter': 'zoom', 'bg': 'ph_phone_compare', 'items': [
    cover('+0.02'),
    swapnum('소문 30%', '확인 10%', '삼십', '십 퍼센트입니다', y=280, size=120, tone='bad'),
    glow('그 10%가 다른 곳을 검색하게 만든다', '검색해', y=620, size=68),
]},
{'from': '둘째, 환율입니다', 'enter': 'flash', 'bg': 'ph_yen_exchange', 'cam': [('crash', '팔백이십육', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    tag('기억해 두신 숫자: 2025 945만 명', '앞에서', 470, 150, icon='key', tone='dark', size=54),
    roll(0, 826, '팔백이십육', y=290, size=210, suffix='만 명', tone='good', dur=0.8),
    tag('2026 1~9월 방일 한국인 · 역대 최다 · +20%↑', '이십 퍼센트', None, 630, icon='trending-up', tone='green', size=46),
]},
{'from': '같은 아홉 달 동안 베트남은', 'enter': 'wipe', 'bg': 'ph_flight_board', 'items': [
    cover('+0.02'),
    tag('같은 기간 베트남을 찾은 한국인', '+0.1', 560, 150, icon='users', tone='dark', size=56),
    bars([('2025 1~9월', 1.0, '약 320만 명', '삼백이십만', True), ('2026 1~9월', 300 / 320, '약 300만 명', '삼백만', False)], top=290),
    tag('상위 10개국 중 한국만 감소 (대만 언론)', '하나뿐이었다고', None, 650, icon='trending-down', tone='red', size=46),
]},
{'from': '이유를 계산으로', 'enter': 'zoom', 'bg': 'ph_ryokan', 'cam': [('push', '+0.1', 50, 55, 1.2)], 'items': [
    cover('+0.02'),
    swapnum('100엔 = 1,000원+', '800원대', '천 원이', '팔백', y=170, size=100, tone='good'),
    tag('하룻밤 1만 엔 료칸', '료칸이라면', 680, 420, icon='home', tone='dark', size=58),
    swapnum('10만 원+', '8만 원대', '십만', '팔만', y=540, size=110, tone='good'),
]},
{'from': '베트남 호텔 방값은 흔히', 'enter': 'strips', 'bg': 'ph_usd_price_board', 'items': [
    BRIGHT,
    tag('베트남 호텔 = 달러 가격', '달러로', 120, 140, icon='currency-dollar-off', tone='dark', size=58),
    tag('원화 약세면 우리 돈으로 더 비싸다', '비싸집니다', 120, 300, icon='trending-up', tone='red', size=54),
    tag('엔화 여행만 싸졌다', '엔화로', 120, 460, icon='currency-won', tone='green', size=58),
]},
{'from': '이건 우리 노후 여행', 'enter': 'wipe', 'bg': 'ph_retired_couple_plan', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    BRIGHT,
    tag('같은 200만 원, 일본 며칠 · 다낭 며칠?', '이백만', 120, 140, icon='coin', tone='dark', size=54),
    glow('다낭이 나빠진 게 아니라, 비교 대상이 싸졌다', '비교', y=620, size=64),
]},
]
