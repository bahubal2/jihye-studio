"""아침 소재 탐색: 최근 1~2일 사이 뜨는 경제 이야기를 무료 공개 자료로 모은다 (2026-10-31 담당자 요청). LLM·API 키 없이 돈다.
   python3 tools/trend.py [--hours 48] [--out 파일.md]

모으는 것
  1) 감시 채널(brand/channel.json technique_radar.channels)의 48시간 안 새 영상 → VPH(시간당 조회수) 순
  2) 유튜브 검색(오늘·이번 주 업로드) 경제 키워드 영상 → VPH 순 (숏츠 제외)
  3) 구글 트렌드 한국 일간 급상승 검색어 (+ 관련 기사)
  4) 네이버 뉴스 많이 본 뉴스 (언론사별 랭킹 첫 화면)
채널 목록 파일이 없으면(새 세션) 아래 CHANNELS 를 쓴다.
"""
import os, re, sys, json, html, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
UA = {'User-Agent': 'Mozilla/5.0', 'Accept-Language': 'ko'}
CHANNELS = ['경제상담소', '돈흐르네', '이상하TV', '무궁화경제', '경제화이팅1', '돈맥상통', '지식한입', 'studio_pirates']
QUERIES = ['경제', '몰락', '부동산', '노후', '물가', '자영업', '브랜드', '연금']

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

def channel_videos(handle):
    out = []
    for v in walk(initial(get(f'https://www.youtube.com/@{urllib.parse.quote(handle)}/videos')), 'lockupViewModel', []):
        md = v['metadata']['lockupMetadataViewModel']
        rows = [q.get('text', {}).get('content', '') for r in md.get('metadata', {}).get('contentMetadataViewModel', {}).get('metadataRows', []) for q in r.get('metadataParts', [])]
        vw = next((r for r in rows if not r.endswith('전')), ''); ag = next((r for r in rows if r.endswith('전')), '')
        out.append({'id': v.get('contentId'), 'title': md['title']['content'], 'views': num(vw), 'h': hours(ag), 'age': ag, 'ch': handle})
    return out

def search(q, sp):
    out = []
    for v in walk(initial(get(f'https://www.youtube.com/results?search_query={urllib.parse.quote(q)}&sp={sp}')), 'videoRenderer', []):
        if 'lengthText' not in v: continue
        ln = v['lengthText'].get('simpleText', '0:00')
        if len(ln.split(':')) == 2 and int(ln.split(':')[0]) < 4: continue          # 4분 미만(숏폼 성격) 제외
        ag = v.get('publishedTimeText', {}).get('simpleText', '')
        out.append({'id': v['videoId'], 'title': ''.join(r['text'] for r in v['title']['runs']), 'views': num(v.get('viewCountText', {}).get('simpleText', '')),
                    'h': hours(ag), 'age': ag, 'ch': ''.join(r['text'] for r in v.get('ownerText', {}).get('runs', [])), 'len': ln})
    return out

def trends():
    root = ET.fromstring(get('https://trends.google.com/trending/rss?geo=KR')); ns = {'ht': 'https://trends.google.com/trending/rss'}; out = []
    for it in root.iter('item'):
        n = it.find('ht:news_item', ns)
        out.append((it.findtext('title'), it.findtext('ht:approx_traffic', '', ns), n.findtext('ht:news_item_title', '', ns) if n is not None else '', n.findtext('ht:news_item_url', '', ns) if n is not None else ''))
    return out

def naver():
    s = urllib.request.urlopen(urllib.request.Request('https://news.naver.com/main/ranking/popularDay.naver', headers=UA), timeout=30).read().decode('cp949', 'replace'); out = []
    for u, t in re.findall(r'<a href="(https://n\.news\.naver\.com/article/[^"]+)" class="list_title[^"]*"[^>]*>([^<]+)</a>', s):
        t = html.unescape(t).strip()
        if t not in [x[1] for x in out]: out.append((u, t))
    return out

def main():
    a = sys.argv[1:]; H = float(a[a.index('--hours') + 1]) if '--hours' in a else 48
    try: chs = [c['handle'] for c in json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'brand', 'channel.json'), encoding='utf-8'))['technique_radar']['channels']]
    except Exception: chs = CHANNELS
    L = ['# 아침 소재 탐색', '']
    vids = []
    for c in chs:
        try: vids += [v for v in channel_videos(c) if v['h'] <= H]
        except Exception as e: L.append(f'- ({c} 실패: {e})')
    for v in vids: v['vph'] = v['views'] / max(v['h'], 1)
    L += ['## 1. 감시 채널 새 영상 (최근 %d시간, VPH 순)' % H] + [f"- VPH {v['vph']:,.0f} · {v['views']:,}회 · {v['age']} · [{v['ch']}] {v['title']} https://youtu.be/{v['id']}" for v in sorted(vids, key=lambda v: -v['vph'])[:12]] + ['']
    found = {}
    for q in QUERIES:
        for sp in ('EgIIAg%253D%253D', 'EgIIAw%253D%253D'):                  # 오늘 / 이번 주 업로드
            try:
                for v in search(q, sp):
                    if v['h'] <= H and v['id'] not in found: v['vph'] = v['views'] / max(v['h'], 1); v['q'] = q; found[v['id']] = v
            except Exception: pass
    L += ['## 2. 유튜브 검색 (경제 키워드, 최근 %d시간, VPH 순)' % H] + [f"- VPH {v['vph']:,.0f} · {v['views']:,}회 · {v['age']} · {v['len']} · [{v['ch']}] {v['title']} https://youtu.be/{v['id']}  (검색어: {v['q']})" for v in sorted(found.values(), key=lambda v: -v['vph'])[:20]] + ['']
    try: L += ['## 3. 구글 트렌드 한국 급상승'] + [f'- {t} ({tr}) · {nt} {nu}' for t, tr, nt, nu in trends()[:20]] + ['']
    except Exception as e: L.append(f'(구글 트렌드 실패: {e})')
    try: L += ['## 4. 네이버 많이 본 뉴스 (언론사별 랭킹 첫 화면)'] + [f'- {t} {u}' for u, t in naver()[:40]] + ['']
    except Exception as e: L.append(f'(네이버 실패: {e})')
    txt = '\n'.join(L)
    if '--out' in a: open(a[a.index('--out') + 1], 'w', encoding='utf-8').write(txt)
    print(txt)

if __name__ == '__main__': main()
