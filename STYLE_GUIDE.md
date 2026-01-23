# 이미지 스타일 가이드

원클릭 스튜디오는 5가지 이미지 스타일 프리셋을 제공합니다.

## 📸 1. 실사 (Photorealistic)

**프리픽스**: `photorealistic, 8k, detailed, professional photography, `

**용도**:
- 현실감 있는 영상 제작
- 다큐멘터리 스타일
- 비즈니스/프로페셔널 콘텐츠
- 리뷰 영상

**예시 결과**:
```
AI 생성 프롬프트: "A modern office with people working on computers"
최종 프롬프트: "photorealistic, 8k, detailed, professional photography, A modern office with people working on computers"
→ 고해상도, 사실적인 사무실 이미지 생성
```

---

## 🎨 2. 애니메이션 (Anime/Cartoon)

**프리픽스**: `anime style, cartoon, vibrant colors, cel shading, `

**용도**:
- 어린이 콘텐츠
- 설명 영상 (Explainer videos)
- 캐릭터 기반 스토리텔링
- 게임 관련 콘텐츠

**예시 결과**:
```
AI 생성 프롬프트: "A hero standing on a mountain peak"
최종 프롬프트: "anime style, cartoon, vibrant colors, cel shading, A hero standing on a mountain peak"
→ 일본 애니메이션 스타일의 영웅 캐릭터 이미지
```

---

## ✏️ 3. 스틱맨 (Simple Stickman)

**프리픽스**: `simple stick figure drawing, minimalist, black lines on white background, `

**용도**:
- 빠른 컨셉 설명
- 교육 콘텐츠
- 프로세스 설명
- 미니멀한 디자인

**예시 결과**:
```
AI 생성 프롬프트: "Two people shaking hands in a business meeting"
최종 프롬프트: "simple stick figure drawing, minimalist, black lines on white background, Two people shaking hands in a business meeting"
→ 간단한 선으로만 표현된 악수 장면
```

**주의사항**: 
- 매우 단순한 스타일이므로 복잡한 장면에는 부적합
- 세부 디테일이 생략됨

---

## 🖼️ 4. 일러스트 (Illustration)

**프리픽스**: `digital illustration, artistic, stylized, `

**용도**:
- 크리에이티브 콘텐츠
- 스토리텔링
- 블로그 썸네일
- 소셜 미디어 포스트

**예시 결과**:
```
AI 생성 프롬프트: "A colorful sunset over the ocean"
최종 프롬프트: "digital illustration, artistic, stylized, A colorful sunset over the ocean"
→ 예술적이고 스타일화된 일몰 이미지
```

---

## ⚙️ 5. 커스텀 (Custom)

**프리픽스**: 사용자 직접 입력

**용도**:
- 특정 아트 스타일 적용
- 브랜드 일관성 유지
- 고급 사용자 맞춤 설정

**예시**:

### 예시 1: 수채화 스타일
```
커스텀 프리픽스: "watercolor painting, soft colors, artistic, "
AI 생성 프롬프트: "A peaceful garden with flowers"
최종 프롬프트: "watercolor painting, soft colors, artistic, A peaceful garden with flowers"
→ 수채화 느낌의 정원 이미지
```

### 예시 2: 사이버펑크 스타일
```
커스텀 프리픽스: "cyberpunk style, neon lights, futuristic city, "
AI 생성 프롬프트: "A street scene at night"
최종 프롬프트: "cyberpunk style, neon lights, futuristic city, A street scene at night"
→ 네온사인이 빛나는 미래 도시 거리
```

### 예시 3: 유화 스타일
```
커스텀 프리픽스: "oil painting, impressionist style, thick brushstrokes, "
AI 생성 프롬프트: "A portrait of a person"
최종 프롬프트: "oil painting, impressionist style, thick brushstrokes, A portrait of a person"
→ 인상파 유화 스타일의 초상화
```

**팁**:
- 프리픽스 끝에 항상 쉼표와 공백 추가 (`, `)
- 구체적인 스타일 키워드 사용
- 여러 번 테스트하여 최적의 프리픽스 찾기

