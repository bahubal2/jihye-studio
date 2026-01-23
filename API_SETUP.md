# API 키 설정 가이드

원클릭 스튜디오를 사용하려면 다음 외부 API 키가 필요합니다.

## 1. Google Gemini API 키

**용도**: 대본 분석 및 장면 분할

**발급 방법**:
1. [Google AI Studio](https://makersuite.google.com/app/apikey) 방문
2. "Get API Key" 클릭
3. API 키 복사

**환경변수 설정**:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 2. Replicate API Token

**용도**: 이미지 생성 (FLUX) 및 영상 생성 (Kling)

**발급 방법**:
1. [Replicate](https://replicate.com) 회원가입
2. [API Tokens 페이지](https://replicate.com/account/api-tokens) 이동
3. "Create token" 클릭
4. 토큰 복사

**환경변수 설정**:
```bash
REPLICATE_API_TOKEN=your_replicate_api_token_here
```

**비용 안내**:
- FLUX Schnell: $0.003/image (약 3.6원)
- Kling Video: $0.30/video (약 360원)

---

## 3. ElevenLabs API Key ⚠️ 중요

**용도**: 음성 생성 (TTS) - 한국어 지원

**발급 방법**:
1. [ElevenLabs](https://elevenlabs.io) 회원가입
2. [API Keys 설정](https://elevenlabs.io/app/settings/api-keys) 이동 ⭐ 올바른 URL
3. "+ Create" 버튼 클릭
4. API 키 이름 입력 (예: "지혜스튜디오")
5. "Create key" 클릭
6. 생성된 API 키 복사 (한 번만 표시됨!)

**환경변수 설정**:
```bash
ELEVENLABS_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxxxxxxx
```

**한국어 음성 설정**:
- 모델: `eleven_multilingual_v2` (기본값, 한국어 지원)
- 기본 음성 ID: `21m00Tcm4TlvDq8ikWAM` (Rachel - 영어/다국어)
- 한국어 음성 추천:
  - `EXAVITQu4vr4xnSDxMaL` (Sarah - 여성, 한국어 우수)
  - `onwK4e9ZLuTAKqWW03F9` (Daniel - 남성, 한국어 우수)

**비용 안내**:
- Free 플랜: 월 10,000 characters (약 5,000자 한글)
- Starter 플랜: $5/월, 30,000 characters
- Creator 플랜: $22/월, 100,000 characters

**⚠️ API 키 확인 방법**:
```bash
# API 키 유효성 테스트
curl -X GET "https://api.elevenlabs.io/v1/voices" \
  -H "xi-api-key: YOUR_API_KEY"
```

**성공 응답 예시**:
```json
{
  "voices": [
    {
      "voice_id": "21m00Tcm4TlvDq8ikWAM",
      "name": "Rachel"
    }
  ]
}
```

**실패 응답 (401 Unauthorized)**:
```json
{
  "detail": {
    "status": "invalid_api_key",
    "message": "Invalid API key"
  }
}
```

---

## 로컬 개발 환경 설정

### 1. `.dev.vars` 파일 생성

프로젝트 루트에 `.dev.vars` 파일을 만들고 API 키를 입력하세요:

```bash
# .dev.vars
GEMINI_API_KEY=AIzaSyB...
REPLICATE_API_TOKEN=r8_...
ELEVENLABS_API_KEY=sk_...
```

⚠️ **주의**: `.dev.vars` 파일은 절대 Git에 커밋하지 마세요! (이미 .gitignore에 포함됨)

### 2. 개발 서버 실행

```bash
npm run build
pm2 start ecosystem.config.cjs
```

---

## Cloudflare Pages 프로덕션 배포 설정

로컬 개발과 달리, 프로덕션 배포 시에는 **Cloudflare Secrets**로 환경변수를 관리합니다.

### 방법 1: Wrangler CLI로 설정

```bash
# 프로젝트명 확인
npx wrangler pages project list

# Secrets 추가
npx wrangler pages secret put GEMINI_API_KEY --project-name youtube-studio
npx wrangler pages secret put REPLICATE_API_TOKEN --project-name youtube-studio
npx wrangler pages secret put ELEVENLABS_API_KEY --project-name youtube-studio

# Secrets 확인
npx wrangler pages secret list --project-name youtube-studio
```

### 방법 2: Cloudflare Dashboard로 설정

1. [Cloudflare Dashboard](https://dash.cloudflare.com) 로그인
2. Workers & Pages → 프로젝트 선택
3. Settings → Environment Variables
4. Production 탭에서 "Add variable" 클릭
5. 각 환경변수 이름과 값 입력:
   - `GEMINI_API_KEY`
   - `REPLICATE_API_TOKEN`
   - `ELEVENLABS_API_KEY`
6. "Save" 클릭

---

## 보안 주의사항

✅ **올바른 방법**:
- 백엔드 `/api/*` 경로에서만 API 호출
- 환경변수로 API 키 관리
- `.dev.vars`를 .gitignore에 포함

❌ **절대 금지**:
- 프론트엔드 JavaScript에 API 키 하드코딩
- API 키를 Git에 커밋
- 공개 저장소에 `.dev.vars` 업로드

---

## 무료 플랜으로 시작하기

모든 API는 무료 플랜을 제공합니다:

| 서비스 | 무료 제공량 |
|--------|-------------|
| Google Gemini | 월 60 requests/minute |
| Replicate | $10 크레딧 (가입 시) |
| ElevenLabs | 월 10,000 characters |

**테스트용 예산**:
- 이미지 50장 생성: ~$0.15 (약 180원)
- 영상 5개 생성: ~$1.50 (약 1,800원)
- 음성 5분 분량: 무료 플랜 충분

---

## 문제 해결

### "API key not found" 오류

**원인**: 환경변수가 설정되지 않음

**해결**:
1. `.dev.vars` 파일 생성 확인
2. 파일 경로가 프로젝트 루트인지 확인
3. 서버 재시작: `pm2 restart youtube-studio`

### "Rate limit exceeded" 오류

**원인**: API 호출 횟수 초과

**해결**:
- Gemini: 1분당 60회 제한 (무료 플랜)
- Replicate: 크레딧 부족 시 충전 필요
- ElevenLabs: 월간 character 제한 확인

### "Invalid API key" 오류

**원인**: API 키가 만료되었거나 잘못됨

**해결**:
1. 각 서비스 대시보드에서 API 키 재발급
2. `.dev.vars` 파일 업데이트
3. 프로덕션: Cloudflare Secrets 재설정

---

## 지원 링크

- [Google Gemini API 문서](https://ai.google.dev/docs)
- [Replicate API 문서](https://replicate.com/docs)
- [ElevenLabs API 문서](https://elevenlabs.io/docs/api-reference)
- [Cloudflare Wrangler 문서](https://developers.cloudflare.com/workers/wrangler/)
