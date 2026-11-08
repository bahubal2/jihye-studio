"""숨은명소 TOP5 소리 최종 믹스 (2026-11-08). 환경음(낙엽·바람·장작·기차) 중심, 쿵 소리는 반전 3곳만. 새 일레븐랩스 비용 0: 다낭 때 만든 소리 재사용. 담당자: 인트로는 담당자 배경음악, 돈·공은 앞쪽, 뒤쪽은 재사용·최소.
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
BACK = T(232)                                                     # 마무리부터 = 뒷부분

# 1) 뒷부분 무료 효과음 줄이기
sp = os.path.join(HERE, 'plan', 'sfx.json'); sfx = json.load(open(sp))
keep = [x for x in sfx if x[0] < BACK or x[1] in ('ding', 'swish', 'whoosh', 'stamp')]
json.dump(keep, open(sp, 'w')); print(f'무료 효과음 {len(sfx)} → {len(keep)}개 (뒷부분 {BACK:.0f}초 이후 정리)')
subprocess.run([os.path.join(KIT, '.venv', 'bin', 'python'), os.path.join(KIT, 'tools', 'sfx.py'), '숨은명소', '--gain', '2'], cwd=KIT, check=True)

# 2) 배경음악 구간 (시작, 끝, 파일, 볼륨 dB, 페이드인, 페이드아웃) — 내레이션 -14 LUFS 기준, 음악 원본 -16 dB 안팎
BGM = [
    (0.0, 48.0, 'music_intro.mp3', -27, 0.0, 4.0),                # 담당자 인트로 음악 (-27dB 기본, 2026-11-07)
    (T(14) - 1, T(47), 'music_nostalgia.mp3', -23, 2.5, 3.0),     # 5위 자작나무숲
    (T(47), T(92), 'music_doc_tension.mp3', -23, 3.0, 3.0),       # 4위 화순 적벽 (댐)
    (T(92), T(137), 'music_nostalgia.mp3', -23, 3.0, 3.0),        # 3위 저도
    (T(137), T(183), 'music_doc_tension.mp3', -23, 3.0, 3.0),     # 2위 금성산 (지뢰)
    (T(183), BACK, 'music_doc_tension.mp3', -24, 3.0, 3.0),       # 1위 북악산
    (BACK, DUR, 'music_nostalgia.mp3', -25, 3.0, 4.0),            # 마무리
]
HITS = []
def reveal(t, rise=True, gain=-5):
    if rise: HITS.append((max(0, t - 2.9), 'sfx_riser.mp3', -9))
    HITS.append((t, 'sfx_impact.mp3', gain))
reveal(T(43))                        # 지금부터는 다릅니다 (3:15)
reveal(T(134), rise=False)           # 문을 연 건 세월이 아니라 종이 한 장
reveal(T(213))                       # 59년 만이었습니다 (마지막 철문)
reveal(T(247), rise=False)           # 실제로 문을 연 건 협약서 한 장
HITS += [(T(1) + 0.2, 'sfx_leaves.mp3', -16), (T(33) + 0.2, 'sfx_leaves.mp3', -17), (T(137) + 0.2, 'sfx_wind.mp3', -18), (T(183) + 0.2, 'sfx_wind.mp3', -18)]

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
