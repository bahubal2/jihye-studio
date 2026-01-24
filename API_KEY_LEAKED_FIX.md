# 🚨 긴급: API 키 유출 문제 해결

## 문제 상황

**에러 메시지:**
```
[403 Forbidden] Your API key was reported as leaked. 
Please use another API key.
```

**원인:**
- GitHub 저장소에 `.dev.vars` 파일이 커밋되어 API 키가 유출되었습니다
- Google이 자동으로 유출된 API 키를 감지하고 차단했습니다
- 현재 Gemini API 키는 사용할 수 없습니다

---

## ✅ 즉시 해결 방법

### 1단계: 새로운 Gemini API 키 발급

1. **Google AI Studio 접속**
   ```
   https://aistudio.google.com/app/apikey
   ```

2. **기존 유출된 키 삭제**
   - "Revoke" 또는 "Delete" 버튼 클릭

3. **새 API 키 생성**
   - "Create API Key" 버튼 클릭
   - 새로 생성된 키 복사

4. **API 키 입력 (2가지 방법 중 선택)**

   **방법 A: 프론트엔드 설정 (권장)** 🌟
   ```
   1. https://3000-i4e4tiae39injbyl3xfj0-5c13a017.sandbox.novita.ai 접속
   2. 좌측 하단 "설정" 버튼 클릭
   3. "API 키 설정" 탭
   4. Gemini API 키 입력
   5. 저장 버튼 클릭
   ```

   **방법 B: 서버 환경변수**
   ```bash
   # .dev.vars 파일 수정
   nano /home/user/webapp/.dev.vars
   
   # 새 API 키 입력
   GEMINI_API_KEY=AIzaSyB_your_new_key_here
   
   # 서버 재시작
   cd /home/user/webapp
   pm2 restart youtube-studio
   ```

---

### 2단계: Git에서 민감한 파일 제거 (중요!)

**`.dev.vars` 파일이 Git 히스토리에 남아있으면 계속 유출 위험이 있습니다.**

```bash
cd /home/user/webapp

# .dev.vars를 Git 히스토리에서 완전히 제거
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .dev.vars" \
  --prune-empty --tag-name-filter cat -- --all

# 원격 저장소에 강제 푸시
git push origin --force --all

# 또는 간단하게 .gitignore에 추가하고 커밋 (권장)
echo ".dev.vars" >> .gitignore
git add .gitignore
git commit -m "Add .dev.vars to gitignore"
git push origin main
```

---

### 3단계: 확인

```bash
# 서버 로그 확인
pm2 logs youtube-studio --nostream --lines 10

# API 테스트
curl -X POST http://localhost:3000/api/generate-draft-script \
  -H "Content-Type: application/json" \
  -d '{"keyword":"테스트","geminiApiKey":"YOUR_NEW_KEY"}'
```

---

## 🔒 보안 체크리스트

### ✅ 완료해야 할 것

- [ ] 기존 유출된 API 키 삭제
- [ ] 새 API 키 발급
- [ ] 새 API 키를 안전하게 입력 (프론트엔드 설정 또는 .dev.vars)
- [ ] `.dev.vars`를 `.gitignore`에 추가
- [ ] Git 히스토리에서 민감한 파일 제거 (선택)
- [ ] 서버 재시작 후 테스트

### ❌ 절대 하지 말아야 할 것

- ❌ API 키를 코드에 하드코딩
- ❌ `.dev.vars` 파일을 Git에 커밋
- ❌ API 키를 공개 채널에 공유
- ❌ 스크린샷에 API 키 노출

---

## 📋 현재 .gitignore 상태 확인

```bash
cat .gitignore
```

**확인할 내용:**
```
.dev.vars      ← 이것이 있어야 합니다!
node_modules/
dist/
.wrangler/
```

만약 없다면:
```bash
echo ".dev.vars" >> .gitignore
git add .gitignore
git commit -m "Add .dev.vars to gitignore for security"
git push origin main
```

---

## 🎯 빠른 테스트

1. **새 API 키 입력 완료**
2. **브라우저 접속**: https://3000-i4e4tiae39injbyl3xfj0-5c13a017.sandbox.novita.ai
3. **대본 생성 탭**
4. **키워드 입력**: "건강한 식습관"
5. **검수 대본 생성 클릭**
6. **결과 확인** ✅

---

## 💡 향후 예방 방법

### 1. 항상 .gitignore 확인
```bash
# 커밋 전 체크
git status
git diff

# 민감한 파일이 없는지 확인
```

### 2. Pre-commit Hook 설정
```bash
# .git/hooks/pre-commit 파일 생성
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
if git diff --cached --name-only | grep -q ".dev.vars"; then
    echo "❌ Error: .dev.vars cannot be committed!"
    echo "This file contains sensitive API keys."
    exit 1
fi
EOF

chmod +x .git/hooks/pre-commit
```

### 3. GitHub Secret Scanning 활성화
- GitHub Settings → Security → Secret scanning
- 자동으로 유출된 키를 감지하고 알림

---

## 📞 문제가 계속되면?

1. **브라우저 콘솔 확인**
   ```
   F12 → Console 탭
   ```

2. **서버 로그 확인**
   ```bash
   pm2 logs youtube-studio --nostream --lines 50
   ```

3. **API 키 유효성 테스트**
   ```bash
   curl -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=YOUR_NEW_KEY \
     -H "Content-Type: application/json" \
     -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
   ```

---

**최종 업데이트**: 2026-01-24  
**해결 상태**: ⚠️ 사용자 액션 필요 - 새 API 키 발급 및 입력