---

## 🎛️ 이미지 비율 옵션

### 16:9 (가로) - 기본값
- 유튜브 영상 표준
- 가로로 긴 풍경 촬영
- 대부분의 영상 콘텐츠

### 9:16 (세로)
- 인스타그램 릴스
- 유튜브 쇼츠
- TikTok 영상
- 모바일 우선 콘텐츠

### 1:1 (정사각형)
- 인스타그램 피드
- 프로필 이미지
- 썸네일

### 4:3 (클래식)
- 전통적인 TV 비율
- 프레젠테이션
- 복고풍 느낌

### 3:4 (포트레이트)
- 세로 사진
- 포스터
- 인물 중심 콘텐츠

---

## ⚡ 품질 옵션

### 빠름 (Schnell)
- **생성 시간**: 3-5초
- **모델**: FLUX Schnell
- **용도**: 빠른 프로토타이핑, 대량 생성
- **비용**: 저렴 (~$0.003/image)

### 고품질 (Dev)
- **생성 시간**: 20-30초
- **모델**: FLUX Dev
- **용도**: 최종 결과물, 높은 품질 요구
- **비용**: 높음 (~$0.05/image)

**권장사항**:
- 초기 테스트: "빠름" 사용
- 최종 결과물: "고품질" 사용

---

## 💡 스타일 조합 팁

### 시나리오 1: 유튜브 교육 콘텐츠
```
스타일: 일러스트 (Illustration)
비율: 16:9
품질: 빠름
→ 빠르게 많은 이미지를 생성하여 테스트
```

### 시나리오 2: 인스타그램 릴스
```
스타일: 애니메이션 (Anime)
비율: 9:16
품질: 고품질
→ 세로 형태의 고품질 애니메이션 이미지
```

### 시나리오 3: 비즈니스 프레젠테이션
```
스타일: 실사 (Photorealistic)
비율: 16:9
품질: 고품질
→ 전문적이고 사실적인 이미지
```

### 시나리오 4: 빠른 컨셉 설명
```
스타일: 스틱맨 (Stickman)
비율: 16:9
품질: 빠름
→ 간단하고 빠른 설명용 이미지
```

---

## 🎨 고급 커스텀 프리픽스 예시

### 영화 같은 느낌
```
cinematic lighting, film grain, dramatic atmosphere, 
```

### 3D 렌더링
```
3D render, unreal engine, octane render, high detail, 
```

### 픽셀 아트
```
pixel art, 8-bit style, retro gaming, 
```

### 종이 컷아웃
```
paper cutout style, layered, shadow depth, 
```

### 라인 드로잉
```
line art, ink drawing, clean lines, black and white, 
```

---

## 🚀 사용 흐름

1. **스타일 선택** - 상단 "이미지 스타일 설정" 카드에서 선택
2. **비율 선택** - 콘텐츠 플랫폼에 맞게 선택
3. **품질 선택** - 테스트는 빠름, 최종은 고품질
4. **대본 입력** - AI가 장면별 프롬프트 자동 생성
5. **이미지 생성** - 선택한 스타일이 모든 장면에 적용
6. **결과 확인** - 마음에 들지 않으면 다른 스타일로 재생성

---

## ⚠️ 주의사항

1. **스타일 일관성**: 한 영상 내에서는 동일한 스타일 유지 권장
2. **프리픽스 순서**: 프리픽스가 AI 프롬프트 **앞에** 붙음
3. **쉼표 필수**: 커스텀 프리픽스 끝에 `, ` 추가
4. **비용 고려**: 고품질 모드는 빠름 모드의 약 15배 비용

---

## 🎯 스타일별 적합도

| 스타일 | 교육 | 엔터테인먼트 | 비즈니스 | 빠른 설명 | 예술적 표현 |
|--------|------|-------------|----------|-----------|-------------|
| 실사 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| 애니메이션 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 스틱맨 | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| 일러스트 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 커스텀 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

**이제 원하는 스타일로 멋진 영상을 만들어보세요!** 🎬✨
