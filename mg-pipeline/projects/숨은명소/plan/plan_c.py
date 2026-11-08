"""숨은명소 TOP5 — 1위 서울 북악산 · 마무리 (자막 183~282)."""
from gen import (hook, flashhit, tag, stamp, big, cover, glow, raw, stack, card, flipcard, timeline, split, side,
                 puppet, particles, mgbg, rankbadge)
BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
SOFT = raw('<style>.bg{--dark:.7; --blur:0px}</style>')
C = [
{'from': '천구백육십팔 년 일월', 'enter': 'flash', 'bg': 'i_seoul_1968', 'cam': [('push', '+0.1', 50, 45, 1.2)], 'items': [
    BRIGHT,
    tag('1968.1.21 밤 · 청와대 뒷산', '+0.1', 120, 140, icon='calendar', tone='dark', size=56),
    stamp('출입 금지', '뒷산이었습니다', x=1100, y=520, size=110),
]},
{'from': '일 위는 서울 북악산', 'enter': 'flash', 'bg': [('v:s_seoul_wall', None), ('v:s_gyeongbok', '경복궁')], 'items': [
    SOFT, rankbadge('1', '서울 북악산', '일 위는'),
    tag('철책 · 초소 · 민간인 출입 금지', '철책이', 120, 200, icon='alert-triangle', tone='red', size=54),
]},
{'from': '그날 밤 내려온 일당', 'enter': 'zoom', 'bg': [('i_seoul_1968', None), ('v:s_seoul_night', '+10')], 'items': [
    BRIGHT,
    tag('반공 교육 시간에 들은 그 이름', '반공', 120, 140, icon='scan', tone='dark', size=54),
    glow('반세기 넘게 멀리서만 본 산', '멀리서만', y=600, size=64),
]},
{'from': '문이 조금씩 열리기', 'enter': 'wipe', 'bg': 'v:s_seoul_wall', 'items': [
    BRIGHT,
    tag('2006년 무렵 · 성곽 일부 구간부터', '이천육', 120, 140, icon='calendar', tone='dark', size=54),
    tag('청와대 바로 뒤쪽은 여전히 막힘', '여전히', 120, 300, icon='user-x', tone='red', size=54),
]},
{'from': '이 산의 문은 한 번에', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    tag('세 번에 나눠 열린 문', '한 번에', None, 130, icon='key', tone='dark', size=58),
    timeline([('2020.11', '북측 2.2km · 52년 만', '이천이십 년'), ('2022.4', '남동측 3km · 54년 만', '이천이십이'),
              ('2026.10', '마지막 한 조각은?', '+13', 1)], y=330),
]},
{'from': '이때 새로 열린 산의 넓이가', 'enter': 'zoom', 'bg': [('v:s_seoul_wall', None), ('v:s_hike_deck', '+10')], 'items': [
    cover('+0.02'),
    card('새로 열린 면적', '110만㎡', '백십만', 220, 200, w=660, h=300, vat='백십만'),
    card('여의도 공원', '4배+', '네 배가', 1040, 200, w=660, h=300, vat='네 배가'),
    tag('출입증 · 감시 카메라 촬영 금지', '출입증을', None, 620, icon='user-x', tone='dark', size=52),
]},
{'from': '그때 성곽 북쪽에 둘렀던', 'enter': 'wipe', 'bg': 'i_fortress_fence', 'items': [
    cover('+0.02'),
    card('걷어 낸 철책', '2.28km', '이 점 이팔', 220, 200, w=660, h=300, vat='이 점 이팔'),
    card('남겨 둔 철책', '189m', '백팔십구', 1040, 200, w=660, h=300, vat='백팔십구', hot=True),
    glow('그 시절을 기억하라고', '기억하라고', y=600, size=64),
]},
{'from': '그리고 마지막 남은 한 조각', 'enter': 'flash', 'bg': [('i_iron_gate', None), ('i_bugak_open', '오십구')], 'cam': [('crash', '오십구', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    tag('2026.10.17 오전 9시 · 남서측 1.32km', '시월', None, 150, icon='calendar', tone='red', size=52),
    big('59년 만', '오십구', y=290, size=210, color='#ffcf4a'),
    tag('24시간 개방', '스물네', None, 620, icon='clock', tone='green', size=58),
    puppet('c_hiker', '스물네', -400, 500, w=380, move='enter', dx=560, dur=5),
]},
{'from': '세 구간을 합치면', 'enter': 'zoom', 'bg': [('v:s_seoul_wall', None), ('v:s_gyeongbok', '+8'), ('v:s_bus_road', '광화문에서'), ('v:s_seoul_night', '청와대')], 'items': [
    BRIGHT,
    tag('탐방로 6km+ · 순찰과 카메라', '육 킬로미터', 120, 140, icon='map-pin', tone='dark', size=54),
    tag('광화문 → 창의문 안내소, 반나절', '광화문에서', 120, 300, icon='clock', tone='green', size=54),
    tag('원칙: 열린 경호, 낮은 경호', '열린 경호', 120, 460, icon='scan', tone='dark', size=54),
]},
{'from': '인트로에서 보신 그 철문이', 'enter': 'flash', 'bg': [('i_iron_gate', None), ('i_seoul_1968', '라디오와'), ('v:s_seoul_wall', '생각해')], 'items': [
    cover('+0.02'),
    flipcard('사건 하나로 닫힌 산', '세 번에 나눠 열렸다', '생각해', '세 번에', y=180, size=72),
    glow('열쇠는 산이 아니라 기관이 쥐고 있었다', '열쇠는', y=600, size=60),
]},
{'from': '여기서 우리 자신을', 'enter': 'zoom', 'bg': 'v:s_phone_news', 'items': [
    SOFT,
    tag('“언젠가 가 보지…”', '언젠가', None, 200, icon='device-mobile', tone='dark', size=64),
    glow('59년을 기다린 문 앞에서, 또 한 해를 미룬다', '미룹니다', y=600, size=56),
]},
# ================= 마무리 =================
{'from': '오늘의 순위를 다시', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    *stack([('5위 영양 자작나무숲 · 26년', '오 위,', 'map-pin', 'dark'), ('4위 화순 적벽 · 30년', '사 위,', 'map-pin', 'dark'),
            ('3위 거제 저도 · 47년', '삼 위,', 'map-pin', 'dark'), ('2위 나주 금성산 · 57년', '이 위,', 'map-pin', 'dark'),
            ('1위 서울 북악산 · 59년', '일 위,', 'flag', 'red')], x=440, y=110, gap=128, size=54),
]},
{'from': '처음 질문으로 돌아가', 'enter': 'zoom', 'bg': 'v:s_seoul_wall', 'items': [
    cover('+0.02'),
    *stack([('화순: 상생 협약', '화순은', 'file-invoice', 'green'), ('저도: 다섯 기관 협약', '저도는', 'file-invoice', 'green'),
            ('금성산: 나주시 · 공군 협약', '금성산은', 'file-invoice', 'green'), ('북악산: 기관 협의', '북악산은', 'file-invoice', 'green')],
           x=300, y=150, gap=135, size=54),
]},
{'from': '겉으로는 오랜 세월이', 'enter': 'flash', 'bg': 'i_iron_gate', 'cam': [('crash', '협약서', 50, 50, 1.3)], 'items': [
    cover('+0.02'), flashhit('협약서'),
    hook('문을 연 건 세월이 아니라<br><strong>협약서 한 장</strong>', '협약서', y=230, size=100),
    tag('약속이 바뀌면, 다시 닫힌다', '약속이 바뀌면', None, 640, icon='alert-triangle', tone='red', size=56),
]},
{'from': '동창회를 떠올려', 'enter': 'wipe', 'bg': 'i_reunion', 'items': [
    BRIGHT,
    tag('“다음에 보자” → 대개 못 본다', '다음에', 120, 140, icon='users', tone='dark', size=54),
    tag('날짜를 잡은 곳만 간다', '날짜를', 120, 300, icon='calendar', tone='green', size=56),
]},
{'from': '희망적인 소식도', 'enter': 'fade', 'bg': [('v:s_waterfall', None), ('i_waterfall_gorge', '+8'), ('v:s_birch', '청남대도')], 'items': [
    BRIGHT,
    tag('포천 비둘기낭 폭포 · 2012 천연기념물', '비둘기낭', 120, 140, icon='heart-handshake', tone='green', size=52),
    glow('반쯤 열린 문이 활짝 열리기도 한다', '활짝', y=600, size=62),
]},
{'from': '아직 닫힌 문도', 'enter': 'zoom', 'bg': 'v:s_mountain_peak', 'items': [
    BRIGHT,
    tag('아직 오를 수 없는 정상도 적지 않다', '적지', None, 150, icon='alert-triangle', tone='red', size=54),
    glow('오늘 명단은 지금까지 열린 문의 목록일 뿐', '목록일', y=600, size=58),
]},
{'from': '그럼 오늘 드린 세 가지', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    *stack([('① 내 차로 못 가는 곳', '내 차로', 'user-x', ''), ('② 하루 인원 제한', '하루 인원', 'users', ''),
            ('③ 시범 · 협약으로 열림', '시범이나', 'file-invoice', '')], x=380, y=130, gap=140, size=56),
    tag('둘이면 올해 안 · 셋이면 지금 예약', '셋 다라면', None, 620, icon='calendar', tone='red', size=54),
]},
{'from': '이 명단에 없는 곳은', 'enter': 'zoom', 'bg': 'i_iron_gate', 'items': [
    SOFT,
    tag('우리 동네 뒷산에도 철조망이?', '뒷산', None, 150, icon='scan', tone='dark', size=56),
    glow('다음 철문이 열릴 때, 그 앞에 설 사람은?', '다음 철문이', y=600, size=58),
]},
{'from': '댓글로 하나만 골라', 'enter': 'wipe', 'bg': 'v:s_seoul_wall', 'items': [
    cover('+0.02'),
    *split('철문이', vs=True),
    side('l', '철문이', tag('1번', '철문이', 0, 0, tone='red', size=80), tag('59년 만의 북악산', '철문이', 0, 0, size=50)),
    side('r', '대통령의', tag('2번', '대통령의', 0, 0, tone='green', size=80), tag('대통령의 섬 저도', '대통령의', 0, 0, size=50)),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'fade', 'bg': 'v:s_birch', 'items': [
    BRIGHT, particles('leaf', '+0.1', n=12),
    hook('지혜호수<br><strong>경제연구소</strong>', '지혜호수', y=260, size=150, sfx='ding'),
    tag('숫자로 확인하고 사실로 말합니다', '+0.3', None, 620, tone='dark', size=56),
]},
]
