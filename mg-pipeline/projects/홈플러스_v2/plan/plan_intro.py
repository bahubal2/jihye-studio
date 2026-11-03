"""홈플러스 인트로 시안 (키트 2판). 레퍼런스 JV7ONuxsbm4 밀도: 1분에 그래픽 12~15개, 한 화면 3~4개.
흰 둥근 박스+아이콘 칩, 로고 타일, 누끼, 말풍선, 좌우 분할, 숫자 롤링, 다시 쓴 기사 카드, 픽토그램, 마스크·슬라이드 전환.
"""
from gen import (label, line, big, stamp, chip, cover, inset, tag, stack, logo, cut, bubble, split, side, article, pictos, roll)

PLAN = [
# 0:00 텅 빈 매대 (클립) — 장면을 묘사하는 짧은 칩을 차례로
{'from': '진열대에 생수', 'bg': 'ph_empty_shelf', 'items': [
    tag('텅 빈 생수 매대', '생수', 120, 640, icon='droplet', tone='red', size=56),
    tag('주류 코너', '주류', 1240, 250, icon='building-store', size=50),
    tag('빈 쇼핑백만 수북', '쇼핑백이', 1240, 350, icon='package', tone='red', size=50),
    logo('homeplus', '홈플러스', 120, 150, h=60),
    tag('2026년 초여름', '초여름,', 120, 260, icon='calendar', tone='dark', size=46),
]},
# 0:10 4년 전, 간석점 (마스크 전환, 클립)
{'from': '4년 전, 같은 회사', 'enter': 'mask', 'bg': 'ph_reopen_crowd', 'items': [
    tag('4년 전', '4년', 120, 160, icon='calendar', tone='dark', size=56),
    tag('2022년 2월 · 인천 간석점', '간석점.', 120, 270, icon='map-pin', size=50),
    tag('새 단장 첫 주말', '단장을', 120, 370, icon='building-store', tone='green', size=50),
    roll(0, 11, '11억', y=500, size=190, suffix='억 원', tone='good'),
    stamp('전국 1등', '1등이었죠', x=1300, y=300, size=96),
]},
# 0:27 숫자 하나를 겹쳐 본다: 임차료 (슬라이드 전환)
{'from': '그런데 여기에 숫자', 'enter': 'slide', 'bg': 'ph_rent_invoice', 'items': [
    tag('숫자 하나 더', '겹쳐', 120, 150, icon='alert-triangle', tone='dark', size=46),
    tag('세 들어 장사하는 매장', '세', 120, 250, icon='home', size=52),
    tag('임차료', '임차료입니다', 120, 350, icon='receipt', tone='red', size=60),
    tag('1년', '1년에', 1260, 250, icon='calendar', size=52),
    roll(3000, 4000, '4,000억', y=470, size=180, suffix='억 원', prefix='약 ', tone='bad', dur=1.2),
    tag('하루로 나누면 약 11억', '하루로', 640, 740, icon='clock', tone='red', size=54),
]},
# 0:40 좌우 분할: 1등 매장 최고 매출 = 매일 나가는 임차료
{'from': '전국 1등 매장이', 'bg': 'ph_shutter', 'items': [
    cover('+0.02'),
    *split('+0.05'),
    side('l', '+0.1', tag('전국 1등 매장', '+0.1', 170, 0, icon='trending-up', tone='green', size=50),
         tag('가장 잘 팔린 날', '+0.3', 200, 110, size=46), roll(0, 11, '+0.5', y=230, size=150, suffix='억', tone='good')),
    side('r', '매일,', tag('매일 나가는 임차료', '매일,', 150, 0, icon='receipt', tone='red', size=50),
         tag('셔터 올리기 전에', '셔터를', 170, 110, icon='lock', size=46), roll(0, 11, '셔터를', y=230, size=150, suffix='억', tone='bad')),
]},
# 0:49 흔한 설명: 주민 누끼 + 말풍선 + 로고
{'from': '흔히들 쿠팡', 'enter': 'slide', 'bg': 'st_phone_order', 'items': [
    cut('cut_residents', '흔히들', 150, 330, h=640, move=(-60, 40, .82), moveat='사모펀드의'),
    bubble('쿠팡 때문?', '쿠팡', 700, 250, size=58),
    logo('coupang', '쿠팡', 1060, 245, h=54),
    bubble('사모펀드 욕심 때문?', '사모펀드의', 700, 420, size=58, tone='red'),
    logo('mbk', '사모펀드의', 1300, 420, h=48),
    tag('틀린 말은 아니다', '틀린', 1150, 600, icon='scale', tone='dark', size=46),
    tag('진짜 이유는 따로', '진짜', 1100, 720, icon='key', tone='red', size=60),
]},
# 0:59 같은 쿠팡 시대, 롯데마트는 일어설 발판
{'from': '같은 쿠팡 시대를', 'bg': 'st_boxes', 'items': [
    *split('+0.05', vs=True),
    side('l', '+0.1', logo('homeplus', '+0.1', 260, 0, h=60), tag('법원 앞으로', '+0.4', 230, 130, icon='gavel', tone='red', size=54)),
    side('r', '롯데마트는', logo('lottemart', '롯데마트는', 210, 0, h=60), tag('다시 일어설 발판', '발판을', 170, 130, icon='trending-up', tone='green', size=54)),
]},
# 1:04 오늘의 질문 + 다시 쓴 기사 카드
{'from': '그래서 오늘 드릴 질문', 'enter': 'slide', 'bg': 'ph_court_steps', 'items': [
    article('파이낸셜뉴스', '2025. 3. 4', '홈플러스, 기업회생 신청… 법원 같은 날 개시 결정', '+0.1', mark='기업회생', markat='+1.4', x=460, y=180, until='늘고'),
    tag('매출은 늘었는데', '늘고', 260, 300, icon='trending-up', tone='green', size=64),
    tag('왜 법원 문 앞에?', '법원', 900, 470, icon='gavel', tone='red', size=72),
]},
# 1:14 이유는 세 겹
{'from': '오늘은 그 이유를 세 겹', 'enter': 'mask', 'bg': 'st_city_night', 'items': [
    cover('+0.02'),
    *stack([('이유 1', '세 겹으로:세', 'circle-1' if False else 'key', 'dark'), ('이유 2', '세 겹으로:벗겨', 'key', 'dark'), ('이유 3', '세 번째에서:세', 'key', 'red')], x=760, y=220, gap=140, size=84),
    stamp('무릎을 친다', '무릎을', x=1180, y=640, size=84),
]},
