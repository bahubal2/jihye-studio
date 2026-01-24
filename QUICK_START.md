# 🚀 빠른 시작 가이드

## 문제: "대본 생성 버튼이 작동하지 않아요!"

### ✅ 해결 방법 (2가지 중 선택)

---

## 방법 1: 프론트엔드에서 API 키 입력 (권장) 🌟

1. **지혜스튜디오 접속**
   ```
   http://localhost:3000
   ```

2. **좌측 하단 "설정" 버튼 클릭**
   - 회색 톱니바퀴 아이콘 버튼

3. **"API 키 설정" 탭에서 Gemini API 키 입력**
   - Gemini API 키 발급: https://makersuite.google.com/app/apikey
   - 입력 후 "저장" 버튼 클릭

4. **"대본 생성" 탭으로 이동**
   - 좌측 사이드바 → 대본 생성

5. **주제/키워드 입력 후 "검수 대본 생성" 버튼 클릭**
   - 예: "건강한 노후를 위한 운동법"

6. **완료! 🎉**
   - AI가 자동으로 대본을 생성합니다

---

## 방법 2: 서버 환경변수 설정 (개발자용)

1. **`.dev.vars` 파일 열기**
   ```bash
   cd /home/user/webapp
   nano .dev.vars
   ```

2. **API 키 입력**
   ```bash
   GEMINI_API_KEY=AIzaSyB...your_actual_key...
   REPLICATE_API_TOKEN=r8_...your_actual_token...
   ELEVENLABS_API_KEY=sk_...your_actual_key...
   ```

3. **서버 재시작**
   ```bash
   pm2 restart youtube-studio
   ```

4. **완료! 🎉**

---

## 🔑 API 키 발급 링크

### Google Gemini API (무료)
- **발급**: https://makersuite.google.com/app/apikey
- **무료 플랜**: 월 60 requests/minute
- **용도**: 대본 분석 및 장면 분할

### Replicate API (가입 시 $10 무료 크레딧)
- **발급**: https://replicate.com/account/api-tokens
- **무료 크레딧**: $10 (가입 시)
- **용도**: 이미지 및 영상 생성

### ElevenLabs API (무료 10,000 characters/월)
- **발급**: https://elevenlabs.io/app/settings/api-keys
- **무료 플랜**: 월 10,000 characters
- **용도**: 음성 생성 (TTS)

---

## 📱 UI 가이드

### 설정 버튼 위치
```
┌─────────────────────────────────────┐
│  좌측 사이드바                       │
│                                     │
│  📝 대본 생성                        │
│  🎬 영상 제작                        │
│  ...                                │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  🆕 새 창 열기    (초록색)          │
│  ⚙️ 설정        (회색) ← 여기!      │
│  🌐 브라우저로 열기 (파란색)         │
└─────────────────────────────────────┘
```

### API 키 입력 화면
```
설정 모달
├── API 키 설정 ← 여기를 선택
│   ├── Gemini API 키 [입력창] 👁️
│   ├── Replicate API Token [입력창] 👁️
│   └── ElevenLabs API Key [입력창] 👁️
│
└── 음성 설정
    └── (음성 관련 설정)
```

---

## ⚠️ 자주 발생하는 오류

### 오류 1: "Gemini API 키가 설정되지 않았습니다"
**해결**: 위 방법 1 또는 방법 2로 API 키 입력

### 오류 2: "Invalid API key"
**해결**: API 키를 다시 발급받아 입력

### 오류 3: "대본 생성 중 오류가 발생했습니다"
**해결**: 
1. API 키가 올바른지 확인
2. 인터넷 연결 확인
3. Gemini API 무료 한도 확인 (월 60 requests)

---

## 🎯 빠른 테스트

1. **설정 → API 키 입력**
2. **대본 생성 탭**
3. **키워드 입력**: "건강한 식습관"
4. **검수 대본 생성 클릭**
5. **10초 후 결과 확인** ✅

---

## 💡 팁

- **localStorage 자동 저장**: 한번 입력한 API 키는 브라우저에 자동 저장됩니다
- **페이지 새로고침**: API 키는 유지됩니다 (브라우저 캐시 삭제 전까지)
- **보안**: API 키는 브라우저 localStorage에만 저장되며, 서버로 전송 시 HTTPS 사용

---

## 📞 문제가 계속되면?

1. **브라우저 콘솔 확인**
   - F12 → Console 탭
   - 에러 메시지 확인

2. **서버 로그 확인**
   ```bash
   pm2 logs youtube-studio --nostream
   ```

3. **API 키 테스트**
   ```bash
   curl -X POST http://localhost:3000/api/generate-draft-script \
     -H "Content-Type: application/json" \
     -d '{"keyword":"테스트","geminiApiKey":"YOUR_KEY"}'
   ```

---

**제작**: 지혜스튜디오 v5.1  
**최종 업데이트**: 2026-01-24
