"""ElevenLabs 음성 엔진: 대본 → input/narration.wav + input/narration.srt

project.json 의 tts 에 "engine": "elevenlabs" 로 켠다.
    "engine": "elevenlabs", "voice_id": "<보이스 ID>", "model": "eleven_v4", "language": "ko",
    "settings": {"stability": 0.7, "style": 0.0},          (선택) 목소리 설정
    "say_as": {"클로드": "클로오드"}                        (선택) 읽는 법 사전 — 음성에만 적용, 자막은 원문 그대로

- 문단을 통째로 읽힌다(문장마다 따로 합성하지 않는다). 일레븐랩스가 글자별 시각을 돌려주므로 자막 시각은 그 값을 그대로 쓴다.
- 외래어를 영어식으로 굴려 읽으면 say_as 에 한국식으로 풀어 쓴 표기를 넣는다. 채널 공통은 brand/channel.json 의 "say_as".
- 문단별 결과는 input/_tts/ 에 저장해, 대본을 고치면 바뀐 문단만 다시 합성한다.
"""
import os, sys, json, time, base64, hashlib, urllib.request, urllib.error
import numpy as np
import tts as T

API = 'https://api.elevenlabs.io/v1'
EL_DEFAULTS = {'model': 'eleven_v4', 'language': 'ko', 'settings': {'stability': 0.7, 'style': 0.0}, 'say_as': {}}
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def config(cfg):
    c = dict(EL_DEFAULTS); c.update({k: v for k, v in cfg.items() if v is not None})
    if not str(c.get('model', '')).startswith('eleven_'): c['model'] = EL_DEFAULTS['model']        # 다른 엔진의 모델 이름이 남아 있으면 무시
    say = {}
    try: say.update(json.load(open(os.path.join(KIT, 'brand', 'channel.json'), encoding='utf-8')).get('say_as', {}))
    except Exception: pass
    say.update(cfg.get('say_as') or {}); c['say_as'] = say
    if not c.get('voice_id'): raise SystemExit('project.json 의 tts.voice_id 가 없습니다 (일레븐랩스 보이스 ID).')
    return c

def spoken(text, say_as):
    """읽는 법 사전을 적용한 문장 (긴 낱말부터 바꾼다)."""
    for k in sorted(say_as, key=len, reverse=True): text = text.replace(k, say_as[k])
    return text

def _key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if not k: raise SystemExit('.env 에 ELEVENLABS_API_KEY 가 없습니다. (python mgp.py keys 로 열어 넣는다. sk_ 로 시작하는 값)')
    return k

def synth(text, c, prev='', nxt=''):
    """→ (int16 24kHz 음성, 글자별 시작 시각, 글자별 끝 시각)"""
    body = {'text': text, 'model_id': c['model'], 'voice_settings': c.get('settings') or {}}
    if c.get('language') and c['model'] != 'eleven_multilingual_v2': body['language_code'] = c['language']
    if prev: body['previous_text'] = prev[-300:]
    if nxt: body['next_text'] = nxt[:300]
    req = urllib.request.Request(f"{API}/text-to-speech/{c['voice_id']}/with-timestamps?output_format=pcm_24000", json.dumps(body).encode(),
                                 {'xi-api-key': _key(), 'Content-Type': 'application/json'})
    last = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as r: res = json.load(r)
            a = np.frombuffer(base64.b64decode(res['audio_base64']), np.int16)
            al = res.get('alignment') or {}
            st, en = al.get('character_start_times_seconds') or [], al.get('character_end_times_seconds') or []
            if len(st) != len(text):                              # 글자 수가 안 맞으면 길이 비례로 대신한다
                n = max(len(text), 1); d = len(a) / T.RATE; st = [d * i / n for i in range(n)]; en = [d * (i + 1) / n for i in range(n)]
            return a, st, en
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:400]}"
            if e.code in (400, 401, 403, 404, 422): break
        except Exception as e: last = repr(e)
        time.sleep(2 ** attempt)
    hint = ''
    if last and 'api_key' in last: hint = '\n  .env 의 ELEVENLABS_API_KEY 를 확인하세요 (sk_ 로 시작하는 실제 키. 키 ID 가 아니다).'
    if last and 'quota' in last: hint = '\n  이번 달 글자 한도를 다 썼습니다.'
    if last and 'voice' in last.lower(): hint = '\n  tts.voice_id 가 이 계정에서 쓸 수 있는 목소리인지 확인하세요.'
    raise SystemExit(f'일레븐랩스 TTS 실패: {last}{hint}')

