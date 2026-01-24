# 지혜스튜디오 v5.1 🎬

AI 기반 유튜브 영상 제작 솔루션

## 프로젝트 개요

- **이름**: 지혜스튜디오 (Wisdom Studio)
- **목표**: 유튜브 대본을 입력하면 AI가 자동으로 장면 분석, 이미지/영상 생성, 음성 생성까지 원클릭으로 처리
- **대상 시청자**: 한국 시니어 (노인층) 👴👵
- **핵심 기능**:
  - 📝 대본 AI 분석 (Gemini 2.5 Flash)
  - 🖼️ 자동 이미지 생성 (4가지 AI 모델 선택) - **한국 노인 중심 이미지**
  - 🎥 이미지를 영상으로 변환 (Replicate Kling)
  - 🎤 전체 음성 생성 (ElevenLabs TTS)
  - 💡 시청 이탈 방지 AI 피드백

## 완료된 기능

✅ 대본 입력 UI (다크모드 디자인)  
✅ Gemini 2.5 Flash API 연동 - 장면별 분할 및 이미지 프롬프트 자동 생성  
✅ **AI 모델 선택** - 6가지 AI 모델 드롭다운 ⭐ NEW v5.1  
  - 🌟 Nanobanana Pro (고품질 실사 + 캐릭터 일관성) ⭐ NEW
  - 📸 Nanobanana (실사 + 캐릭터 일관성) ⭐ NEW
  - 🏆 FLUX 1.1 Pro (최고 품질) - 기본값
  - 💎 FLUX Dev (고품질 무료)
  - ⚡ FLUX Schnell (빠름)
  - ✨ Recraft V3 (초고품질)
✅ **캐릭터 일관성 기능** - 동일 캐릭터 유지 ⭐ NEW v5.1  
  - 캐릭터 참조 이미지 업로드 (PNG, JPG 최대 10MB)
  - 캐릭터 설명 입력 (선택)
  - 일관성 강도 슬라이더 (0~1, 기본값 0.7)
  - "모든 장면에 이 캐릭터 사용" 체크박스
  - Nanobanana/Nanobanana Pro 모델에서 완벽 지원
✅ **품질 향상 프롬프트** - 자동 품질 키워드 추가 ⭐ NEW  
✅ **네거티브 프롬프트** - 저품질 이미지 자동 제외 ⭐ NEW  
✅ **이미지 스타일 선택** - 5가지 프리셋 + 커스텀 스타일  
✅ **이미지 비율 선택** - 16:9, 9:16, 1:1, 4:3, 3:4  
✅ Replicate Kling API 연동 - 이미지 투 비디오 변환  
✅ ElevenLabs TTS API 연동 - 음성 파일 생성  
✅ **설정 모달** - API 키 & 음성 설정 ⭐ NEW v5.1
  - API 키 설정 탭: Replicate, ElevenLabs, Gemini API 키 입력/관리
  - 음성 설정 탭: Voice ID, 안정성, 유사성, 스타일 조절
  - 음성 미리듣기: '안녕하세요' 샘플 테스트
  - 내 음성 불러오기: ElevenLabs 음성 목록 조회
  - localStorage 자동 저장: 페이지 새로고침 시 설정 유지
✅ **프로젝트 관리** - 저장/불러오기 기능 ⭐ NEW v5.1
  - 프로젝트 저장: 현재 작업 내용을 이름과 함께 저장
  - 프로젝트 불러오기: 저장된 프로젝트 목록에서 선택하여 복원
  - 프로젝트 삭제: 불필요한 프로젝트 제거
  - localStorage 저장: 브라우저에 자동 저장
✅ **드래그앤드롭** - 장면 순서 변경 ⭐ NEW v5.1
  - 장면 카드를 드래그하여 순서 재배치
  - 직관적인 시각적 피드백
✅ **전체 다운로드 (ZIP)** - 모든 에셋 일괄 다운로드 ⭐ NEW v5.1
  - 모든 이미지 파일 포함
  - 모든 영상 파일 포함
  - 대본 텍스트 파일 포함
  - JSZip을 통한 압축 및 다운로드
