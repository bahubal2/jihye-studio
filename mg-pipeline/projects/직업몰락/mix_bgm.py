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
BACK = T(162)                                                     # 마무리부터 = 뒷부분

# 1) 뒷부분 무료 효과음 줄이기
sp = os.path.join(HERE, 'plan', 'sfx.json'); sfx = json.load(open(sp))
keep = [x for x in sfx if x[0] < BACK or x[1] in ('ding', 'swish', 'whoosh', 'stamp')]
json.dump(keep, open(sp, 'w')); print(f'무료 효과음 {len(sfx)} → {len(keep)}개 (뒷부분 {BACK:.0f}초 이후 정리)')
subprocess.run([os.path.join(KIT, '.venv', 'bin', 'python'), os.path.join(KIT, 'tools', 'sfx.py'), os.path.basename(HERE), '--gain', '2'], cwd=KIT, check=True)

# 2) 배경음악 구간 (시작, 끝, 파일, 볼륨 dB, 페이드인, 페이드아웃) — 내레이션 -14 LUFS 기준, 음악 원본 -16 dB 안팎
BGM = [
    (0.0, T(24) - 1, 'music_intro.mp3', -27, 0.0, 4.0),            # 인트로 (-27dB 기본)
    (T(24) - 1, T(58), 'music_doc_tension.mp3', -23, 2.5, 3.0),   # 7위 요금소 · 6위 은행
    (T(58), T(89), 'music_nostalgia.mp3', -23, 3.0, 3.0),         # 5위 콜센터 · 4위 마트
    (T(89), T(132), 'music_doc_tension.mp3', -23, 3.0, 3.0),      # 3위 교사 · 2위 신입
    (T(132), BACK, 'music_doc_tension.mp3', -24, 3.0, 3.0),       # 1위 경비원 · 정리
    (BACK, DUR, 'music_nostalgia.mp3', -25, 3.0, 4.0),            # 남는 자리 · 마무리
]

HITS = []
def reveal(t, rise=True, gain=-5):
    if rise: HITS.append((max(0, t - 2.9), 'sfx_riser.mp3', -9))
    HITS.append((t, 'sfx_impact.mp3', gain))
reveal(T(66))                        # 콜센터 반전
reveal(T(136))                       # 1위 아파트 경비원
reveal(T(189), rise=False)           # 그가 딴 자격증은 전기기사

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
