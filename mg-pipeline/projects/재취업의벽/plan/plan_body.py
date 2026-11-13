"""재취업의벽 본문 (0:45~18:15). 5위 대기업 출신 부담 / 4위 나이 / 3위 근로계약서 / 2위 학교 문 / 1위 경비실 / 정리·결말.
그림은 input/그림_대본대조.json 의 자막 문장과 1:1. 쓰러진 조정진 씨·과로 사망 경비원 이야기는 담담하게(도장·쿵 없음)."""
from gen import (tag, stack, stamp, big, roll, swapnum, card, donut, flipcard, bubble, group, raw, flow, igrid, rankbadge,
                 puppet, mgbg, qbadge, kin, cutsfx, clist, droppile)
SOFT = raw('<style>.bg{--dark:.6; --blur:0px}</style>')
CLEAR = raw('<style>.bg{--dark:.9; --blur:0px}</style>')
VID = raw('<style>.bg{--dark:.62; --blur:0px}</style>')
def RB(rank, name, first=False): return rankbadge(rank, name, '+0.05', still=not first)
def Q(n, text, note, at): return [mgbg('teal'), kin(f'자가진단 *{n}*', '+0.0', y=170, size=90, mode='drop'),
                                  kin(text, '+0.3', y=320, size=96, mode='pop'), tag(note, at, None, 640, tone='dark', size=50)]

