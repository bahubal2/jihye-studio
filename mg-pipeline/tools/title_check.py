"""제목 최종 확인 (2026-11-10 담당자 필수 규칙): "그 제목으로 검색하면 VPH 높은 레퍼런스 영상이 나오는가?"
우리 영상이 그 영상들 옆에 추천 영상으로 뜨려면, 제목의 검색어 덩어리가 잘 되는 영상들과 같은 검색 결과를 공유해야 한다.

   python3 tools/title_check.py "제목 후보 1" "제목 후보 2" ... [--ref 영상ID]

후보마다 제목 전체를 그대로(담당자 시크릿 창 검사와 같게) 두 번 유튜브 검색(공개 페이지, API 키 없음)을 하고
상위 결과의 조회수·VPH·채널을 보여 준다. 점수 = 상위 20개 중 VPH 상위 5개 합(롱폼만), --ref 영상이 결과에 나오면 표시.
"""
import re, sys, json, urllib.request, urllib.parse
UA = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'ko'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode('utf-8', 'replace')
def num(t):
    m = re.search(r'([\d.,]+)\s*(천|만|억)?', t or '')
    return int(float(m.group(1).replace(',', '')) * {'천': 1e3, '만': 1e4, '억': 1e8}.get(m.group(2), 1)) if m else 0
def hours(t):
    m = re.search(r'(\d+)\s*(분|시간|일|주|개월|년)', t or '')
    if not m: return 1e9
    n = int(m.group(1)); return {'분': n / 60, '시간': n + .5, '일': n * 24, '주': n * 168, '개월': n * 720, '년': n * 8760}[m.group(2)]
def walk(o, key, out):
    if isinstance(o, dict):
        if key in o: out.append(o[key])
        for v in o.values(): walk(v, key, out)
    elif isinstance(o, list):
        for v in o: walk(v, key, out)
    return out
def search(q):
    s = get('https://www.youtube.com/results?search_query=' + urllib.parse.quote(q))
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', s); d = json.loads(m.group(1)) if m else {}
    out = []
    for v in walk(d, 'videoRenderer', []):
        ln = v.get('lengthText', {}).get('simpleText', '')
        if not ln or (len(ln.split(':')) == 2 and int(ln.split(':')[0]) < 4): continue      # 숏츠·짧은 영상 제외
        ag = v.get('publishedTimeText', {}).get('simpleText', ''); views = num(v.get('viewCountText', {}).get('simpleText', ''))
        h = hours(ag)
        out.append({'id': v['videoId'], 'title': ''.join(r['text'] for r in v['title']['runs']), 'views': views, 'age': ag,
                    'vph': views / max(h, 1) if h < 1e8 else 0, 'ch': ''.join(r.get('text', '') for r in v.get('ownerText', {}).get('runs', []))})
    return out[:20]
def report(q, ref):
    seen = {}
    for _ in range(2):                      # 검색 결과가 매번 조금씩 달라서 두 번 합친다
        for x in search(q): seen.setdefault(x['id'], x)
    res = list(seen.values()); top = sorted(res, key=lambda x: -x['vph'])[:5]; score = sum(x['vph'] for x in top)
    hit = next((i + 1 for i, x in enumerate(res) if x['id'] == ref), None) if ref else None
    print(f'  검색 "{q}" → 결과 {len(res)}개 · 점수(VPH 상위5 합) {score:,.0f}' + (f' · 레퍼런스 {hit}위' if hit else (' · 레퍼런스 없음' if ref else '')))
    for x in top: print(f'     VPH {x["vph"]:>7,.0f} · 조회 {x["views"]:>9,} · {x["age"]:>6} · [{x["ch"]}] {x["title"][:60]}')
    return score, hit
def main():
    a = sys.argv[1:]; ref = None
    if '--ref' in a: i = a.index('--ref'); ref = a[i + 1]; del a[i:i + 2]
    rows = []
    for t in a:
        print(f'■ {t}')
        s1, h1 = report(t, ref)              # 담당자가 시크릿 창에 제목을 그대로 붙여 넣는 검사 = 이것이 합격 기준
        rows.append((s1, t, h1))
    print('\n순위 (점수 높을수록 잘 되는 영상과 같은 검색 결과를 공유)')
    for s, t, h in sorted(rows, reverse=True): print(f'  {s:>9,.0f}  {"합격 " if s >= 500 else "불합격 "}{"[레퍼런스 노출] " if h else ""}{t}')
    print('기준: 제목 전체를 그대로 검색해 VPH 높은 같은 주제 영상이 나와야 합격 (곧은 따옴표 \"…\" 는 정확히 일치 검색이 되어 결과가 0개가 되기 쉽다)')
if __name__ == '__main__': main()
