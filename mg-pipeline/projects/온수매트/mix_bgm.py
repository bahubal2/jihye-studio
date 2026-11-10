"""온수매트 TOP5 소리 믹스 (2026-11-10). 환경음(낙엽·바람·장작·기차) 중심, 쿵 소리는 반전 3곳만. 새 일레븐랩스 비용 0: 다낭 때 만든 소리 재사용. 담당자: 인트로는 담당자 배경음악, 돈·공은 앞쪽, 뒤쪽은 재사용·최소.
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
BACK = T(12)                                                      # 인트로 끝 = 본문 시작

# 1) 효과음 정리 (2026-11-09 담당자): 쿵·탁(hit/boom) 영상 전체 5회 이하, 같은 소리 연속 금지
sp = os.path.join(HERE, 'plan', 'sfx.json'); sfx = sorted(json.load(open(sp)))
keep = []; hits = 0; last = None
for x in sfx:
    if x[1] in ('hit', 'boom'):
        if hits >= 5: continue
        hits += 1
    if last and last[1] == x[1] and x[0] - last[0] < 2.5: continue
    keep.append(x); last = x
json.dump(keep, open(sp, 'w')); print(f'무료 효과음 {len(sfx)} → {len(keep)}개 (쿵 {hits}회)')
subprocess.run([os.path.join(KIT, '.venv', 'bin', 'python'), os.path.join(KIT, 'tools', 'sfx.py'), os.path.basename(HERE), '--gain', '2'], cwd=KIT, check=True)

# 2) 배경음악 구간 (시작, 끝, 파일, 볼륨 dB, 페이드인, 페이드아웃) — 내레이션 -14 LUFS 기준, 음악 원본 -16 dB 안팎
BGM = [
    (0.0, T(12) + 0.5, 'music_intro_tense.mp3', -30, 0.0, 2.0),     # 인트로만: 긴박 (-30dB)
]
HITS = []
def reveal(t, gain=-6):
    HITS.append((max(0, t - 2.9), 'sfx_riser.mp3', -10)); HITS.append((t, 'sfx_impact.mp3', gain))
HITS += [(T(1) + 0.1, 'sfx_wind.mp3', -18), (T(250) + 0.2, 'sfx_wind.mp3', -20)]   # 눈보라 바람 (처음·끝 캠핑장)
STINGS = [(T(11) - 0.1, 'music_sting_reveal.mp3', -25),   # 인트로 끝 → 1막
          (T(46), 'music_sting_clue.mp3', -27),            # 2막: 어떻게 건너갔나
          (T(76), 'music_sting_clue.mp3', -27),            # 3막: 왜 통했나
          (T(101), 'music_sting_reveal.mp3', -26),         # 4막: 남은 이유 셋
          (T(140), 'music_sting_clue.mp3', -27),           # 둘째 가격표
          (T(181), 'music_sting_hope.mp3', -27),           # 두 단서 회수
          (T(200), 'music_sting_clue.mp3', -27),           # 5막: 같은 기술 다른 길
          (T(229), 'music_sting_reveal.mp3', -26),         # 결말: 다시 처음 질문
          (T(250), 'music_sting_hope.mp3', -27)]           # 다시 그 캠핑장
reveal(T(163))                                             # 답은 그 지하실에
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
