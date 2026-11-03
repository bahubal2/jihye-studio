"""기법 레이더: 감시 채널의 최근 영상을 찾아 Gemini 로 첫 몇 분의 연출 기법을 분석한다 (2026-10-30 담당자 요청).
   python tools/radar.py              최근 영상 목록과 예상 비용만 출력 (무료)
   python tools/radar.py --yes        분석 실행 (Gemini, 소액)
   옵션: --days 45 (최근 며칠) --per 1 (채널당 영상 수) --sec 180 (앞에서 몇 초) --only 지식한입,이상하TV
   --body          본편 분석 (2026-11-03): 인트로 뒤 --from 300 초부터 --sec 초 동안 '끝까지 보게 만드는 장치'를 본다
   --ids a,b,c     채널 목록 대신 이 영상들만 (경쟁 상위 영상 직접 지정)

채널 목록은 brand/channel.json 의 technique_radar.channels. 결과는 brand/radar/<날짜>/ 에 영상별 .md 와 썸네일, 제목·썸네일 패턴 분석(_titles.md).
영상 찾기는 채널의 공개 '동영상' 탭 첫 화면만 읽는다(키 필요 없음, 숏츠는 그 탭에 없다). RSS 피드는 2026-10 기준 404라 쓰지 않는다.
"""
import os, re, sys, json, time, datetime, urllib.request, urllib.error, base64
import xml.etree.ElementTree as ET
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS = ('gemini-flash-latest', 'gemini-3.8-flash')
UA = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'ko'}

ASK = """당신은 한국 경제·지식 유튜브 영상의 편집 연출 분석가입니다. 이 영상의 앞 {sec}초를 보고, 우리 채널(40대 이상 대상 경제·심리 해설, 모션그래픽 자동 제작)이 배울 연출 기법을 한국어로 정리하세요. 추측은 '추정'이라고 표시하세요.

1. 후킹 대본 구조: 첫 30초 내레이션을 문장 단위로 요약하고, 각 문장이 쓰는 장치(숫자 충격, 질문, 반전, 오픈 루프(뒤에서 알려 주겠다), 시청자 지목, 결과 먼저 보여 주기 등)를 적는다.
2. 컷 타임라인 0~30초: '초 | 화면 | 기법' 표. 컷이 바뀔 때마다 한 줄.
3. 30초 이후 1분당 컷 수와 그래픽 등장 수(추정).
4. 화면 레이어: 바닥(배경)·중간·앞(글자/그래픽) 각각 무엇을 쓰는지. 실사 사진/영상, AI 이미지, 스톡, 일러스트, 3D, 지도, 기사 캡처, 차트 등.
5. 글자 연출: 크기(화면 높이 대비), 색, 등장 방식, 강조 방식(박스, 밑줄, 하이라이트, 흔들림 등), 자막 스타일.
6. 전환과 카메라: 전환 종류, 줌·팬, 화면 흔들림, 플래시 등.
7. 소리: 효과음이 나는 순간과 빈도, 배경음 유무와 분위기.
8. 특히 새롭거나 강력하다고 느낀 기법 3가지: 각각 '무엇을 / 언제 쓰나 / HTML·CSS 모션그래픽으로 만드는 방법'을 구체적으로.
"""
ASK_B = """당신은 한국 경제·지식 유튜브의 '시청 지속' 분석가입니다. 이 영상은 인트로가 끝난 뒤 본편 구간({a}~{b}초)입니다. 시청자가 중간에 나가지 않고 끝까지 보게 만드는 장치를 한국어로 정리하세요. 추측은 '추정'이라고 표시하세요.

1. 대본 장치 타임라인: '초 | 내레이션 요약 | 장치' 표. 장치 예: 다시 걸기(재후킹), 오픈 루프(뒤에서 알려 주겠다), 1위 예고 되풀이, 인물·사연 이어 가기, 반전, 비교·대결, 퀴즈, 시청자 지목, 감정(분노·안타까움·통쾌), 생활 체감 환산, 말투 변화, 짧은 정리.
2. 같은 틀의 반복을 어떻게 피하는가: 순위(섹션)마다 시작 방식·길이·전개 순서가 어떻게 달라지는지.
3. 숫자 전달: 1분에 소리로 나오는 숫자 개수, 숫자를 화면으로만 보여 주는 경우, 숫자를 체감시키는 방법.
4. 화면 리듬: 1분당 컷 수, 20~30초마다 화면에서 새로 일어나는 일(카메라 움직임, 줌, 사진 축소·확대, 선·화살표 긋기, 지도, 차트, 기사, 인물 사진, 실사 영상).
5. 카메라워크와 그래픽 연출 목록: 각각 몇 초에, 무엇을, 어떻게(크래쉬줌, 줌아웃 공개, 화면 분할, 액자 축소, 하이라이트, 마스킹 등).
6. 소리: 배경음악의 분위기 변화 지점, 효과음 종류와 빈도, 무음(정적) 사용.
7. 우리 채널(55세 이상 남성 중심 경제 채널, HTML/CSS 모션그래픽 자동 제작)이 바로 가져올 '중간 이탈 막는 기법' 5가지: 각각 '무엇을 / 대본에서 어떻게 / 화면에서 어떻게 (CSS·HTML로 만드는 법)'.
"""
ASK_T = """아래는 한국 경제·지식 유튜브 채널들의 최근 인기 영상 제목과 썸네일입니다(조회수 포함). 클릭을 부르는 패턴을 한국어로 분석하세요.
1. 제목 패턴: 앞쪽에 오는 낱말 종류, 따옴표 인용, 숫자, 순위(TOP N), 반전·부정 표현, 길이. 조회수가 높은 것과 낮은 것의 차이.
2. 썸네일 패턴: 큰 글자 개수·글자 수·색·위치, 인물(표정·나이), 사물·로고, 화살표·뱃지, 배경, 대비. 제목과 썸네일 글자가 어떻게 역할을 나누는지.
3. 40대 이상 시청자 경제 채널이 바로 쓸 규칙 7가지.
제목 목록:
{titles}
"""

