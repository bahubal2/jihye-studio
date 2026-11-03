"""본편 1: 예고 꼬리 · 7위 피죤 · 6위 푸르밀 (자막 17~137)."""
from gen import (tag, logo, stamp, roll, split, side, big, cover, ranks, punch, pictos, line, raw, chip, flow, glow,
                 article, inset, rankbadge, swapnum, igrid, donut, steps, bubble, card)

def RB(rank, name, first=False): return rankbadge(rank, name, '+0.05', still=not first)
OPEN7 = {}

S1 = [
# 0:43 여러분 장바구니 속 그 브랜드 — 다음 차례?
{'from': '여러분 장바구니', 'enter': 'slide', 'bg': 'ph_basket', 'items': [
    tag('내 장바구니 속 브랜드', '장바구니', 140, 180, icon='shopping-cart', size=66),
    tag('다음 차례?', '다음', 140, 330, icon='alert-triangle', tone='red', size=80),
]},
# 0:50 끝까지 들으면 챙겨 갈 두 가지
{'from': '끝까지 들으시면', 'bg': 'st_crowd_mall', 'items': [
    cover('+0.02'),
    tag('끝까지 보면 두 가지', '끝까지', 560, 130, icon='key', tone='dark', size=64),
    tag('① 7개 순위를 꿰는 마음의 법칙', '하나,', 220, 330, icon='scale', size=62),
    tag('② 30초 자가진단', '둘,', 220, 480, icon='clock', tone='green', size=62),
]},
# 1:01 덜 무너진 7위부터
{'from': '덜 무너진', 'enter': 'flash', 'bg': 'st_hypermarket', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=7, nowat='7위부터', top=360),
    tag('덜 무너진 순서대로', '무너진', 640, 140, icon='trending-down', tone='dark', size=60),
]},
# ---------------- 7위 피죤 ----------------
# 1:03 일요일 오후 베란다 건조대
{'from': '일요일 오후', 'enter': 'mask', 'bg': 'ph_balcony_towels', 'items': [
    line('일요일 오후, 베란다', '일요일', x=150, y=200, cls='say', size=84),
]},
{'from': '햇볕에 마른', 'bg': 'ph_towel_face', 'items': [
    tag('보송한 감촉', '보송한', 1080, 220, icon='wash', size=60),
    tag('은은한 향', '향이', 1080, 360, icon='droplet', tone='ghost', size=60),
]},
# 1:13 빨래엔 피죤 — 7위 카드 뒤집힘
{'from': '그 향의 이름을', 'enter': 'flash', 'bg': 'st_laundry', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=7, opened={7: ('피죤', '피죤')}, top=500),
    big('“빨래엔 피죤”', '피죤', y=110, size=140),
]},
# 1:17 1978년 창업, 30여 년 1등
{'from': '이 회사가 세워진', 'bg': 'ph_crt_tv_room', 'items': [
    RB(7, '피죤', first=True),
    tag('1978년 창업', '세워진', 140, 230, icon='calendar', size=64),
    tag('섬유유연제 1등', '섬유유연제', 140, 380, icon='flag', tone='green', size=64),
    big('30여 년', '년입니다', y=560, size=200, color='#3fe08a'),
]},
{'from': '신혼살림 장만할', 'bg': 'ph_newlywed_shop', 'items': [
    RB(7, '피죤'),
    tag('신혼살림 필수품', '신혼살림', 140, 230, icon='heart-handshake', size=64),
    tag('한 세대가 같은 향으로', '세대가', 140, 380, icon='users', tone='ghost', size=60),
]},
# 1:34 그런데 2011년 여름 — 다시 쓴 기사 카드
{'from': '그런데 2011년 여름', 'enter': 'slide', 'bg': 'ph_magazine_press', 'items': [
    RB(7, '피죤'),
    article('시사주간지', '2011년 여름', '피죤 회장, 직원 폭행·회삿돈 유출 의혹 내부 문건', '+0.1', mark='의혹', markat='의혹이었습니다', x=460, y=190),
    tag('보도 = 의혹 단계', '의혹이었습니다', 140, 760, icon='alert-triangle', tone='dark', size=52),
]},
# 1:44 전 사장 피습 → 청부 폭행 → 실형
{'from': '몇 주 뒤', 'enter': 'mask', 'bg': 'ph_apartment_night', 'items': [
    RB(7, '피죤'),
    tag('해임된 전 사장 피습', '해임된', 140, 230, icon='user-x', tone='red', size=64),
    tag('배후는 회장', '회장이', 140, 380, icon='key', tone='dark', size=64),
]},
{'from': '조직폭력배에게', 'bg': 'st_court', 'items': [
    RB(7, '피죤'),
    tag('조폭에게 3억 원 · 청부 폭행', '조직폭력배에게', 140, 230, icon='cash', tone='red', size=62),
    stamp('징역 10개월 실형', '징역', x=880, y=480, size=110),
]},
# 1:59 통념: 주부들 불매? → 아닙니다
{'from': '이쯤 되면 뉴스를', 'bg': 'ph_softener_shelf', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    tag('뉴스 보고 불매해서?', '불매해서', 560, 260, icon='alert-triangle', size=80, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=500, size=160),
]},
# 2:06 보도는 8월, 순위는 1~2월에 이미
{'from': '보도가 나온 건', 'enter': 'slide', 'bg': 'ph_magazine_press', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    tag('보도: 2011년 8월', '+0.1', 560, 200, icon='calendar', size=66),
    tag('순위 역전: 이미 1~2월', '순위는', 560, 360, icon='trending-down', tone='red', size=66),
    stamp('보도보다 먼저', '뒤집혀', x=1150, y=560, size=96),
]},
# 2:13 점유율 도넛: 35.8% vs 42.6% → 27%
{'from': '피죤 35.8%', 'bg': 'ph_softener_shelf', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    donut(35.8, '+0.05', '피죤', x=380, y=300, d=400, tone='bad'),
    donut(42.6, '경쟁사', '경쟁사', x=1140, y=300, d=400, tone='gray'),
]},
{'from': '3월과 4월엔', 'bg': 'ph_softener_shelf', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    swapnum('35.8%', '27%', '+0.05', '내려갑니다', y=280, size=180),
    tag('넷 중 하나 남짓', '넷', 680, 600, icon='trending-down', tone='red', size=64),
]},
{'from': '소비자가 알기도', 'bg': 'st_city_night', 'items': [
    RB(7, '피죤'),
    glow('안에서부터 기울었다', '안에서부터', y=420, size=110),
]},
# 2:30 경쟁사가 잘해서? 맞다. 그런데 경쟁은 30년 내내
{'from': '경쟁사가 잘해서', 'bg': 'st_hypermarket', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    tag('경쟁사가 잘해서?', '경쟁사가', 200, 200, icon='scale', size=66),
    tag('맞는 말', '맞는', 200, 340, icon='flag', tone='green', size=60),
    tag('경쟁은 30년 내내 있었다', '경쟁은', 200, 480, icon='clock', tone='dark', size=62),
    stamp('달라진 건 안쪽', '안쪽이었습니다', x=1100, y=620, size=96),
]},
# 2:40 넉 달 만에 해임된 새 사장
{'from': '그해 2월에 온', 'enter': 'slide', 'bg': 'ph_receipts_desk', 'items': [
    RB(7, '피죤'),
    tag('새 사장 · 넉 달 만에 해임', '해임됩니다', 140, 200, icon='user-x', tone='red', size=62),
    tag('두 달 만에 월 매출 2배+', '두', 140, 350, icon='trending-up', tone='green', size=62),
    tag('회장 일가 영수증 없는 비용 지적', '영수증', 140, 500, icon='receipt', size=58),
]},
{'from': '한 전직 임원은', 'bg': 'st_city_night', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    bubble('고객보다 직원을 먼저 감동시켜야 하는데…', '고객보다', 300, 300, size=60),
    tag('그런 문화가 없었다', '문화가', 640, 560, icon='mood-sad', tone='red', size=66),
]},
# 3:04 열 통 중 세 통 반 → 세 통도 안 됨
{'from': '마트 섬유유연제 칸에', 'bg': 'ph_softener_shelf', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    tag('섬유유연제 10통', '열', 680, 150, icon='bottle', size=60),
    igrid('bottle', 10, '+0.1', lit=3, half=True, litat='세', y=330, size=130, tone='bad'),
    tag('연초 3.5통 → 석 달 뒤 3통 미만', '석', 420, 600, icon='trending-down', tone='red', size=58),
]},
{'from': '손님의 손이', 'bg': 'ph_put_back', 'items': [
    RB(7, '피죤'),
    tag('한 통씩 옆 칸으로', '옆', 140, 220, icon='shopping-cart', tone='dark', size=66),
]},
# 3:18 가용성 휴리스틱
{'from': '사람은 사실보다', 'enter': 'mask', 'bg': 'ph_crt_tv_room', 'items': [
    RB(7, '피죤'),
    cover('+0.02'),
    tag('사실보다 자주 본 장면', '자주', 520, 180, icon='device-mobile', size=64),
    glow('가용성 휴리스틱', '가용성', y=400, size=110),
    flow([('30년 광고', '30년'), ('한 철 뉴스', '철')], y=640, size=66),
]},
{'from': '보송한 수건의 향으로', 'bg': 'st_court', 'items': [
    RB(7, '피죤'),
    swapnum('보송한 향', '법정의 회장', '+0.05', '법정에', y=380, size=120),
]},
# 3:38 다음 칸 예고: 주먹 한 사람 → 이메일 400명
{'from': '피죤에선 회장의 주먹이', 'enter': 'slide', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', logo('pigeon', '+0.1', 0, 0, h=72), tag('주먹 → 직원 1명', '+0.3', 0, 0, icon='user', tone='red', size=50)),
    side('r', '이메일', logo('purmil', '이메일', 0, 0, h=72), tag('이메일 → 직원 400명', '400명을', 0, 0, icon='mail', tone='red', size=50)),
]},
# ---------------- 6위 푸르밀 ----------------
{'from': '편의점 냉장고에서', 'enter': 'flash', 'bg': 'ph_conv_fridge', 'items': [
    tag('갈색 초코우유', '초코우유', 140, 200, icon='milk', size=62),
    tag('검은콩 우유', '검은콩', 140, 340, icon='milk', tone='ghost', size=60),
    tag('작은 병 요구르트', '요구르트', 140, 480, icon='bottle', tone='ghost', size=60),
]},
{'from': '계산대에서 뒷면을', 'bg': 'ph_conv_fridge', 'items': [
    cover('+0.02'),
    bubble('어, 이게 푸르밀 거였어?', '푸르밀', 520, 180, size=72),
    ranks('+0.1', n=7, now=6, opened={7: ('피죤', None), 6: ('푸르밀', '푸르밀')}, top=470),
]},
{'from': '간판보다 제품이', 'bg': 'st_warehouse', 'items': [
    RB(6, '푸르밀', first=True),
    tag('간판보다 제품이 유명', '간판보다', 140, 230, icon='package', size=62),
    flow([('1978 롯데우유', '롯데우유입니다'), ('2009 푸르밀', '이름을')], y=440, size=72),
]},
{'from': '아이 소풍 가방에', 'bg': 'ph_picnic_bag', 'items': [
    RB(6, '푸르밀'),
    tag('소풍 가방 · 운동회 간식', '소풍', 140, 230, icon='heart-handshake', size=62),
]},
{'from': '2016년 매출은', 'bg': 'st_warehouse', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    roll(0, 2736, '+0.1', y=250, size=190, suffix='억 원', tone='good'),
    tag('2016년 매출', '+0.05', 760, 130, icon='chart-bar', tone='green', size=58),
    tag('마트·편의점 자체 상표까지 납품', '대형마트와', 470, 560, icon='truck-delivery', size=58),
]},
# 4:26 2022.10.17 이메일 한 통 (클립 — 중반 반전)
{'from': '그런데 2022년 10월', 'enter': 'flash', 'bg': 'ph_email_layoff', 'items': [
    RB(6, '푸르밀'),
    tag('2022. 10. 17', '+0.1', 140, 220, icon='calendar', tone='dark', size=62),
    tag('전 직원에게 이메일 한 통', '이메일', 140, 360, icon='mail', tone='red', size=66),
]},
{'from': '11월 30일 자로', 'bg': 'ph_email_layoff', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    article('푸르밀 사내 공지 (요약)', '2022. 10. 17', '11월 30일 자로 사업 종료 · 전 직원 정리해고', '+0.05', mark='전 직원 정리해고', markat='정리해고한다는', x=420, y=120, rot=-1.5),
    big('400명+', '넘었습니다', y=560, size=140, color='#ff5a5a'),
]},
{'from': '사전 협의는', 'bg': 'ph_union_table', 'items': [
    RB(6, '푸르밀'),
    tag('사전 협의 없음 (회사 스스로 인정)', '사전', 140, 200, icon='alert-triangle', tone='red', size=58),
    tag('노조위원장 · 대표와 단 한 번', '노조위원장은', 140, 350, icon='users', size=58),
    tag('노조 해산까지 사정', '해산하겠다고까지', 140, 500, icon='hand-stop', tone='dark', size=58),
]},
{'from': '돌아온 답은', 'bg': 'ph_union_table', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    glow('“더 이상 얼굴 볼 일 없다”', '얼굴', y=420, size=100),
]},
{'from': '이쯤 되면 우유', 'bg': 'ph_conv_fridge', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    tag('우유 안 마시는 시대라서?', '우유', 460, 240, icon='milk', size=76, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=490, size=160),
]},
{'from': '저출산도 코로나도', 'bg': 'st_chart', 'items': [
    RB(6, '푸르밀'),
    tag('저출산 · 코로나 = 업계 전체', '저출산도', 140, 200, icon='users', tone='dark', size=60),
    tag('적자가 시작된 해는 따로', '적자가', 140, 350, icon='key', tone='red', size=62),
]},
{'from': '2018년, 창업주의', 'enter': 'slide', 'bg': 'st_chart', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', tag('~2017 전문경영인', '+0.1', 0, 0, icon='user', tone='green', size=48), tag('흑자', '+0.3', 0, 0, icon='trending-up', size=66)),
    side('r', '+0.6', tag('2018~ 창업주 차남 대표', '+0.6', 0, 0, icon='user', tone='red', size=48), tag('적자 시작', '+0.9', 0, 0, icon='trending-down', tone='red', size=66)),
]},
{'from': '그 뒤 매출은', 'bg': 'st_stock_down', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    tag('매출 해마다 -8%', '그', 620, 160, icon='trending-down', tone='red', size=66),
    tag('100원어치 → 해마다 8원씩', '백', 520, 320, icon='coin', size=60),
    swapnum('2,736억', '1,799억', '+0.5', '내려옵니다', y=500, size=150),
]},
{'from': '노조는 설비 투자를', 'bg': 'ph_factory_stopped', 'items': [
    RB(6, '푸르밀'),
    tag('설비 투자 요구 외면 (노조 주장)', '설비', 140, 200, icon='building-factory', size=58),
    tag('감원 · 임금 삭감', '감원과', 140, 350, icon='user-x', tone='red', size=62),
]},
{'from': '통보 24일 만에', 'enter': 'slide', 'bg': 'ph_factory_bus', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    tag('24일 만에 사업 종료 철회', '통보', 520, 130, icon='arrows-exchange', tone='dark', size=60),
    tag('대신 직원 30% 감원', '30%를', 600, 270, icon='user-x', tone='red', size=64),
    igrid('bus', 10, '열', lit=0, drop=3, dropat='세 대가', y=470, size=120, tone='bad'),
]},
{'from': '전주 공장은', 'bg': 'ph_factory_stopped', 'items': [
    RB(6, '푸르밀'),
    stamp('전주 공장 가동 중단', '멈췄습니다', x=600, y=400, size=110),
]},
{'from': '그리고 이듬해 봄', 'enter': 'mask', 'bg': 'ph_fridge_gap', 'items': [
    RB(6, '푸르밀'),
    article('유통 업계 보도 (요약)', '2023년 봄', '대형마트·편의점 매대에서 푸르밀 제품 사라져', '+0.1', mark='사라져', markat='사라졌다는', x=460, y=180),
]},
{'from': '문제는 맛이 아니라', 'bg': 'ph_fridge_gap', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    swapnum('맛', '신뢰', '+0.05', '신뢰였습니다', y=300, size=200),
    tag('언제 끊길지 모르는 납품', '끊길지', 560, 600, icon='truck-delivery', tone='dark', size=58),
]},
{'from': '비교할 길이', 'enter': 'mask', 'bg': 'ph_conv_fridge', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    flow([('충성', '충성은'), ('계산', '계산으로')], y=200, size=90),
    glow('대안의 등장', '대안의', y=470, size=110),
]},
{'from': '초코우유는 다른', 'bg': 'ph_fridge_gap', 'items': [
    RB(6, '푸르밀'),
    tag('옆 칸 대안이 금세 채운다', '대안이', 140, 220, icon='package', size=62),
]},
{'from': '어, 이게 푸르밀 거였어 하던', 'bg': 'ph_fridge_gap', 'items': [
    RB(6, '푸르밀'),
    cover('+0.02'),
    swapnum('“이게 푸르밀 거였어?”', '“그 우유 어디 갔지?”', '+0.1', '어디', y=380, size=80),
]},
]