BODY = [
# ================= 5위 대기업 출신이라 부담스럽습니다 (0:45~2:53) =================
{'from': '삼성전자에서', 'enter': 'zoom', 'bg': [('g_engineer_home', None)], 'cam': [('cardL', '그룹장까지')], 'items': [
    CLEAR,
    kin('대기업 *32년*', '+0.1', y=240, size=130, mode='pop', until='그룹장까지'),
    clist([('그룹장 · 연봉 *2억 원*', '그룹장까지'), ('재직 중 *특허* 여럿', '특허도'), ('퇴직 후 *공인중개사* 자격증', '공인중개사'), ('사무보조 알바도 !하늘의 별 따기!', '사무보조')], size=56),
]},
{'from': '오 위는 대기업 출신이라', 'enter': 'flash', 'bg': [('g_interview_burden', None)], 'cam': [('push', '+0.0', 45, 45, 1.1)], 'items': [
    SOFT, RB(5, '대기업 출신 부담', True),
    kin('5위', '+0.0', y=110, size=110, mode='drop', until='대기업 자동차'),
    bubble('대기업 출신이라 부담스럽습니다', '대기업 자동차', 480, 160, size=58, tone='red'),
    tag('가장 많이 들은 말', '가장 많이', None, 620, tone='dark', size=54),
]},
{'from': '퇴직 후 첫 이력서를 어디에', 'enter': 'zoom', 'bg': [('g_ladder_down', None)], 'cam': [('push', '+0.0', 40, 45, 1.1)], 'items': [
    SOFT, RB(5, '대기업 출신 부담'),
    kin('순위 기준', '+0.0', y=110, size=84, mode='drop'),
    kin('재취업 *사다리*를 / 한 칸씩 !아래로!', '사다리를', y=240, size=116, mode='pop'),
]},
{'from': '이런 노후 일자리 이야기', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('노후 일자리 이야기', '+0.0', y=200, size=90, mode='drop'),
    kin('*구독* 눌러 두세요', '구독', y=360, size=150, mode='pop', sfx='ding'),
]},
{'from': '그리고 질문 하나 드리겠습니다', 'enter': 'wipe', 'bg': None, 'items':
    Q(1, '이력서 첫 줄이 / *직함*인가요?', '채점은 마지막에', '채점은')},
{'from': '부담의 정체는 숫자에서', 'enter': 'zoom', 'bg': [('v:s_office_tower', None)], 'items': [
    VID, RB(5, '대기업 출신 부담'),
    card('대기업 임원 첫해 연봉', '4억~5억 원', '헤드헌팅', 200, 240, w=720, h=300, vsize=96),
    card('중견기업', '1억 원도 손사래', '중견기업은', 1000, 240, w=720, h=300, hot=True, vsize=84),
]},
{'from': '중소기업에 중장년 채용 계획을', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), RB(5, '대기업 출신 부담'),
    kin('중소기업 · 관리·사무직으로 뽑겠다', '+0.1', y=170, size=78, mode='drop'),
    igrid('building-store', 10, '관리·사무직', lit=1, litat='일곱 곳', cols=10, y=330, size=120, tone='bad'),
    kin('100곳 중 *7곳*', '일곱 곳', y=560, size=120, mode='pop'),
    tag('문이 좁아도 너무 좁다', '문이 좁아도', None, 760, tone='red', size=54),
]},
{'from': '경력이 길수록 문이 넓어질', 'enter': 'zoom', 'bg': [('g_drawer_resume', None)], 'cam': [('push', '+0.0', 50, 50, 1.12)], 'items': [
    SOFT, RB(5, '대기업 출신 부담'),
    kin('경력 = / *월급 청구서*로 보였다', '받는 쪽에선', y=140, size=110, mode='pop', until='삼십 년 동안'),
    kin('명함 없이 / 나를 설명하는 *순간*', '삼십 년 동안', y=140, size=110, mode='drop', until='그 어색함이'),
    kin('첫 면접을 / *슬금슬금* 미룬다', '그 어색함이', y=140, size=116, mode='pop'),
]},
{'from': '그래서 경력을 내려놓고', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('경력을 *내려놓으면*?', '+0.0', y=220, size=110, mode='drop'),
    kin('먼저 묻는 !질문!', '경력보다 먼저', y=400, size=120, mode='pop'),
]},
# ================= 4위 나이가 어떻게 되십니까 (2:53~5:25) =================
{'from': '나이가 어떻게 되십니까', 'enter': 'zoom', 'bg': [('g_interviewer_age', None)], 'cam': [('crash', '+0.1', 60, 40, 1.2)], 'items': [
    SOFT, RB(4, '나이', True),
    bubble('나이가 어떻게 되십니까?', '+0.05', 640, 150, size=64, tone='red'),
    kin('4위', '사 위는', y=600, size=110, mode='pop'),
]},
{'from': '팔월 국가데이터처 발표를', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), RB(4, '나이'),
    kin('55~79세 취업자', '+0.1', y=140, size=90, mode='drop'),
    roll(0, 1012, '천십이만', y=290, size=220, suffix='만 명', tone='good', dur=1.6),
    stamp('역대 최대', '역대', x=1250, y=600, size=110, rot=-7),
]},
{'from': '그런데 같은 조사에 이런 숫자가', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('dusk'), RB(4, '나이'),
    card('가장 오래 일한 직장을 떠난 나이', '53세', '가장 오래', 200, 230, w=720, h=300, vsize=130),
    card('일하고 싶은 나이', '73세+', '앞으로 일하고', 1000, 230, w=720, h=300, hot=True, vsize=130),
    kin('*20년*이 텅', '꼬박', y=640, size=120, mode='pop'),
]},
{'from': '일하는 사람이 역대 최대인데, 왜', 'enter': 'zoom', 'bg': [('g_elderly_labor', None)], 'cam': [('cardR', '같은 통계에서')], 'items': [
    CLEAR, RB(4, '나이'),
    kin('일자리의 *얼굴*이 바뀌었다', '+0.1', y=240, size=116, mode='pop', until='같은 통계에서'),
    clist([('고령 취업자 1위 = *단순노무*', '같은 통계에서'), ('5명 중 1명 *넘게*', '다섯 명 중'), ('평생 해 온 일과 !다른 자리!', '숫자는 늘었는데')], x=110, y=280, size=58),
]},
{'from': '이 벽은 부모와 자식이', 'enter': 'flash', 'bg': [('g_father_son_resume', None)], 'cam': [('push', '+0.0', 45, 45, 1.1)], 'items': [
    SOFT, RB(4, '나이'),
    kin('아버지 *56세* · 아들 *29세*', '증권사에서', y=140, size=110, mode='pop'),
    tag('서로 이력서를 봐 준다', '서로 이력서', None, 600, size=56),
    tag('30년 만에 쓰는 이력서', '삼십 년 만에', None, 720, tone='dark', size=54),
]},
{'from': '그 길목에서 가장 먼저 만나는 게', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), RB(4, '나이'),
    kin('재취업이 어려운 이유 1위', '한국경제인협회가', y=120, size=86, mode='drop'),
    kin('*나이* 중시 풍토', '첫째로', y=250, size=130, mode='pop'),
    donut(32, '셋 중', label='구직자 응답', x=760, y=430, d=320, tone='bad'),
]},
{'from': '물론 법은 있습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(4, '나이'),
    flipcard('나이 차별 = 500만 원 이하 벌금', '서류에서 슬쩍 거른다', '모집과', '문제는', y=300, size=76),
    tag('10명 중 2명 업무와 무관한 나이 제한 경험', '한 구직자', None, 700, tone='red', size=50),
]},
{'from': '이 벽이 무서운 건 노력으로', 'enter': 'zoom', 'bg': [('g_calendar_clock', None)], 'cam': [('cardR', '경력은 다시')], 'items': [
    CLEAR, RB(4, '나이'),
    kin('노력으로 못 바꾸는 / *숫자*', '+0.1', y=240, size=116, mode='pop', until='경력은 다시'),
    clist([('나이는 해마다 *꼬박꼬박*', '경력은 다시'), ('공백 길수록 *더 커 보인다*', '쉬는 기간이'), ('골든타임 = 퇴직 후 *1~2년*', '골든타임'), ('그날부터 시계는 !째깍째깍!', '달력에')], x=110, y=250, size=54),
]},
{'from': '그리고 나이를 묻는 이 질문은', 'enter': 'flash', 'bg': [('v:s_clock_tick', None)], 'items': [
    VID, RB(4, '나이'),
    kin('이 질문, / *1위*에서 다시', '+0.0', y=180, size=124, mode='drop', until='그 전에'),
    kin('합격자가 받아 든 / *종이 한 장*', '그 전에', y=180, size=116, mode='pop'),
]},
{'from': '두 번째 질문입니다', 'enter': 'wipe', 'bg': None, 'items':
    Q(2, '희망 월급 기준이 / *예전 월급*인가요?', '이번 칸이 아프실 수도', '기준이')},