def channels():
    d = json.load(open(os.path.join(KIT, 'brand', 'channel.json'), encoding='utf-8'))
    return d['technique_radar']['channels']

def get(url, timeout=30, raw=False):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
    return r if raw else r.decode('utf-8', 'replace')

def _num(t):
    m = re.match(r'([\d.,]+)\s*(천|만|억)?', t or '')
    if not m: return 0
    return int(float(m.group(1).replace(',', '')) * {'천': 1e3, '만': 1e4, '억': 1e8}.get(m.group(2), 1))
def _days(t):
    m = re.match(r'(\d+)\s*(분|시간|일|주|개월|년)', t or '')
    if not m: return 9999
    return int(m.group(1)) * {'분': 0, '시간': 0, '일': 1, '주': 7, '개월': 30, '년': 365}[m.group(2)]
def videos(url):
    """채널의 '동영상' 탭(숏츠 제외) 첫 화면 30개: 조회수·올린 지 며칠."""
    s = get(url.rstrip('/') + '/videos')
    d = json.loads(re.search(r'var ytInitialData = (\{.*?\});</script>', s).group(1)); out = []
    def walk(o):
        if isinstance(o, dict):
            if 'lockupViewModel' in o:
                v = o['lockupViewModel']; md = v['metadata']['lockupMetadataViewModel']
                rows = [q.get('text', {}).get('content', '') for r in md.get('metadata', {}).get('contentMetadataViewModel', {}).get('metadataRows', []) for q in r.get('metadataParts', [])]
                vw = next((r for r in rows if re.search(r'[\d.]+\s*(천|만|억)?회?$', r) and not re.search(r'전$', r)), ''); ag = next((r for r in rows if r.endswith('전')), '')
                out.append({'id': v.get('contentId'), 'title': md['title']['content'], 'views': _num(vw), 'age': _days(ag), 'published': ag})
            for x in o.values(): walk(x)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(d); return out

def gemini(parts, key, cfg=None):
    body = {'contents': [{'parts': parts}], 'generationConfig': cfg or {}}
    err = ''
    for model in MODELS:
        try:
            req = urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent', json.dumps(body).encode(), {'Content-Type': 'application/json', 'x-goog-api-key': key})
            r = json.load(urllib.request.urlopen(req, timeout=600))
            txt = ''.join(p.get('text', '') for p in r['candidates'][0]['content']['parts'] if not p.get('thought')).strip()
            return txt, r.get('usageMetadata', {}), model
        except urllib.error.HTTPError as e: err = f'{model} HTTP {e.code} ' + e.read().decode('utf-8', 'replace')[:200]
        except Exception as e: err = f'{model} ' + str(e)[:200]
    raise RuntimeError(err)