✅ 폴링 시스템 - 영상 생성 상태 실시간 체크  
✅ 로딩 상태 & 토스트 알림 UI  
✅ 장면별 카드 레이아웃 및 미리보기  
✅ **저작권 푸터** - © 2026 지혜스튜디오랩 ⭐ NEW  

## 아직 구현되지 않은 기능

⏳ 영상 자동 합성 (FFmpeg 기반)  
⏳ 클라우드 스토리지 연동 (Cloudflare KV/R2)  
⏳ 실시간 협업 기능  
⏳ 템플릿 갤러리  

## 기능 진입 경로

### 메인 페이지
- **URL**: `/`
- **기능**: 대본 입력, 장면 분석, 전체 UI

### API 엔드포인트

| 메서드 | 경로 | 파라미터 | 설명 |
|--------|------|----------|------|
| POST | `/api/analyze-script` | `{ script: string }` | 대본 분석 및 장면 분할 |
| POST | `/api/generate-image` | `{ prompt: string, sceneId: number, stylePrefix?: string, aspectRatio?: string, model?: string, characterImage?: string, characterDescription?: string, characterStrength?: number }` | 이미지 생성 (AI 모델 선택 가능, 캐릭터 일관성 지원) |
| POST | `/api/generate-video` | `{ imageUrl: string, prompt: string, sceneId: number }` | 영상 생성 시작 |
| POST | `/api/generate-voice` | `{ text: string, voiceId?: string, voiceSettings?: { stability: number, similarity_boost: number, style: number } }` | 음성 생성 (MP3 반환, 음성 설정 커스터마이징 가능) |
| GET | `/api/check-status/:jobId` | - | 영상 생성 상태 확인 (폴링용) |

## 데이터 구조

### AI 모델 옵션 (v5.1)
```typescript
const AI_MODELS = {
  'flux-pro': {
    name: 'FLUX 1.1 Pro (최고 품질)',
    model: 'black-forest-labs/flux-1.1-pro',
    speed: '2-5초',
    default: true
  },
  'flux-dev': {
    name: 'FLUX Dev (고품질 무료)',
    model: 'black-forest-labs/flux-dev',
    parameters: { guidance: 3.5, steps: 28 },
    speed: '약 2초'
  },
  'flux-schnell': {
    name: 'FLUX Schnell (빠름)',
    model: 'black-forest-labs/flux-schnell',
    parameters: { steps: 4 },
    speed: '약 2초'
  },
  'recraft-v3': {
    name: 'Recraft V3 (초고품질)',
    model: 'recraft-ai/recraft-v3',
    parameters: { style: 'realistic_image' },
    speed: '약 6초'
  }
}

// 품질 향상 프롬프트
const QUALITY_ENHANCEMENT = "masterpiece, best quality, highly detailed, sharp focus, professional photography, "

// 네거티브 프롬프트
const NEGATIVE_PROMPT = "low quality, blurry, distorted, disfigured, bad anatomy, wrong proportions, watermark, text, logo, ugly, duplicate"
```

### 이미지 스타일 프리셋 (한국 시니어 최적화)
```typescript
const STYLE_PRESETS = {
  photorealistic: 'photorealistic, Korean elderly person, Asian features, Korean senior citizen, 8k, detailed, warm lighting, natural Korean environment, ',
  anime: 'Korean traditional folktale anime style, Korean characters, Asian features, Ghibli inspired, soft colors, historical Korean setting, hanbok, ',
  stickman: 'simple stick figure drawing, minimalist, black lines on white background, ',
  illustration: 'warm emotional digital illustration, Korean elderly, Asian features, soft pastel colors, nostalgic Korean life scene, ',
  custom: '' // 사용자 정의
}
```

### Scene 객체
```typescript
{
  id: number,
  text: string,              // 장면 내레이션 텍스트
  duration: number,          // 예상 시간 (초)
  imagePrompt: string,       // AI 생성 이미지 프롬프트
  feedback: string,          // 시청 이탈 방지 피드백
  imageUrl?: string,         // 생성된 이미지 URL
  videoUrl?: string,         // 생성된 영상 URL
  imageLoading: boolean,
  videoLoading: boolean,
  videoJobId?: string
}
```

