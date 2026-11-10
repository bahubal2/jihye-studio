"""Gemini 이미지 편집: 원본 이미지 + 지시문 → 새 이미지.  python3 tools/gemini_edit.py <원본> <저장> "<지시문>" """
import os, sys, json, base64, io, urllib.request
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); import mgp; mgp.load_env(); KEY = os.environ['GEMINI_API_KEY']
src, dst, prompt = sys.argv[1], sys.argv[2], sys.argv[3]
b = base64.b64encode(open(src, 'rb').read()).decode()
for model in ('gemini-3.1-flash-image', 'gemini-3-pro-image', 'gemini-2.5-flash-image'):
    body = {'contents': [{'parts': [{'inlineData': {'mimeType': 'image/jpeg', 'data': b}}, {'text': prompt}]}],
            'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '16:9'}}}
    try:
        r = json.load(urllib.request.urlopen(urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent', json.dumps(body).encode(), {'Content-Type': 'application/json', 'x-goog-api-key': KEY}), timeout=300))
        for p in r['candidates'][0]['content']['parts']:
            if 'inlineData' in p:
                im = Image.open(io.BytesIO(base64.b64decode(p['inlineData']['data']))).convert('RGB').resize((1280, 720), Image.LANCZOS); im.save(dst, quality=95); print('생성', model, dst); sys.exit()
    except Exception as e: print('실패', model, str(e)[:150])
