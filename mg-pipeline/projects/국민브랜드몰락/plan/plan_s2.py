"""본편 2: 5위 미스터피자 · 4위 남양유업 · 3위 대우 (자막 136~293)."""
from gen import (tag, logo, stamp, roll, split, side, big, cover, ranks, punch, pictos, line, raw, chip, flow, glow,
                 article, inset, rankbadge, swapnum, igrid, donut, bubble)

def RB(rank, name, first=False): return rankbadge(rank, name, '+0.05', still=not first)
O76 = {7: ('피죤', None), 6: ('푸르밀', None)}

S2 = [
# 6:33 여기까지는 열 개 중 일곱은 남았다 → 5위부터는 간판까지
{'from': '여기까지는 열 개 중', 'enter': 'slide', 'bg': 'st_crowd_mall', 'items': [
    cover('+0.02'),
    tag('7·6위: 간판은 지켰다', '+0.1', 520, 160, icon='building-store', tone='green', size=62),
    tag('5위부터: 매장 · 매출 · 회장 자리까지', '5위부터는', 360, 330, icon='trending-down', tone='red', size=62),
    ranks('5위부터는', n=7, now=5, opened=O76, top=520, sfx=None),
]},
# ---------------- 5위 미스터피자 ----------------
{'from': '2016년 4월 6일', 'enter': 'mask', 'bg': 'ph_owners_bow_img', 'items': [
    tag('2016. 4. 6 · 서울 서초구 본사 앞', '+0.1', 140, 200, icon='map-pin', tone='dark', size=58),
    bubble('피해자와 국민께 진심으로 사과드립니다', '피해자와', 300, 380, size=56),
]},
{'from': '그런데 고개 숙인', 'bg': 'st_shutter', 'items': [
    cover('+0.02'),
    swapnum('잘못한 사람', '점주들', '+0.1', '회장을', y=300, size=130),
    tag('회장 대신 사과', '대신해', 700, 580, icon='user-x', tone='red', size=66),
]},
{'from': '시간을 26년', 'enter': 'flash', 'bg': 'ph_campus_street_1990', 'items': [
    tag('1990 · 이화여대 앞 1호점', '1호점이', 140, 220, icon='building-store', size=62),
    ranks('+0.4', n=7, now=5, opened={**O76, 5: ('미스터피자', '미스터피자')}, top=520),
]},
{'from': '자녀 생일날', 'bg': 'ph_pizza_family', 'items': [
    RB(5, '미스터피자', first=True),
    tag('생일 · 수능 끝난 저녁', '생일날', 140, 230, icon='heart-handshake', size=62),
    stamp('왕년의 1위', '왕년의', x=1180, y=560, size=110),
]},
{'from': '2015년까지 국내', 'bg': 'st_pizza', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    roll(0, 400, '+0.1', y=230, size=190, suffix='여 개', tone='good'),
    tag('2015년 국내 매장', '+0.05', 720, 120, icon='building-store', tone='green', size=58),
    tag('중국 100호점', '백호점을', 760, 520, icon='world', size=60),
]},
{'from': '그런데 2016년 4월', 'enter': 'slide', 'bg': 'ph_guard_booth', 'items': [
    RB(5, '미스터피자'),
    tag('회장, 건물 경비원 폭행', '경비원을', 140, 230, icon='user-x', tone='red', size=66),
    stamp('벌금 200만 원 약식기소', '벌금', x=860, y=480, size=96),
]},
{'from': '그 뒤 반년 동안', 'bg': 'ph_pizza_shutter', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    tag('반년 새 문 닫은 가맹점', '그', 560, 140, icon='building-store', tone='dark', size=60),
    big('약 60곳', '가량입니다', y=270, size=180, color='#ff5a5a'),
    swapnum('400여 개', '367개', '+0.1', '줄어듭니다', y=560, size=120),
]},
{'from': '동네에 미스터피자가', 'bg': 'ph_pizza_shutter', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    tag('동네 매장 7곳 중', '일곱', 660, 180, icon='map-pin', size=62),
    igrid('building-store', 7, '+0.1', drop=1, dropat='셔터가', cols=7, y=360, size=150, tone='bad'),
]},
{'from': '이쯤 되면 폭행', 'bg': 'st_pizza', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    tag('폭행 한 번에 손님이 떠났다?', '폭행', 400, 240, icon='alert-triangle', size=72, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=480, size=160),
]},
{'from': '폭행은 문을 연', 'enter': 'mask', 'bg': 'ph_cheese_boxes', 'items': [
    RB(5, '미스터피자'),
    tag('폭행은 시작일 뿐', '폭행은', 140, 180, icon='key', tone='dark', size=60),
    tag('이듬해 검찰 수사', '검찰', 140, 320, icon='gavel', size=60),
]},
{'from': '회장 친동생의 회사가', 'bg': 'ph_cheese_boxes', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    *[tag(t, a, x, 300, icon=i, tone=tn, size=50) for t, a, x, i, tn in
      (('치즈 공급사', '치즈', 90, 'cheese', ''), ('회장 친동생 회사', '친동생의', 620, 'user', 'red'), ('가맹점', '유통', 1380, 'building-store', ''))],
    tag('통행세', '통행세는', 780, 520, icon='receipt', tone='dark', size=58),
    big('57억 원', '57억', y=630, size=120, color='#ff5a5a'),
]},
{'from': '본사를 떠난 점주의', 'bg': 'ph_pizza_shutter', 'items': [
    RB(5, '미스터피자'),
    tag('떠난 점주 옆에 직영점 · 할인 공세', '직영점을', 140, 220, icon='building-store', tone='red', size=58),
    tag('회사 설명: 외식이 배달로 바뀐 탓', '회사는', 140, 380, icon='truck-delivery', tone='ghost', size=56),
]},
{'from': '2017년 6월', 'enter': 'flash', 'bg': 'ph_press_bow', 'items': [
    RB(5, '미스터피자'),
    tag('2017. 6 · 회장 대국민 사과 · 사퇴', '+0.1', 140, 200, icon='microphone', tone='dark', size=58),
    tag('여론은 차가웠다', '여론은', 140, 350, icon='snowflake', size=62),
]},
{'from': '1년 전엔 점주들이', 'bg': 'ph_press_bow', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', tag('1년 전: 점주들이 대신', '+0.1', 0, 0, icon='users', size=48)),
    side('r', '이번엔', tag('이번엔: 회장이 직접', '이번엔', 0, 0, icon='user', tone='red', size=48), tag('받아 주는 손님 없음', '받아', 0, 0, icon='user-x', tone='dark', size=48)),
]},
{'from': '그 물건을 누가', 'enter': 'mask', 'bg': 'ph_pizza_box_walk', 'items': [
    RB(5, '미스터피자'),
    cover('+0.02'),
    tag('누가 드는가 = 물건의 뜻', '누가', 520, 180, icon='package', size=62),
    glow('정체성 신호', '정체성', y=400, size=120),
]},
{'from': '피자 상자 위 로고가', 'bg': 'ph_pizza_box_walk', 'items': [
    RB(5, '미스터피자'),
    swapnum('로고', '회장의 얼굴', '+0.1', '얼굴로', y=280, size=120),
    tag('경비실 앞이 괜히 마음에 걸린다', '경비실', 360, 560, icon='alert-triangle', tone='dark', size=56),
]},
{'from': '미스터피자는 한 사람의', 'enter': 'slide', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', logo('mrpizza', '+0.1', 0, 0, h=72), tag('한 사람의 손버릇', '+0.3', 0, 0, icon='user', size=56)),
    side('r', '다음', logo('namyang', '다음', 0, 0, h=72), tag('회사 전체의 말투', '말투가', 0, 0, icon='microphone', tone='red', size=56)),
]},
# ---------------- 4위 남양유업 ----------------
{'from': '계산 문제 하나', 'enter': 'flash', 'bg': 'st_calc', 'items': [
    cover('+0.02'),
    tag('계산 문제', '계산', 720, 130, icon='coin', tone='dark', size=60),
    flow([('4,160억 원', '+0.4'), ('365일', '+1.2')], y=280, size=100),
    big('하루 11억+', '하루에', y=520, size=180, color='#ff5a5a'),
]},
{'from': '매일 아침 11억', 'bg': 'st_money', 'items': [
    tag('매일 아침 11억 원어치 덜 팔림', '매일', 140, 230, icon='trending-down', tone='red', size=62),
    tag('어느 회사?', '어느', 140, 380, icon='alert-triangle', tone='dark', size=66),
]},
{'from': '한때 유업계 큰형님', 'bg': 'ph_formula_can', 'items': [
    ranks('+0.1', n=7, now=4, opened={**O76, 5: ('미스터피자', None), 4: ('남양유업', '큰형님이라')}, top=520),
    tag('유업계 큰형님', '큰형님이라', 680, 200, icon='flag', size=66),
]},
{'from': '1964년', 'bg': 'st_baby_bottle', 'items': [
    RB(4, '남양유업', first=True),
    tag('1964년 · 한국 아기 분유', '분유를', 140, 230, icon='baby-carriage', size=62),
    tag('첫아이의 분유 통', '첫아이', 140, 380, icon='heart-handshake', tone='ghost', size=60),
]},
{'from': '분유와 발효유에서', 'bg': 'st_chart', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    tag('분유 · 발효유 1등', '분유와', 160, 160, icon='flag', tone='green', size=62),
    tag('황제주 (1주 100만 원+)', '황제주로', 160, 310, icon='coin', size=62),
    roll(0, 13650, '2012년', y=470, size=150, suffix='억 원', tone='good'),
]},
# 9:51 녹음 파일 (클립 — 중반 반전)
{'from': '그런데 2013년 5월', 'enter': 'flash', 'bg': 'ph_phone_recording', 'items': [
    RB(4, '남양유업'),
    tag('2013. 5 · 녹음 파일 공개', '+0.1', 140, 200, icon='microphone', tone='red', size=64),
    tag('영업사원 → 대리점주 욕설', '욕설을', 140, 350, icon='user-x', size=60),
]},
{'from': '원치 않는 물량을', 'bg': 'ph_agency_storage', 'items': [
    RB(4, '남양유업'),
    stamp('밀어내기', '밀어내기였죠', x=900, y=420, size=140),
    tag('원치 않는 물량 떠넘기기', '원치', 140, 220, icon='package', tone='dark', size=60),
]},
{'from': '주가는 얼마나', 'bg': 'st_stock_down', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    swapnum('100만 원+', '100만 원 아래', '+0.3', '내려앉았습니다', y=260, size=140),
    tag('보름도 안 돼', '보름도', 700, 520, icon='clock', tone='dark', size=60),
    tag('6분기 연속 적자', '여섯', 660, 660, icon='trending-down', tone='red', size=60),
]},
{'from': '이쯤 되면 우유 시장이', 'bg': 'ph_milk_aisle', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    tag('우유 시장이 쪼그라든 탓?', '시장이', 400, 240, icon='milk', size=72, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=480, size=160),
]},
{'from': '2013년부터 2년 동안', 'bg': 'st_chart', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', tag('우유 소매시장', '+0.1', 0, 0, icon='milk', size=56), big('-1.6%', '+0.3', y=0, size=150, color='#9aa3b2')),
    side('r', '회사만', tag('이 회사만', '회사만', 0, 0, icon='trending-down', tone='red', size=56), big('크게 미끄러짐', '미끄러졌습니다', y=0, size=90, color='#ff5a5a')),
]},
{'from': '그리고 상처가', 'enter': 'mask', 'bg': 'st_stock_down', 'items': [
    RB(4, '남양유업'),
    tag('2019 · 분유 녹가루 논란', '녹가루', 140, 200, icon='alert-triangle', size=60),
    tag('2021 · “코로나 77.8% 억제” 발표', '발효유가', 140, 350, icon='microphone', tone='red', size=60),
    tag('다시 불매에 불', '불매에', 140, 500, icon='flame', tone='dark', size=60),
    stamp('회장 사퇴', '물러났습니다', x=1200, y=600, size=100),
]},
{'from': '2020년 매출은', 'bg': 'st_stock_down', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    swapnum('1조 3,650억', '9,489억', '+0.1', '+0.9', y=200, size=130),
    tag('8년 새 -30.5%', '8년', 700, 420, icon='trending-down', tone='red', size=66),
    igrid('home', 10, '열', lit=0, drop=3, dropat='세', y=560, size=100, tone='bad'),
]},
{'from': '영업이익은', 'bg': 'st_chart', 'items': [
    RB(4, '남양유업'),
    big('영업적자 771억', '+0.1', y=380, size=150, color='#ff5a5a'),
]},
{'from': '사람들은 바코드', 'bg': 'ph_barcode_scan', 'items': [
    RB(4, '남양유업'),
    tag('바코드 판독기까지 등장', '판독기까지', 140, 230, icon='scan', tone='red', size=62),
]},
{'from': '줄이 줄을 부르고', 'enter': 'mask', 'bg': 'st_queue', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    glow('사회적 증거', '사회적', y=260, size=120),
    pictos(8, '판독기에', '피하면', 300, 520, dx=900, fade=True, dur=1.8),
]},
{'from': '처음에 계산한 하루', 'bg': 'ph_milk_aisle', 'items': [
    RB(4, '남양유업'),
    cover('+0.02'),
    tag('하루 11억 원', '처음에', 700, 200, icon='coin', tone='red', size=66),
    flow([('남양 칸', '그'), ('바로 옆 칸', '옆')], y=420, size=96),
]},
{'from': '여기까지는 약자를', 'enter': 'slide', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    tag('7~4위: 약자를 향한 말투 · 손버릇', '약자를', 360, 180, icon='user-x', tone='dark', size=58),
    tag('3위부터: 숫자 자체가 거짓말', '숫자', 420, 340, icon='file-invoice', tone='red', size=64),
    ranks('+0.3', n=7, now=3, nowat='부아가', opened={**O76, 5: ('미스터피자', None), 4: ('남양유업', None)}, top=520, sfx=None),
]},
# ---------------- 3위 대우 ----------------
{'from': '1998년', 'enter': 'flash', 'bg': 'ph_ledger', 'items': [
    tag('1998년 · 결산 직전 회장의 지시', '지시를', 140, 180, icon='user', tone='dark', size=58),
    swapnum('적자 1조 원', '흑자 1,000억 원', '+1.4', '흑자로', y=400, size=110, tone='good'),
    stamp('판결로 확정', '확정된', x=1180, y=640, size=96),
]},
{'from': '회장의 이름은', 'bg': 'ph_tower_1990s', 'items': [
    ranks('+0.05', n=7, now=3, opened={**O76, 5: ('미스터피자', None), 4: ('남양유업', None), 3: ('대우', '대우였습니다')}, top=520),
    tag('김우중 회장', '김우중', 720, 200, icon='user', size=66),
]},
{'from': '1967년, 서른 살', 'bg': 'ph_trade_office_1967', 'items': [
    RB(3, '대우', first=True),
    tag('1967 · 서른 살 청년의 무역회사', '무역회사를', 140, 230, icon='building-skyscraper', size=58),
]},
{'from': '30년 남짓 만에', 'bg': 'ph_tower_1990s', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    big('재계 2위', '2위', y=200, size=170, color='#3fe08a'),
    tag('계열사 41개', '계열사는', 700, 470, icon='building-skyscraper', tone='green', size=62),
    bubble('세계는 넓고 할 일은 많다', '세계는', 560, 620, size=56),
]},
{'from': '대우 배지 단', 'bg': 'ph_badge_photo', 'items': [
    RB(3, '대우'),
    tag('거실 벽의 자랑', '거실', 1100, 230, icon='home', size=60),
]},
{'from': '그런데 외환위기가', 'enter': 'slide', 'bg': 'ph_imf_bank_line', 'items': [
    RB(3, '대우'),
    tag('외환위기 · 회사채·어음 발행 막힘', '외환위기가', 140, 200, icon='alert-triangle', tone='red', size=58),
    tag('1999. 8 · 계열사 12곳 워크아웃', '워크아웃에', 140, 350, icon='building-bank', size=58),
    stamp('사실상 해체', '해체였습니다', x=1150, y=580, size=110),
]},
{'from': '이쯤 되면 외환위기라는', 'bg': 'ph_imf_bank_line', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    tag('외환위기 폭풍에 쓰러졌다?', '폭풍에', 400, 240, icon='alert-triangle', size=72, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=480, size=160),
]},
{'from': '폭풍은 이미', 'bg': 'st_contract', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    tag('폭풍은 기운 집을 드러냈을 뿐', '폭풍은', 400, 140, icon='home', tone='dark', size=58),
    tag('부풀린 장부', '부풀려진', 260, 300, icon='file-invoice', tone='red', size=58),
    big('41조 1,000억', '41조', y=410, size=150, color='#ff5a5a'),
    tag('그 장부로 빌린 돈  9조 9,000억', '빌린', 380, 640, icon='building-bank', size=58),
]},
{'from': '수출대금을 조작하고', 'bg': 'st_contract', 'items': [
    RB(3, '대우'),
    tag('수출대금 조작 · 빚을 장부에서 빼기', '수출대금을', 140, 200, icon='file-invoice', tone='red', size=58),
]},
{'from': '해체 무렵 부채는', 'bg': 'st_city_night', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', tag('부채', '+0.1', 0, 0, icon='trending-down', tone='red', size=58), big('89조', '+0.3', y=0, size=170, color='#ff5a5a')),
    side('r', '자산은', tag('자산', '자산은', 0, 0, icon='building-bank', size=58), big('76조', '자산은', y=0, size=170, color='#fff')),
    tag('갚을 돈이 13조 더 많다', '갚을', 600, 680, icon='alert-triangle', tone='dark', size=58),
]},
{'from': '공정하게 덧붙이겠습니다', 'enter': 'mask', 'bg': 'st_court', 'items': [
    RB(3, '대우'),
    tag('김 전 회장 측 주장: 정부와 맞서다 불이익', '김', 140, 200, icon='scale', tone='ghost', size=56),
    tag('지금도 논쟁 중', '논쟁', 140, 350, icon='scale', size=56),
    stamp('장부 조작은 판결로 확정', '다만', x=760, y=560, size=90),
]},
{'from': '가계부로 바꿔', 'enter': 'slide', 'bg': 'ph_household_ledger', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    tag('이번 달 가계부', '가계부로', 720, 120, icon='file-invoice', tone='dark', size=58),
    swapnum('-1만 원', '+1,000원', '이번', '남았다고', y=300, size=150, tone='good'),
    tag('그 가계부로 은행 대출', '은행', 600, 600, icon='building-bank', tone='red', size=62),
]},
{'from': '그해 대우자동차의', 'bg': 'ph_bank_loan', 'items': [
    RB(3, '대우'),
    tag('대우자동차의 장부가 꼭 그랬다', '대우자동차의', 140, 220, icon='car', tone='red', size=58),
]},
{'from': '처음 본 숫자는', 'enter': 'mask', 'bg': 'ph_tower_1990s', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    glow('기준점 효과', '기준점', y=200, size=120),
    tag('은행 · 투자자 · 취업 준비생', '은행도', 460, 470, icon='users', size=58),
    tag('휜 잣대 → 모든 길이가 틀림', '잣대가', 460, 610, icon='alert-triangle', tone='red', size=58),
]},
{'from': '1,000억 원 흑자로 시작한', 'bg': 'ph_household_ledger', 'items': [
    RB(3, '대우'),
    cover('+0.02'),
    swapnum('첫 장 +1,000억', '마지막 장 -13조', '+0.1', '마지막', y=380, size=110),
]},
]
