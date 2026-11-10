"""아침 추천: 구독자 5만 이하 경제 채널(특히 AI 제작 채널)의 VPH 높은 영상 (2026-11-10 담당자 요청). API 키 없이 공개 페이지만 읽는다.
   python3 small_vph.py [--hours 72] [--max-subs 50000]"""
import re, sys, json, urllib.request, urllib.parse
UA = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'ko'}
QUERIES = ['경제', '노후', '연금', '퇴직금', '부동산', '집값', '상속 증여', '노후 파산', '몰락', '자영업 폐업', '물가', '사기 피해', '은퇴', '국민연금', '주택연금', '기업 몰락']
AI_HINT = re.compile(r'(AI|인공지능|생성형|TTS|음성 ?합성|이미지 ?생성|일레븐랩스|ElevenLabs|Midjourney|미드저니|브루|Vrew|vrew|챗GPT|ChatGPT|가상 ?인간|AI ?내레이션|AI ?음성)')
def get(u, t=30): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read().decode('utf-8', 'replace')
def num(t):
    m = re.search(r'([\d.,]+)\s*(천|만|억)?', t or '')
    return int(float(m.group(1).replace(',', '')) * {'천': 1e3, '만': 1e4, '억': 1e8}.get(m.group(2), 1)) if m else 0
def hours(t):
    m = re.search(r'(\d+)\s*(분|시간|일|주|개월|년)', t or '')
    if not m: return 1e9
    n = int(m.group(1)); return {'분': n / 60, '시간': n + .5, '일': n * 24, '주': n * 168, '개월': n * 720, '년': n * 8760}[m.group(2)]
def initial(s):
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', s); return json.loads(m.group(1)) if m else {}
def walk(o, key, out):
    if isinstance(o, dict):
        if key in o: out.append(o[key])
        for v in o.values(): walk(v, key, out)
    elif isinstance(o, list):
        for v in o: walk(v, key, out)
    return out
def search(q, sp):
    out = []
    for v in walk(initial(get(f'https://www.youtube.com/results?search_query={urllib.parse.quote(q)}&sp={sp}')), 'videoRenderer', []):
        if 'lengthText' not in v: continue
        ln = v['lengthText'].get('simpleText', '0:00')
        if len(ln.split(':')) == 2 and int(ln.split(':')[0]) < 4: continue          # 숏츠·짧은 영상 제외
        runs = v.get('ownerText', {}).get('runs', [{}]); cid = runs[0].get('navigationEndpoint', {}).get('browseEndpoint', {}).get('browseId', '')
        ag = v.get('publishedTimeText', {}).get('simpleText', '')
        out.append({'id': v['videoId'], 'title': ''.join(r['text'] for r in v['title']['runs']), 'views': num(v.get('viewCountText', {}).get('simpleText', '')),
                    'h': hours(ag), 'age': ag, 'ch': ''.join(r.get('text', '') for r in runs), 'cid': cid, 'len': ln, 'q': q})
    return out
def channel_info(cid):
    s = get(f'https://www.youtube.com/channel/{cid}')
    m = re.search(r'"content":"구독자 ([\d.,]+\s*[천만억]?)명"', s); v = re.search(r'"content":"동영상 ([\d.,]+\s*[천만]?)개"', s)   # 추천 채널 목록 말고 이 채널 머리글
    d = re.search(r'"description":"(.*?)","', s)
    return (num(m.group(1)) if m else -1), (num(v.group(1)) if v else -1), (d.group(1)[:400] if d else '')
def video_desc(vid):
    s = get(f'https://www.youtube.com/watch?v={vid}')
    m = re.search(r'"shortDescription":"(.*?)","', s); return m.group(1)[:1500] if m else ''
def main():
    a = sys.argv[1:]; H = float(a[a.index('--hours') + 1]) if '--hours' in a else 72
    MAXS = int(a[a.index('--max-subs') + 1]) if '--max-subs' in a else 50000
    found = {}
    for q in QUERIES:
        for sp in ('EgIIAg%253D%253D', 'EgIIAw%253D%253D'):               # 오늘 · 이번 주 업로드
            try:
                for v in search(q, sp):
                    if v['h'] <= H and v['id'] not in found: v['vph'] = v['views'] / max(v['h'], 1); found[v['id']] = v
            except Exception: pass
    cand = sorted(found.values(), key=lambda v: -v["vph"])[:150]; ch = {}; out = []
    for v in cand:
        if not v['cid']: continue
        if v['cid'] not in ch:
            try: ch[v['cid']] = channel_info(v['cid'])
            except Exception: ch[v['cid']] = (-1, -1, '')
        subs, nvid, cdesc = ch[v['cid']]
        if subs < 0 or subs > MAXS: continue
        try: desc = video_desc(v['id'])
        except Exception: desc = ''
        hint = sorted(set(AI_HINT.findall(desc + ' ' + cdesc + ' ' + v['title'])))
        out.append({**v, 'subs': subs, 'nvid': nvid, 'ai': hint, 'ratio': v['views'] / max(subs, 1)})
        if len(out) >= 25: break
    print(f'# 구독자 {MAXS:,} 이하 경제 채널 · 최근 {H:.0f}시간 · VPH 순 (후보 {len(found)}개 중)')
    for v in out:
        print(f"- VPH {v['vph']:,.0f} · 조회 {v['views']:,} · 구독 {v['subs']:,} (조회/구독 {v['ratio']:.1f}배) · {v['age']} · {v['len']}"
              f" · AI단서 {','.join(v['ai']) or '없음'} · [{v['ch']}] {v['title']} https://youtu.be/{v['id']}")
if __name__ == '__main__': main()
