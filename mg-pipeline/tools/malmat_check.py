"""말맛 검사 (2026-11-10 담당자: "클로드(대본 AI)가 제대로 못 쓰면 자네가 고쳐라").
   python3 tools/malmat_check.py <대본.txt>
1분(415자)당 말맛 표현 수, 소리·모양말 없는 문단, 수위 위반(대사 밖 거친 말·금지어), 지어낸 사실 의심 표현을 보여 준다.
기준: brand/말맛_가이드_2026-11.md (1분에 2~4개, 문단마다 소리·모양말 1개, 거친 말은 대사 안 1~2회, 욕설·비하·신조어 금지)."""
import re, sys
SOUND = ['뚝뚝', '휙휙', '쩍쩍', '덜덜', '스멀스멀', '야금야금', '졸졸', '송골송골', '새근새근', '사르르', '따끈따끈', '찌끈', '칼칼', '푹푹', '바들바들',
         '오들오들', '후끈', '훈훈', '꽁꽁', '펄펄', '보글보글', '부글부글', '살살', '뜨끈', '뜨뜻', '쨍쨍', '꾸벅', '벌벌', '와르르', '줄줄', '꽉꽉', '팍팍', '쑥쑥', '툭', '휙', '쫙', '싹', '쭉', '콕', '꾹', '딱', '덥석', '슬금슬금', '차곡차곡', '꼬박꼬박', '바짝', '시퍼렇', '시뻘건', '시꺼먼', '텅텅', '뒤숭숭', '허겁지겁', '부랴부랴', '우르르', '덜컥', '고스란히', '와글와글', '수군수군', '콩닥', '두근두근', '바글바글', '썰렁', '휑', '꾸역꾸역', '주섬주섬', '부스럭', '덜덜', '흘끔', '슬쩍', '불쑥', '훌쩍', '홀쭉', '빵빵', '터질 듯', '숭숭', '주렁주렁', '멈칫', '우르르', '훌쩍', '떡하니', '쭉', '휘둥그레', '썰렁', '휩쓸', '하나둘', '쓱', '뚝']