# ================= 3위 근로계약서 (5:37~7:45) =================
{'from': '삼 위는 합격 통보와', 'enter': 'zoom', 'bg': [('g_contract', None)], 'cam': [('push', '+0.0', 50, 55, 1.15)], 'items': [
    SOFT, RB(3, '근로계약서', True),
    kin('3위 / *근로계약서*', '+0.0', y=150, size=140, mode='pop', sfx='whoosh', until='같이 계산'),
    kin('부장 시절 월급 = *10*', '부장 시절', y=150, size=120, mode='drop'),
]},
{'from': '중장년일자리희망센터 조사에서', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'), RB(3, '근로계약서'),
    clist([('10명 중 4명 가까이 → 새 월급 *5 미만*', '재취업한 사람'), ('더 받는 사람 *100명 중 2명* 미만', '예전보다'), ('반토막 월급마저 !1년도 못 다님! 절반', '반토막'), ('가장 큰 이유 = *계약 종료*', '가장 큰 이유')], x=260, y=230, size=58),
    tag('2018년 조사', '+0.2', None, 720, tone='dark', size=44),
]},
{'from': '받는 쪽 계산도 있습니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), RB(3, '근로계약서'),
    card('중소기업 제시 월급', '월 248만 원', '평균 월', 200, 240, w=720, h=300, vsize=110),
    card('임원·관리자 자리 보장', '10곳 중 1곳도 안 돼', '임원이나', 1000, 240, w=720, h=300, hot=True, vsize=70),
    tag('대부분 사원·대리급', '대부분은', None, 640, tone='red', size=56),
]},
{'from': '그럼 연금으로 메우면', 'enter': 'zoom', 'bg': [('g_pension_bankbook', None)], 'cam': [('cardR', '오월 기준')], 'items': [
    CLEAR, RB(3, '근로계약서'),
    kin('연금으로 *메우면*?', '+0.0', y=240, size=124, mode='pop', until='오월 기준'),
    clist([('고령층 연금 월평균 *88만 원*', '오월 기준'), ('1인 최저 생계비의 *절반 남짓*', '혼자 사는'), ('모자란 반 달치 → 통장에서 !야금야금!', '모자란')], x=110, y=280, size=56),
]},
{'from': '이 계산은 사람을 두 번', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(3, '근로계약서'),
    kin('사람을 *두 번* 묶는다', '+0.0', y=130, size=100, mode='drop'),
    flow([('월급 ↓', '월급이 깎이니'), ('자존심 구겨짐', '자존심이'), ('공백 ↑', '공백이')], y=360, size=96),
    tag('골든타임이 그렇게 지나간다', '골든타임이', None, 640, tone='red', size=54),
]},
{'from': '그래서 계산을 거꾸로', 'enter': 'zoom', 'bg': [('g_consultant', None)], 'cam': [('push', '+0.0', 45, 45, 1.1)], 'items': [
    SOFT, RB(3, '근로계약서'),
    kin('월급 크기보다 / *몇 년* 다닐 수 있나', '+0.1', y=150, size=110, mode='pop', until='퇴직 후 첫'),
    tag('다음 편 예고', '퇴직 후 첫', None, 120, tone='red', size=56),
    kin('퇴직 후 *첫 1년*, / 무엇부터?', '퇴직 후 첫', y=250, size=116, mode='drop'),
]},
{'from': '여기서 단서를 한번 모아', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('단서 모으기', '+0.0', y=90, size=84, mode='drop'),
    clist([('경력 → *부담*', '경력은'), ('나이 → *걸러 낼 이유*', '나이는'), ('월급 → *반으로*', '월급은')], x=560, y=230, size=70),
    qbadge('맞지 않는 조각', '맞지 않는', pop=True),
    kin('다 내려놔도 / 왜 또 !떨어질까!', '경력도 내려놓고', y=700, size=72, mode='pop'),
]},
{'from': '세 번째이자 마지막 질문', 'enter': 'wipe', 'bg': None, 'items':
    Q(3, '석 달 넘게 / 지원 *0건*인가요?', '1위 직전에 다시', '일 위 직전')},
