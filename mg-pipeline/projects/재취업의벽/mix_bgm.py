"""재취업의벽 소리 믹스 (2026-11-12). 환경음(낙엽·바람·장작·기차) 중심, 쿵 소리는 반전 3곳만. 새 일레븐랩스 비용 0: 다낭 때 만든 소리 재사용. 담당자: 인트로는 담당자 배경음악, 돈·공은 앞쪽, 뒤쪽은 재사용·최소.
   1) plan/sfx.json 에서 12분(뒷부분) 이후 쿵·뾱 계열을 빼고 tools/sfx.py 로 무료 효과음 믹스(input/_mix/mix.wav)
   2) 그 위에 배경음악 구간 + 일레븐랩스 고조음·타격음·비행기음을 얹어 input/_mix/mix.wav 를 덮어쓴다 (final 이 이 파일을 쓴다)
   python3 projects/숨은명소/mix_bgm.py
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
BACK = T(13)                                                      # 인트로 끝 = 본문 시작

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
BGM = [
    (0.0, T(13) + 0.5, 'music_intro_tense.mp3', -30, 0.0, 2.0),
]
HITS = []
def reveal(t, gain=-6):
    HITS.append((max(0, t - 2.9), 'sfx_riser.mp3', -10)); HITS.append((t, 'sfx_impact.mp3', gain))
STINGS = [(T(13) - 0.1, 'music_sting_reveal.mp3', -25),         # 인트로 끝 → 5위
          (T(45), 'music_sting_clue.mp3', -27),                     # 4위 나이
          (T(83), 'music_sting_clue.mp3', -27),                     # 3위 근로계약서
          (T(117), 'music_sting_hope.mp3', -28),                    # 2위 학교 (아침 교문)
          (T(165), 'music_sting_reveal.mp3', -26),                  # 1위 퀴즈
          (T(219), 'music_sting_clue.mp3', -27),                    # 다섯 벽 정리
          (T(264), 'music_sting_hope.mp3', -28)]                    # 서정배 씨: 결국 왔다
reveal(T(167))                                                      # 퀴즈 답: 20대
reveal(T(230))                                                      # 반전: 눈높이가 아니라 이름표로 거르는 사다리
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
