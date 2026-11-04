"""다낭 편 — 4막 뒷부분 · 5막 · 결말 (자막 159~272, 11:54~20:30). 담당자 규칙: 뒤쪽은 돈을 쓰지 않는다 → 그림 재사용, 장면 단순, 무료 효과음만."""
from gen import (hook, tag, big, cover, glow, raw, stack, swapnum, card, bars, timeline, split, side)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

C = [
{'from': '이제 셋째, 가장 큰 원인', 'enter': 'flash', 'bg': 'ph_ceremony_stage', 'items': [
    cover('+0.02'),
    hook('셋째<br><strong>가장 큰 원인</strong>', '+0.05', y=300, size=150),
]},
{'from': '두 숫자를 나란히', 'enter': 'zoom', 'bg': 'ph_mykhe_crowded', 'items': [
    cover('+0.02'),
    card('다낭 한국인 (1~7월)', '100만 → 120만+', '백이십만', 220, 220, w=700, h=300, vat='백이십만'),
    card('외국인 중 한국인 비중', '절반 → 20%', '비중은', 1000, 220, w=700, h=300, vat='이십 퍼센트였습니다', hot=True),
    glow('사라진 게 아니라, 자리가 줄었다', '자리가', y=640, size=74),
]},
{'from': '교실로 바꿔 보면', 'enter': 'wipe', 'bg': 'ph_classroom', 'items': [
    BRIGHT,
    tag('30명 반, 우리 동네 아이 절반', '삼십', 120, 140, icon='users', tone='dark', size=58),
    tag('반이 2배 → 비중은 1/3 아래', '삼분의', 120, 300, icon='trending-down', tone='red', size=58),
]},
{'from': '이천이십사 년, 다낭을 찾은 러시아인', 'enter': 'zoom', 'bg': 'ph_new_tourists_arrive', 'items': [
    cover('+0.02'),
    tag('다낭을 찾은 러시아 손님', '+0.1', 620, 150, icon='users', tone='dark', size=56),
    bars([('2024 러시아', 6.8 / 40, '약 6만 8천 명', '육만팔천', True), ('2026 1~8월 러시아·CIS', 1.0, '40만 명+', '사십만', False)], top=290),
]},
{'from': '올해 오월 이십삼일', 'enter': 'flash', 'bg': 'ph_moscow_charter', 'items': [
    BRIGHT,
    tag('2026.5.23 모스크바 직항 전세기', '+0.1', 120, 140, icon='flag', tone='dark', size=56),
    tag('377명 · 꽃다발과 공연으로 환영', '삼백칠십칠', 120, 300, icon='heart-handshake', tone='red', size=54),
]},
{'from': '여기서 시간의 순서를', 'enter': 'wipe', 'bg': 'ph_report_documents', 'items': [
    cover('+0.02'),
    timeline([('2024 가을', '새 시장 개척 선언', '이천이십사'), ('2025.4', '카자흐스탄 직항', '사월에는'), ('2025.8', '100만 번째 한국인', '백만', 1), ('같은 해', '다른 하늘길도 개방', '하늘길도')], y=330),
]},
{'from': '앞에서 보신 비행기 숫자', 'enter': 'zoom', 'bg': 'ph_plane_takeoff', 'items': [
    cover('+0.02'),
    swapnum('주 150편', '주 140편 안팎', '백오십', '백사십', y=300, size=120, tone='good'),
    tag('여전히 1위', '여전히', None, 560, icon='flag', tone='green', size=66),
]},
{'from': '반대쪽 사정도', 'enter': 'wipe', 'bg': 'ph_promo_booth', 'items': [
    BRIGHT,
    tag('다낭시: 한국은 여전히 핵심 시장', '핵심', 120, 140, icon='flag', tone='dark', size=56),
    glow('한국 손님은 지키고, 바구니를 여러 개로', '바구니를', y=620, size=66),
]},
{'from': '그런데 그 바구니 나누기에서', 'enter': 'zoom', 'bg': 'ph_empty_korean_shop', 'items': [
    BRIGHT,
    tag('밀려난 곳: 한국 손님만 보던 가게', '밀려난', 120, 140, icon='user-x', tone='red', size=56),
    tag('여러분의 경험을 댓글로', '댓글로', 120, 600, icon='mail', tone='dark', size=58),
]},
{'from': '그리고 같은 시기, 한 나라', 'enter': 'flash', 'bg': 'ph_tokyo_crowd', 'items': [
    cover('+0.02'),
    hook('무너지지 않은 곳<br><strong>일본</strong>', '일본입니다', y=180, size=130),
    big('중국인 -55%', '오십오', y=520, size=150, color='#ff5a5a'),
]},
{'from': '그런데 일본의 관광 지갑은', 'enter': 'zoom', 'bg': 'ph_tokyo_crowd', 'items': [
    cover('+0.02'),
    big('7조 574억 엔', '칠조', y=220, size=170, color='#2ee66b'),
    tag('외국인 소비, 같은 기간 역대 최대', '역대', 520, 470, icon='trending-up', tone='green', size=54),
    tag('9월 방일 1위 = 한국', '구월', 700, 620, icon='flag', tone='red', size=60),
]},
{'from': '일본과 다낭은 같은', 'enter': 'wipe', 'bg': 'ph_japan_street', 'items': [
    cover('+0.02'),
    glow('손님 바구니가 여러 개 = 버틴다', '버텼습니다', y=360, size=68),
]},
{'from': '그렇다면 바구니가 하나뿐인', 'enter': 'zoom', 'bg': 'ph_single_customer_shop', 'items': [
    BRIGHT,
    tag('공식 매출·폐업 통계는 아직 없음', '통계는', 120, 140, icon='file-invoice', tone='dark', size=54),
    glow('한 번에 많이 남기려는 유혹 → 단골이 사라진다', '유혹이', y=620, size=60),
]},
{'from': '희망적인 장면도', 'enter': 'wipe', 'bg': 'ph_phuquoc_beach', 'items': [
    BRIGHT,
    tag('푸꾸옥 열흘, 100만 원도 다 못 씀 (여행 후기)', '푸꾸옥에서', 120, 140, icon='heart-handshake', tone='green', size=50),
]},
{'from': '냉정한 한계도', 'enter': 'zoom', 'bg': 'ph_nhatrang_beach', 'items': [
    cover('+0.02'),
    tag('9월 베트남 한국인 -8.8% (대만 언론)', '팔 점', None, 220, icon='trending-down', tone='red', size=50),
    tag('11~12월 서울·부산 홍보 예정', '서울과', 560, 400, icon='calendar', tone='dark', size=56),
    glow('둘 중 한 명 시절로는 돌아가기 어렵다', '돌아가기', y=640, size=64),
]},
{'from': '이건 우리 동네 이야기', 'enter': 'wipe', 'bg': 'ph_neighborhood_shop', 'items': [
    BRIGHT,
    glow('내 가게의 손님 바구니는 몇 개인가', '바구니가', y=620, size=70),
]},
{'from': '처음 질문으로 돌아가겠습니다', 'enter': 'flash', 'bg': 'th_beach_full', 'items': [
    cover('+0.02'),
    *stack([('① 도시는 끝나지 않았다', '먼저,', 'trending-up', 'green'), ('② 줄어든 건 한국인 비중', '다음으로,', 'chart-bar', 'red'),
            ('③ 지갑은 엔저 따라 일본으로', '마지막으로,', 'currency-won', 'dark')], x=420, y=220, gap=170, size=62),
]},
{'from': '무너진 건 도시가 아니라', 'enter': 'zoom', 'bg': 'ph_hanmarket_signs', 'items': [
    cover('+0.02'),
    hook('무너진 건 도시가 아니라<br><strong>한 나라 손님만 본 장사</strong>', '무너진', y=300, size=110),
]},
{'from': '오늘 하실 수 있는 일', 'enter': 'wipe', 'bg': 'ph_retired_couple_plan', 'items': [
    cover('+0.02'),
    *stack([('① 엔화·달러 환율을 같은 날 비교', '하나,', 'currency-won', ''), ('② 택시 문제엔 휴대폰 촬영', '둘,', 'device-mobile', ''),
            ('③ 성수기 입국 대기 2시간 대비', '셋,', 'clock', '')], x=200, y=220, gap=170, size=54),
]},
{'from': '다시 한시장 앞 골목', 'enter': 'flash', 'bg': 'th_hanmarket_street', 'items': [
    BRIGHT,
    tag('다시, 한시장 앞', '+0.1', 120, 140, icon='map-pin', tone='dark', size=60),
]},
{'from': '댓글로 하나만', 'enter': 'zoom', 'bg': 'ph_tourists_mixed', 'items': [
    cover('+0.02'),
    *split('엔저의', vs=True),
    side('l', '엔저의', tag('1번', '엔저의', 0, 0, tone='red', size=80), tag('엔저의 일본', '엔저의', 0, 0, size=54)),
    side('r', '넓어진', tag('2번', '넓어진', 0, 0, tone='green', size=80), tag('넓어진 베트남', '넓어진', 0, 0, size=54)),
]},
{'from': '다음 이야기 후보', 'enter': 'wipe', 'bg': 'ph_tokyo_crowd', 'items': [
    cover('+0.02'),
    *stack([('1번 엔저가 끝나면 일본 여행은?', '일 번,', 'currency-won', ''), ('2번 손님 최대인데 관광수지는 적자?', '이 번,', 'chart-bar', ''),
            ('3번 면세점은 왜 텅 비었나', '삼 번,', 'building-store', '')], x=200, y=220, gap=170, size=52),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'flash', 'bg': 'th_beach_full', 'items': [
    BRIGHT,
    hook('지혜호수<br><strong>경제연구소</strong>', '지혜호수', y=260, size=150, sfx='ding'),
    tag('숫자로 확인하고 사실로 말합니다', '+0.3', None, 620, tone='dark', size=56),
]},
]
