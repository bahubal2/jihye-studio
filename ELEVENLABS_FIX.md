# ElevenLabs 음성 생성 문제 해결 가이드

## 🔍 진단 결과

### 문제 상황
음성 생성 시 `401 Unauthorized` 에러 발생

### 원인
현재 `.dev.vars`에 저장된 ElevenLabs API 키가 **만료되었거나 유효하지 않음**

```bash
# 현재 API 키 테스트 결과
HTTP Status: 401 Unauthorized
{
  "detail": {
    "status": "invalid_api_key",
    "message": "Invalid API key"
  }
}
```

---

## ✅ 해결 방법

### 1단계: 새 API 키 발급

1. **ElevenLabs 대시보드 접속**
   - URL: https://elevenlabs.io/app/settings/api-keys

2. **API 키 생성**
   - "+ Create" 버튼 클릭
   - 키 이름 입력 (예: "지혜스튜디오")
   - "Create key" 클릭

3. **API 키 복사**
   - ⚠️ 주의: 생성 직후 한 번만 표시됩니다!
   - 형식: `sk_xxxxxxxxxxxxxxxxxxxxxxxxxx`

### 2단계: 환경변수 업데이트

```bash
# .dev.vars 파일 수정
cd /home/user/webapp
nano .dev.vars
```

```bash
# .dev.vars 내용
GEMINI_API_KEY=AIzaSyBceM2dJRoK4TcaHYJEd1oPBU69UEqeFq8
REPLICATE_API_TOKEN=r8_TpFv1k9Wy1gLFNu7MmWIBrmMfnNnFm33BGAES
ELEVENLABS_API_KEY=sk_새로발급받은키를여기에입력
```

### 3단계: API 키 유효성 검증

```bash
# 명령어로 직접 테스트
ELEVENLABS_KEY="sk_새로발급받은키"
curl -X GET "https://api.elevenlabs.io/v1/voices" \
  -H "xi-api-key: $ELEVENLABS_KEY"
```

**성공 응답**:
```json
{
  "voices": [
    {
      "voice_id": "21m00Tcm4TlvDq8ikWAM",
      "name": "Rachel",
      "category": "premade"
    }
  ]
}
```

### 4단계: 서버 재시작

```bash
cd /home/user/webapp
pm2 restart youtube-studio
```

### 5단계: 음성 생성 테스트

```bash
curl -X POST http://localhost:3000/api/generate-voice \
  -H "Content-Type: application/json" \
  -d '{"text": "안녕하세요. 지혜스튜디오입니다."}' \
  -o test_voice.mp3
```

**성공 시**: `test_voice.mp3` 파일 생성됨

---

## 🎤 한국어 음성 추천

### 기본 설정
- **모델**: `eleven_multilingual_v2` (한국어 지원)
- **기본 음성**: Rachel (다국어)

### 추천 한국어 음성 ID

1. **Sarah** (여성, 한국어 우수)
   - Voice ID: `EXAVITQu4vr4xnSDxMaL`
   - 특징: 부드럽고 자연스러운 한국어

2. **Daniel** (남성, 한국어 우수)
   - Voice ID: `onwK4e9ZLuTAKqWW03F9`
   - 특징: 명확하고 권위있는 목소리

### 음성 변경 방법

프론트엔드에서 `voiceId` 파라미터 추가:
```javascript
await fetch('/api/generate-voice', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    text: fullScript,
    voiceId: 'EXAVITQu4vr4xnSDxMaL' // Sarah 음성
  })
})
```

---

## 💰 비용 정보

| 플랜 | 월 비용 | 무료 문자 수 | 한국어 글자 수 |
|------|---------|--------------|----------------|
| Free | $0 | 10,000 characters | 약 5,000자 |
| Starter | $5 | 30,000 characters | 약 15,000자 |
| Creator | $22 | 100,000 characters | 약 50,000자 |

**예시**:
- 1분 대본 (약 500자) = 1,000 characters
- Free 플랜으로 약 5분 분량 음성 생성 가능

---

## 🔧 개선된 에러 메시지

### 이전 (❌)
```json
{
  "error": "음성 생성 중 오류가 발생했습니다",
  "details": "ElevenLabs API error: Unauthorized"
}
```

### 현재 (✅)
```json
{
  "error": "ElevenLabs API 키가 유효하지 않습니다",
  "details": "API 키를 확인해주세요.\n\n해결 방법:\n1. https://elevenlabs.io/app/settings/api-keys 에서 새 API 키 발급\n2. .dev.vars 파일의 ELEVENLABS_API_KEY 업데이트\n3. 서버 재시작: pm2 restart youtube-studio\n\nElevenLabs 오류: {\"detail\":{\"status\":\"invalid_api_key\",\"message\":\"Invalid API key\"}}"
}
```

---

## 📚 참고 자료

- **ElevenLabs API 문서**: https://elevenlabs.io/docs/api-reference
- **음성 라이브러리**: https://elevenlabs.io/voice-library
- **가격 정책**: https://elevenlabs.io/pricing
- **API Keys 관리**: https://elevenlabs.io/app/settings/api-keys

---

## ✅ 완료 체크리스트

- [ ] ElevenLabs 대시보드에서 새 API 키 발급
- [ ] `.dev.vars` 파일에 새 API 키 저장
- [ ] curl로 API 키 유효성 검증
- [ ] 서버 재시작 (`pm2 restart youtube-studio`)
- [ ] 음성 생성 테스트
- [ ] (선택) 한국어 음성 ID 설정

---

**마지막 업데이트**: 2026-01-23  
**커밋**: `ea41952`