# ================= 2위 학교 문 (7:58~10:44) =================
{'from': '아침 여덟 시 반', 'enter': 'zoom', 'bg': [('g_school_morning', None)], 'cam': [('push', '+0.0', 55, 45, 1.1)], 'items': [
    SOFT,
    kin('아침 8시 반 · *교문 앞*', '+0.0', y=120, size=96, mode='slide', x=90, w=1100),
    bubble('교장 선생님, 안녕하세요!', '교장 선생님', 720, 300, size=56),
    tag('40년 가까이 익숙한 아침', '사십 년', None, 650, tone='dark', size=52),
]},
{'from': '이 위는 교장 선생님도', 'enter': 'flash', 'bg': [('g_retired_teachers', None)], 'cam': [('push', '+0.0', 40, 50, 1.12)], 'items': [
    SOFT, RB(2, '학교 문', True),
    kin('2위 / 교장도 못 들어가는 *학교 문*', '+0.0', y=140, size=110, mode='pop', until='교원의 정년'),
    kin('교원 정년 *62세*', '교원의 정년', y=150, size=120, mode='drop', until='퇴직한 선생님'),
    kin('다시 학교로 / *등하굣길 지킴이*', '퇴직한 선생님', y=150, size=110, mode='pop'),
]},
{'from': '그런데 서울의 학교보안관', 'enter': 'zoom', 'bg': [('g_school_guard', None)], 'cam': [('cardL', '처음엔')], 'items': [
    CLEAR, RB(2, '학교 문'),
    kin('서울 *학교보안관*', '+0.0', y=240, size=124, mode='pop', until='처음엔'),
    clist([('처음엔 나이 제한 없음 · *82세*까지', '처음엔'), ('2017 조례: *55~70세*', '쉰다섯에서'), ('*국민체력 인증* 등급 제출', '국민체력'), ('당시 신규 최대 *5년*', '당시'), ('지금은 해마다 !체력 측정!', '지금은 해마다')], size=50),
]},
{'from': '평생 교단에 선 분이 체력', 'enter': 'flash', 'bg': [('g_principal_gate', None)], 'cam': [('push', '+0.0', 55, 40, 1.12)], 'items': [
    SOFT, RB(2, '학교 문'),
    kin('평생 교단 → / *체력 인증서* 들고', '+0.0', y=150, size=110, mode='pop'),
    stamp('기가 막힐 노릇', '기가 막힐', x=1200, y=560, size=96, rot=-7),
    tag('처음에 말씀드린 그 장면', '처음에 말씀', None, 760, tone='dark', size=50),
]},
{'from': '이유가 없지는 않습니다', 'enter': 'wipe', 'bg': None, 'items': [
    mgbg('teal'), RB(2, '학교 문'),
    kin('이유는 *있다*', '+0.0', y=150, size=110, mode='drop'),
    tag('낯선 사람을 막아서야 하는 자리', '학교보안관은', None, 320, size=58),
    tag('현장 걱정 → 서울시 기준', '고령화로', None, 460, tone='dark', size=58),
]},
{'from': '문제는 문이 좁아진 만큼', 'enter': 'zoom', 'bg': [('g_daegu_applicants', None)], 'cam': [('push', '+0.0', 50, 45, 1.1)], 'items': [
    SOFT, RB(2, '학교 문'),
    kin('대구 학교 당직경비·미화 *29자리*', '대구의', y=120, size=84, mode='drop'),
    roll(0, 418, '사백십팔', y=250, size=200, suffix='명 지원', tone='bad', dur=1.4),
    stamp('14 대 1', '열네 대', x=1220, y=540, size=120, rot=-8),
    tag('자리 하나에 14명이 우르르 · 지원자 평균 50대', '자리 하나', None, 760, tone='red', size=48),
]},
{'from': '정부가 만드는 노인일자리도', 'enter': 'flash', 'bg': [('g_senior_job_queue', None)], 'cam': [('cardR', '올해 일자리')], 'items': [
    CLEAR, RB(2, '학교 문'),
    kin('정부 *노인일자리*도', '+0.0', y=240, size=124, mode='pop', until='올해 일자리'),
    clist([('일자리 *115만 개*', '올해 일자리'), ('신청 *122만 명*', '신청했고'), ('8월까지 대기자 !19만 명+!', '대기자만')], x=110, y=280, size=62),
]},
{'from': '퇴직 교원 모임을 이끌던', 'enter': 'zoom', 'bg': [('g_teacher_letter', None)], 'cam': [('push', '+0.0', 40, 45, 1.1)], 'items': [
    SOFT, RB(2, '학교 문'),
    kin('선배 지킴이를 / *창피해*하는 후배들', '후배들 가운데', y=140, size=110, mode='pop', until='부르는 쪽도'),
    kin('예전 *호칭*을 / 내려놓기 어렵다', '부르는 쪽도', y=140, size=110, mode='drop'),
]},
{'from': '연금도 있는 분들이 왜 굳이', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(2, '학교 문'),
    kin('왜 굳이 *일하려* 할까?', '+0.0', y=120, size=96, mode='drop'),
    donut(37, '같은 해', label='일하는 즐거움 때문', x=760, y=230, d=380, tone='good'),
    tag('5년째 증가 · 돈만의 문제가 아니다', '다섯 해째', None, 680, size=52),
]},
{'from': '우리 아이가 다니던 학교 정문', 'enter': 'zoom', 'bg': [('g_school_guard', None)], 'cam': [('push', '+0.0', 30, 50, 1.15)], 'items': [
    SOFT, RB(2, '학교 문'),
    kin('학교 정문 앞, / 몇 년 뒤 *내 모습*?', '+0.0', y=150, size=116, mode='pop'),
]},
{'from': '학교 문도, 공공 일자리도', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('학교 문도 · 공공 일자리도 *붐볐다*', '+0.0', y=180, size=86, mode='drop'),
    kin('남은 건 / !은퇴자의 마지막 보루!', '처음에 본', y=360, size=116, mode='pop'),
]},
{'from': '다시 그 질문입니다', 'enter': 'wipe', 'bg': None, 'items':
    Q(3, '석 달 넘게 / 지원 *0건*?', '지금부터는 남의 일이 아니다', '지금부터')},
