"""다낭 편 소리 최종 믹스 (2026-11-04). 담당자: 인트로는 담당자 배경음악, 돈·공은 앞쪽, 뒤쪽은 재사용·최소.
   1) plan/sfx.json 에서 12분(뒷부분) 이후 쿵·뾱 계열을 빼고 tools/sfx.py 로 무료 효과음 믹스(input/_mix/mix.wav)
   2) 그 위에 배경음악 구간 + 일레븐랩스 고조음·타격음·비행기음을 얹어 input/_mix/mix.wav 를 덮어쓴다 (final 이 이 파일을 쓴다)
   python3 projects/다낭/mix_bgm.py
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
BACK = T(159)                                                     # 4막 셋째 원인부터 = 뒷부분

# 1) 뒷부분 무료 효과음 줄이기
sp = os.path.join(HERE, 'plan', 'sfx.json'); sfx = json.load(open(sp))
keep = [x for x in sfx if x[0] < BACK or x[1] in ('ding', 'swish', 'whoosh', 'stamp')]
json.dump(keep, open(sp, 'w')); print(f'무료 효과음 {len(sfx)} → {len(keep)}개 (뒷부분 {BACK:.0f}초 이후 정리)')
subprocess.run([os.path.join(KIT, '.venv', 'bin', 'python'), os.path.join(KIT, 'tools', 'sfx.py'), '다낭', '--gain', '2'], cwd=KIT, check=True)

# 2) 배경음악 구간 (시작, 끝, 파일, 볼륨 dB, 페이드인, 페이드아웃) — 내레이션 -14 LUFS 기준, 음악 원본 -16 dB 안팎
BGM = [
    (0.0, 48.0, 'music_intro.mp3', -20, 0.0, 4.0),                # 담당자 인트로 음악 (47초부터 허밍이 들어와 그 전에 줄인다)
    (T(19) - 1, T(76), 'music_nostalgia.mp3', -22, 2.5, 3.0),     # 1막·2막 회상
    (T(76), BACK, 'music_doc_tension.mp3', -22, 3.0, 3.0),        # 3막·4막 앞부분 수사
    (BACK, T(242), 'music_doc_tension.mp3', -26, 3.0, 3.0),       # 뒷부분: 같은 곡을 더 작게
    (T(242), DUR, 'music_nostalgia.mp3', -25, 3.0, 4.0),          # 결말
]
# 3) 일레븐랩스 효과음 (시각, 파일, dB) — 반전 자리에만
HITS = []
def reveal(t, rise=True, gain=-4):
    if rise: HITS.append((max(0, t - 2.9), 'sfx_riser.mp3', -8))
    HITS.append((t, 'sfx_impact.mp3', gain))
reveal(T(7))                       # 그런데 숫자는 정반대를
reveal(T(94), rise=False)          # 정말 그랬을까요? 아닙니다
reveal(T(123))                     # 줄어든 건 한국인의 비중뿐
reveal(T(167), rise=False, gain=-7)  # 비중은 반 아래로 (뒷부분 시작 직후, 재사용 소리라 추가 비용 없음)
HITS += [(T(25) + 0.3, 'sfx_airplane.mp3', -12), (T(180) + 0.3, 'sfx_airplane.mp3', -14)]

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
