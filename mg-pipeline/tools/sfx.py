"""효과음 자동 싱크: 화면 요소가 나타나는 순간에 짧은 효과음을 깐다 (2026-10-30 레퍼런스 JV7ONuxsbm4 기법).
   python tools/sfx.py <이름> [--gain -2]

plan/gen.py 가 만든 plan/sfx.json ([[초, 종류], ...]) 을 읽어 input/narration.wav 에 섞고 input/_mix/mix.wav 로 쓴다.
final 은 mix.wav 가 내레이션보다 새것이면 그것을 쓴다. 대본·장면을 고치면 gen.py → sfx.py 를 다시 돌린다.
효과음은 외부 음원 없이 여기서 합성한다(저작권 걱정 없음, 무료). 처음 한 번 brand/sfx/*.wav 로 저장해 두고 다시 쓴다.
종류: tick(글자 강조) pop(태그·카드·아이콘) swish(막대·화살표) whoosh(창 등장) hit(강조 글자) boom(큰 숫자, 아껴 쓴다) stamp(도장) ding(숫자·정답 공개) riser(공개 직전 긴장) blip(질문·체크 항목)
"""
import os, sys, wave, subprocess
import numpy as np
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = 24000
try:
    sys.path.insert(0, os.path.join(KIT, 'engine')); from mg import ffmpeg_exe; FF = ffmpeg_exe()
except Exception: FF = 'ffmpeg'
GAIN = {'tick': -26, 'pop': -21, 'swish': -24, 'whoosh': -22, 'hit': -18, 'boom': -16, 'stamp': -16, 'ding': -22, 'riser': -24, 'blip': -24, 'scribble': -22, 'paper': -24, 'tap': -24}   # dBFS (내레이션은 대략 -16 LUFS)

def _env(n, a=0.004, d=0.08):
    t = np.arange(n) / R; e = np.minimum(1, t / a) * np.exp(-t / d); return e
def _noise(n, seed): return np.random.default_rng(seed).standard_normal(n)
def _lp(x, k):
    """간단한 저역 통과 (이동 평균 k 칸)."""
    return np.convolve(x, np.ones(k) / k, mode='same')
def make(kind):
    if kind == 'tick':
        n = int(R * .05); t = np.arange(n) / R; x = np.sin(2 * np.pi * 2400 * t) * _env(n, .001, .012)
    elif kind == 'pop':
        n = int(R * .12); t = np.arange(n) / R; f = 900 * np.exp(-t * 22) + 260
        x = np.sin(2 * np.pi * np.cumsum(f) / R) * _env(n, .002, .045) + .25 * _noise(n, 1) * _env(n, .0005, .004)
    elif kind in ('swish', 'whoosh'):
        L = .22 if kind == 'swish' else .42; n = int(R * L); t = np.arange(n) / R
        x = _noise(n, 2 if kind == 'swish' else 3); out = np.zeros(n); step = int(R * .01)
        for i in range(0, n, step):                                       # 거르는 폭을 바꿔 가며 '휙' 하고 지나가는 느낌
            k = int(3 + 22 * (1 - np.sin(np.pi * i / n))); seg = x[max(0, i - 40):i + step + 40]
            out[i:i + step] = _lp(seg, k)[min(40, i):min(40, i) + step][:len(out[i:i + step])]
        x = out * np.sin(np.pi * t / L) ** 1.5
    elif kind == 'hit':
        n = int(R * .45); t = np.arange(n) / R; f = 140 * np.exp(-t * 9) + 55
        x = np.sin(2 * np.pi * np.cumsum(f) / R) * _env(n, .002, .16) + .35 * _lp(_noise(n, 4), 6) * _env(n, .001, .03)
    elif kind == 'boom':
        n = int(R * .8); t = np.arange(n) / R; f = 90 * np.exp(-t * 5) + 38
        x = np.sin(2 * np.pi * np.cumsum(f) / R) * _env(n, .003, .3) + .3 * _lp(_noise(n, 5), 12) * _env(n, .001, .06)
    elif kind == 'stamp':
        n = int(R * .3); t = np.arange(n) / R
        x = .9 * _lp(_noise(n, 6), 10) * _env(n, .0008, .035) + np.sin(2 * np.pi * 95 * t) * _env(n, .001, .07)
    elif kind == 'ding':                                                 # 숫자·정답이 열릴 때 '띵' (솔깃한 맑은 종소리, 2026-10-31 쿵 대신)
        n = int(R * .9); t = np.arange(n) / R
        x = (np.sin(2 * np.pi * 1318.5 * t) + .55 * np.sin(2 * np.pi * 1975.5 * t) + .25 * np.sin(2 * np.pi * 2637 * t)) * _env(n, .002, .28)
    elif kind == 'riser':                                                # 공개 직전 '스으윽' 올라가는 긴장 (0.7초)
        n = int(R * .7); t = np.arange(n) / R; f = 220 * (4 ** (t / .7))
        x = .6 * np.sin(2 * np.pi * np.cumsum(f) / R) * (t / .7) ** 2 + .5 * _lp(_noise(n, 7), 6) * (t / .7) ** 3
        x = x * np.minimum(1, (.7 - t) / .03)
    elif kind == 'blip':                                                 # 알림처럼 '뽁' 두 번 (질문·체크 항목)
        n = int(R * .22); t = np.arange(n) / R
        x = np.sin(2 * np.pi * 880 * t) * _env(n, .002, .03) + np.sin(2 * np.pi * 1320 * np.maximum(0, t - .09)) * (t > .09) * _env(n, .002, .05)[::1] * 0 + np.sin(2 * np.pi * 1320 * t) * ((t > .09) * np.exp(-np.maximum(0, t - .09) / .04))
    elif kind == 'scribble':                                             # 펜으로 사각사각 긋는 소리 (동그라미·밑줄, 2026-11-03 레이더: 머니프렌즈)
        n = int(R * .55); t = np.arange(n) / R
        x = _noise(n, 11) - _lp(_noise(n, 11), 6); x *= (0.55 + 0.45 * np.abs(np.sin(2 * np.pi * 9 * t))) * np.minimum(1, t / .02) * np.minimum(1, (.55 - t) / .08)
    elif kind == 'paper':                                                # 종이 바스락 (기사·서류 카드)
        n = int(R * .35); t = np.arange(n) / R
        x = _lp(_noise(n, 12), 3) * (np.random.default_rng(13).random(n) > .7) * np.exp(-t / .15)
    elif kind == 'tap':                                                  # 휴대폰 화면 '톡' (앱·채팅 장면)
        n = int(R * .08); t = np.arange(n) / R
        x = np.sin(2 * np.pi * 1600 * t) * _env(n, .001, .012) + _noise(n, 14) * _env(n, .0005, .004) * .4
    else: raise SystemExit(f'모르는 효과음 종류: {kind}')
    x = x / (np.abs(x).max() + 1e-9)
    return x * 10 ** (GAIN[kind] / 20)

