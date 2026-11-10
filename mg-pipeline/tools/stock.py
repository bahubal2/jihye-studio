"""Pixabay 무료 스톡 영상 검색·다운로드 (.env 의 PIXABAY_API_KEY).
   python tools/stock.py <이름> <id> "<영어 검색어>" [--pick N] [--min 8]

검색 결과 중 가로 영상(16:9 근처), min 초 이상, 1920px 이상인 것을 골라 captures/_raw/<id>.mp4 로 받고,
확인용으로 처음·중간·끝 장면을 out/_stock_<id>.jpg 에 붙여 둔다. --pick N 으로 N번째 후보를 고른다.
받은 뒤 motion.json 의 clips 에 {"id": ..., "prompt": "", "src": "pixabay"} 로 넣으면 animate.py 가 장면 길이에 맞춰 변환한다(fal 호출 없음).
Pixabay 콘텐츠 라이선스: 상업적 사용 가능, 출처 표기 불필요 (원본 그대로 재판매 금지).
"""
import os, sys, json, subprocess, urllib.request, urllib.parse, argparse
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, KIT)
import mgp
UA = {'User-Agent': 'mg-pipeline/1.0 (jihye-hosu channel video tool)'}

def search(key, q, n=20):
    u = 'https://pixabay.com/api/videos/?' + urllib.parse.urlencode({'key': key, 'q': q, 'per_page': n, 'safesearch': 'true', 'video_type': 'film'})
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30)).get('hits', [])

def used_pages(proj, me):
    """채널의 모든 프로젝트 captures/_credits.json 에 적힌 Pixabay 페이지 = 이미 쓴 클립 (지금 받는 id 자리는 제외)."""
    import glob
    out = set()
    for f in glob.glob(os.path.join(os.path.dirname(proj), '*', 'captures', '_credits.json')):
        try: cr = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        for k, v in cr.items():
            if os.path.abspath(f).startswith(os.path.abspath(proj)) and k == me: continue
            if isinstance(v, dict) and v.get('page'): out.add(v['page'])
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('project'); ap.add_argument('id'); ap.add_argument('query')
    ap.add_argument('--pick', type=int, default=0); ap.add_argument('--min', type=float, default=8)
    ap.add_argument('--reuse', action='store_true', help='다른 영상·다른 id 에서 이미 쓴 클립도 허용 (기본: 건너뜀)')
    a = ap.parse_args(); mgp.load_env(); proj = mgp.use(a.project)
    from mg import ffmpeg_exe
    key = os.environ.get('PIXABAY_API_KEY')
    if not key: raise SystemExit('.env 에 PIXABAY_API_KEY 가 없습니다.')
    used = used_pages(proj, a.id) if not a.reuse else set()   # 2026-11-10 담당자: 예전 영상에 쓴 스톡이 자꾸 나온다 → 채널 전체에서 한 번만
    ok = []; skipped = 0
    for h in search(key, a.query, 40):
        if h['pageURL'] in used: skipped += 1; continue
        v = h['videos'].get('large') if h['videos'].get('large', {}).get('width', 0) >= 1920 else None
        v = v if v and v['width'] <= 2560 else h['videos'].get('medium')
        if not v or not v.get('url') or v['width'] < 1280 or h['duration'] < a.min: continue
        if not 1.6 <= v['width'] / max(1, v['height']) <= 1.9: continue
        ok.append((h, v))
    if not ok: raise SystemExit(f'조건에 맞는 새 영상이 없습니다: "{a.query}" (이미 쓴 클립 {skipped}개 건너뜀 → 검색어를 바꾸세요)')
    h, v = ok[min(a.pick, len(ok) - 1)]
    raw = os.path.join(proj, 'captures', '_raw', a.id + '.mp4'); os.makedirs(os.path.dirname(raw), exist_ok=True)
    open(raw, 'wb').write(urllib.request.urlopen(urllib.request.Request(v['url'], headers=UA), timeout=300).read())
    ff = ffmpeg_exe(); d = h['duration']; sheet = os.path.join(proj, 'out', f'_stock_{a.id}.jpg')
    subprocess.run([ff, '-v', 'error', '-y'] + sum([['-ss', f'{t:.2f}', '-i', raw] for t in (0.5, d / 2, max(0, d - 1))], []) +
                   ['-filter_complex', '[0]scale=480:-1[a];[1]scale=480:-1[b];[2]scale=480:-1[c];[a][b][c]hstack=3', '-frames:v', '1', sheet], check=True)
    cred = os.path.join(proj, 'captures', '_credits.json'); cr = json.load(open(cred, encoding='utf-8')) if os.path.exists(cred) else {}
    cr[a.id] = {'source': 'Pixabay', 'page': h['pageURL'], 'user': h.get('user'), 'tags': h['tags']}
    json.dump(cr, open(cred, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{a.id}: 후보 {len(ok)}개 중 {a.pick}번 · {v["width"]}x{v["height"]} · {d}초 · {h["tags"][:60]}\n  확인: {sheet}')

if __name__ == '__main__': main()
