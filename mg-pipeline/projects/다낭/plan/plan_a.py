"""다낭 편 — 인트로 · 1막 · 2막 (자막 1~75, 0:00~5:16). 앞쪽 집중: 2~4초 컷, 카메라워크, 액자 축소, 복선 카드, 세피아 회상."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, punch, glow, igrid, raw, stack, swapnum, card, bubble, donut, bars,
                 shrink, arrow, circ, uline, foreshadow, flipcard, PAST)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')

A = [
# ================= 인트로 =================
{'from': '다낭 한시장 앞', 'enter': 'flash', 'bg': 'th_hanmarket_street', 'cam': [('push', '+0.1', 50, 40, 1.15)], 'items': [
    BRIGHT,
    hook('베트남 <strong>다낭</strong>', '+0.05', y=560, size=170),
    tag('한시장 앞 골목', '+0.3', 120, 140, icon='map-pin', tone='dark', size=60),
]},
{'from': '간판은 한글인데', 'enter': 'zoom', 'bg': 'ph_hanmarket_signs', 'cam': [('crash', '한국어가', 50, 30, 1.45)], 'items': [
    BRIGHT,
    tag('간판은 한글', '간판은', 120, 140, icon='building-store', tone='dark', size=64),
    stamp('손님은 외국인', '아닙니다', x=900, y=560, size=110),
]},
{'from': '올해 베트남 다낭을', 'enter': 'strips', 'bg': 'ph_review_phone', 'items': [
    BRIGHT,
    tag('다녀온 여행객의 후기', '+0.1', 120, 140, icon='device-mobile', tone='dark', size=58),
    bubble('한국어 간판은 그대로인데, 한국 사람은 잘 안 보여요', '한국어', 160, 560, size=48),
]},
{'from': '그래서 요즘 이런 말이', 'enter': 'flash', 'bg': 'ph_empty_korean_shop', 'cam': [('push', '+0.1', 50, 45, 1.2)], 'items': [
    BRIGHT,
    hook('“다낭은<br><strong>끝났다</strong>”', '끝났다', y=300, size=180),
]},
{'from': '그런데 숫자는 정반대를', 'enter': 'flash', 'bg': 'th_beach_full', 'cam': [('crash', '정반대를', 50, 50, 1.35)], 'items': [
    cover('+0.02'),
    flashhit('정반대를'),
    tag('그런데 숫자는 정반대', '정반대를', None, 330, icon='alert-triangle', tone='red', size=110, until='외국인은'),
    tag('2025 다낭을 찾은 외국인', '외국인은', 560, 170, icon='users', tone='dark', size=60),
    roll(0, 760, '칠백육십만', y=300, size=230, suffix='만 명', tone='good', dur=0.9),
    tag('+25% · 역대 최대', '이십오 퍼센트:이십오', 640, 620, icon='trending-up', tone='green', size=66),
]},
{'from': '손님은 넘쳐나는데', 'enter': 'zoom', 'bg': 'ph_airport_arrivals_crowd', 'items': [
    BRIGHT,
    hook('손님은 넘치는데<br><strong>왜 끝났다?</strong>', '+0.05', y=300, size=150),
]},
{'from': '흔히들 바가지', 'enter': 'wipe', 'bg': 'ph_taxi_meter_night', 'items': [
    tag('흔한 설명: 바가지', '바가지', 120, 140, icon='alert-triangle', tone='red', size=64),
    shrink('ph_inspection_officers', '단속에', 1150, 170, 660, 372, cap='다낭시 바가지 단속'),
    arrow('단속에', 900, 260, 1135, 330),
]},
{'from': '그런데 바가지가 이유라면', 'enter': 'zoom', 'bg': 'ph_tourists_mixed', 'cam': [('push', '+0.2', 50, 60, 1.2)], 'items': [
    cover('+0.02'),
    flipcard('바가지라면 모두 줄었어야', '다른 나라 손님은 늘었다', '바가지가', '늘었습니다', y=330, size=76),
]},
{'from': '이천이십오 년 팔월 일일 밤', 'enter': 'flash', 'bg': 'ph_ceremony_stage', 'items': [
    BRIGHT,
    tag('2025.8.1 밤 · 다낭 바닷가 공원', '+0.1', 120, 140, icon='calendar', tone='dark', size=58),
    big('100만 번째 한국인 손님', '백만', y=560, size=110, color='#ffd400'),
    glow('그날 이후, 숫자가 움직였다', '움직이기', y=720, size=70),
]},
# ================= 1막 한국인이 키운 도시 =================
{'from': '그 한시장 골목으로', 'enter': 'wipe', 'bg': 'th_hanmarket_street', 'cam': [('pull', '+0.05', 40, 35, 1.8)], 'items': [
    BRIGHT,
    tag('한글 간판이 많은 이유', '한글', 120, 140, icon='building-store', tone='dark', size=60),
    tag('손님 대부분이 한국인이던 시절', '대부분이', 120, 600, icon='users', tone='red', size=58),
]},
{'from': '다낭과 한국의 인연은', 'enter': 'zoom', 'bg': 'ph_flight_board', 'cam': [('push', '+0.1', 50, 40, 1.25)], 'items': [
    BRIGHT,
    tag('한국–다낭 직항', '직항이', 120, 140, icon='flag', tone='dark', size=60),
    hook('2016년부터<br><strong>외국인 손님 1위</strong>', '이천십육', y=380, size=130),
]},
{'from': '비행기 숫자를 보면', 'enter': 'flash', 'bg': 'ph_plane_takeoff', 'items': [
    cover('+0.02'),
    tag('한국–다낭 일주일 항공편', '+0.05', 560, 150, icon='flag', tone='dark', size=58),
    bars([('처음', 7 / 150, '주 7편', '칠 편', True), ('2025년', 1.0, '주 150편', '백오십', False)], top=300),
    tag('항공사 12곳 · 20배+', '이십 배', 620, 620, icon='trending-up', tone='green', size=62),
    foreshadow('주 150편', '이 비행기', label='이 숫자, 뒤에서 다시'),
]},
{'from': '쉽게 말하면 이렇습니다', 'enter': 'strips', 'bg': 'ph_korean_menu_restaurant', 'cam': [('push', '+0.1', 60, 45, 1.2)], 'items': [
    BRIGHT,
    tag('한국 손님으로 문 열고, 한국 손님으로 컸다', '커졌습니다', 120, 140, icon='building-store', tone='red', size=54),
    tag('메뉴판 · 간판 · 인사말 = 한국어', '메뉴판도', 120, 600, icon='flag', tone='dark', size=56),
]},
{'from': '어쩌면 여러분 댁에도', 'enter': 'wipe', 'bg': 'ph_family_resort', 'items': [
    BRIGHT,
    tag('첫 해외 · 첫 효도여행', '효도', 120, 140, icon='heart-handshake', tone='red', size=62),
    tag('가깝고 만만한 곳', '만만한', 120, 600, icon='home', tone='dark', size=58),
]},
{'from': '그런데 손님 한 부류에', 'enter': 'zoom', 'bg': 'ph_single_customer_shop', 'cam': [('push', '+0.1', 45, 50, 1.25)], 'items': [
    cover('+0.02'),
    tag('약점: 손님이 한 부류', '약점이', 600, 200, icon='alert-triangle', tone='red', size=66),
    hook('전성기에 이미<br><strong>신호가 있었다</strong>', '신호가', y=420, size=130),
]},
# ================= 2막 전성기 (회상은 세피아) =================
{'from': '다낭의 전성기는', 'enter': 'flash', 'bg': 'ph_mykhe_crowded', 'items': [
    PAST, cover('+0.02'),
    tag('2019 · 다낭의 전성기', '+0.05', 120, 140, icon='calendar', tone='dark', size=58),
    donut(50, '둘 중', label='외국인 둘 중 한 명 = 한국인', x=760, y=250, d=420, tone='good'),
    tag('2위 중국은 그 절반도 안 됨', '절반에도', 520, 720, icon='chart-bar', tone='dark', size=54),
]},
{'from': '미케비치 해변에서는', 'enter': 'zoom', 'bg': [('ph_mykhe_crowded', None), ('ph_golden_bridge', '바나힐')], 'items': [
    PAST,
    tag('미케비치', '미케비치', 120, 140, icon='map-pin', tone='dark', size=60, until='바나힐'),
    tag('바나힐 골든브릿지', '골든브릿지', 120, 140, icon='map-pin', tone='red', size=60),
    shrink('ph_photo_album', '사진첩에도', 1180, 170, 640, 360, cap='내 사진첩 속 그 다리'),
]},
{'from': '코로나가 지나고', 'enter': 'strips', 'bg': 'ph_airport_arrivals_crowd', 'items': [
    cover('+0.02'),
    tag('2024 다낭을 찾은 한국인', '이천이십사', 600, 150, icon='users', tone='dark', size=58),
    roll(0, 168, '백육십팔만', y=270, size=220, suffix='만 명', tone='good', dur=0.8),
    tag('하루 약 4,600명', '사천육백', None, 560, icon='clock', tone='dark', size=58),
    tag('매일 여객기 20대 가까이', '스무', None, 700, icon='flag', tone='red', size=54),
]},
{'from': '여행 커뮤니티 후기들도', 'enter': 'wipe', 'bg': 'ph_immigration_queue', 'cam': [('push', '+0.1', 50, 55, 1.2)], 'items': [
    BRIGHT,
    bubble('비행기 세 대가 한꺼번에… 입국 심사만 두 시간!', '세 대가', 160, 300, size=48),
    glow('줄 서는 가게는 언제까지 1등일지 묻지 않는다', '언제까지', y=640, size=66),
]},
{'from': '같은 시기, 한국 사람들의', 'enter': 'flash', 'bg': 'ph_japan_street', 'items': [
    cover('+0.02'),
    hook('또 다른 이름<br><strong>일본</strong>', '일본입니다', y=150, size=130),
    roll(0, 945, '구백사십오', y=470, size=170, suffix='만 명', tone='good', dur=0.8),
    foreshadow('2025 방일 한국인 945만 명', '기억해'),
]},
{'from': '서랍 이야기도', 'enter': 'zoom', 'bg': 'ph_vnd_drawer', 'cam': [('push', '+0.1', 50, 60, 1.3)], 'items': [
    BRIGHT,
    tag('쓰다 남은 베트남 동 지폐', '동', 120, 140, icon='coin', tone='dark', size=60),
    tag('그때와 지금, 값어치는 같을까?', '값어치는', 120, 600, icon='scale', tone='red', size=58),
]},
{'from': '이제 균열입니다', 'enter': 'flash', 'bg': 'ph_report_documents', 'cam': [('push', '+0.1', 50, 50, 1.25)], 'items': [
    cover('+0.02'),
    tag('2024 가을 · 다낭시 관광 당국 자료', '자료에', 440, 160, icon='file-invoice', tone='dark', size=56),
    big('-8.5%', '팔 점', y=290, size=230, color='#ff5a5a'),
    circ('팔 점', 640, 270, 640, 300),
    tag('9개월 한국인, 2019년보다 적음', '적었다는', 470, 640, icon='trending-down', tone='red', size=56),
]},
{'from': '같은 자료에는', 'enter': 'strips', 'bg': 'ph_new_tourists_arrive', 'items': [
    BRIGHT,
    tag('늘어난 손님', '+0.1', 120, 140, icon='trending-up', tone='green', size=60),
    tag('대만', '대만', 120, 300, size=60), tag('인도', '인도', 420, 300, size=60), tag('호주', '호주', 720, 300, size=60), tag('러시아', '러시아', 1020, 300, size=60),
    glow('빈자리를 처음 보는 손님이 채운다', '조용히', y=660, size=70),
]},
]
