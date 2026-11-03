"""작업이 끝날 때마다 GitHub 보관 (2026-11-03 담당자: GitHub 저장소 bahubal2/jihye-studio, 브랜치 mg-pipeline).
   python3 tools/git_backup.py "무엇을 했는지 한 줄"

작업 폴더(/home/user/mg-pipeline)를 저장소 안 mg-pipeline/ 폴더로 복사하고 커밋·푸시한다.
API 키(.env), 가상환경, 그림·영상·음성 같은 큰 파일은 복사하지 않는다 (저장소의 mg-pipeline/.gitignore 와 같은 기준).
"""
import os, sys, subprocess, tarfile, io, fnmatch

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.environ.get('MG_BACKUP_REPO', '/home/user/jihye-studio')
DST = os.path.join(REPO, 'mg-pipeline')
EXCL = ['./.env', './.venv', '*/__pycache__', './API키*.txt', '*키*.txt', '*.wav', '*.mp3', '*.mp4', '*.mov', '*.m4a',
        './projects/*/assets', './projects/*/captures', './projects/*/input/_tts', './projects/*/input/_listen', './projects/*/input/_mix',
        './projects/*/input/_src', './projects/*/out/scenes', './projects/*/out/_*', './projects/*/out/*.jpg', './projects/_backup',
        './brand/_voice_samples', './out']

def run(*a, **k):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True, **k)
    if r.returncode: raise SystemExit(f"실패: {' '.join(a)}\n{r.stdout}{r.stderr}")
    return r.stdout

def main():
    msg = ' '.join(sys.argv[1:]) or '작업 저장'
    if not os.path.isdir(os.path.join(REPO, '.git')): raise SystemExit(f'저장소가 없습니다: {REPO} (새 작업 공간이면 먼저 clone)')
    cmd = ['tar', '-cf', '-'] + [f'--exclude={e}' for e in EXCL] + ['.']
    data = subprocess.run(cmd, cwd=SRC, capture_output=True, check=True).stdout
    os.makedirs(DST, exist_ok=True)
    subprocess.run(['tar', '-xf', '-', '-C', DST], input=data, check=True)
    if os.path.exists(os.path.join(DST, '.env')): raise SystemExit('중단: .env 가 복사되었습니다. 올리지 않습니다.')
    run('git', 'add', 'mg-pipeline')
    if not run('git', 'status', '--porcelain', 'mg-pipeline').strip(): print('바뀐 것 없음'); return
    run('git', 'commit', '-q', '-m', f'{msg}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0121zjaLByTLA8Z9jq3epKK2')
    run('git', 'push', '-q', 'origin', 'mg-pipeline')
    print('GitHub 저장 완료:', run('git', 'log', '--oneline', '-1').strip())

if __name__ == '__main__': main()
