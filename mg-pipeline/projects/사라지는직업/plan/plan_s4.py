"""1위 신입 개발자 (자막 359~427) · 정리·자가진단·희망·엔딩 (428~507)."""
from gen import (hook, flashhit, tag, stamp, roll, big, cover, ranks, punch, glow, igrid, raw, stack, swapnum, card, article, logo, rankbadge, bubble, bars, split, side)

BRIGHT = raw('<style>.bg{--dark:.86; --blur:0px}</style>')
def RB(n, name, first=False): return rankbadge(n, name, '+0.05', still=not first)
OPEN6 = {7: ('경비원', None), 6: ('콜센터', None), 5: ('초등교사', None), 4: ('공인중개사', None), 3: ('은행원', None), 2: ('회계사', None)}

S4 = [
# ================= 1위 신입 개발자 =================
{'from': '일 위로 가기 전에', 'enter': 'flash', 'bg': 'ph_kid_coding_class', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, now=1, nowat='일 위로:일', opened=OPEN6, top=260),
    glow('화보다 가슴이 먼저 저릿해지는 이야기', '저릿해지는', y=640, size=76),
]},
{'from': '저녁 아홉 시, 학원가 앞', 'enter': 'zoom', 'bg': 'ph_academy_van', 'items': [
    BRIGHT, RB(1, '???', True),
    tag('저녁 9시 학원가', '아홉', 120, 260, icon='bus', tone='dark', size=62),
]},
{'from': '아이 하나가 무거운', 'enter': 'strips', 'bg': 'ph_kid_stairs', 'items': [
    BRIGHT, RB(1, '???'),
    tag('무거운 노트북 가방', '노트북', 120, 260, icon='package', tone='dark', size=60),
]},
{'from': '차 안에서 기다리던', 'enter': 'wipe', 'bg': 'ph_mom_car', 'items': [
    BRIGHT, RB(1, '???'),
    bubble('오늘은 뭐 배웠어?', '오늘은', 700, 360, size=64),
    tag('평생 밥그릇이라 믿고 낸 학원비', '밥그릇이라', 120, 620, icon='coin', tone='red', size=58),
]},
{'from': '몇 년 전, 개발자는', 'enter': 'flash', 'bg': 'ph_dev_office_boom', 'items': [
    BRIGHT, RB(1, '신입 개발자', True),
    hook('1위<br><strong>신입 개발자</strong>', '개발자는', y=230, size=180),
    flashhit('개발자는'),
    tag('“코딩만 잘하면 취업 걱정 없다”', '코딩만', 380, 640, icon='key', tone='dark', size=58),
]},
{'from': '이천이십사 년 국내 소프트웨어', 'enter': 'zoom', 'bg': 'ph_dev_office_boom', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    tag('2024 국내 SW 인력', '+0.05', 160, 180, icon='users', tone='dark', size=58),
    big('+7.3%', '칠 점:칠', y=300, size=170, color='#2ee66b', x=160, center=False),
    logo('indeed', '인디드에선', 1180, 200, h=72),
    tag('인디드 2022 · 개발 공고 100장 중 3장 초급', '세 장', None, 620, icon='file-invoice', tone='green', size=50),
]},
{'from': '그런데 AI가 코드를', 'enter': 'flash', 'bg': 'ph_senior_dev_ai', 'items': [
    BRIGHT, RB(1, '신입 개발자'),
    tag('숙련 개발자 + AI 도구', '숙련', 120, 260, icon='robot', tone='red', size=62),
    tag('신입 몫 코드를 직접 해치운다', '해치우게', 120, 420, icon='user-x', tone='dark', size=58),
]},
{'from': '한국은행도 챗GPT', 'enter': 'zoom', 'bg': 'ph_senior_dev_ai', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    logo('bok', '+0.05', 420, 220, h=80),
    logo('chatgpt', '챗GPT', 1060, 220, h=80),
    tag('챗GPT 이후 3년, 정보서비스업 청년 고용 감소', '청년', None, 460, icon='trending-down', tone='red', size=46),
]},
{'from': '이쯤 되면 개발자라는', 'enter': 'strips', 'bg': 'ph_job_board', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    tag('개발자 직업 자체가 사라진다?', '자체가', None, 200, icon='user-x', size=68, strike='아닙니다'),
    punch('아닙니다', '아닙니다', y=420, size=150),
    glow('사라지는 건 직업이 아니라 첫 자리', '첫', y=660, size=84),
]},
{'from': '이천이십오 년 소프트웨어 인력은', 'enter': 'zoom', 'bg': 'ph_dev_floor_empty', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    tag('2025 SW 인력', '+0.05', 760, 160, icon='users', tone='dark', size=58),
    roll(0, 643000, '육십사만', y=270, size=180, suffix='명', tone='good', dur=1.0),
    tag('+0.2% = 천 명당 2명', '영 점:영', 560, 500, icon='trending-up', tone='red', size=62),
    glow('회사는 커지는데 사람은 안 뽑는다', '안 뽑는', y=680, size=76),
]},
{'from': '인디드의 초급 공고 비율은', 'enter': 'strips', 'bg': 'ph_job_board', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    logo('indeed', '+0.05', 820, 180, h=72),
    bars([('2022년 초급 공고', 1.0, '3.2%', '+0.3', True), ('2025년', 1.2 / 3.2, '1.2%', '한 장', False)], top=340),
]},
{'from': '국내 대기업 정규직 신입 공고도', 'enter': 'zoom', 'bg': 'ph_dev_floor_empty', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    tag('대기업 정규직 신입 공고 (2025.1~11)', '+0.05', 340, 160, icon='building-skyscraper', tone='dark', size=56),
    big('-43%', '사십삼', y=260, size=200, color='#ff5a5a'),
    igrid('file-invoice', 10, '+0.3', cols=10, y=530, size=110, tone='good', drop=4, dropat='여섯'),
    tag('IT·통신 업종에서 특히', 'IT와', 600, 730, icon='device-mobile', tone='red', size=54),
]},
{'from': 'AI 개발자 공고는 오히려', 'enter': 'flash', 'bg': 'ph_ai_engineer', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    tag('AI 개발자 공고는 늘었다?', '+0.05', None, 180, icon='robot', size=68),
    big('약 5배', '다섯', y=330, size=220, color='#2ee66b'),
    tag('국내 AI 개발자 수요 · 4년 사이', '사 년', 520, 640, icon='trending-up', tone='green', size=56),
]},
{'from': '다만 업계 전문가들조차', 'enter': 'zoom', 'bg': 'ph_ai_engineer', 'items': [
    BRIGHT, RB(1, '신입 개발자'),
    tag('주니어 자리는 더 구하기 어렵다', '주니어', 120, 260, icon='user-x', tone='red', size=60),
    glow('문은 실력을 증명한 사람에게 먼저 열린다', '증명한', y=620, size=74),
]},
{'from': '여기서 영상 댓글에', 'enter': 'wipe', 'bg': 'ph_comment_phone', 'items': [
    BRIGHT, RB(1, '신입 개발자'),
    bubble('신입을 안 뽑으면, 10년 뒤 경력자는 어디서?', '신입을', 160, 300, size=48),
    stamp('가장 정확한 질문', '정확한', x=1100, y=580, size=100),
]},
{'from': '사람은 사실보다', 'enter': 'zoom', 'bg': 'ph_tv_news_dev', 'items': [
    cover('+0.02'), RB(1, '신입 개발자'),
    tag('사실보다 자주 본 장면을 믿는다', '+0.1', 420, 200, icon='bell-ringing', tone='dark', size=58),
    big('가용성 휴리스틱', '가용성', y=340, size=160, color='#ffd400'),
    tag('억대 연봉 개발자 뉴스', '억대', 600, 620, icon='coin', tone='red', size=60),
]},
{'from': '노란 학원 차 앞에서', 'enter': 'strips', 'bg': 'ph_academy_van', 'items': [
    BRIGHT, RB(1, '신입 개발자'),
    bubble('오늘은 뭐 배웠어?', '오늘은', 700, 360, size=64),
]},
{'from': '몇 해 뒤, 다 자란', 'enter': 'zoom', 'bg': 'ph_rejection_laptop', 'items': [
    BRIGHT, RB(1, '신입 개발자'),
    tag('몇 해 뒤', '+0.05', 120, 140, icon='calendar', tone='dark', size=60),
    article('채용 결과 안내', '메일', '아쉽게도 이번에는 함께하지 못하게 되었습니다', '아쉽게도', mark='함께하지 못하게', x=500, y=330, rot=-2),
]},
# ================= 다시 세우기 · 세 갈래 =================
{'from': '이제 다시 세워 보겠습니다', 'enter': 'flash', 'bg': 'th_lineup_office', 'items': [
    cover('+0.02'),
    ranks('+0.05', n=7, top=300, opened={7: ('경비원', '칠 위'), 6: ('콜센터', '육 위'), 5: ('초등교사', '오 위'), 4: ('공인중개사', '사 위'),
                                         3: ('은행원', '삼 위'), 2: ('회계사', '이 위'), 1: ('신입 개발자', '그리고 일 위:일')}),
]},
{'from': '이 일곱은 세 갈래로', 'enter': 'zoom', 'bg': 'ph_crossroad', 'items': [
    cover('+0.02'),
    tag('① 손님이 다른 길로', '첫째', 160, 140, icon='door-exit', tone='red', size=48),
    tag('은행원 · 공인중개사', '은행원과', 300, 265, size=44),
    tag('② 기계 다음 다시 사람', '둘째', 160, 400, icon='robot', tone='red', size=48),
    tag('콜센터 · 경비원', '콜센터와', 300, 525, size=44),
    tag('③ 문 앞에서 대기', '셋째', 160, 660, icon='clock', tone='red', size=48),
    tag('교사 · 회계사 · 신입 개발자', '교사,', 300, 785, size=44),
]},
{'from': '그리고 일곱 모두에', 'enter': 'strips', 'bg': 'ph_ladder_bottom', 'items': [
    BRIGHT,
    hook('직업보다 먼저<br><strong>첫 칸이 사라진다</strong>', '첫 칸이:첫', y=200, size=140),
    flashhit('첫 칸이:첫'),
    glow('가르치고 기다려 줄 마음이 먼저 문을 닫았다', '마음이', y=640, size=72),
]},
{'from': '동네 미용실을', 'enter': 'wipe', 'bg': 'ph_hair_salon', 'items': [
    BRIGHT,
    tag('바쁘다고 막내를 안 뽑는다', '막내를', 120, 200, icon='user-x', tone='dark', size=60),
    tag('당장은 월급 한 사람 분 절약', '월급', 120, 360, icon='coin', tone='green', size=58),
    tag('10년 뒤, 가위를 이어받을 사람이 없다', '이어받을', 120, 600, icon='alert-triangle', tone='red', size=58),
]},
{'from': '혹시 이게 전부 AI 탓', 'enter': 'flash', 'bg': 'ph_crossroad', 'items': [
    cover('+0.02'),
    tag('전부 AI 탓?', 'AI', 700, 160, icon='robot', size=84, strike='그런데'),
    *stack([('AI 개발 공고 4년 새 5배', '다섯', 'trending-up', 'green'), ('교사 감소 = 아이가 줄어서', '교사가', 'baby-carriage', ''),
            ('중개사 감소 = 손님이 직접', '중개사가', 'device-mobile', '')], x=420, y=340, gap=140, size=58),
]},
{'from': '기술 하나로는', 'enter': 'zoom', 'bg': 'ph_ladder_bottom', 'items': [
    cover('+0.02'),
    tag('기술 하나로는 설명 안 된다', '+0.05', 520, 220, icon='alert-triangle', tone='dark', size=60),
    glow('공통점: 사람을 키울 시간을 아끼려는 마음', '키울', y=460, size=80),
]},
{'from': '그렇다면 이 명단에', 'enter': 'wipe', 'bg': 'ph_office_youngest', 'items': [
    BRIGHT,
    tag('명단에 없는 직업은 안전할까?', '안전할까요', 120, 200, icon='alert-triangle', tone='dark', size=58),
    hook('우리 회사<br><strong>마지막 신입은 언제?</strong>', '마지막으로', y=380, size=130),
]},
# ================= 30초 자가진단 =================
{'from': '삼십초 자가진단입니다', 'enter': 'flash', 'bg': 'ph_office_youngest', 'items': [
    cover('+0.02'),
    tag('30초 자가진단', '+0.05', 700, 120, icon='clock', tone='red', size=66),
    *stack([('① 최근 3년, 막내가 안 들어왔다', '하나.', 'user-x', ''), ('② 내 일 절반을 고객이 앱으로 직접', '둘.', 'device-mobile', ''),
            ('③ 자격증 보유자만 늘고 자리는 그대로', '셋.', 'file-invoice', '')], x=200, y=290, gap=170, size=52),
]},
{'from': '하나도 해당하지 않으면', 'enter': 'zoom', 'bg': 'ph_cert_pile', 'items': [
    cover('+0.02'),
    *stack([('0개 · 안심', '하나도', 'lock', 'green'), ('1개 · 지켜볼 만', '하나면', 'clock', ''),
            ('2개 · 이미 자리가 움직이는 중', '둘이면', 'alert-triangle', 'dark'), ('3개 · 다음 순위표 후보', '셋', 'flame', 'red')], x=420, y=200, gap=150, size=60),
]},
# ================= 희망 · 처음 숫자 · 질문 · 끝 =================
{'from': '희망도 있습니다', 'enter': 'flash', 'bg': 'ph_residents_vote', 'items': [
    BRIGHT,
    tag('서울 강북구 한 아파트', '강북구의', 120, 200, icon='map-pin', tone='dark', size=58),
    big('경비원 87명 지켰다', '팔십칠', y=330, size=130, color='#2ee66b'),
    tag('고지서 숫자보다 새벽 눈삽', '눈삽의', 120, 620, icon='snowflake', tone='green', size=58),
]},
{'from': '은행 콜센터도 AI만으로', 'enter': 'zoom', 'bg': 'ph_callcenter_rehire', 'items': [
    BRIGHT,
    tag('콜센터, 다시 사람을 부른다', '다시', 120, 220, icon='users', tone='green', size=60),
    glow('마지막에 값을 받는 건 사람만 할 수 있는 실력', '실력입니다', y=620, size=70),
]},
{'from': '처음 그 숫자로', 'enter': 'wipe', 'bg': 'ph_training_center', 'items': [
    cover('+0.02'),
    swapnum('합격 1,200명', '수습 등록 338명', '천이백', '삼백삼십팔', y=230, size=110, tone='bad'),
    logo('fsc', '금융위원회가', 560, 470, h=70),
    tag('수습처 배정 방안', '배정', 980, 470, icon='hand-stop', tone='dark', size=58),
    tag('답은 내년 봄 연수원 강당에서', '내년', 520, 660, icon='calendar', tone='red', size=58),
]},
{'from': '하나 여쭙겠습니다', 'enter': 'flash', 'bg': 'ph_choice_tools', 'items': [
    cover('+0.02'),
    *split('일 번,', vs=True),
    side('l', '일 번,', tag('1번', '일 번,', 0, 0, tone='red', size=80), tag('시험으로 따는 자격증', '일 번,', 0, 0, icon='file-invoice', size=44)),
    side('r', '이 번,', tag('2번', '이 번,', 0, 0, tone='green', size=80), tag('손으로 익히는 기술', '이 번,', 0, 0, icon='wash', size=44)),
    tag('댓글로 번호를!', '댓글로', 700, 720, icon='mail', tone='red', size=60),
]},
{'from': '그리고 합격하고도 기다려', 'enter': 'zoom', 'bg': 'ph_choice_tools', 'items': [
    BRIGHT,
    tag('합격하고 기다려 본 경험', '+0.1', 120, 220, icon='clock', tone='dark', size=58),
    tag('우리 회사 마지막 신입은 언제?', '마지막', 120, 380, icon='user', tone='dark', size=58),
]},
{'from': '숫자 뒤에 숨은', 'enter': 'flash', 'bg': 'ph_training_center', 'items': [
    BRIGHT,
    hook('지혜호수<br><strong>경제연구소</strong>', '지혜호수', y=260, size=150, sfx='ding'),
    tag('구독하고 다음 순위표 받기', '구독해', 620, 660, icon='bell-ringing', tone='red', size=60),
]},
]
