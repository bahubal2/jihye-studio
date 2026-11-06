"""밤나무 편 — 3막(한국 밤나무혹벌과 역전) · 4막(의심과 진짜 원인) (자막 75~172, 5:01~12:01)."""
from gen import (hook, flashhit, tag, stamp, big, cover, punch, glow, raw, stack, swapnum, card, bubble, bars, article,
                 shrink, foreshadow, flipcard, split, side, timeline, PAST, puppet, particles, polaroid, mgbg, mg_scale, mg_ship, mg_people)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
SOFT = raw('<style>.bg{--dark:.7; --blur:0px}</style>')

B = [
# ================= 3막: 한국 =================
{'from': '천구백오십팔 년, 충청북도', 'enter': 'fade', 'bg': 'i_korea_1958', 'cam': [('push', '+0.1', 50, 45, 1.2)], 'items': [
    tag('1958 충북 제천 · 밤나무혹벌', '제천의', 120, 140, icon='calendar', tone='dark', size=58),
    puppet('c_wasp', '밤나무혹벌입니다', 1420, 200, w=260, move='hop'),
    tag('새순에 혹 → 밤이 안 열린다', '새순에', 120, 300, icon='alert-triangle', tone='red', size=54),
]},
{'from': '몇 년 만에 강원과', 'enter': 'zoom', 'bg': 'i_korea_1958', 'items': [
    cover('+0.02'),
    tag('강원 · 경기 · 경북 북부로', '강원과', None, 170, icon='map-pin', tone='dark', size=60),
    stamp('재래종 거의 전멸', '전멸했습니다', x=640, y=380, size=120),
]},
{'from': '그런데 한국은 미국과', 'enter': 'wipe', 'bg': 'i_korea_harvest', 'cam': [('push', '+0.1', 50, 50, 1.15)], 'items': [
    BRIGHT,
    tag('한국은 다른 길: 혹벌에 강한 품종으로', '혹벌에 강한', 120, 140, icon='flag', tone='green', size=54),
    tag('옥광 · 축파', '옥광', 120, 300, icon='heart-handshake', tone='dark', size=60),
    puppet('c_old_farmer', '갈아', -380, 470, w=380, move='enter', dx=560, dur=2.4),
]},
{'from': '결과는 숫자로 남았습니다', 'enter': 'flash', 'bg': 'i_korea_harvest', 'items': [
    cover('+0.02'),
    tag('1995년 한국 밤 생산', '천구백구십오', None, 150, icon='chart-bar', tone='dark', size=58),
    big('93,000톤+', '구만', y=270, size=200, color='#2ee66b'),
    tag('수출만 29,000톤 가까이', '이만', None, 560, icon='flag', tone='green', size=58),
]},
{'from': '그리고 내리막이 왔습니다', 'enter': 'zoom', 'bg': 'v:s_mountain_village', 'items': [
    cover('+0.02'),
    bars([('1995년', 1.0, '93,654톤', '+0.1', False), ('2024년', 37010 / 93654, '37,010톤', '삼만', True)], top=250),
    tag('정점의 40%', '사십', None, 620, icon='trending-down', tone='red', size=66),
]},
# ================= 4막: 의심 =================
{'from': '첫 번째 의심은 역시 병', 'enter': 'wipe', 'bg': 'v:s_falling_leaves', 'items': [
    cover('+0.02'),
    card('2025 폭염 피해 산지', '25%', '이십오', 220, 220, w=660, h=300, vat='이십오', hot=True),
    card('그해 생산', '오히려 증가', '늘었습니다', 1040, 220, w=660, h=300, vat='늘었습니다'),
    glow('한두 해 흉작 ≠ 30년 내리막', '설명하지', y=620, size=64),
]},
{'from': '두 번째 의심입니다', 'enter': 'zoom', 'bg': 'v:s_supermarket', 'items': [
    SOFT,
    tag('밤을 안 먹어서? (일부 사실)', '안 먹어서구나', 120, 140, icon='user-x', tone='red', size=56),
    tag('일본 젊은 세대 소비 감소 (2011)', '일본에서', 120, 300, icon='trending-down', tone='dark', size=52),
    tag('국내 추석 차례: 열 집 중 세 집 미만', '올 추석', 120, 460, icon='home', tone='dark', size=52),
]},
{'from': '그런데 국내 숫자는', 'enter': 'flash', 'bg': 'v:s_cargo_ship', 'cam': [('crash', '구천팔백', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    card('밤 수입 (2025 1~11월)', '약 9,800톤', '구천팔백', 220, 200, w=660, h=300, vat='구천팔백'),
    card('평년보다', '+17.6%', '십칠', 1040, 200, w=660, h=300, vat='십칠', hot=True),
    tag('올해도: 1만 톤+, 열 중 여덟은 가공용', '만 톤을', None, 600, icon='flag', tone='red', size=52),
]},
{'from': '경제학 교과서는', 'enter': 'zoom', 'bg': 'v:s_supermarket', 'items': [
    cover('+0.02'),
    big('대체재', '대체재라고', y=220, size=200, color='#ffd400'),
    glow('밤이 싫어진 게 아니라, 사 오는 곳이 바뀌었다', '사 오는', y=600, size=58),
]},
{'from': '그럼 왜 하필 우리 밤이', 'enter': 'flash', 'bg': 'i_empty_slope', 'items': [
    cover('+0.02'),
    *stack([('① 값', '값,', 'coin', 'red'), ('② 수출길', '수출길,', 'flag', 'red'), ('③ 사람', '사람입니다', 'users', 'red')], x=640, y=220, gap=170, size=72),
]},
# ================= 4막: 진짜 원인 =================
{'from': '첫째는 값입니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    tag('국제 도매 단가 (2025.12) · 손님은 싼 쪽으로', '국제', None, 40, icon='chart-bar', tone='dark', size=52),
    mg_scale('+0.1', '육십'),
]},
{'from': '중국은 오랫동안', 'enter': 'wipe', 'bg': 'i_korea_harvest', 'items': [
    cover('+0.02'),
    article('한국농촌경제연구원 논단 (요약)', '2011', '중국의 싸고 맛있는 밤, 우리 안방까지 파고든다', '이천십일', mark='안방', x=460, y=140, rot=-2),
    tag('밤 봉지 뒷면 원산지 한 줄', '원산지', None, 640, icon='scan', tone='red', size=54),
]},
{'from': '둘째는 수출길입니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    mg_ship('+0.1', '지금은', boxes=12, keep=5, a_label='1995년 · 생산의 31%가 배를 탔다', b_label='지금 열에 하나 남짓 · 올해 9월까지 921톤'),
]},
{'from': '애팔래치아의 밤이 기차를', 'enter': 'zoom', 'bg': 'v:s_cargo_ship', 'items': [
    SOFT,
    puppet('c_ship', '배를', -760, 330, w=720, move='walk', dx=2900, dur=9, step=1.35, tilt=1.5, sfx=None),
    *stack([('일본: 젊은 세대가 덜 찾는다', '일본에선', 'trending-down', 'dark'), ('중국: 해외 공장 등록 서류 50여 가지', '쉰 가지', 'file-invoice', 'red')],
           x=200, y=560, gap=150, size=48),
]},
{'from': '정부와 업계가 손을', 'enter': 'wipe', 'bg': 'v:s_cargo_ship', 'items': [
    BRIGHT,
    tag('중국 등록 완료 · 미국 수출 여지', '등록을', 120, 140, icon='flag', tone='green', size=54),
    tag('수출 물류비 지원 폐지', '물류비', 120, 300, icon='alert-triangle', tone='red', size=56),
]},
{'from': '그런데 값과 수출길만으로는', 'enter': 'zoom', 'bg': 'i_empty_slope', 'cam': [('push', '+0.1', 50, 60, 1.25)], 'items': [
    SOFT, particles('leaf', '+0.1', n=14, seed=23),
    hook('왜 아무도<br><strong>안 주울까?</strong>', '처음의', y=240, size=130),
]},
{'from': '셋째, 가장 큰 원인은', 'enter': 'flash', 'bg': 'v:s_mountain_village', 'cam': [('crash', '사람입니다', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    tag('셋째, 가장 큰 원인', '+0.05', None, 170, icon='key', tone='dark', size=60),
    punch('사람', '사람입니다', y=330, size=200),
]},
{'from': '보통은 이렇게 생각합니다', 'enter': 'zoom', 'bg': 'i_empty_slope', 'items': [
    cover('+0.02'),
    flipcard('값이 떨어져서 사람이 떠났다?', '날짜를 보면 순서가 반대', '밤값이', '거꾸로', y=300, size=70),
]},
{'from': '이천십일 년, 농촌경제연구원은', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('cream'),
    tag('2011 · 이미 일손 부족, 새로 심는 나무 거의 없음', '이천십일', None, 60, icon='calendar', tone='dark', size=50),
    mg_people('+0.1', '이천이십사', n=10, keep=3, a_label='', b_label='2024 고령화로 재배 포기 · 2026 빈자리 메우기'),
]},
{'from': '그리고 올가을, 그 장면이', 'enter': 'flash', 'bg': 'i_empty_slope', 'items': [
    cover('+0.02'),
    tag('2026.10 관측: 남부 수확 포기', '포기했습니다', None, 150, icon='alert-triangle', tone='red', size=56),
    card('산청 특대 1kg', '2,200원', '이천이백', 640, 280, w=640, h=280, vat='이천이백', hot=True),
    tag('▶ 지난 공주 밤 편', '공주 밤', None, 620, icon='key', tone='dark', size=56),
]},
{'from': '손이 덜 간 밭은', 'enter': 'zoom', 'bg': 'i_empty_slope', 'items': [
    cover('+0.02'),
    tag('2025 봄 관측: 품질 저하 → 소비 감소', '이천이십오', None, 150, icon='file-invoice', tone='dark', size=52),
    *stack([('사람 ↓', '사람이', 'users', 'red'), ('관리 ↓', '관리가', 'home', 'red'), ('품질·값 ↓', '품질과', 'chart-bar', 'red')], x=640, y=290, gap=150, size=64),
]},
{'from': '밤 농사는 가을 몇 주에', 'enter': 'wipe', 'bg': 'i_empty_slope', 'cam': [('push', '+0.1', 40, 60, 1.15)], 'items': [
    BRIGHT, particles('leaf', '+0.1', n=10, seed=29),
    puppet('c_old_farmer', '허리', -400, 470, w=400, move='walk', dx=1500, dur=9, step=0.90, tilt=4),
    tag('나무는 그대로, 손만 뗀다', '손만', None, 150, icon='user-x', tone='red', size=56),
]},
{'from': '길에 떨어진 밤, 왜 아무도 안 주울까요. 미국', 'enter': 'flash', 'bg': 'i_park_bench', 'items': [
    cover('+0.02'),
    *split('미국', vs=True),
    side('l', '미국', tag('미국 공원', '미국', 0, 0, tone='dark', size=64), tag('답: 독 열매', '독이었습니다', 0, 0, tone='red', size=60)),
    side('r', '우리 산의', tag('우리 산', '우리 산의', 0, 0, tone='dark', size=64), tag('답: 주울 사람이 없다', '없어서', 0, 0, tone='red', size=56)),
]},
{'from': '그 밤밭이 우리 부모님', 'enter': 'zoom', 'bg': 'v:s_phone_elderly', 'items': [
    SOFT,
    tag('그 밤밭, 우리 부모님 산일 수도', '부모님', 120, 140, icon='home', tone='dark', size=56),
    tag('고향 산의 밤나무, 지금은 누가 줍나요? 댓글로', '댓글로', 120, 300, icon='mail', tone='red', size=50),
]},
]