### 스토리지 서비스
- **임시 저장소**: Map (메모리) - 영상 생성 작업 상태 관리
- **향후 권장**: Cloudflare KV - 프로젝트 영구 저장용

## 사용 가이드

### 1. 환경변수 설정
`.dev.vars` 파일에 API 키 입력:
```bash
GEMINI_API_KEY=your_key
REPLICATE_API_TOKEN=your_token
ELEVENLABS_API_KEY=your_key
```

### 2. 개발 서버 실행
```bash
npm run build
pm2 start ecosystem.config.cjs
```

### 3. 사용 흐름
1. **AI 모델 선택** → FLUX 1.1 Pro (기본값), FLUX Dev, FLUX Schnell, Recraft V3 중 선택
2. **이미지 스타일 선택** → 실사, 애니메이션, 스틱맨, 일러스트, 커스텀 중 선택
3. **이미지 비율 설정** → 16:9, 9:16, 1:1 등 선택
4. 대본 입력 → "AI 분석 시작" 클릭
5. 장면별로 자동 생성된 이미지 프롬프트 확인
6. "전체 이미지 생성" 또는 개별 "이미지 생성" 클릭
7. 원하는 장면에서 "영상 변환" 클릭 (2-5분 소요)
8. "전체 음성 생성" 클릭 → MP3 다운로드

### 4. 화면 구성
- **상단**: 지혜스튜디오 v5.1 타이틀
- **이미지 설정 패널**: AI 모델, 스타일, 비율 선택
- **좌측**: 대본 입력 영역
- **우측**: 장면 카드 그리드 (이미지 미리보기, 생성 버튼)
- **하단**: 전체 음성 생성, 다운로드 버튼
- **푸터**: © 2025 지혜스튜디오랩. All Rights Reserved.

## 다음 개발 단계 권장사항

1. **프로젝트 저장 기능**: Cloudflare KV로 작업 내역 저장
2. **일괄 영상 생성**: 모든 장면을 자동으로 영상 변환
3. **타임라인 에디터**: 장면 순서 재배치 및 시간 조정
4. **자막 자동 생성**: 음성 파일 기반 SRT 생성
5. **최종 렌더링**: FFmpeg로 장면 합성 + 음성 믹싱

## URLs

- **GitHub**: https://github.com/bahubal2/jihye-studio ⭐ NEW
- **로컬 개발**: http://localhost:3000
- **퍼블릭 테스트 URL**: https://3000-i4e4tiae39injbyl3xfj0-5c13a017.sandbox.novita.ai
- **프로덕션**: (Cloudflare Pages 배포 필요)

## 배포 상태

- **플랫폼**: Cloudflare Pages
- **상태**: ✅ 모든 API 정상 작동 - 즉시 사용 가능!
- **기술 스택**: Hono + TypeScript + React + TailwindCSS + Gemini 2.5 Flash
- **브랜드**: 지혜스튜디오 v5.1
- **저작권**: © 2026 지혜스튜디오랩. All Rights Reserved.
- **최종 업데이트**: 2026-01-23

## 기술 스택

- **프론트엔드**: React 18 (CDN), TailwindCSS, FontAwesome
- **백엔드**: Hono (Cloudflare Workers)
- **AI 서비스**:
  - Google Gemini 2.5 Flash (대본 분석) ✅ 작동 확인
  - Replicate FLUX 1.1 Pro (초고품질 이미지) ⭐ 기본값
  - Replicate FLUX Dev (고품질 무료) ✅ 테스트 완료
  - Replicate FLUX Schnell (빠른 생성) ✅ 테스트 완료
  - Replicate Recraft V3 (초고품질) ✅ 테스트 완료
  - Replicate Kling (영상 생성) ✅ 준비 완료
  - ElevenLabs (음성 합성) ✅ 준비 완료

## 주의사항

⚠️ **API 키 보안**: 절대 프론트엔드에 노출하지 말 것  
⚠️ **영상 생성 시간**: Kling 모델은 2-5분 소요 (폴링 필수)  
⚠️ **비용**: Replicate 및 ElevenLabs는 사용량 기반 과금  
⚠️ **환경변수**: .dev.vars는 절대 Git에 커밋하지 말 것

## 라이선스

MIT License - 개인/상업적 자유 사용 가능