def lib(kind):
    d = os.path.join(KIT, 'brand', 'sfx'); os.makedirs(d, exist_ok=True); p = os.path.join(d, kind + '.wav')
    if not os.path.exists(p):
        a = (make(kind) * 32767).astype(np.int16)
        with wave.open(p, 'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(R); w.writeframes(a.tobytes())
    with wave.open(p) as w: return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768

def main():
    a = sys.argv[1:]; name = [x for i, x in enumerate(a) if not x.startswith('--') and (i == 0 or a[i - 1] not in ('--gain', '--out'))][0]
    gain = float(a[a.index('--gain') + 1]) if '--gain' in a else 0.0
    proj = os.path.join(KIT, 'projects', name); import json
    marks = json.load(open(os.path.join(proj, 'plan', 'sfx.json'), encoding='utf-8'))
    nwav = os.path.join(proj, 'input', 'narration.wav')
    with wave.open(nwav) as w: sr, ch = w.getframerate(), w.getnchannels()
    # 어떤 형식이든(일레븐랩스 24kHz 모노 / VREW 48kHz 스테레오 + BGM) 그대로 읽어 섞는다 (2026-11-02)
    raw = subprocess.run([FF, '-v', 'error', '-i', nwav, '-f', 'f32le', '-ac', str(ch), '-ar', str(sr), '-'], capture_output=True, check=True).stdout
    nar = np.frombuffer(raw, np.float32).reshape(-1, ch).copy()
    out = nar; g = 10 ** (gain / 20); cnt = {}
    for t, k in marks:
        s = lib(k) * g
        if sr != R: s = np.interp(np.arange(int(len(s) * sr / R)) * R / sr, np.arange(len(s)), s)
        i = int(t * sr)
        if i >= len(out): continue
        j = min(len(out), i + len(s)); out[i:j] += s[:j - i, None]; cnt[k] = cnt.get(k, 0) + 1
    peak = np.abs(out).max()
    if peak > .99: out *= .99 / peak
    d = os.path.join(proj, 'input', '_mix'); os.makedirs(d, exist_ok=True)
    outp = a[a.index('--out') + 1] if '--out' in a else os.path.join(d, 'mix.wav')
    with wave.open(outp, 'wb') as w: w.setnchannels(ch); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out * 32767).astype(np.int16).tobytes())
    print(f'효과음 {sum(cnt.values())}개 섞음 ' + ', '.join(f'{k} {v}' for k, v in sorted(cnt.items())) + f' → input/_mix/mix.wav')

if __name__ == '__main__': main()
