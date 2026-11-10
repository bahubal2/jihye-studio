"""Gemini 이미지 생성 → assets/<id>.png (fal 잔액 없을 때 대체).
   python gemini_img.py <프로젝트 폴더> <spec.json>
   spec: [{"id":..., "prompt":..., "aspect":"16:9", "cutout": false}]  cutout=true 면 초록 배경(#00FF00)으로 그려서 투명하게 뺀다."""
import os, sys, json, base64, io, urllib.request
import numpy as np
from PIL import Image
P = os.path.abspath(sys.argv[1]); KIT = os.path.dirname(os.path.dirname(P)); sys.path.insert(0, KIT)
import mgp; mgp.load_env(); KEY = os.environ['GEMINI_API_KEY']
SPEC = json.load(open(sys.argv[2], encoding='utf-8')); OUT = os.path.join(P, 'assets'); os.makedirs(OUT, exist_ok=True)
MODELS = ('gemini-3.1-flash-image', 'gemini-3-pro-image', 'gemini-2.5-flash-image')
for a in SPEC:
    dst = os.path.join(OUT, a['id'] + '.png')
    if os.path.exists(dst): print('있음', a['id']); continue
    prompt = a['prompt'] + (' Isolated on a perfectly flat solid pure green (#00FF00) background, no shadow on the background, no ground.' if a.get('cutout') else '') + ' No text, no letters, no watermark.'
    img = None
    for model in MODELS:
        body = {'contents': [{'parts': [{'text': prompt}]}], 'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': a.get('aspect', '16:9')}}}
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent', json.dumps(body).encode(), {'Content-Type': 'application/json', 'x-goog-api-key': KEY}), timeout=300))
            for p in r['candidates'][0]['content']['parts']:
                if 'inlineData' in p: img = Image.open(io.BytesIO(base64.b64decode(p['inlineData']['data']))).convert('RGBA'); break
            if img: print('생성', a['id'], model, img.size); break
        except Exception as e: print('  실패', a['id'], model, str(e)[:150])
    if img is None: continue
    if a.get('cutout'):
        x = np.array(img).astype(np.int16); r, g, b = x[..., 0], x[..., 1], x[..., 2]
        green = (g > 150) & (g > r + 60) & (g > b + 60)
        x[..., 3] = np.where(green, 0, 255)
        sp = (x[..., 1] > x[..., 0] + 25) & (x[..., 1] > x[..., 2] + 25) & ~green   # 가장자리 초록 번짐 줄이기
        x[..., 1] = np.where(sp, np.maximum(x[..., 0], x[..., 2]), x[..., 1])
        img = Image.fromarray(x.clip(0, 255).astype(np.uint8), 'RGBA'); bb = img.getbbox(); img = img.crop(bb) if bb else img
    elif img.size[0] < 1920: img = img.resize((1920, round(1920 * img.size[1] / img.size[0])), Image.LANCZOS)
    img.save(dst)
