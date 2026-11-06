"""밤나무 편 — 5막(이탈리아·미국 120년) · 결말 (자막 173~244, 12:01~16:48). 뒤쪽은 그림 재사용, 장면 단순."""
from gen import (hook, tag, big, cover, glow, raw, stack, card, stamp, split, side, PAST, puppet, particles, polaroid, shrink)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
SOFT = raw('<style>.bg{--dark:.7; --blur:0px}</style>')

C = [
{'from': '그런데 같은 곰팡이를 맞고도', 'enter': 'fade', 'bg': 'i_genoa_1938', 'cam': [('push', '+0.1', 40, 50, 1.2)], 'items': [
    PAST,
    tag('1938 이탈리아 제노바', '제노바', 120, 140, icon='calendar', tone='dark', size=58),
    puppet('c_italian', '발견됩니다', -360, 480, w=380, move='enter', dx=560, dur=2.4),
]},
{'from': '비밀은 곰팡이에 붙은', 'enter': 'zoom', 'bg': 'i_genoa_1938', 'items': [
    PAST, cover('+0.02'),
    tag('곰팡이에 붙은 바이러스 → 곰팡이 약화', '바이러스였습니다', None, 160, icon='scan', tone='green', size=52),
    tag('나무 상처가 저절로 아묾', '아물었습니다', None, 320, icon='heart-handshake', tone='dark', size=56),
    glow('25년 안에 회복 조짐 · 미국에선 퍼지지 않음', '이십오', y=560, size=56),
]},
{'from': '차이점도 짚어야', 'enter': 'wipe', 'bg': 'i_genoa_1938', 'items': [
    BRIGHT,
    tag('정책보다 운에 가까웠다', '운에', 120, 140, icon='alert-triangle', tone='red', size=58),
]},
{'from': '이제 처음에 말씀드린 장면', 'enter': 'flash', 'bg': 'v:s_supermarket', 'cam': [('crash', '육십오', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    tag('2024 미국 밤 수입 약 2,900톤', '이천구백', None, 150, icon='flag', tone='dark', size=56),
    tag('이탈리아 · 중국 · 한국', '이탈리아와', None, 310, icon='map-pin', tone='dark', size=56),
    big('이탈리아 65%', '육십오', y=420, size=150, color='#ffd400'),
]},
{'from': '여기서 하나가 더', 'enter': 'zoom', 'bg': 'i_genoa_1938', 'items': [
    cover('+0.02'),
    card('이탈리아 밤 도매가', '한국의 2배+', '이 배가', 640, 170, w=640, h=280, vat='이 배가'),
    tag('비싸도 팔린다', '비싸도', None, 500, icon='coin', tone='green', size=58),
    tag('우리 길: 가공과 품질', '가공과', None, 650, icon='key', tone='red', size=56),
]},
{'from': '미국은 아직 싸우는', 'enter': 'wipe', 'bg': 'v:s_roast', 'items': [
    SOFT,
    tag('앞에서 말씀드린 뿌리', '뿌리 이야기', 120, 140, icon='key', tone='dark', size=56),
    tag('싹 → 다시 죽고 → 또 싹', '다시 죽고', 120, 300, icon='trending-down', tone='red', size=56),
    big('120년째', '백이십', y=520, size=150, color='#ffd400'),
]},
{'from': '유전자를 바꾼 밤나무로', 'enter': 'zoom', 'bg': 'v:s_lab', 'items': [
    SOFT,
    puppet('c_scientist', '+0.2', -340, 480, w=360, move='enter', dx=520, dur=2.2),
    stamp('계통 뒤바뀜 (2023)', '뒤바뀌어', x=960, y=180, size=84),
    tag('미국밤나무재단 지원 철회 (2023.12)', '십이월', None, 640, icon='file-invoice', tone='dark', size=46),
]},
{'from': '한국 밤에도 숨 돌릴', 'enter': 'wipe', 'bg': 'i_korea_harvest', 'items': [
    cover('+0.02'),
    card('2025 생산', '+5.9% · 약 39,000톤', '육 퍼센트', 640, 170, w=700, h=280, vat='육 퍼센트'),
    glow('반등이라 부르기엔 아직 이르다', '반등이라', y=600, size=64),
]},
# ================= 결말 =================
{'from': '처음 질문으로 돌아가', 'enter': 'flash', 'bg': 'i_park_bench', 'items': [
    cover('+0.02'),
    *stack([('① 병은 주범이 아니었다', '첫째,', 'scan', 'dark'), ('② 더 싼 밤 · 좁아진 수출길', '둘째,', 'flag', 'red'),
            ('③ 밤을 줍고 가꿀 손이 줄었다', '셋째,', 'users', 'red')], x=300, y=220, gap=170, size=60),
]},
{'from': '미국 밤나무를 쓰러뜨린', 'enter': 'zoom', 'bg': 'i_empty_slope', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'), particles('leaf', '+0.1', n=14, seed=31),
    hook('밤을 흔든 건 벌레가 아니라<br><strong>비어 가는 손</strong>', '비어', y=300, size=106),
]},
{'from': '이건 밤만의 이야기가', 'enter': 'wipe', 'bg': 'v:s_mountain_village', 'items': [
    BRIGHT,
    glow('나무는 남는데, 누가 거둘 것인가', '누가 거둘', y=620, size=70),
]},
{'from': '오늘 해 볼 수 있는 일이', 'enter': 'flash', 'bg': 'v:s_autumn_park', 'items': [
    cover('+0.02'),
    *stack([('① 송이 가시 · 알 개수 확인', '공원에서', 'scan', ''), ('② 원산지 한 줄 읽기', '원산지', 'file-invoice', ''),
            ('③ 고향에 전화 한 통', '그리고 고향', 'device-mobile', '')], x=300, y=220, gap=170, size=60),
]},
{'from': '다시 그 동물원입니다', 'enter': 'zoom', 'bg': 'i_bronx_planting', 'items': [
    BRIGHT,
    tag('브롱크스 동물원 · 잡종 밤나무 20그루', '스무', 120, 140, icon='heart-handshake', tone='dark', size=52),
    glow('나무는 다시 심을 수 있다, 손은 쉽게 돌아오지 않는다', '줍는 손은', y=620, size=54),
]},
{'from': '하나 여쭙겠습니다', 'enter': 'flash', 'bg': 'v:s_supermarket', 'items': [
    cover('+0.02'),
    *split('일 번', vs=True),
    side('l', '일 번', tag('1번', '일 번', 0, 0, tone='red', size=80), tag('국산이면 비싸도 산다', '일 번', 0, 0, size=50)),
    side('r', '이 번', tag('2번', '이 번', 0, 0, tone='green', size=80), tag('맛이 같으면 싼 쪽', '이 번', 0, 0, size=50)),
]},
{'from': '다음 이야기도 골라', 'enter': 'wipe', 'bg': 'v:s_seoul', 'items': [
    cover('+0.02'),
    *stack([('1번 소나무가 사라지면 송이값은?', '일 번,', 'chart-bar', ''), ('2번 수출 효자 고려인삼은 어디로', '이 번,', 'flag', ''),
            ('3번 사과 한 알은 왜 비싸졌나', '삼 번,', 'coin', '')], x=220, y=220, gap=170, size=54),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'fade', 'bg': 'v:s_autumn_park', 'items': [
    BRIGHT, particles('leaf', '+0.1', n=12, seed=37),
    hook('지혜호수<br><strong>경제연구소</strong>', '지혜호수', y=260, size=150, sfx='ding'),
    tag('숫자로 확인하고 사실로 말합니다', '+0.3', None, 620, tone='dark', size=56),
]},
]
