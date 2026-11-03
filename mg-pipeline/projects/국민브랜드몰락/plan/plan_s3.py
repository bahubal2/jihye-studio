"""본편 3: 2위 동양 · 1위 옥시(무거운 구간: 효과음·튀는 등장 없이) · 정리 · 자가진단 · 쌍용 · 마무리 (자막 293~517)."""
from gen import (tag, logo, stamp, roll, split, side, big, cover, ranks, punch, pictos, line, raw, chip, flow, glow,
                 article, inset, rankbadge, swapnum, igrid, donut, bubble)

def RB(rank, name, first=False): return rankbadge(rank, name, '+0.05', still=not first)
O = {7: ('피죤', None), 6: ('푸르밀', None), 5: ('미스터피자', None), 4: ('남양유업', None), 3: ('대우', None)}
def soft(text, at, x, y, size=56, icon=None):          # 무거운 구간용: 효과음 없는 어두운 칩
    return tag(text, at, x, y, icon=icon, tone='dark', size=size)

S3 = [
{'from': '대우의 장부는 은행을', 'enter': 'slide', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', logo('daewoo', '+0.1', 0, 0, h=72), tag('장부 → 은행을 속임', '+0.3', 0, 0, icon='building-bank', size=48)),
    side('r', '다음', logo('tongyang', '다음', 0, 0, h=72), tag('장부 → 동네 노후 통장', '노후', 0, 0, icon='home', tone='red', size=48)),
]},
# ---------------- 2위 동양 ----------------
{'from': '2023년 1월, 신문에', 'enter': 'mask', 'bg': 'st_contract', 'items': [
    article('일간지 보도 (요약)', '2023. 1', '10년 전 사건… 투자자 집단소송 아직도 진행 중', '+0.1', mark='아직도', markat='이어진다는', x=460, y=180),
]},
{'from': '10년 전엔 아무도', 'bg': 'ph_broker_counter', 'items': [
    tag('10년 전 증권사 창구', '10년', 140, 200, icon='building-bank', size=60),
    tag('직원도 손님도 웃었다', '웃고', 140, 350, icon='heart-handshake', tone='green', size=60),
]},
{'from': '은행보다 이자를', 'bg': 'ph_broker_counter', 'items': [
    tag('은행보다 이자 조금 더', '은행보다', 140, 200, icon='percentage', tone='green', size=60),
    tag('퇴직금 · 딸 결혼 자금', '퇴직금', 140, 350, icon='heart-handshake', size=60),
]},
{'from': '처음엔 100만 원', 'enter': 'slide', 'bg': 'ph_bankbook_hand', 'items': [
    cover('+0.02'),
    flow([('100만 원', '처음엔'), ('1,000만 원', '이자를'), ('1억 원', '+4.8')], y=300, size=100),
    tag('웃돈 얹어서라도', '웃돈을', 660, 560, icon='coin', tone='dark', size=60),
]},
{'from': '그룹이 찍은 회사채와', 'bg': 'st_money', 'items': [
    cover('+0.02'),
    tag('회사채·어음 2조 3,000억', '+0.1', 520, 140, icon='file-invoice', size=60),
    tag('개인 몫 1조 5,000억', '개인이', 560, 280, icon='users', tone='red', size=60),
    igrid('user', 3, '셋', lit=2, litat='둘이', cols=3, y=430, size=170, tone='bad'),
]},
{'from': '그런데 2013년 9월과', 'enter': 'flash', 'bg': 'ph_investor_protest', 'items': [
    tag('2013. 9~10 · 계열사 5곳 법정관리', '+0.1', 140, 200, icon='gavel', tone='red', size=60),
    ranks('동양그룹', n=7, now=2, opened={**O, 2: ('동양', '동양그룹')}, top=520),
]},
{'from': '피해자는 몇 명', 'bg': 'ph_investor_protest', 'items': [
    RB(2, '동양', first=True),
    cover('+0.02'),
    big('4만여 명', '4만여', y=230, size=190, color='#ff5a5a'),
    tag('피해액 1조 3,000억 (검찰 추산)', '피해액은', 460, 520, icon='cash', size=60),
    tag('대우 사태 이후 최대 개인 피해', '대우', 460, 660, icon='alert-triangle', tone='dark', size=56),
]},
{'from': '이쯤 되면 운 나쁜', 'bg': 'ph_investor_protest', 'items': [
    RB(2, '동양'),
    cover('+0.02'),
    tag('운 나쁜 투자였을 뿐?', '운', 460, 240, icon='alert-triangle', size=72, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=480, size=160),
]},
{'from': '법원은 부도 위험을', 'bg': 'st_court', 'items': [
    RB(2, '동양'),
    stamp('사기성 어음', '사기성', x=1150, y=380, size=110),
    tag('부도 위험 숨기고 판매', '부도', 140, 230, icon='file-invoice', tone='red', size=60),
    tag('경영권 지키려 빚을 개인에게', '경영권을', 140, 520, icon='users', size=58),
]},
{'from': '회장은 1심에서', 'bg': 'st_court', 'items': [
    RB(2, '동양'),
    cover('+0.02'),
    swapnum('1심 징역 12년', '대법원 7년 확정', '+0.1', '대법원에서', y=360, size=110),
]},
{'from': '높은 이자를 노린', 'enter': 'mask', 'bg': 'ph_broker_counter', 'items': [
    RB(2, '동양'),
    tag('투자자 책임은? → 맞는 말', '높은', 140, 180, icon='scale', size=58),
    tag('그런데 판 곳 = 같은 그룹 증권사', '판', 140, 330, icon='building-bank', tone='red', size=60),
    tag('위험 설명 못 들었다', '위험', 140, 480, icon='alert-triangle', tone='dark', size=58),
]},
{'from': '금융감독원 분쟁조정엔', 'bg': 'ph_dispute_form', 'items': [
    RB(2, '동양'),
    cover('+0.02'),
    tag('금감원 분쟁조정', '금융감독원', 700, 150, icon='building-bank', tone='dark', size=58),
    big('한두 달 새 2만 명+', '2만', y=320, size=130, color='#ff5a5a'),
    tag('전례 없는 규모', '전례', 700, 580, icon='alert-triangle', size=60),
]},
{'from': '4만 명을 결혼식', 'enter': 'slide', 'bg': 'ph_wedding_hall', 'items': [
    RB(2, '동양'),
    cover('+0.02'),
    tag('4만 명 = 하객 300명 결혼식', '결혼식', 480, 140, icon='users', size=60),
    big('130번+', '130번', y=290, size=200, color='#ff5a5a'),
    tag('잔칫집마다 노후 자금이 빠져나갔다', '잔칫집', 360, 600, icon='home', tone='dark', size=56),
]},
{'from': '첫 이자가 들어오던', 'enter': 'mask', 'bg': 'ph_bankbook_hand', 'items': [
    RB(2, '동양'),
    cover('+0.02'),
    glow('쾌락 적응', '쾌락', y=200, size=120),
    flow([('100만', '100만'), ('1,000만', '1,000만'), ('1억', '1억')], y=480, size=100),
]},
{'from': '제 눈엔 이 대목이', 'bg': 'ph_bankbook_hand', 'items': [
    RB(2, '동양'),
    swapnum('욕심', '익숙해진 안심', '위험을', '안심이었으니까요', y=380, size=120),
]},
{'from': '웃으며 통장을', 'bg': 'ph_dispute_form', 'items': [
    RB(2, '동양'),
    swapnum('통장', '분쟁조정 신청서', '+0.1', '분쟁조정', y=380, size=110),
]},
# ---------------- 1위 옥시 (무거운 구간) ----------------
{'from': '동양은 사람들의 돈을', 'enter': 'fade', 'bg': 'ph_hospital_hall', 'items': [
    cover('+0.02'),
    ranks('+0.1', n=7, now=1, nowat='1위는', opened=O | {2: ('동양', None)}, top=380, sfx=None),
    line('돈으로는 셀 수 없는 것', '셀', x=None, y=160, cls='say', size=80, center=True),
]},
{'from': '겨울밤, 아이 방입니다', 'enter': 'fade', 'bg': 'ph_fill_tank', 'items': [
    line('겨울밤, 아이 방', '겨울밤', x=150, y=200, cls='say', size=84),
]},
{'from': '엄마는 물통을', 'bg': 'ph_fill_tank', 'items': [
    line('세균이 끼지 않게', '세균이', x=150, y=200, cls='say', size=76),
    line('아이 숨길이 깨끗하도록', '숨길이', x=150, y=310, cls='say', size=76),
]},
{'from': '그 한 뚜껑의 이름은', 'enter': 'fade', 'bg': 'ph_hospital_hall', 'items': [
    cover('+0.02'),
    line('가습기 살균제', '살균제였습니다', x=None, y=400, cls='head', size=140, center=True),
]},
{'from': '이 제품을 가장 많이 판', 'bg': 'ph_closet_absorber', 'items': [
    soft('우리 집 곳곳에 있던 회사', '곳곳에', 140, 180, size=58, icon='home'),
    soft('표백제', '표백제', 140, 320, icon='droplet'),
    soft('물먹는 하마', '하마', 140, 440, icon='package'),
    soft('손 세정제 · 목캔디', '손', 140, 560, icon='wash'),
]},
{'from': '시민단체 추산으로', 'bg': 'ph_closet_absorber', 'items': [
    cover('+0.02'),
    soft('시민단체 추산 · 약 1,000만 병', '+0.1', 520, 160, icon='bottle', size=60),
    igrid('user', 5, '국민', lit=1, litat='한', cols=5, y=380, size=170, tone='bad', sfx=None),
]},
{'from': '그런데 2011년', 'enter': 'fade', 'bg': 'ph_hospital_hall', 'items': [
    soft('2011 · 원인 모를 폐 질환', '원인', 140, 200, icon='alert-triangle', size=60),
    soft('산모와 아이들', '산모와', 140, 340, icon='baby-carriage', size=60),
]},
{'from': '지금까지 피해를 신고한', 'bg': 'ph_hospital_hall', 'items': [
    cover('+0.02'),
    soft('피해 신고 (2025. 2 기준)', '+0.1', 560, 150, icon='file-invoice', size=58),
    line('7,993명', '+1.2', x=None, y=260, cls='head', size=130, center=True),
    line('그중 사망 1,891명', '숨진', x=None, y=470, cls='head', size=110, center=True, color='#ff8a8a'),
]},
{'from': '가장 많은 피해를 낸', 'bg': 'ph_closet_absorber', 'items': [
    cover('+0.02'),
    soft('2013 국정감사 · 제품별 사망 사례', '국정감사', 420, 140, icon='file-invoice', size=56),
    igrid('user', 10, '+0.3', lit=6, litat='열에', cols=10, y=330, size=120, tone='bad', sfx=None),
    ranks('옥시', n=7, now=1, opened=O | {2: ('동양', None), 1: ('옥시', '옥시')}, top=560, sfx=None),
]},
{'from': '이쯤 되면 사건이', 'bg': 'ph_closet_absorber', 'items': [
    RB(1, '옥시', first=True),
    cover('+0.02'),
    soft('알려지자마자 등을 돌렸다?', '돌렸다고', 500, 240, size=66),
    line('아닙니다', '아닙니다', x=None, y=440, cls='head', size=130, center=True, color='#ff8a8a'),
]},
{'from': '사건은 2011년에', 'bg': 'st_hypermarket', 'items': [
    RB(1, '옥시'),
    cover('+0.02'),
    soft('2011 사건 알려짐', '+0.1', 400, 160, icon='calendar', size=58),
    soft('2016. 4 “매출 영향 없다” 기사', '영향이', 400, 300, icon='file-invoice', size=58),
    line('5년 동안 장바구니에', '5년', x=None, y=470, cls='head', size=100, center=True),
]},
{'from': '진열대를 비운 건', 'enter': 'fade', 'bg': 'ph_empty_shelf', 'items': [
    RB(1, '옥시'),
    soft('2016 봄 검찰 수사', '검찰', 140, 180, icon='gavel', size=58),
    soft('실험 보고서 조작 의혹', '조작', 140, 310, icon='file-invoice', size=58),
    soft('옥시 전 대표 · 징역 6년 확정', '징역', 140, 440, icon='scale', size=58),
]},
{'from': '회사의 공식 사과는', 'bg': 'ph_empty_shelf', 'items': [
    RB(1, '옥시'),
    soft('공식 사과까지 5년', '사과는', 140, 200, icon='clock', size=60),
]},
{'from': '그제야 둑이', 'bg': 'st_hypermarket', 'items': [
    RB(1, '옥시'),
    cover('+0.02'),
    donut(53, '제습제', '제습제 -53%', x=420, y=300, d=380, tone='bad'),
    donut(38, '표백제는', '표백제 -38%', x=1120, y=300, d=380, tone='bad'),
]},
{'from': '약사회가 불매', 'bg': 'ph_empty_shelf', 'items': [
    RB(1, '옥시'),
    soft('약사회 불매 지지', '약사회가', 140, 200, icon='flag', size=58),
    soft('대형 편의점 체인 취급 중단', '편의점', 140, 340, icon='building-store', size=58),
]},
{'from': '1,891명을 버스로', 'enter': 'fade', 'bg': 'ph_tour_buses', 'items': [
    RB(1, '옥시'),
    cover('+0.02'),
    soft('관광버스 1대 = 45명', '마흔다섯', 640, 130, icon='bus', size=58),
    igrid('bus', 42, '마흔두', lit=42, litat='마흔두', cols=14, y=280, size=86, tone='bad', sfx=None),
    line('돌도 안 된 아기들도', '아기들이', x=None, y=640, cls='say', size=70, center=True),
]},
{'from': '정부가 인정한 피해자는', 'bg': 'ph_station_petition', 'items': [
    RB(1, '옥시'),
    soft('정부 인정 피해자 누적 6,000명+', '정부가', 140, 180, icon='users', size=58),
    soft('특별법 개정 → 국가 배상 체계', '특별법이', 140, 320, icon='scale', size=58),
    soft('참사 알려진 지 15년', '15년', 140, 460, icon='clock', size=58),
]},
{'from': '사람은 손해를 이득보다', 'enter': 'fade', 'bg': 'ph_hospital_hall', 'items': [
    RB(1, '옥시'),
    cover('+0.02'),
    line('손실 회피', '손실', x=None, y=200, cls='head', size=120, center=True),
    soft('되돌릴 수 없는 손해 → 그 이름 전부 내려놓음', '되돌릴', 300, 460, size=56),
    soft('옷장 속 하마까지', '하마까지요', 660, 600, icon='package', size=56),
]},
{'from': '깨끗하라고 따라 넣었던', 'enter': 'fade', 'bg': 'ph_station_petition', 'items': [
    RB(1, '옥시'),
    soft('2023 겨울 · 서울역 앞 탄원서', '서울역', 140, 220, icon='map-pin', size=58),
]},
# ---------------- 정리 ----------------
{'from': '이제 일곱 개를 다시', 'enter': 'flash', 'bg': 'st_crowd_mall', 'items': [
    cover('+0.02'),
    ranks('+0.1', n=7, top=380, opened={7: ('피죤', '피죤.'), 6: ('푸르밀', '푸르밀.'), 5: ('미스터피자', '미스터피자.'), 4: ('남양유업', '남양유업.'),
                                       3: ('대우', '대우.'), 2: ('동양', '동양.'), 1: ('옥시', '옥시.')}),
    line('다시 세워 보면', '다시', x=None, y=160, cls='say', size=76, center=True),
]},
{'from': '일곱을 겹쳐 보면', 'enter': 'slide', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    tag('세 갈래', '세', 800, 100, icon='key', tone='dark', size=60),
    tag('① 약자를 때린 손', '약자를', 100, 250, icon='user-x', tone='red', size=54),
    lambda sc: '<div class="row" style="left:820px; top:262px">' + ''.join(logo(n, '피죤,', 0, 0, h=44)(sc) for n in ('pigeon', 'purmil', 'mrpizza', 'namyang')) + '</div>',
    tag('② 숫자를 속인 손', '숫자를', 100, 420, icon='file-invoice', tone='red', size=54),
    lambda sc: '<div class="row" style="left:820px; top:432px">' + ''.join(logo(n, '대우와', 0, 0, h=44)(sc) for n in ('daewoo', 'tongyang')) + '</div>',
    tag('③ 생명 앞에서 눈감은 손', '생명', 100, 590, icon='alert-triangle', tone='dark', size=54),
    lambda sc: '<div class="row" style="left:820px; top:602px">' + logo('oxy', '옥시.', 0, 0, h=44)(sc) + '</div>',
]},
{'from': '무너지는 순서도', 'enter': 'mask', 'bg': 'st_crowd_mall', 'items': [
    cover('+0.02'),
    tag('무너지는 순서', '순서도', 760, 110, icon='trending-down', tone='dark', size=58),
    flow([('안: 약자 밀어내기', '안에서'), ('밖: 분노·불매', '밖에서'), ('조용한 외면', '조용한')], y=340, size=60),
]},
{'from': '값이 무너뜨린 게', 'bg': 'ph_crowd_walk_away', 'items': [
    cover('+0.02'),
    swapnum('값', '손버릇', '+0.1', '손버릇이', y=220, size=170),
    tag('지갑보다 마음이 먼저 떠났다', '마음이', 520, 560, icon='heart-handshake', tone='red', size=62),
]},
{'from': '동네 미용실을', 'enter': 'slide', 'bg': 'ph_hair_salon', 'items': [
    tag('머리는 마음에 들게', '머리는', 140, 200, icon='flag', tone='green', size=60),
    tag('거울 너머 막내 직원을 몰아세우는 원장', '거울', 140, 350, icon='user-x', tone='red', size=56),
]},
{'from': '가위 솜씨엔', 'bg': 'ph_hair_salon', 'items': [
    tag('솜씨는 문제없음', '가위', 140, 200, icon='scale', size=58),
    stamp('다음 달엔 다른 미용실', '다음', x=760, y=480, size=96),
]},
{'from': '그래도 결국 시장 탓', 'enter': 'flash', 'bg': 'ph_milk_aisle', 'items': [
    cover('+0.02'),
    tag('그래도 시장 탓?', '시장', 700, 70, icon='alert-triangle', size=60),
    raw('<style>.side{top:250px; gap:22px}</style>'),
    *split('반대편'),
    side('l', '반대편', logo('maeil', '반대편', 0, 0, h=72), tag('2012  1조 723억', '2012년', 0, 0, icon='chart-bar', size=46),
         tag('2020  1조 4,630억', '2020년엔', 0, 0, icon='trending-up', tone='green', size=50)),
    side('r', '남양유업이', logo('namyang', '남양유업이', 0, 0, h=72), tag('같은 저출산·시장', '같은', 0, 0, icon='users', size=46),
         tag('2014 1분기 첫 역전', '1분기', 0, 0, icon='arrows-exchange', tone='red', size=50)),
]},
{'from': '시장이 문제였다면', 'bg': 'st_chart', 'items': [
    cover('+0.02'),
    tag('시장 문제면 둘 다 미끄러졌어야', '시장이', 360, 220, icon='scale', size=62),
    stamp('원인은 시장 밖', '밖에', x=720, y=460, size=120),
]},
{'from': '이 명단에 없는 곳은', 'enter': 'mask', 'bg': 'ph_bakery', 'items': [
    tag('명단 밖은 안전할까?', '명단에', 140, 180, icon='alert-triangle', tone='dark', size=62),
    tag('단골 빵집 · 마트 · 내 회사', '단골', 140, 330, icon='building-store', size=60),
    tag('윗사람의 태도는 손님 귀에 빨리 들어간다', '윗사람이', 140, 480, icon='users', tone='red', size=54),
]},
# ---------------- 30초 자가진단 ----------------
{'from': '지금 바로 30초', 'enter': 'flash', 'bg': 'ph_basket', 'items': [
    cover('+0.02'),
    big('30초 자가진단', '자가진단을', y=150, size=140, color='#ffd166'),
    tag('자주 쓰는 브랜드 · 내 회사 하나', '자주', 520, 420, icon='shopping-cart', size=60),
]},
{'from': '하나.', 'bg': 'ph_basket', 'items': [
    cover('+0.02'),
    tag('□ 제품보다 오너 얼굴이 먼저 떠오른다', '+0.05', 160, 180, icon='user', size=56),
    tag('□ 최근 1년, 직원·대리점과 다툰 뉴스', '둘.', 160, 340, icon='file-invoice', size=56),
    tag('□ 사과가 늦었거나 다른 사람이 고개 숙였다', '셋.', 160, 500, icon='alert-triangle', size=56),
]},
{'from': '몇 개 해당하시나요', 'enter': 'slide', 'bg': 'ph_basket', 'items': [
    cover('+0.02'),
    tag('0개  안심', '0개라면', 260, 150, icon='flag', tone='green', size=62),
    tag('1개  지켜볼 만', '한', 260, 290, icon='alert-triangle', size=62),
    tag('2개  손님은 이미 이동 중', '두', 260, 430, icon='trending-down', tone='red', size=62),
    tag('3개  다음 순위표 후보', '세', 260, 570, icon='flame', tone='red', size=66),
]},
# ---------------- 쌍용 → KG모빌리티 ----------------
{'from': '그래도 희망은', 'enter': 'flash', 'bg': 'ph_car_factory', 'items': [
    tag('그래도 희망', '희망은', 140, 160, icon='flag', tone='green', size=62),
    tag('2009 · 2,646명 감원 발표', '줄이겠다고', 140, 300, icon='user-x', tone='red', size=58),
    igrid('user', 10, '전체의', lit=4, half=False, litat='열', cols=10, y=470, size=100, tone='bad'),
]},
{'from': '쌍용자동차입니다', 'bg': 'ph_car_factory', 'items': [
    tag('쌍용자동차', '쌍용자동차입니다', 140, 180, icon='car', tone='dark', size=66),
    tag('해고자와 가족들의 긴 고통', '해고자와', 140, 330, icon='mood-sad', size=58),
    tag('2018 · 복직 합의', '복직에', 140, 480, icon='heart-handshake', tone='green', size=58),
]},
{'from': '주인이 여러 번', 'bg': 'ph_suv_road', 'items': [
    tag('2022 · 새 주인', '새', 140, 180, icon='key', size=58),
    logo('kgm', '케이지모빌리티로', 140, 320, h=72),
    stamp('16년 만에 영업 흑자', '흑자를', x=860, y=520, size=100),
]},
{'from': '무엇으로 일어섰을까요', 'bg': 'ph_suv_road', 'items': [
    cover('+0.02'),
    swapnum('사과문', '차 한 대', '+0.1', '차', y=260, size=160, tone='good'),
    tag('결국 실력', '실력이었습니다', 700, 560, icon='trending-up', tone='green', size=70),
]},
# ---------------- 마무리 ----------------
{'from': '처음에 말씀드린 그 우유', 'enter': 'mask', 'bg': 'ph_conv_fridge', 'items': [
    tag('바코드부터 확인하는 손', '바코드부터', 140, 200, icon='scan', size=60),
    tag('어느 칸으로? → 그 회사가 안에서 사람을 대한 방식', '그', 140, 350, icon='users', tone='red', size=52),
]},
{'from': '그 답은 내년 봄', 'bg': 'st_hypermarket', 'items': [
    line('답은 동네 마트 냉장 진열대가 먼저', '진열대가', x=None, y=400, cls='say', size=76, center=True),
]},
{'from': '댓글로 하나만', 'enter': 'flash', 'bg': 'ph_crowd_walk_away', 'items': [
    cover('+0.02'),
    tag('댓글로 골라 주세요', '댓글로', 660, 70, icon='heart-handshake', tone='dark', size=56),
    raw('<style>.side{top:270px}</style>'),
    *split('그래도'),
    side('l', '그래도', tag('그래도 산다', '그래도', 0, 0, icon='shopping-cart', tone='green', size=70)),
    side('r', '아니면', tag('절대 안 산다', '절대', 0, 0, icon='hand-stop', tone='red', size=70)),
    tag('+ 조용히 끊은 브랜드와 계기', '조용히', 520, 640, icon='file-invoice', size=56),
]},
{'from': '숫자 뒤에 숨은', 'enter': 'fade', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    line('숫자 뒤에 숨은 사람의 마음', '숫자', x=None, y=300, cls='say', size=80, center=True),
    line('지혜호수 경제심리연구소', '지혜호수', x=None, y=440, cls='head', size=110, center=True),
]},
]