BODY = ['등짝', '뒷목', '마디마디', '허리를 지지', '허리부터', '이빨', '코피', '입이 쩍', '배를 잡고', '등골', '오금', '간이 콩알', '눈이 휘둥그레', '발목을 붙잡', '가슴 졸', '발등 찍', '혀를 내두', '발등', '손사래', '무릎을 탁']
STRONG = ['나발이고', '미친 노릇', '미치게', '난리가', '끝내', '수두룩', '우습게', '팩폭', '본전', '꿀잠', '짝퉁', '떼로', '대판', '말 다 했', '잡아먹', '날벼락', '뒤집어졌', '박살', '쪽박', '대박', '헛물', '생돈', '눈뜨고 코 베', '피 같은', '쟁여', '쟁였', '싹쓸이', '쓸어 담', '호들갑', '유난', '설레발', '동났', '바닥났', '카드를 긁', '목돈', '헛돈', '생돈', '지갑이 열', '지갑을 열']
IDIOM = ['엎친 데 덮친', '사시나무', '철석같이', '속는 셈 치고', '자존심이고 뭐고', '피 터지는', '판을 뒤집', '칼같이', '귀신같이', '쌍수를 들고', '울며 겨자', '빛 좋은 개살구', '소 잃고', '티끌 모아', '그림의 떡', '언 발에 오줌', '하늘의 별 따기', '꿩 먹고 알 먹고', '누워서 떡 먹기', '배보다 배꼽', '눈 깜짝할 새', '하늘과 땅', '하늘로 치솟', '발을 동동', '발 동동', '불난 집', '부채질', '마른하늘에 날벼락', '가랑비에 옷 젖', '돌다리도 두들겨', '긁어 부스럼', '줄을 이었', '불 보듯', '반토막', '짐을 쌉', '씨가 말랐', '하늘로 치솟']
METAPHOR = ['시베리아', '지옥', '러시안 룰렛', '극락', '식빵처럼', '매운맛', '얼음장', '냉동실', '찜질방', '아랫목', '구들장', '어허 시원']
ROUGH = ['젠장', '멍청', '마누라', '빌어먹을', '제기랄', '썩을']          # 대사 안에서만, 영상당 1~2회
BANNED = ['씨발', '시발', '병신', '좆', '개새', '짱깨', '쪽바리', '똥남아', '중국산 싸구려', '흑형', 'ㅋㅋ', '킹받', '갓생', '존맛', '레알', '헐']
SUSPECT = ['이라며 기절초풍', '신의 발명품', '서류를 집어 던지며', '라고 외쳤습니다', '레딧', '후기를 올렸', '댓글이 폭포수']   # 지어낸 사실·대사 의심 (출처 확인)
def quoted_spans(t): return [(m.start(), m.end()) for m in re.finditer(r'["“][^"”]*["”]', t)]
def main():
    t = open(sys.argv[1], encoding='utf-8').read(); t0 = t; t = t.replace('방콕', '방ㅋ').replace('뚝섬', '뚝ㅅ'); paras = [p for p in t.split('\n\n') if p.strip()]
    mins = len(t) / 415; spans = quoted_spans(t)
    inq = lambda i: any(a <= i < b for a, b in spans)
    found = {}
    for name, lex in (('소리·모양말', SOUND), ('몸 입말', BODY), ('센 입말', STRONG), ('관용구', IDIOM), ('과장 비유·자부심', METAPHOR)):
        hits = [w for w in lex for _ in re.finditer(re.escape(w), t)]; found[name] = hits
    total = sum(len(v) for v in found.values())
    print(f'분량 {len(t):,}자 ≈ {mins:.1f}분 · 말맛 표현 {total}개 = 1분당 {total / max(mins, .1):.1f}개 (기준 2~4)')
    for k, v in found.items(): print(f'  {k} {len(v)}: {", ".join(sorted(set(v)))[:120]}')
    dry = [i + 1 for i, p in enumerate(paras) if not any(w in p for w in SOUND)]
    print(f'소리·모양말 없는 문단 {len(dry)}/{len(paras)}개' + (f' → {dry[:25]}' if dry else ''))
    rough = [(w, m.start()) for w in ROUGH for m in re.finditer(w, t)]
    out = [w for w, i in rough if not inq(i)]
    print(f'거친 말 {len(rough)}회 (대사 밖 {len(out)}회' + (f': {out}' if out else '') + ') · 기준 대사 안 1~2회')
    bad = [w for w in BANNED if w in t]; sus = [w for w in SUSPECT if w in t]
    # 2026-11-10 담당자: 너무 심하면 오히려 퀄리티가 낮아 보인다 → 상한·반복·자리 검사 (스스로 검열)
    per = total / max(mins, .1)
    if per > 4: print(f'  [과함] 1분당 {per:.1f}개 > 4 → 덜어 낸다')
    from collections import Counter
    rep = [f'{w} {n}번' for w, n in Counter(sum(found.values(), [])).items() if n > 2 and len(w) > 1]
    if rep: print('  [반복] ' + ', '.join(rep) + ' → 같은 표현은 영상당 2번까지')
    strong = found['센 입말']; 
    if len(strong) > mins * 1.0: print(f'  [과함] 센 입말 {len(strong)}개 > 1분당 1개 → 줄인다')
    SAD = ['숨졌', '사망', '목숨을 잃', '유가족', '참사', '희생']
    near = [p[:30] for p in paras if any(w in p for w in SAD) and any(x in p for x in STRONG + ROUGH)]
    if near: print('  [자리] 사망·사고 문단에 센 말: ' + ' / '.join(near) + ' → 이 문단은 담담하게')
    sents = re.split(r'(?<=[.?!])\s+', t); lexall = STRONG + IDIOM + ROUGH
    run = [i for i in range(len(sents) - 1) if any(w in sents[i] for w in lexall) and any(w in sents[i + 1] for w in lexall)]
    if run: print(f'  [몰림] 센 말·관용구가 연달아 나온 문장 {len(run)}곳 → 한 문장 건너 하나')
    print('금지어: ' + (', '.join(bad) if bad else '없음'))
    print('지어낸 사실 의심: ' + (', '.join(sus) + ' → 출처 확인, 없으면 "떠올려 보시죠"로 가상임을 밝히거나 삭제' if sus else '없음'))
if __name__ == '__main__': main()
