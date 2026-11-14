"""중산층몰락 소리 믹스 (2026-11-14). 담당자 녹음(vrew.mp3)에 채널 인트로 배경음악이 이미 섞여 있다(0~52초, 목소리보다 15~18dB 아래 = 적당).
   → 인트로 배경음악을 따로 깔지 않는다(BGM 비움). 본문 시작에 차분한 짧은 음, 반전에만 쿵(전체 5회 이하).
   python3 projects/중산층몰락/mix_bgm.py
"""
import os, re, json, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.dirname(os.path.dirname(HERE))
SND = os.path.join(HERE, 'sound'); MIX = os.path.join(HERE, 'input', '_mix', 'mix.wav')

def cue_times():
    out = {}
    for b in re.split(r'\n\s*\n', open(os.path.join(HERE, 'input', 'narration_한글숫자.srt'), encoding='utf-8-sig').read().strip()):
        l = b.strip().split('\n'); h, m, s = l[1].split(' --> ')[0].split(':'); out[int(l[0])] = (int(h) * 3600 + int(m) * 60 + float(s.replace(',', '.')), ' '.join(l[2:]))
    return out
C = cue_times(); T = lambda n: C[n][0]
DUR = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', os.path.join(HERE, 'input', 'narration.wav')], capture_output=True, text=True).stdout)
BACK = T(14)                                                      # 인트로 끝 = 본문 시작

# 1) 효과음 정리 (2026-11-09 담당자): 쿵·탁(hit/boom) 영상 전체 5회 이하, 같은 소리 연속 금지
sp = os.path.join(HERE, 'plan', 'sfx.json'); sfx = sorted(json.load(open(sp)))
keep = []; hits = 0; last = None
for x in sfx:
    if x[1] in ('hit', 'boom'):
        if hits >= 3: continue                                      # 휴양지몰락: 반전 2곳(impact)과 합쳐 쿵 5회 이하
        hits += 1
    if last and last[1] == x[1] and x[0] - last[0] < 2.5: continue
    keep.append(x); last = x
json.dump(keep, open(sp, 'w')); print(f'무료 효과음 {len(sfx)} → {len(keep)}개 (쿵 {hits}회)')
subprocess.run([os.path.join(KIT, '.venv', 'bin', 'python'), os.path.join(KIT, 'tools', 'sfx.py'), os.path.basename(HERE), '--gain', '2'], cwd=KIT, check=True)

# 2) 배경음악 구간 (시작, 끝, 파일, 볼륨 dB, 페이드인, 페이드아웃) — 인트로만 -30dB
BGM = []                                                          # 인트로 음악은 녹음에 이미 들어 있음
HITS = []
def reveal(t, gain=-6):
    HITS.append((max(0, t - 2.9), 'sfx_riser.mp3', -10)); HITS.append((t, 'sfx_impact.mp3', gain))
STINGS = [(T(14) - 0.2, 'music_sting_hope.mp3', -28),            # 담당자 음악이 끝난 뒤 본문 첫 장면(골목 이야기)
          (T(83) - 0.1, 'music_sting_clue.mp3', -27),               # 흔한 설명 3가지 시작
          (T(142) - 0.1, 'music_sting_reveal.mp3', -26),            # 진짜 원인 3가지
          (T(179) - 0.1, 'music_sting_clue.mp3', -27),              # 마지막이자 가장 큰 원인(상가)
          (T(213) - 0.1, 'music_sting_hope.mp3', -28),              # 끄떡없는 분들
          (T(246) - 0.1, 'music_sting_clue.mp3', -28)]              # 다시 황학동 (정리)
reveal(T(152))                                                      # 여덟 달이 안 됩니다
reveal(T(166))                                                      # 사 년 만에 십사 배
for t, f, db in STINGS: HITS.append((t, f, db))
inputs = ['-i', MIX]; fl = []; k = 1
for a, b, f, db, fi, fo in BGM:
    L = max(0.5, b - a); inputs += ['-stream_loop', '-1', '-i', os.path.join(SND, f)]
    fl.append(f'[{k}:a]atrim=0:{L:.2f},asetpts=PTS-STARTPTS,volume={db}dB,afade=t=in:st=0:d={fi},afade=t=out:st={max(0, L - fo):.2f}:d={fo},adelay={int(a * 1000)}|{int(a * 1000)}[m{k}]'); k += 1
for t, f, db in HITS:
    inputs += ['-i', os.path.join(SND, f)]
    fl.append(f'[{k}:a]volume={db}dB,adelay={int(t * 1000)}|{int(t * 1000)}[m{k}]'); k += 1
labels = ''.join(f'[m{i}]' for i in range(1, k))
fl.append(f'[0:a]{labels}amix=inputs={k}:duration=first:normalize=0,alimiter=limit=0.97[out]')
tmp = MIX + '.tmp.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fl), '-map', '[out]', '-ar', '48000', '-ac', '2', tmp], check=True)
os.replace(tmp, MIX)
print(f'배경음악 {len(BGM)}구간 · 일레븐랩스 효과음 {len(HITS)}개 → {MIX}')
