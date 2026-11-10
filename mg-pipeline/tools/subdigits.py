"""자막 글자만 숫자로 바꾸기: 대본은 음성을 위해 한글로 풀어 쓰고("이천이십오 년"), 화면 자막은 숫자로("2025년").
   python tools/subdigits.py <이름> [--check]

input/narration.srt 를 고친다(원본은 narration_한글숫자.srt 로 보관). 음성과 자막 시각은 그대로다.
--check: 바꾸지 않고 대본(input/script.txt)에서 무엇이 어떻게 바뀌는지만 보여 준다.
한자어 숫자 + 단위(년·월·일·명·원·퍼센트 …)만 바꾼다. 고유어 숫자(한·두·세·열일곱 살)는 그대로 둔다.
"""
import os, re, sys, shutil

D = dict(zip('영공일이삼사오육칠팔구', [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
SMALL = {'십': 10, '백': 100, '천': 1000}; BIG = {'만': 10 ** 4, '억': 10 ** 8, '조': 10 ** 12}
NUM = '영공일이삼사오육칠팔구십백천만억'
UNITS = ['퍼센트포인트', '학년도', '킬로미터', '킬로그램', '헥타르', '톤', '편', '건', '등', '달러', '퍼센트', '킬로와트시', '킬로와트', '와트', '볼트', '년대', '개월', '개년', '개국', '가구', '분기', '세대', '년', '월', '일', '명', '원', '개', '곳', '평', '도', '번', '인', '층', '대', '배']
SINGLE_OK = {'킬로그램', '헥타르', '톤', '등', '년', '월', '일', '명', '원', '번', '층', '인', '평', '분기', '년대', '퍼센트', '퍼센트포인트', '개월', '개', '곳', '볼트', '와트', '가구', '개년'}
PARTICLE = tuple('이 가 은 는 을 를 에 의 도 만 로 엔 째 간 씩 짜 대 쯤 뿐 과 와 전 후 부 까 이었 이던 이나 으로 에서 동안 급 용 라 였 입 어치 당 안팎 남짓 가까이'.split())
FIXED = [('일삼삼공', '1330'), ('오십분', '50분'), ('이삼십분', '20~30분'), ('단 십분', '단 10분'), ('오십오 명', '55명'), ('칠 위', '7위'), ('육 위', '6위'), ('오 위', '5위'), ('사 위', '4위'), ('삼 위', '3위'), ('백여덟 곳', '108곳'), ('일오팔팔 팔일일이', '1588-8112'), ('삼사십 대', '30~40대'), ('십분의 일', '10분의 1'), ('네 분의 일', '4분의 1'), ('사분의 일', '4분의 1'), ('사 분의 일', '4분의 1'), ('삼에서 오 퍼센트', '3~5%'),
         ('일조 사천억 원', '1조 4,000억 원'), ('삼조 사천억 원', '3조 4,000억 원'), ('삼십이조 원', '32조 원'),
         ('구십팔분', '98분'), ('오십칠분', '57분'), ('이십분', '20분'), ('십일분', '11분'), ('구분대', '9분대'),
         ('천오백 집씩', '1,500집씩'), ('십일월', '11월'), ('십이월', '12월'), ('칠월', '7월'), ('시월', '10월'), ('삼월', '3월'), ('이월', '2월'), ('사월', '4월'), ('오월', '5월'), ('유월', '6월'), ('팔월', '8월'), ('구월', '9월'),
         ('이분기', '2분기'), ('일 위', '1위'), ('월 이 일', '월 2일'), ('이 위 ', '2위 '), ('일호점', '1호점'), ('오십 호점', '50호점'), ('십일억이', '11억이'), ('삼십초', '30초'), ('일등 ', '1등 '), ('일등.', '1등.'), ('일월과', '1월과'), ('사백여 개', '400여 개'), ('십일억 원어치', '11억 원어치'), ('일분기', '1분기'), ('일심에서', '1심에서'), ('년 일월', '년 1월')]

def parse(s):
    """한자어 숫자 문자열(공백 없이) → 정수."""
    total = sec = num = 0
    for ch in s:
        if ch in D: num = D[ch]
        elif ch in SMALL: sec += (num or 1) * SMALL[ch]; num = 0
        elif ch in BIG: total += ((sec + num) or 1) * BIG[ch]; sec = num = 0
    return total + sec + num

KEEP = {'백 번', '이 일'}
SHOW = {'킬로미터': 'km', '킬로그램': 'kg', '헥타르': 'ha', '퍼센트': '%', '퍼센트포인트': '%p', '볼트': 'V', '킬로와트시': 'kWh', '킬로와트': 'kW', '와트': 'W'}   # 화면에 기호로 쓰는 단위                                                                       # 비유로 쓴 수는 그대로 ("내일 백 번을 잃는")

def fmt(v, plain=False):
    if plain: return str(v)
    if v >= 10 ** 8:
        e, r = divmod(v, 10 ** 8); m = r // 10 ** 4
        return f'{e:,}억' + (f' {m:,}만' if m else '')
    if v >= 10 ** 4 and v % 10 ** 4 == 0: return f'{v // 10 ** 4:,}만'
    return f'{v:,}'

U = '|'.join(UNITS)
# 숫자 덩어리: 만·억으로 끝난 덩어리 뒤에는 띄어 쓴 덩어리가 이어질 수 있다 ("만 천", "칠억 오천만", "십이만 육천팔백구십육")
CH = f'[{NUM}]+'
RX = re.compile(rf'(?<![가-힣0-9,])((?:[{NUM}]*[만억] )*{CH})(?: 점 ([영공일이삼사오육칠팔구]+))?(여)?( ?)({U})?(?=([가-힣]*))')

JO = re.compile(r'(?<![가-힣])([일이삼사오육칠팔구십백천]+)조(?: ([일이삼사오육칠팔구십백천]+)억)? 원')   # "팔조 구천억 원" → "8조 9,000억 원" ("구조로" 같은 낱말은 '원'이 안 붙어 그대로)
def _jo(m): return f'{parse(m.group(1))}조' + (f' {parse(m.group(2)):,}억' if m.group(2) else '') + ' 원'
def convert(text):
    for a, b in FIXED: text = text.replace(a, b)
    text = JO.sub(_jo, text)
    text = re.sub(r'(?<![가-힣])([일이삼사오육칠팔구십백천]+)년대', lambda m: f'{parse(m.group(1))}년대', text)   # "천구백오십년대" → "1950년대"
    text = re.sub(r'(\d+)월 ([일이삼사오육칠팔구십]+) 일(?![가-힣])', lambda m: f'{m.group(1)}월 {parse(m.group(2))}일', text)   # "1월 이십일 일 밤" → "1월 21일 밤" (띄어 읽은 날짜)
    text = re.sub(r'(\d+)월 ([일이삼사오육칠팔구십]+)일', lambda m: f'{m.group(1)}월 {parse(m.group(2))}일', text)   # "9월 이십삼일" → "9월 23일"
    out = []; last = 0; changes = []
    for m in RX.finditer(text):
        num, dec, yeo, sp, unit, after = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6)
        chars = num.replace(' ', '')
        if not unit:
            if not (len(chars) >= 2 and chars[-1] in '만억' and not sp): continue          # "이백만에서" 처럼 만·억으로 끝나는 수만
            if set(chars) <= set('만억') or (after and not after.startswith(PARTICLE)): continue   # "만만한", "억억" 같은 낱말은 숫자가 아니다
        else:
            rest = after or ''
            if rest and not rest.startswith(PARTICLE) and unit not in SHOW and not (unit == '년' and rest.startswith('대')): continue
            if len(chars) == 1 and unit not in SINGLE_OK: continue
            if not sp and not yeo: continue                                                    # 수와 단위는 띄어 쓴 경우만 ("이번엔", "사이도" 제외)
            if m.group(0) in KEEP: continue
        v = parse(chars); s = fmt(v, plain=unit in ('년', '년대', '월', '일', '학년도'))       # 연도·날짜는 쉼표 없이
        if dec: s += '.' + ''.join(str(D[c]) for c in dec)
        if yeo: s += '여'
        u = SHOW.get(unit, unit or '')
        sep = ' ' if (u and (s.endswith(('만', '억', '여')) and u not in ('%', '%p', 'V', 'W'))) else ''
        new = s + sep + u
        out.append(text[last:m.start()]); out.append(new); last = m.end(); changes.append((m.group(0), new))
    out.append(text[last:])
    return ''.join(out), changes

def main():
    a = sys.argv[1:]; check = '--check' in a; name = [x for x in a if not x.startswith('--')][0]
    K = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); inp = os.path.join(K, 'projects', name, 'input')
    if check:
        t, ch = convert(open(os.path.join(inp, 'script.txt'), encoding='utf-8').read())
        for x, y in ch: print(f'  {x}  →  {y}')
        print(f'{len(ch)}곳'); return
    srt = os.path.join(inp, 'narration.srt'); bak = os.path.join(inp, 'narration_한글숫자.srt')
    if not os.path.exists(bak): shutil.copy(srt, bak)
    blocks = open(bak, encoding='utf-8-sig').read().strip().split('\n\n'); n = 0; res = []
    # 수가 자막 두 개에 걸쳐 끊긴 경우("이천십사" / "년 29%였습니다") 앞 자막 끝의 수를 다음 자막 앞으로 옮긴다 (시각은 그대로)
    parts = [b.split('\n') for b in blocks]
    for i in range(len(parts) - 1):
        a, b = ' '.join(parts[i][2:]), ' '.join(parts[i + 1][2:])
        m = re.search(rf'(?:^| )([{NUM}]+(?: [{NUM}]+)*)$', a)
        if m and re.match(rf'({U}|[{NUM}])', b) and parse(m.group(1).replace(' ', '')) > 0:
            frag = m.group(1); parts[i][2:] = [a[:m.start(1)].rstrip()]; parts[i + 1][2:] = [frag + (' ' if not b[0] in NUM else ' ') + b]
    blocks = ['\n'.join(x) for x in parts]
    for b in blocks:
        ln = b.split('\n'); body, ch = convert('\n'.join(ln[2:])); n += len(ch); res.append('\n'.join(ln[:2] + [body]))
    for k in range(len(res) - 1):                                        # 자막 끝의 "일조" + 다음 자막이 숫자로 시작 → "1조"
        a_, b_ = res[k].split('\n'), res[k + 1].split('\n')
        m = re.search(r'(?:^| )([일이삼사오육칠팔구십백천]+)조$', a_[-1])
        if m and len(b_) > 2 and re.match(r'[0-9]', b_[2]): a_[-1] = a_[-1][:m.start(1)] + f'{parse(m.group(1))}조'; res[k] = '\n'.join(a_)
    open(srt, 'w', encoding='utf-8').write('\n\n'.join(res) + '\n'); print(f'자막 {len(blocks)}개 중 숫자 {n}곳을 바꿨습니다. 원본: {bak}')

if __name__ == '__main__': main()