# ================= 1위 경비도 젊은 분 뽑는다 (10:52~14:32) =================
{'from': '문제를 하나 드리겠습니다', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('dusk'),
    qbadge('가장 빠르게 늘어난 경비원은 몇 살?', '+0.1', pop=True),
    kin('?', '+0.2', y=300, size=200, mode='pop', until='이십 대입니다'),
    kin('!20대!', '이십 대입니다', y=260, size=240, mode='pop', sfx='whoosh'),
    tag('입이 쩍 벌어지는 답', '입이 쩍', None, 620, tone='red', size=56),
]},
{'from': '십이월 경찰청 집계를', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    card('20대 경비 인력', '+18.8%', '이십 대 경비', 200, 230, w=720, h=300, hot=True, vsize=130),
    card('70세 이상', '+3%', '일흔 살 이상', 1000, 230, w=720, h=300, vsize=130),
    igrid('user', 6, '다섯이던', lit=5, litat='다섯이던', cols=6, y=640, size=100, tone='good', drop=0),
    tag('경찰청 2025.12', '+0.2', None, 110, tone='dark', size=44),
]},
{'from': '일 위는 경비도 젊은 분을', 'enter': 'zoom', 'bg': [('g_young_guard', None)], 'cam': [('push', '+0.0', 50, 50, 1.1)], 'items': [
    SOFT, RB(1, '경비실', True),
    kin('1위 / 경비도 *젊은 분* 뽑는다', '+0.0', y=180, size=124, mode='pop', sfx='whoosh'),
]},
{'from': '지방 소도시의 공기업에서', 'enter': 'flash', 'bg': [('g_bus_terminal', None)], 'cam': [('cardL', '이천십육')], 'items': [
    CLEAR, RB(1, '경비실'),
    kin('공기업 *38년*', '+0.1', y=240, size=130, mode='pop', until='이천십육'),
    clist([('2016년 *60세* 정년퇴직', '이천십육'), ('막내는 아직 *대학 3학년*', '막내는'), ('첫 일: 터미널 *배차 계장*', '버스터미널'), ('경비·청소·보안 *전전*', '이후 아파트')], size=54),
]},
{'from': '그리고 한여름 무더위 속', 'enter': 'zoom', 'bg': [('g_labor_diary', None)], 'cam': [('push', '+0.0', 50, 50, 1.08)], 'items': [
    SOFT, RB(1, '경비실'),
    kin('현장에서 부르던 이름', '현장에서', y=140, size=90, mode='drop', until='임계장'),
    kin('*임계장*', '임계장', y=150, size=170, mode='pop'),
    tag('임시 계약직 노인장', '임시 계약직', None, 400, size=60),
    tag('노동일지를 적어 책으로', '노동일지', None, 540, tone='dark', size=54),
]},
{'from': '그때만 해도 경비는 들어갈', 'enter': 'flash', 'bg': [('g_guard_line', None)], 'cam': [('cardR', '증권사 건물')], 'items': [
    CLEAR, RB(1, '경비실'),
    kin('이제 입구에 / *줄*이 길게', '+0.1', y=240, size=124, mode='pop', until='증권사 건물'),
    clist([('경비 1자리에 이력서 *170장*', '증권사 건물'), ('대기업·석사급 지원자 *크게 늘어*', '파견업체 대표'), ('후기: 동료가 대기업 부장·석사', '아버지가')], x=110, y=280, size=54),
]},
{'from': '그런데 왜 젊은 쪽으로', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'), RB(1, '경비실'),
    kin('왜 *젊은 쪽*으로?', '+0.0', y=120, size=100, mode='drop'),
    tag('경비협회장: 지병·사고 책임 문제', '고령자는', None, 290, size=56),
    tag('중대재해처벌법 이후 채용 꺼려', '중대재해', None, 420, tone='dark', size=56),
    tag('2024년 과로로 숨진 경비원 31명', '실제로', None, 560, tone='dark', size=56),
]},
{'from': '다른 쪽 문으로는 청년이', 'enter': 'flash', 'bg': [('g_training_young', None)], 'cam': [('cardL', '서울 영등포')], 'items': [
    CLEAR, RB(1, '경비실'),
    kin('다른 문으로 / *청년*이 들어온다', '+0.0', y=240, size=116, mode='pop', until='서울 영등포'),
    clist([('신임교육 월 *4회 → 9회*', '서울 영등포'), ('대형 병원 경비에도 *젊은 지원자*', '대형 병원'), ('아파트 경비도 *이력 꼼꼼히*', '아파트 경비도')], size=54),
]},
{'from': '년 넘게 경비원을 뽑아 온', 'enter': 'zoom', 'bg': [('g_guard_interview', None)], 'cam': [('push', '+0.0', 60, 50, 1.12)], 'items': [
    SOFT, RB(1, '경비실'),
    kin('들어오는 모습과 / *뒷모습*을 본다', '면접에서', y=140, size=110, mode='pop', until='그러면서'),
    kin('나이로 자르는 건 / !편의주의!', '그러면서', y=140, size=116, mode='drop', until='경제학'),
    kin('이름: *통계적 차별*', '경제학', y=140, size=116, mode='pop'),
    tag('사람 대신 나이대 평균으로 판단', '한 사람을 보는', None, 640, tone='dark', size=52),
]},
{'from': '그래도 경비원 대부분은', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'), RB(1, '경비실'),
    card('60대 경비원', '7만 9천여 명', '같은 집계에서', 200, 220, w=720, h=280, vsize=96),
    card('70세 이상', '5만 1천여 명', '일흔 살 이상이', 1000, 220, w=720, h=280, vsize=96),
    tag('60대도 1년 새 10% 넘게 증가', '육십 대 경비원도', None, 520, size=50),
    kin('닫힌 게 아니라 / *줄이 길어졌다*', '문이 닫힌', y=740, size=76, mode='pop'),
]},
# ================= 정리·결말 (14:32~18:15) =================
{'from': '다섯 개의 벽을 모두', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('다섯 개의 벽', '+0.0', y=80, size=84, mode='drop'),
    clist([('5위 · *대기업 출신* 부담', '오 위'), ('4위 · *나이* 질문', '사 위'), ('3위 · 반토막 *근로계약서*', '삼 위'), ('2위 · 체력 인증 *학교 문*', '이 위'), ('1위 · 청년과 같은 줄 !경비실!', '그리고 일 위')], x=380, y=200, size=60),
]},
{'from': '다섯 벽을 겹쳐 보면', 'enter': 'zoom', 'bg': [('g_ladder_down', None)], 'cam': [('push', '+0.0', 40, 50, 1.1)], 'items': [
    SOFT,
    kin('사다리를 *아래로만*', '퇴직자들은', y=140, size=116, mode='pop', until='겉으로는'),
    flipcard('눈높이 탓', '이름표로 거르는 사다리', '겉으로는', '실제로는', y=330, size=92),
]},
{'from': '나이 자체가 문을 닫는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('dusk'),
    kin('거꾸로 가는 숫자', '그런데 있습니다', y=100, size=90, mode='drop'),
    card('70세+ 상용직 (10년)', '× 4', '일 년 이상', 200, 220, w=720, h=300, vsize=150),
    card('그중 전문가', '× 8', '그중 전문가로', 1000, 220, w=720, h=300, hot=True, vsize=150),
    kin('나이보다 / *무엇을 들고* 두드렸나', '나이보다', y=560, size=80, mode='pop'),
    tag('보육·사회복지 재취업률 70%+', '보육과', None, 760, tone='dark', size=46),
]},
{'from': '동창회를 떠올려 보시죠', 'enter': 'zoom', 'bg': [('g_reunion', None)], 'cam': [('push', '+0.0', 45, 50, 1.1)], 'items': [
    SOFT,
    kin('현역 땐 *명함*부터', '현역일 때는', y=140, size=110, mode='pop', until='어디 다니느냐'),
    kin('어디 다니느냐 → / *요즘 뭐 하느냐*', '어디 다니느냐', y=140, size=110, mode='drop'),
]},
{'from': '이 명단에 없는 자리는', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    kin('채점', '이제 채점', y=90, size=84, mode='drop'),
    clist([('① 이력서 첫 줄 = *직함*', '이력서 첫 줄이'), ('② 희망 월급 기준 = *예전 월급*', '희망 월급'), ('③ 석 달 넘게 *지원 0건*', '석 달 넘게')], x=440, y=220, size=66),
]},
{'from': '하나도 없다면 안심하셔도', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('dusk'),
    tag('0개 → 안심', '+0.0', None, 220, tone='green', size=64),
    tag('1개 → 지켜볼 만', '하나라면', None, 360, size=64),
    tag('2개 → 줄 뒤로 밀리는 중', '둘이라면', None, 500, tone='red', size=64),
    tag('3개 → 다음 순위표의 사연', '셋 모두라면', None, 640, tone='red', size=72),
]},
{'from': '그래서 오늘 할 일은', 'enter': 'wipe', 'bg': [('g_job_center', None)], 'cam': [('cardL', '이력서 첫 줄을')], 'items': [
    CLEAR,
    kin('오늘 할 일 *3가지*', '+0.0', y=240, size=124, mode='pop', until='이력서 첫 줄을'),
    clist([('이력서 첫 줄 → *할 수 있는 일*', '이력서 첫 줄을'), ('*중장년내일센터* 상담 (40세+ 무료)', '중장년내일센터'), ('내년 *노인일자리* 모집 시기 문의', '노인일자리')], size=54),
]},
{'from': '제도도 움직이고 있습니다', 'enter': 'flash', 'bg': None, 'items': [
    mgbg('teal'),
    tag('정년 65세 법안 · 장관 "연내 처리 필요" (2026.10)', '법정 정년', None, 220, size=50),
    kin('아직 *법 개정 전*', '다만 아직', y=380, size=120, mode='pop'),
    kin('시계는 *째깍째깍*', '기다리는 동안', y=580, size=100, mode='drop'),
]},
{'from': '대구의 서정배 씨는', 'enter': 'zoom', 'bg': [('g_water_patrol', None)], 'cam': [('push', '+0.0', 40, 50, 1.08)], 'items': [
    SOFT,
    kin('65세 · 경비·청소는 *맞지 않았다*', '+0.1', y=140, size=96, mode='drop', until='그리고 올봄'),
    kin('올봄부터 / *상수도 보호구역 감시원*', '그리고 올봄', y=140, size=100, mode='pop', until='맞는 자리는'),
    kin('맞는 자리는 / 결국 *왔다*', '맞는 자리는', y=140, size=116, mode='pop'),
]},
{'from': '다시 그 인력파견업체로', 'enter': 'flash', 'bg': [('g_agency_resumes', None)], 'cam': [('push', '+0.0', 45, 45, 1.1)], 'items': [
    SOFT,
    kin('이력서 *170장* 중 / 뽑힌 한 장', '이력서 백칠십', y=140, size=110, mode='pop', until='그 이력서의'),
    kin('그 첫 줄에는 / *무엇*이?', '그 이력서의', y=150, size=124, mode='drop'),
]},
{'from': '여러분이라면 어느 쪽을', 'enter': 'zoom', 'bg': None, 'items': [
    mgbg('teal'),
    kin('여러분이라면?', '+0.0', y=110, size=96, mode='drop'),
    card('1번', '월급 적어도 경력 살리는 일', '월급은 적어도', 200, 270, w=720, h=300, vsize=60),
    card('2번', '경력 상관없이 오래 다닐 일', '아니면', 1000, 270, w=720, h=300, hot=True, vsize=60),
    tag('가장 서운했던 한마디도 댓글로', '그리고 퇴직 후', None, 680, tone='dark', size=52),
]},
{'from': '숫자로 확인하고 사실로', 'enter': 'flash', 'bg': [('g_ending_walk', None)], 'cam': [('push', '+0.0', 50, 45, 1.08)], 'items': [
    SOFT,
    kin('숫자로 확인하고 / *사실로* 말합니다', '+0.0', y=180, size=110, mode='pop'),
    tag('지혜호수 경제연구소', '+0.5', None, 460, tone='dark', size=56),
    kin('*구독*해 두세요', '구독', y=600, size=110, mode='pop', sfx='ding'),
]},
]