def main():
    a = sys.argv[1:]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    days, per, sec = opt('--days', 45), opt('--per', 1), opt('--sec', 180)
    only = set(opt('--only', '').split(',')) - {''}
    body, frm = '--body' in a, opt('--from', 300)
    ids = [x for x in opt('--ids', '').split(',') if x]
    picks = [dict(id=i, ch='지정', group='', title=i, views=0, published='', all=[]) for i in ids]
    for ch in ([] if ids else channels()):
        if only and ch['handle'] not in only: continue
        try:
            vids = videos(ch['url'])
            recent = [v for v in vids if v['age'] <= days] or vids[:3]
            recent.sort(key=lambda v: -v['views'])
            for v in recent[:per]: picks.append(dict(v, ch=ch['handle'], group=ch['group'], all=vids))
            print(f"{ch['handle']:<12} 영상 {len(vids)}개 중 최근 {days}일 {len([v for v in vids if v['age'] <= days])}개 → " + ', '.join(f"{p['published']} {p['views']:,}회 「{p['title'][:40]}」" for p in picks if p['ch'] == ch['handle']))
        except Exception as e: print(f"{ch['handle']:<12} 실패: {e}")
    est = len(picks) * sec * 100 / 1e6 * 0.5 + 0.02
    print(f'\n분석 대상 {len(picks)}편 · 앞 {sec}초 · 낮은 해상도 → 예상 비용 약 ${est:.2f} (Gemini flash, 대략)')
    if '--yes' not in a: print('실행하려면 --yes'); return
    key = None
    for ln in open(os.path.join(KIT, '.env'), encoding='utf-8'):
        if ln.startswith('GEMINI_API_KEY='): key = ln.split('=', 1)[1].strip()
    if not key: raise SystemExit('.env 에 GEMINI_API_KEY 가 없습니다.')
    out = os.path.join(KIT, 'brand', 'radar', datetime.date.today().isoformat()); os.makedirs(out, exist_ok=True)
    tok = 0; titles = []; imgs = []
    for p in picks:
        fn = os.path.join(out, f"{p['ch']}_{p['id']}{'_본편' if body else ''}.md")
        for v in p['all'][:8]: titles.append(f"- [{p['ch']}] {v['title']} ({v['views']:,}회, {v['published']})")
        try:
            jpg = get(f"https://i.ytimg.com/vi/{p['id']}/hqdefault.jpg", raw=True); open(fn[:-3] + '.jpg', 'wb').write(jpg); imgs.append((p, jpg))
        except Exception: pass
        if os.path.exists(fn): print('있음', fn); continue
        t0 = time.time()
        try:
            s0, s1 = (frm, frm + sec) if body else (0, sec)
            txt, use, model = gemini([{'file_data': {'file_uri': f"https://www.youtube.com/watch?v={p['id']}"}, 'video_metadata': {'start_offset': f'{s0}s', 'end_offset': f'{s1}s'}},
                                      {'text': ASK_B.format(a=s0, b=s1) if body else ASK.format(sec=sec)}], key, {'mediaResolution': 'MEDIA_RESOLUTION_LOW'})
        except Exception as e: print('실패', p['ch'], e); continue
        tok += use.get('totalTokenCount', 0)
        open(fn, 'w', encoding='utf-8').write(f"# [{p['ch']}] {p['title']}\nhttps://youtu.be/{p['id']} · {p['published']} · {p['views']:,}회 · {model} · 토큰 {use.get('totalTokenCount')}\n\n{txt}\n")
        print(f"분석 {p['ch']} ({time.time() - t0:.0f}초, 토큰 {use.get('totalTokenCount')})")
    if body or ids or not titles: print(f'끝: {out} · 총 토큰 {tok:,}'); return
    parts = [{'text': ASK_T.format(titles='\n'.join(titles))}]
    for p, jpg in imgs: parts += [{'text': f"썸네일: [{p['ch']}] {p['title']} ({p['views']:,}회)"}, {'inline_data': {'mime_type': 'image/jpeg', 'data': base64.b64encode(jpg).decode()}}]
    try:
        txt, use, model = gemini(parts, key); tok += use.get('totalTokenCount', 0)
        open(os.path.join(out, '_titles.md'), 'w', encoding='utf-8').write(f'# 제목·썸네일 패턴 ({model})\n\n{txt}\n')
    except Exception as e: print('제목 분석 실패', e)
    print(f'끝: {out} · 총 토큰 {tok:,}')

if __name__ == '__main__': main()
