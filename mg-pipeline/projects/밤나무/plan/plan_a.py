"""밤나무 편 — 인트로 · 1막(마로니에) · 2막(미국 밤나무) (자막 1~74, 0:00~5:01).
   2026-11-06 담당자 방향: 삽화+실사(스톡) 혼합, 종이 인형(puppet) 뒤뚱 걷기, 입자, 사진 액자 — 레이어를 많이, 비용은 최소."""
from gen import (hook, flashhit, tag, stamp, big, cover, punch, glow, raw, stack, swapnum, card, bubble, bars, article,
                 shrink, foreshadow, flipcard, split, side, PAST, puppet, particles, polaroid, mgbg, mg_forest, mg_sap, mg_pile)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
SOFT = raw('<style>.bg{--dark:.7; --blur:0px}</style>')

A = [
# ================= 인트로 =================
{'from': '가을 공원 벤치 아래', 'enter': 'flash', 'bg': 'v:s_autumn_park', 'cam': [('crash', '+0.0', 50, 60, 1.3)], 'items': [
    BRIGHT, particles('leaf', '+0.0', n=18),
    polaroid('p_marron', '+0.1', 1180, 140, w=480, rot=5, cap='실제 사진'),
    big('밤이 수북', '수북합니다', y=520, size=150, color='#ffd400'),
]},
{'from': '그런데 아무도 줍지', 'enter': 'zoom', 'bg': 'i_park_bench', 'cam': [('push', '+0.05', 50, 60, 1.2)], 'items': [
    BRIGHT, particles('leaf', '+0.0', n=12, seed=3),
    puppet('c_grandpa', '+0.05', -400, 470, w=400, move='walk', dx=2700, dur=3.2, step=0.26),
    stamp('아무도 안 줍는다', '줍지', x=1000, y=160, size=100),
]},
{'from': '길에 떨어진 밤, 왜 아무도', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), flashhit('+0.02'),
    hook('길에 떨어진 밤<br><strong>왜 아무도 안 주울까?</strong>', '+0.05', y=230, size=130),
    puppet('c_squirrel', '왜', 1440, 560, w=320, move='hop'),
]},
{'from': '백 년 전 미국 동부', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    mg_forest('+0.2', '지금은', n=40, size=116, y=150, label='100년 전 미국 동부 · 밤나무 수십억 그루'),
    particles('spore', '곰팡이', n=20),
    tag('곰팡이 하나 때문', '곰팡이', None, 690, icon='alert-triangle', tone='red', size=60),
]},
{'from': '한국 밤은 다릅니다', 'enter': 'wipe', 'bg': 'v:s_mountain_village', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    BRIGHT,
    tag('한국 밤 = 해충을 이겨 낸 밤', '해충의', 120, 140, icon='flag', tone='dark', size=60),
    puppet('c_burr', '이겨', 1300, 420, w=420, move='hop'),
]},
{'from': '그런데도 생산량은', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('cream'),
    tag('병을 이겨 낸 밤이, 왜?', '무너지고', None, 40, icon='alert-triangle', tone='red', size=58),
    mg_pile('+0.1', '여섯이', n=10, keep=4, size=180, y=170, a_label='1995년 9만 3천 톤', b_label='지금 3만 7천 톤 · -60%'),
]},
{'from': '또 병 때문일까요', 'enter': 'zoom', 'bg': 'v:s_falling_leaves', 'items': [
    cover('+0.02'),
    flipcard('병 때문?', '피해 비율 낮았다 (2026.10 관측)', '병 때문일까요', '낮았습니다', y=200, size=74),
    tag('날씨? 한두 해의 이야기', '날씨', None, 560, icon='alert-triangle', tone='dark', size=60),
]},
{'from': '실마리는 엉뚱한 곳에', 'enter': 'wipe', 'bg': 'v:s_cargo_ship', 'items': [
    BRIGHT,
    tag('실마리: 미국은 지금 어느 나라 밤을 사 먹나?', '어느 나라', 120, 140, icon='scan', tone='dark', size=52),
    puppet('c_ship', '+0.3', -760, 360, w=720, move='walk', dx=2900, dur=10, step=0.9, tilt=1.5, sfx=None),
    foreshadow('미국 마트의 밤, 원산지는?', '사 먹는지', label='뒤에서 공개'),
]},
{'from': '그 전에, 저 벤치 아래', 'enter': 'zoom', 'bg': 'i_park_bench', 'cam': [('push', '+0.1', 50, 70, 1.3)], 'items': [
    BRIGHT, particles('leaf', '+0.1', n=10, seed=9),
    puppet('c_grandchild', '+0.2', -320, 520, w=340, move='enter', dx=700, dur=2.2),
]},
# ================= 1막: 마로니에 =================
{'from': '벤치 아래 그 열매는', 'enter': 'flash', 'bg': 'v:s_conkers', 'cam': [('crash', '아닙니다', 50, 45, 1.3)], 'items': [
    SOFT,
    stamp('밤 아님!', '아닙니다', x=1200, y=160, size=120),
    tag('마로니에 = 서양칠엽수', '서양칠엽수', 120, 560, icon='alert-triangle', tone='red', size=62),
    polaroid('p_marron', '서양칠엽수', 140, 150, w=420, rot=-5, cap='마로니에 열매 (실제 사진)'),
]},
{'from': '이름에 밤이 붙어', 'enter': 'wipe', 'bg': 'v:s_seoul', 'items': [
    SOFT,
    tag('밤과는 다른 집안', '다른', 120, 140, icon='user-x', tone='dark', size=58),
    tag('서울 대학로 마로니에 공원의 그 나무', '대학로', 120, 300, icon='map-pin', tone='red', size=56),
    tag('도심 공원·가로수 길에도 흔하다', '가로수', 120, 460, icon='building-store', tone='dark', size=56),
]},
{'from': '사포닌 계열의', 'enter': 'zoom', 'bg': 'v:s_conkers', 'items': [
    cover('+0.02'),
    tag('독성분: 사포닌 계열', '사포닌', None, 170, icon='alert-triangle', tone='red', size=66),
    tag('먹으면 복통·구토', '토할', None, 330, tone='dark', size=60),
    puppet('c_conker', '+0.3', 760, 430, w=400, move='shiver'),
]},
{'from': '남의 나라 일만은', 'enter': 'wipe', 'bg': 'i_park_bench', 'items': [
    cover('+0.02'),
    article('응급의학 학술지 (요약)', '2021', '밤인 줄 알고 마로니에 먹은 46세 남성, 응급실행', '국내', mark='응급실행', x=460, y=150, rot=-2),
    tag('명치 통증 · 구역 · 식은땀 · 심장 박동 이상', '심장', None, 620, icon='alert-triangle', tone='red', size=50),
]},
{'from': '온라인 후기에도 공원에서', 'enter': 'zoom', 'bg': 'v:s_autumn_park', 'items': [
    BRIGHT,
    bubble('공원에서 밤인 줄 알고 한 봉지 주워 왔어요', '공원에서', 160, 300, size=50),
]},
{'from': '구별은 어렵지 않습니다', 'enter': 'flash', 'bg': 'i_park_bench', 'items': [
    cover('+0.02'),
    *split('진짜', vs=True),
    side('l', '진짜', tag('진짜 밤', '진짜', 0, 0, tone='green', size=70), tag('가는 가시 빽빽 · 2~3알', '두세', 0, 0, size=46)),
    side('r', '마로니에는', tag('마로니에', '마로니에는', 0, 0, tone='red', size=70), tag('굵은 가시 듬성 · 둥근 1알', '한 알', 0, 0, size=46)),
    puppet('c_burr', '진짜', 300, 380, w=360, move='idle', sfx=None),
    puppet('c_conker', '마로니에는', 1260, 380, w=360, move='shiver', sfx=None),
]},
{'from': '손주가 반짝이는', 'enter': 'zoom', 'bg': 'i_park_bench', 'cam': [('push', '+0.1', 50, 60, 1.2)], 'items': [
    BRIGHT, particles('leaf', '+0.1', n=10, seed=11),
    puppet('c_grandchild', '+0.2', 420, 520, w=340, move='hop'),
    puppet('c_grandpa', '+0.6', -360, 470, w=390, move='enter', dx=560, dur=2.4),
    tag('송이부터 확인!', '송이부터', 1040, 200, icon='scan', tone='red', size=64),
]},
# ================= 2막: 미국 밤나무 =================
{'from': '그럼 진짜 밤나무는', 'enter': 'fade', 'bg': 'i_bronx_zoo', 'cam': [('push', '+0.1', 60, 45, 1.2)], 'items': [
    tag('1904 뉴욕 브롱크스 동물원', '천구백사', 120, 140, icon='calendar', tone='dark', size=58),
    puppet('c_merkel', '헤르만', -360, 500, w=360, move='enter', dx=620, dur=2.6),
]},
{'from': '갈라진 껍질에', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    tag('동아시아에서 건너온 곰팡이 → 수액 길이 막힌다', '동아시아', None, 30, icon='alert-triangle', tone='red', size=50),
    mg_sap('+0.1', '곰팡이였습니다', y=90),
    tag('2년 뒤 동물원 밤나무 98% 감염', '구십팔', None, 740, icon='trending-down', tone='red', size=54),
]},
{'from': '기억해 두세요. 이 곰팡이는', 'enter': 'wipe', 'bg': 'i_stump_sprouts', 'items': [
    BRIGHT,
    tag('곰팡이는 윗부분만 죽였다', '윗부분만', 120, 140, icon='alert-triangle', tone='dark', size=58),
    foreshadow('뿌리는 살아 있다', '뿌리는'),
]},
{'from': '그런데 이 이야기에 늘', 'enter': 'flash', 'bg': 'i_us_forest', 'cam': [('crash', '애팔래치아처럼', 50, 50, 1.3)], 'items': [
    cover('+0.02'),
    tag('유명한 숫자는 부풀려졌다', '부풀려져', None, 150, icon='scan', tone='red', size=58),
    flipcard('“숲의 나무 넷 중 하나”', '애팔래치아 산지 이야기', '넷 중', '애팔래치아처럼', y=320, size=74),
    tag('하버드대 숲 연구진 (2014)', '하버드대', None, 620, icon='file-invoice', tone='dark', size=52),
]},
{'from': '그렇다고 피해가 작았다는', 'enter': 'wipe', 'bg': 'i_appalachia', 'cam': [('pull', '+0.05', 50, 50, 1.4)], 'items': [
    particles('leaf', '+0.1', n=12, seed=13),
    tag('피해는 한 지역에 몰렸다', '몰렸습니다', 120, 140, icon='map-pin', tone='dark', size=58),
    puppet('c_appal_man', '자루로', -380, 470, w=390, move='walk', dx=2500, dur=8, step=0.32),
]},
{'from': '동네 가게에 가져가', 'enter': 'zoom', 'bg': 'i_country_store', 'items': [
    tag('가게에서 물건과 바꾸고', '동네', 120, 140, icon='building-store', tone='dark', size=56),
    tag('기차로 볼티모어·필라델피아·뉴욕', '볼티모어', 120, 300, icon='flag', tone='red', size=54),
    puppet('c_train', '기차역으로', -900, 520, w=780, move='walk', dx=3000, dur=7, step=0.22, tilt=1.2, flip=True, sfx=None),
]},
{'from': '도시 길모퉁이에선', 'enter': 'fade', 'bg': 'i_ny_vendor', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    particles('ember', '+0.1', n=16),
    puppet('c_vendor', '군밤', -420, 450, w=420, move='enter', dx=600, dur=2.4),
    shrink('s_newyork', '백 년 전', 1180, 170, 620, 350, cap='오늘의 뉴욕 거리'),
    tag('신문지 봉투의 군밤, 기억나세요?', '신문지', 120, 140, icon='heart-handshake', tone='red', size=52),
]},
{'from': '그런데 이 장면이 지금', 'enter': 'flash', 'bg': 'i_empty_slope', 'cam': [('crash', '우리는', 50, 50, 1.3)], 'items': [
    cover('+0.02'), flashhit('우리는'), particles('leaf', '+0.1', n=12, seed=17),
    tag('미국: 밤나무가 사라져 주울 밤이 없었다', '미국은', None, 150, icon='flag', tone='dark', size=50),
    hook('우리는 나무가 서 있는데<br><strong>주울 사람이 없다</strong>', '우리는', y=320, size=96),
    tag('왜 그런지, 뒤에서 따라갑니다', '조금 뒤에', None, 680, icon='key', tone='red', size=52),
]},
{'from': '천구백십사 년, 버지니아', 'enter': 'wipe', 'bg': 'i_appalachia', 'items': [
    cover('+0.02'),
    tag('1914 버지니아주 한 곳', '버지니아주', None, 150, icon='calendar', tone='dark', size=58),
    big('900톤+', '구백', y=270, size=200, color='#ffd400'),
    tag('산이 주는 월급봉투', '월급봉투', None, 560, icon='coin', tone='green', size=60),
    puppet('c_hog', '돼지가', -320, 600, w=300, move='walk', dx=2500, dur=6, step=0.2),
]},
{'from': '기억해 두세요. 이 산골의', 'enter': 'zoom', 'bg': 'i_train_station', 'items': [
    foreshadow('기차를 타야 돈이 됐다', '기차를'),
    puppet('c_train', '기차를', -900, 520, w=780, move='walk', dx=3000, dur=6, step=0.22, tilt=1.2, flip=True, sfx=None),
]},
{'from': '나무도 돈이었습니다', 'enter': 'wipe', 'bg': 'i_logging', 'cam': [('push', '+0.1', 50, 50, 1.2)], 'items': [
    cover('+0.02'),
    *stack([('전봇대 · 철도 침목 · 울타리 · 집 기둥', '전봇대와', 'home', 'dark'), ('가죽 무두질 탄닌', '탄닌을', 'flag', 'dark'),
            ('미국 식물성 탄닌의 절반 이상', '이십 세기', 'chart-bar', 'red')], x=200, y=200, gap=170, size=54),
]},
{'from': '그 숲에 곰팡이가', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    mg_forest('+0.1', '팔십', n=40, size=116, y=170, year=(1904, 1940), label='바람과 비를 타고 한 해 80km씩'),
    particles('spore', '팔십', n=22, seed=21),
    tag('동부 활엽수림 목재 값의 절반이 사라졌다', '절반이', None, 690, icon='trending-down', tone='red', size=50),
]},
{'from': '미국은 그렇게 숲을', 'enter': 'zoom', 'bg': 'i_blight_forest', 'cam': [('pull', '+0.05', 50, 50, 1.5)], 'items': [
    tag('그런데 50여 년 뒤, 바다 건너 한국에도', '오십여', 120, 140, icon='flag', tone='red', size=54),
]},
]
