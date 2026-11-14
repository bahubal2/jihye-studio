"""잘 된 레퍼런스 영상의 '대본 기술'을 뜯어본다 (2026-11-14 담당자: "다른 채널 영상에서 대본 스킬을 습득하고, 정리하고, 진화시켜라").
   python3 tools/ref_analyze.py <유튜브 영상 ID 또는 주소> [메모]

Gemini 에 유튜브 영상을 직접 넣어(소리·화면 포함) 우리 채널이 바로 가져다 쓸 수 있는 형태로 분석한다.
결과: brand/레퍼런스_분석/<ID>.md  (분석 원문)  — 여러 편을 모은 뒤 brand/대본_플레이북.md 에 '증거 있는 기법'만 정리해 올린다.
분석 항목: 구간별 구조와 시각 · 첫 30초 훅 장치 · 긴장↔이완 곡선 · 궁금증 고리(열고 닫는 자리) · 말투·입말 · 숫자 다루는 법 · 반전 · 결말 · 우리 채널이 가져올 것 / 버릴 것."""
import os, sys, re, json, urllib.request
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, KIT)
import mgp; mgp.load_env(); KEY = os.environ['GEMINI_API_KEY']
arg = sys.argv[1]; note = ' '.join(sys.argv[2:])
vid = re.search(r'(?:v=|youtu\.be/|shorts/)?([A-Za-z0-9_-]{11})', arg).group(1)
OUT = os.path.join(KIT, 'brand', '레퍼런스_분석'); os.makedirs(OUT, exist_ok=True)
ASK = f"""당신은 한국 유튜브 경제·시사 채널의 대본 작가 겸 편집자입니다. 이 영상은 같은 분야에서 아주 잘 된 영상입니다({note}).
우리 채널(지혜호수_경제연구소, 55~70세 남성 시청자, 숫자로 확인하고 사실로 말하는 존댓말 해설)이 대본 기술을 배우려고 합니다.
영상의 내레이션과 화면을 끝까지 보고, 아래 항목을 한국어로 구체적으로 답하세요. 각 항목에 영상 속 실제 문장을 짧게 그대로 인용하고 시각(분:초)을 붙이세요. 추측은 추측이라고 쓰세요.

1. 전체 구조표: 구간마다 시작 시각, 역할(훅/전환/설명/반전/정리/결말 등), 길이, 그 구간의 긴장도(1~5)
2. 첫 30초: 첫 문장, 시청자를 붙잡는 장치(숫자·장면·질문·대사·위협·약속 등), 문장 길이와 속도
3. 인트로→본문 전환: 어떻게 분위기를 바꾸는가(말투·속도·음악·화면), 실제 문장
4. 긴장↔이완 곡선: 어디서 긴장을 올리고 어디서 풀어 주는가, 그 방법
5. 궁금증 고리: 열어 두고 나중에 닫는 질문·약속·떡밥을 모두 찾고, 연 시각과 닫은 시각
6. 말투: 시청자를 부르는 말, 입말·속어·관용구·감탄 예시, 문장 끝맺음 패턴, 존댓말/반말
7. 숫자 다루는 법: 숫자를 어떻게 체감되게 바꾸는가(비유·환산·비교), 한 문장에 숫자 몇 개
8. 반전과 '안 맞는 조각': 어떻게 설치하고 회수하는가
9. 결말: 마지막 1분 구성, 행동 유도, 댓글 질문, 다음 영상 연결
10. 시청 지속을 위한 장치 목록(재방문 약속, 순위 예고, 중간 요약 등)
11. 우리 채널이 바로 가져다 쓸 기술 5개: '기술 이름 / 어떻게 쓰는가 / 영상 속 예문 / 우리 식 예문'
12. 우리 채널이 따라 하면 안 되는 것(과장·지어낸 사실·자극적 표현 등)과 이유"""
body = {'contents': [{'parts': [{'file_data': {'file_uri': f'https://www.youtube.com/watch?v={vid}'}}, {'text': ASK}]}],
        'generationConfig': {'temperature': 0.3}}
txt = ''; err = ''
for model in ('gemini-3-pro', 'gemini-2.5-pro', 'gemini-flash-latest'):
    try:
        req = urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent', json.dumps(body).encode(),
                                     {'Content-Type': 'application/json', 'x-goog-api-key': KEY})
        r = json.load(urllib.request.urlopen(req, timeout=900))
        txt = ''.join(p.get('text', '') for p in r['candidates'][0]['content']['parts']).strip()
        if txt: print('모델', model); break
    except Exception as e: err = str(e)[:200]; print('  실패', model, err)
if not txt: raise SystemExit('분석 실패: ' + err)
path = os.path.join(OUT, f'{vid}.md')
open(path, 'w', encoding='utf-8').write(f'# 레퍼런스 대본 분석: https://youtu.be/{vid}\n메모: {note}\n\n{txt}\n')
print(f'저장: {path} · {len(txt):,}자')