def _mock(text, c, prev='', nxt=''):
    a = T.synth_mock(text, {}); n = max(len(text), 1); d = len(a) / T.RATE
    return a, [d * i / n for i in range(n)], [d * (i + 1) / n for i in range(n)]

def _para(sents, c, cache, prev, nxt, mock, force):
    """문단 하나: 자막 조각 → 읽을 글 → 음성 + 조각별 (시작, 끝). 반환 (음성, [(시작, 끝, 원문 조각)], 새로 합성했는지)"""
    pieces = [p for s in sents for p in T.split_sub(s, int(c.get('max_sub_chars', 30)))]
    sp = [spoken(p, c['say_as']) for p in pieces]; text = ' '.join(sp)
    h = hashlib.sha1(json.dumps([c['model'], c['voice_id'], c.get('settings'), c.get('language'), text, mock], ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
    pw, pj = os.path.join(cache, 'el_' + h + '.wav'), os.path.join(cache, 'el_' + h + '.json')
    if os.path.exists(pw) and os.path.exists(pj) and not force:
        a = T._load_wav(pw); m = json.load(open(pj, encoding='utf-8')); st, en, fresh = m['st'], m['en'], False
    else:
        a, st, en = (_mock if mock else synth)(text, c, prev, nxt)
        T._save_wav(pw, a); json.dump({'st': st, 'en': en, 'text': text}, open(pj, 'w', encoding='utf-8')); fresh = True
    cues, pos = [], 0; T_ = lambda i: st[min(i, len(st) - 1)]; E_ = lambda i: en[min(i, len(en) - 1)]
    for orig, s in zip(pieces, sp):
        i0, i1 = pos, pos + len(s) - 1
        ow, sw = orig.split(' '), s.split(' '); words = []                # 낱말별 시각 (화면의 움직임을 낱말에 맞출 때 쓴다)
        if len(ow) == len(sw):
            q = i0
            for w_, x in zip(ow, sw): words.append((w_, T_(q), E_(q + len(x) - 1))); q += len(x) + 1
        else:
            d = (E_(i1) - T_(i0)) / max(len(ow), 1); words = [(w_, T_(i0) + d * k, T_(i0) + d * (k + 1)) for k, w_ in enumerate(ow)]
        pos += len(s) + 1
        cues.append((T_(i0), E_(i1), orig, words))
    return a, cues, fresh, text

def tidy(a, pc, max_gap=0.55, keep_gap=0.4, db=-45.0):
    """문단 음성 다듬기 (2026-10-29 담당자 지적: 긴 쉼, 더듬는 첫마디).
    ① 마지막 글자 뒤의 소리는 잘라 낸다: 일레븐랩스가 다음 문단의 첫소리를 미리 읽어 붙이는 일이 있다(더듬는 것처럼 들림).
    ② 첫 글자 앞 무음을 잘라 낸다. ③ 문단 안에서 max_gap 초보다 긴 쉼은 keep_gap 초로 줄인다.
    자막·낱말 시각도 같이 옮긴다. 반환 (음성, 자막 조각)"""
    if not pc or len(a) == 0: return a, pc
    R = T.RATE; hop = int(R * 0.01); n = len(a) // hop
    if n < 3: return a, pc
    e = np.sqrt(((a[:n * hop].astype(np.float32) / 32768).reshape(n, hop) ** 2).mean(1))
    quiet = 20 * np.log10(e + 1e-9) < db
    runs = []; i = 0                                                 # 소리/무음 구간 [(무음?, 시작칸, 끝칸)]
    while i < n:
        j = i
        while j < n and quiet[j] == quiet[i]: j += 1
        runs.append((bool(quiet[i]), i, j)); i = j
    voiced = [(i, j) for q, i, j in runs if not q]
    if not voiced: return a, pc
    # 끝: 마지막 소리가 0.35초보다 짧고 앞과 0.2초 넘게 떨어져 있으면 다음 문단 첫소리를 미리 읽은 조각 → 버린다
    while len(voiced) > 1 and voiced[-1][1] - voiced[-1][0] < 35 and voiced[-1][0] - voiced[-2][1] > 20: voiced.pop()
    # 처음: 첫 소리가 0.15초보다 짧고 뒤와 0.2초 넘게 떨어져 있으면 버린다
    while len(voiced) > 1 and voiced[0][1] - voiced[0][0] < 15 and voiced[1][0] - voiced[0][1] > 20: voiced.pop(0)
    s0 = max(0.0, voiced[0][0] / 100 - 0.05); e1 = min(len(a) / R, voiced[-1][1] / 100 + 0.12)
    cuts = []; i = int(s0 * 100)                                     # (시작 초, 줄인 길이)
    while i < int(e1 * 100):
        if quiet[i]:
            j = i
            while j < int(e1 * 100) and quiet[j]: j += 1
            d = (j - i) / 100
            if d > max_gap and i > int(s0 * 100) + 5 and j < int(e1 * 100) - 5: cuts.append((i / 100 + keep_gap / 2, d - keep_gap))
            i = j
        else: i += 1
    segs = []; t = s0
    for c0, L in cuts: segs.append(a[int(t * R):int(c0 * R)]); t = c0 + L
    segs.append(a[int(t * R):int(e1 * R)]); out = np.concatenate(segs) if segs else a
    def m(x):
        x = min(max(x, s0), e1); y = x - s0
        for c0, L in cuts:
            if x >= c0 + L: y -= L
            elif x > c0: y -= x - c0
        return y
    pc2 = [(m(s), m(e), txt, [(w, m(b), m(c)) for w, b, c in ws]) for s, e, txt, ws in pc]
    return out, pc2

def run(proj, cfg, mock=False, force=False):
    c = config(cfg)
    script = os.path.join(proj, 'input', 'script.txt')
    if not os.path.exists(script): raise SystemExit(f'대본이 없습니다: {script}')
    paras = T.read_script(script)
    if not paras: raise SystemExit('대본에 읽을 문장이 없습니다.')
    cache = os.path.join(proj, 'input', '_tts'); os.makedirs(cache, exist_ok=True)
    texts = [spoken(' '.join(s), c['say_as']) for s in paras]
    used = sorted(k for k in c['say_as'] if any(k in ' '.join(s) for s in paras))
    big = [len(x) for x in texts if len(x) > 1500]
    if big and not mock: raise SystemExit(f"문단이 너무 깁니다 ({max(big)}자). 대본에 빈 줄로 문단을 나눠 주세요 (문단당 1,500자 이하). 2026-10-31: 빈 줄 없는 대본이 한 문단으로 합성돼 4천 자를 날림.")
    print(f"합성 {len(paras)}문단 ({sum(len(x) for x in texts)}자) · 일레븐랩스 {c['model']} · 목소리 {c['voice_id']}" + (' · [모의 실행: 실제 음성 아님]' if mock else ''), flush=True)
    if used: print('  읽는 법 사전 적용: ' + ', '.join(f"{k}→{c['say_as'][k]}" for k in used))
    marks = T.clip_marks(proj, script); cinfo = []
    out = [np.zeros(int(T.RATE * cfg.get('lead_in', 0.3)), np.int16)]; pos = len(out[0]); cues = []; new = 0; words = []
    for i, sents in enumerate(paras):
        a, pc, fresh, _ = _para(sents, c, cache, texts[i - 1] if i else '', texts[i + 1] if i + 1 < len(paras) else '', mock, force)
        if not mock and cfg.get('tidy', True): a, pc = tidy(a, pc, cfg.get('max_gap', 0.55), cfg.get('keep_gap', 0.4))
        new += fresh
        if i:
            g = np.zeros(int(T.RATE * cfg.get('para_gap', 0.65)), np.int16); out.append(g); pos += len(g)
        z, ci = T.clip_gap(marks, i, pos); out.append(z); pos += len(z); cinfo += ci      # 대본의 [영상: 이름] 구간: 내레이션을 비운다
        t0 = pos / T.RATE
        for k, (s, e, txt, ws) in enumerate(pc):
            e2 = pc[k + 1][0] if k + 1 < len(pc) else e                 # 같은 문단 안에서는 다음 자막이 시작될 때까지 이어 보여 준다
            cues.append((t0 + s, t0 + max(e, min(e2, e + 0.6)), txt))
            words.append([{'w': w_, 't0': round(t0 + a_, 3), 't1': round(t0 + b_, 3)} for w_, a_, b_ in ws])
        out.append(a); pos += len(a)
    z, ci = T.clip_gap(marks, len(paras), pos); out.append(z); pos += len(z); cinfo += ci
    out.append(np.zeros(int(T.RATE * cfg.get('tail', 0.6)), np.int16))
    audio = np.concatenate(out)
    T._save_wav(os.path.join(proj, 'input', 'narration.wav'), audio)
    with open(os.path.join(proj, 'input', 'narration.srt'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(f'{i + 1}\n{T._ts(a)} --> {T._ts(b)}\n{t}' for i, (a, b, t) in enumerate(cues)) + '\n')
    d = len(audio) / T.RATE
    print(f'  새로 합성 {new}문단, 저장분 재사용 {len(paras) - new}문단')
    T.save_clips(proj, cinfo)
    json.dump(words, open(os.path.join(proj, 'input', 'words.json'), 'w', encoding='utf-8'), ensure_ascii=False)      # 자막 번호 순서대로, 낱말별 시각
    print(f'완료: input/narration.wav ({int(d // 60)}분 {d % 60:.1f}초), input/narration.srt (자막 {len(cues)}개)')
    return d, len(cues)

def say_clip(proj, text, out_wav, cfg, mock=False):
    """짧은 멘트(마무리 구독 멘트 등) → 음성 + <out>.json({'duration', 'cues'})."""
    c = config(cfg); meta_p = out_wav[:-4] + '.json'
    sents = [s for p in T.read_script_text(text) for s in p] if hasattr(T, 'read_script_text') else [x.strip() for x in __import__('re').split(r'(?<=[.!?…])\s+', ' '.join(text.split())) if x.strip()]
    sp = [spoken(s, c['say_as']) for s in sents]; full = ' '.join(sp)
    h = hashlib.sha1(json.dumps(['el', c['model'], c['voice_id'], c.get('settings'), full, mock], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    if os.path.exists(out_wav) and os.path.exists(meta_p):
        m = json.load(open(meta_p, encoding='utf-8'))
        if m.get('hash') == h: return m
    print(f"멘트 음성 합성 {len(sents)}문장 ({len(full)}자) · 일레븐랩스 {c['model']}", flush=True)
    a, st, en = (_mock if mock else synth)(full, c)
    cues, pos = [], 0
    for orig, s in zip(sents, sp):
        cues.append([round(st[min(pos, len(st) - 1)], 3), round(en[min(pos + len(s) - 1, len(en) - 1)], 3), orig]); pos += len(s) + 1
    T._save_wav(out_wav, a)
    m = {'hash': h, 'duration': round(len(a) / T.RATE, 3), 'cues': cues, 'voice': c['voice_id']}
    json.dump(m, open(meta_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return m

def voices(search=None):
    req = urllib.request.Request(API + '/voices', headers={'xi-api-key': _key()})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: vs = json.load(r).get('voices', [])
    except urllib.error.HTTPError as e: raise SystemExit(f"목소리 목록 조회 실패: HTTP {e.code} {e.read().decode('utf-8', 'replace')[:300]}")
    for v in vs:
        lab = v.get('labels') or {}
        if search and search.lower() not in (v.get('name', '') + json.dumps(lab, ensure_ascii=False)).lower(): continue
        print(f"{v.get('voice_id'):24s} | {v.get('name', ''):20s} | {v.get('category', ''):12s} | {lab.get('language', ''):4s} {lab.get('accent', '')}")
    print('\nproject.json 의 tts.voice_id 에 맨 앞 열을 적는다.')
