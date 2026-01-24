import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { GoogleGenerativeAI } from '@google/generative-ai'
import Replicate from 'replicate'

type Bindings = {
  GEMINI_API_KEY: string
  REPLICATE_API_TOKEN: string
  ELEVENLABS_API_KEY: string
}

const app = new Hono<{ Bindings: Bindings }>()

// CORS 설정
app.use('/api/*', cors())

// 임시 저장소 (실제로는 KV나 D1 사용 권장)
const jobStorage = new Map<string, any>()

// ===== API 엔드포인트 =====

// 0. 검수 대본 생성 (Gemini)
app.post('/api/generate-draft-script', async (c) => {
  try {
    const { keyword, geminiApiKey } = await c.req.json()
    
    if (!keyword) {
      return c.json({ error: '주제나 키워드를 입력해주세요' }, 400)
    }

    // 클라이언트에서 전달받은 API 키 사용, 없으면 서버 환경변수 사용
    const apiKey = geminiApiKey || c.env.GEMINI_API_KEY || ''
    if (!apiKey) {
      return c.json({ error: 'Gemini API 키가 설정되지 않았습니다. 설정에서 API 키를 입력해주세요.' }, 400)
    }

    const genAI = new GoogleGenerativeAI(apiKey)
    const model = genAI.getGenerativeModel({ 
      model: 'gemini-2.5-flash'
    })

    const prompt = `다음 주제/키워드를 바탕으로 한국 시니어(노인층)를 대상으로 한 유튜브 영상 대본을 작성해주세요.

주제/키워드: ${keyword}

요구사항:
1. 대상: 한국 시니어 (60대 이상)
2. 톤: 따뜻하고 친근하며, 이해하기 쉬운 언어 사용
3. 길이: 3-5분 분량 (약 800-1200자)
4. 구성: 인트로 → 본문 → 아웃트로
5. 시청 이탈 방지: 흥미로운 사실, 질문, 공감 유도
6. 한국 문화와 정서 반영

대본만 작성해주세요. 다른 설명 없이 대본 텍스트만 출력하세요.`

    const result = await model.generateContent(prompt)
    const scriptText = result.response.text()

    return c.json({
      success: true,
      data: {
        script: scriptText.trim()
      }
    })
  } catch (error: any) {
    console.error('Draft script generation error:', error)
    return c.json({ 
      error: '대본 생성 중 오류가 발생했습니다',
      details: error.message 
    }, 500)
  }
})

// 1. 대본 분석 (Gemini)
app.post('/api/analyze-script', async (c) => {
  try {
    const { script, geminiApiKey } = await c.req.json()
    
    if (!script) {
      return c.json({ error: '대본을 입력해주세요' }, 400)
    }

    // 클라이언트에서 전달받은 API 키 사용, 없으면 서버 환경변수 사용
    const apiKey = geminiApiKey || c.env.GEMINI_API_KEY || ''
    if (!apiKey) {
      return c.json({ error: 'Gemini API 키가 설정되지 않았습니다. 설정에서 API 키를 입력해주세요.' }, 400)
    }

    const genAI = new GoogleGenerativeAI(apiKey)
    const model = genAI.getGenerativeModel({ 
      model: 'gemini-2.5-flash'
    })

    const prompt = `다음 유튜브 영상 대본을 분석하여 장면별로 분할하고, 각 장면에 적합한 이미지 생성 프롬프트를 만들어주세요.

대본:
${script}

다음 JSON 형식으로 응답해주세요:
{
  "scenes": [
    {
      "id": 1,
      "text": "장면의 내레이션 텍스트",
      "duration": 5,
      "imagePrompt": "A photorealistic image of...",
      "feedback": "이 장면에서 시청자 이탈을 방지하기 위한 피드백"
    }
  ],
  "overallFeedback": "전체 대본에 대한 피드백",
  "suggestions": ["개선 제안 1", "개선 제안 2"]
}`

    const result = await model.generateContent(prompt)
    const responseText = result.response.text()
    
    // JSON 파싱 (마크다운 코드 블록 제거)
    let jsonText = responseText.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim()
    const analysis = JSON.parse(jsonText)

    return c.json({
      success: true,
      data: analysis
    })
  } catch (error: any) {
    console.error('Script analysis error:', error)
    return c.json({ 
      error: '대본 분석 중 오류가 발생했습니다',
      details: error.message 
    }, 500)
  }
})

// 2. 이미지 생성 (다양한 AI 모델 지원)
app.post('/api/generate-image', async (c) => {
  try {
    const { 
      prompt, 
      sceneId, 
      stylePrefix = '', 
      aspectRatio = '16:9', 
      model = 'flux-1.1-pro',
      characterImage = null,
      characterDescription = '',
      characterStrength = 0.7,
      replicateApiKey
    } = await c.req.json()
    
    if (!prompt) {
      return c.json({ error: '프롬프트를 입력해주세요' }, 400)
    }

    // 클라이언트에서 전달받은 API 키 사용, 없으면 서버 환경변수 사용
    const apiKey = replicateApiKey || c.env.REPLICATE_API_TOKEN || ''
    if (!apiKey) {
      return c.json({ error: 'Replicate API 키가 설정되지 않았습니다. 설정에서 API 키를 입력해주세요.' }, 400)
    }

    const replicate = new Replicate({
      auth: apiKey
    })

    // 품질 향상 키워드 추가
    const qualityEnhancement = 'masterpiece, best quality, highly detailed, sharp focus, professional photography, '
    
    // 네거티브 프롬프트
    const negativePrompt = 'low quality, blurry, distorted, disfigured, bad anatomy, wrong proportions, watermark, text, logo, ugly, duplicate, '

    // 캐릭터 설명 추가
    let characterPrefix = ''
    if (characterDescription) {
      characterPrefix = characterDescription + ', '
    }

    // 최종 프롬프트 생성
    const finalPrompt = `${qualityEnhancement}${characterPrefix}${stylePrefix}${prompt}`

    console.log('Generating image with model:', model)
    console.log('Final prompt:', finalPrompt)
    console.log('Character image:', characterImage ? 'provided' : 'none')
    console.log('Character strength:', characterStrength)

    // 모델별 설정
    const modelConfigs: Record<string, any> = {
      'nanobanana-pro': {
        model: 'fofr/nanobanana-pro',
        input: {
          prompt: finalPrompt,
          aspect_ratio: aspectRatio,
          output_format: "webp",
          output_quality: 100,
          num_inference_steps: 28,
          guidance_scale: 3.5,
          ...(characterImage && {
            image: characterImage,
            prompt_strength: characterStrength
          })
        }
      },
      'nanobanana': {
        model: 'fofr/nanobanana',
        input: {
          prompt: finalPrompt,
          aspect_ratio: aspectRatio,
          output_format: "webp",
          output_quality: 95,
          num_inference_steps: 20,
          ...(characterImage && {
            image: characterImage,
            prompt_strength: characterStrength
          })
        }
      },
      'flux-pro': {
        model: 'black-forest-labs/flux-1.1-pro',
        input: {
          prompt: finalPrompt,
          aspect_ratio: aspectRatio,
          output_format: "webp",
          output_quality: 100,
          safety_tolerance: 2
        }
      },
      'flux-dev': {
        model: 'black-forest-labs/flux-dev',
        input: {
          prompt: finalPrompt,
          guidance: 3.5,
          num_inference_steps: 28,
          aspect_ratio: aspectRatio,
          output_format: "webp",
          output_quality: 95
        }
      },
      'flux-schnell': {
        version: '5599ed30703defd1d160a25a63321b4dec97101d98b4674bcc56e41f62f35637',
        input: {
          prompt: finalPrompt,
          num_inference_steps: 4,
          aspect_ratio: aspectRatio,
          output_format: "webp",
          output_quality: 90
        }
      },
      'recraft-v3': {
        model: 'recraft-ai/recraft-v3',
        input: {
          prompt: finalPrompt,
          style: "realistic_image",
          size: aspectRatio === '16:9' ? '1365x1024' : aspectRatio === '9:16' ? '1024x1365' : '1024x1024',
          output_format: "webp"
        }
      },
      'sdxl': {
        model: 'stability-ai/sdxl',
        input: {
          prompt: finalPrompt,
          negative_prompt: negativePrompt,
          guidance_scale: 7.5,
          num_inference_steps: 30,
          width: aspectRatio === '16:9' ? 1344 : aspectRatio === '9:16' ? 768 : 1024,
          height: aspectRatio === '16:9' ? 768 : aspectRatio === '9:16' ? 1344 : 1024
        }
      }
    }

    const config = modelConfigs[model]
    if (!config) {
      throw new Error(`Unknown model: ${model}`)
    }

    // predictions API를 사용하여 예측 생성
    // version 또는 model 사용 (모델명으로 최신 버전 자동 선택)
    const predictionParams: any = { input: config.input }
    if (config.version) {
      predictionParams.version = config.version
    } else if (config.model) {
      predictionParams.model = config.model
    } else {
      throw new Error(`No version or model specified for ${model}`)
    }
    
    const prediction = await replicate.predictions.create(predictionParams)

    console.log('Prediction created:', prediction.id)

    // 예측 완료 대기 (최대 120초 - 고품질 모델은 시간이 더 걸림)
    let result = prediction
    let attempts = 0
    const maxAttempts = 120

    while (result.status !== 'succeeded' && result.status !== 'failed' && attempts < maxAttempts) {
      await new Promise(resolve => setTimeout(resolve, 1000))
      result = await replicate.predictions.get(prediction.id)
      attempts++
      if (attempts % 10 === 0) {
        console.log(`Attempt ${attempts}: Status = ${result.status}`)
      }
    }

    if (result.status === 'failed') {
      throw new Error('Image generation failed: ' + (result.error || 'Unknown error'))
    }

    if (result.status !== 'succeeded') {
      throw new Error('Image generation timeout')
    }

    // 결과에서 이미지 URL 추출
    const imageUrl = Array.isArray(result.output) ? result.output[0] : result.output

    if (!imageUrl || typeof imageUrl !== 'string') {
      throw new Error('Invalid image URL returned')
    }

    console.log('Image generated successfully:', imageUrl)
    console.log('Generation time:', attempts, 'seconds')

    return c.json({
      success: true,
      data: {
        sceneId,
        imageUrl,
        usedPrompt: finalPrompt,
        model,
        generationTime: attempts
      }
    })
  } catch (error: any) {
    console.error('Image generation error:', error)
    return c.json({ 
      error: '이미지 생성 중 오류가 발생했습니다',
      details: error.message 
    }, 500)
  }
})

// 3. 영상 생성 (Replicate Kling)
app.post('/api/generate-video', async (c) => {
  try {
    const { imageUrl, prompt, sceneId, replicateApiKey } = await c.req.json()
    
    if (!imageUrl) {
      return c.json({ error: '이미지 URL을 입력해주세요' }, 400)
    }

    // 클라이언트에서 전달받은 API 키 사용, 없으면 서버 환경변수 사용
    const apiKey = replicateApiKey || c.env.REPLICATE_API_TOKEN || ''
    if (!apiKey) {
      return c.json({ error: 'Replicate API 키가 설정되지 않았습니다. 설정에서 API 키를 입력해주세요.' }, 400)
    }

    const replicate = new Replicate({
      auth: apiKey
    })

    // Kling 비디오 생성 (이미지 투 비디오)
    const prediction = await replicate.predictions.create({
      version: "ee1b121b5e09ace1cf779e1c38c8e9849fdfee1ff63f8d58a5e36a65c29f7a97",
      input: {
        image: imageUrl,
        prompt: prompt || "Cinematic shot, high quality video",
        duration: "5",
        aspect_ratio: "16:9"
      }
    })

    // 작업 ID 저장
    const jobId = prediction.id
    jobStorage.set(jobId, {
      type: 'video',
      sceneId,
      status: 'processing',
      predictionId: prediction.id
    })

    return c.json({
      success: true,
      data: {
        jobId,
        sceneId,
        status: 'processing'
      }
    })
  } catch (error: any) {
    console.error('Video generation error:', error)
    return c.json({ 
      error: '영상 생성 중 오류가 발생했습니다',
      details: error.message 
    }, 500)
  }
})

// 4. 음성 생성 (ElevenLabs)
app.post('/api/generate-voice', async (c) => {
  try {
    const { 
      text, 
      voiceId = '21m00Tcm4TlvDq8ikWAM',
      voiceSettings = {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.0
      },
      elevenlabsApiKey
    } = await c.req.json()
    
    if (!text) {
      return c.json({ error: '텍스트를 입력해주세요' }, 400)
    }

    // 클라이언트에서 전달받은 API 키 사용, 없으면 서버 환경변수 사용
    const apiKey = elevenlabsApiKey || c.env.ELEVENLABS_API_KEY || ''
    if (!apiKey) {
      console.error('ElevenLabs API key not found')
      return c.json({ 
        error: 'ElevenLabs API 키가 설정되지 않았습니다. 설정에서 API 키를 입력해주세요.'
      }, 400)
    }

    console.log('Generating voice with ElevenLabs...')
    console.log('Text length:', text.length, 'characters')
    console.log('Voice ID:', voiceId)
    console.log('Voice Settings:', voiceSettings)

    const response = await fetch(
      `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`,
      {
        method: 'POST',
        headers: {
          'Accept': 'audio/mpeg',
          'Content-Type': 'application/json',
          'xi-api-key': apiKey
        },
        body: JSON.stringify({
          text,
          model_id: 'eleven_multilingual_v2',
          voice_settings: {
            stability: voiceSettings.stability || 0.5,
            similarity_boost: voiceSettings.similarity_boost || 0.75,
            style: voiceSettings.style || 0.0,
            use_speaker_boost: true
          }
        })
      }
    )

    if (!response.ok) {
      const errorText = await response.text()
      console.error('ElevenLabs API error:', response.status, errorText)
      
      // 401 Unauthorized - API 키가 유효하지 않음
      if (response.status === 401) {
        return c.json({ 
          error: 'ElevenLabs API 키가 유효하지 않습니다',
          details: `API 키를 확인해주세요.\n\n해결 방법:\n1. https://elevenlabs.io/app/settings/api-keys 에서 새 API 키 발급\n2. .dev.vars 파일의 ELEVENLABS_API_KEY 업데이트\n3. 서버 재시작: pm2 restart youtube-studio\n\nElevenLabs 오류: ${errorText}`
        }, 401)
      }
      
      // 기타 에러
      throw new Error(`ElevenLabs API error (${response.status}): ${errorText}`)
    }

    const audioBuffer = await response.arrayBuffer()
    console.log('Voice generated successfully, size:', audioBuffer.byteLength, 'bytes')
    
    return new Response(audioBuffer, {
      headers: {
        'Content-Type': 'audio/mpeg',
        'Content-Disposition': 'attachment; filename="voice.mp3"'
      }
    })
  } catch (error: any) {
    console.error('Voice generation error:', error)
    return c.json({ 
      error: '음성 생성 중 오류가 발생했습니다',
      details: error.message 
    }, 500)
  }
})

// 5. 작업 상태 확인 (폴링용)
app.get('/api/check-status/:jobId', async (c) => {
  try {
    const jobId = c.req.param('jobId')
    const job = jobStorage.get(jobId)

    if (!job) {
      return c.json({ error: '작업을 찾을 수 없습니다' }, 404)
    }

    if (job.type === 'video') {
      const replicate = new Replicate({
        auth: c.env.REPLICATE_API_TOKEN || ''
      })

      const prediction = await replicate.predictions.get(job.predictionId)

      if (prediction.status === 'succeeded') {
        jobStorage.set(jobId, {
          ...job,
          status: 'completed',
          videoUrl: prediction.output
        })

        return c.json({
          success: true,
          data: {
            status: 'completed',
            videoUrl: prediction.output,
            sceneId: job.sceneId
          }
        })
      } else if (prediction.status === 'failed') {
        return c.json({
          success: false,
          data: {
            status: 'failed',
            error: prediction.error
          }
        })
      } else {
        return c.json({
          success: true,
          data: {
            status: 'processing',
            progress: prediction.status
          }
        })
      }
    }

    return c.json({
      success: true,
      data: job
    })
  } catch (error: any) {
    console.error('Status check error:', error)
    return c.json({ 
      error: '상태 확인 중 오류가 발생했습니다',
      details: error.message 
    }, 500)
  }
})

// 메인 페이지
app.get('/', (c) => {
  return c.html(`
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>지혜스튜디오 v5.1</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/file-saver@2.0.5/dist/FileSaver.min.js"></script>
        <script src="https://unpkg.com/@ffmpeg/ffmpeg@0.12.10/dist/umd/ffmpeg.js"></script>
        <script src="https://unpkg.com/@ffmpeg/util@0.12.1/dist/umd/index.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
                color: #e0e0e0;
                font-family: 'Inter', system-ui, -apple-system, sans-serif;
            }
            .card {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
            }
            .card:hover {
                background: rgba(255, 255, 255, 0.08);
                border-color: rgba(139, 92, 246, 0.5);
            }
            .btn-primary {
                background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
            }
            .btn-primary:hover {
                background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%);
            }
            .spinner {
                border: 3px solid rgba(255, 255, 255, 0.1);
                border-top-color: #8b5cf6;
                border-radius: 50%;
                width: 30px;
                height: 30px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            .toast {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 16px 24px;
                border-radius: 8px;
                background: rgba(34, 34, 46, 0.95);
                border: 1px solid rgba(139, 92, 246, 0.5);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
                z-index: 1000;
                animation: slideIn 0.3s ease-out;
            }
            @keyframes slideIn {
                from {
                    transform: translateX(400px);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                text-align: center;
                font-size: 12px;
                color: #888;
                padding: 16px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                background: rgba(30, 30, 46, 0.95);
                backdrop-filter: blur(10px);
            }
        </style>
    </head>
    <body class="min-h-screen p-8 pb-24">
        <div id="root"></div>
        
        <script type="text/babel">
            const { useState, useEffect, useCallback } = React;

            // 스타일 프리픽스 정의 (한국 시니어 시청자 대상)
            const STYLE_PRESETS = {
                photorealistic: 'photorealistic, Korean elderly person, Asian features, Korean senior citizen, 8k, detailed, warm lighting, natural Korean environment, negative prompt: western features, caucasian, european, blonde hair, blue eyes, ',
                anime: 'Korean traditional folktale anime style, Korean characters, Asian features, Ghibli inspired, soft colors, historical Korean setting, hanbok traditional clothing, warm nostalgic atmosphere, negative prompt: western animation style, ',
                stickman: 'simple stick figure drawing, minimalist, black lines on white background, ',
                illustration: 'warm emotional digital illustration, Korean elderly, Asian features, soft pastel colors, nostalgic Korean life scene, traditional Korean elements, cozy atmosphere, negative prompt: western style, modern minimalism, ',
                custom: ''
            };

            function App() {
                // 페이지 상태
                const [currentPage, setCurrentPage] = useState('script-gen'); // 'script-gen', 'video-production'
                
                const [script, setScript] = useState('');
                const [scenes, setScenes] = useState([]);
                const [overallFeedback, setOverallFeedback] = useState('');
                const [suggestions, setSuggestions] = useState([]);
                const [loading, setLoading] = useState(false);
                const [toast, setToast] = useState(null);
                
                // 대본 생성 페이지 상태
                const [ideaKeyword, setIdeaKeyword] = useState('');
                const [draftScript, setDraftScript] = useState('');
                const [finalScript, setFinalScript] = useState('');
                const [generatingDraft, setGeneratingDraft] = useState(false);
                
                // 이미지 스타일 설정
                const [imageStyle, setImageStyle] = useState('photorealistic');
                const [customStylePrefix, setCustomStylePrefix] = useState('');
                const [aspectRatio, setAspectRatio] = useState('16:9');
                const [aiModel, setAiModel] = useState('flux-pro');

                // 설정 모달
                const [showSettings, setShowSettings] = useState(false);
                const [settingsTab, setSettingsTab] = useState('api'); // 'api' or 'voice'
                
                // API 키 설정
                const [apiKeys, setApiKeys] = useState(() => {
                    const saved = localStorage.getItem('apiKeys');
                    return saved ? JSON.parse(saved) : {
                        replicate: '',
                        elevenlabs: '',
                        gemini: ''
                    };
                });
                const [showApiKeys, setShowApiKeys] = useState({
                    replicate: false,
                    elevenlabs: false,
                    gemini: false
                });

                // 음성 설정
                const [voiceSettings, setVoiceSettings] = useState(() => {
                    const saved = localStorage.getItem('voiceSettings');
                    return saved ? JSON.parse(saved) : {
                        voiceId: '21m00Tcm4TlvDq8ikWAM',
                        stability: 0.5,
                        similarityBoost: 0.75,
                        style: 0.0
                    };
                });
                const [availableVoices, setAvailableVoices] = useState([]);
                const [loadingVoices, setLoadingVoices] = useState(false);

                // 프로젝트 저장/불러오기
                const [showProjectModal, setShowProjectModal] = useState(false);
                const [projectName, setProjectName] = useState('');
                const [savedProjects, setSavedProjects] = useState(() => {
                    const saved = localStorage.getItem('savedProjects');
                    return saved ? JSON.parse(saved) : [];
                });

                // 드래그앤드롭 상태
                const [draggedIndex, setDraggedIndex] = useState(null);

                // 캐릭터 설정
                const [characterImage, setCharacterImage] = useState(null);
                const [characterImageUrl, setCharacterImageUrl] = useState('');
                const [characterDescription, setCharacterDescription] = useState('');
                const [useCharacter, setUseCharacter] = useState(false);
                const [characterStrength, setCharacterStrength] = useState(0.7);

                // 영상 합성
                const [isComposing, setIsComposing] = useState(false);
                const [composingProgress, setComposingProgress] = useState(0);
                const [finalVideoUrl, setFinalVideoUrl] = useState('');

                // 좌측 사이드바
                const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

                // 자막 설정
                const [subtitleEnabled, setSubtitleEnabled] = useState(true);
                const [subtitleStyle, setSubtitleStyle] = useState({
                    fontSize: 24,
                    fontColor: '#FFFFFF',
                    backgroundColor: '#000000',
                    backgroundOpacity: 0.7,
                    position: 'bottom',
                    fontFamily: 'Arial'
                });
                const [showFinalVideo, setShowFinalVideo] = useState(false);

                // localStorage에 저장
                useEffect(() => {
                    localStorage.setItem('apiKeys', JSON.stringify(apiKeys));
                }, [apiKeys]);

                useEffect(() => {
                    localStorage.setItem('voiceSettings', JSON.stringify(voiceSettings));
                }, [voiceSettings]);

                useEffect(() => {
                    localStorage.setItem('subtitleSettings', JSON.stringify(subtitleStyle));
                }, [subtitleStyle]);

                useEffect(() => {
                    localStorage.setItem('subtitleEnabled', JSON.stringify(subtitleEnabled));
                }, [subtitleEnabled]);

                // 내 음성 목록 불러오기
                const loadMyVoices = async () => {
                    if (!apiKeys.elevenlabs) {
                        showToast('ElevenLabs API 키를 먼저 설정해주세요', 'error');
                        return;
                    }

                    setLoadingVoices(true);
                    try {
                        const response = await fetch('https://api.elevenlabs.io/v1/voices', {
                            headers: {
                                'xi-api-key': apiKeys.elevenlabs
                            }
                        });

                        if (response.ok) {
                            const data = await response.json();
                            setAvailableVoices(data.voices || []);
                            showToast((data.voices?.length || 0) + '개의 음성을 불러왔습니다', 'success');
                        } else {
                            throw new Error('음성 목록 불러오기 실패');
                        }
                    } catch (error) {
                        showToast('음성 목록 불러오기 실패', 'error');
                    } finally {
                        setLoadingVoices(false);
                    }
                };

                // 음성 테스트
                const testVoice = async () => {
                    if (!apiKeys.elevenlabs) {
                        showToast('ElevenLabs API 키를 먼저 설정해주세요', 'error');
                        return;
                    }

                    try {
                        showToast('음성 테스트 중...', 'info');
                        const response = await fetch('/api/generate-voice', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ 
                                text: '안녕하세요. 지혜스튜디오입니다.',
                                voiceId: voiceSettings.voiceId,
                                voiceSettings: {
                                    stability: voiceSettings.stability,
                                    similarity_boost: voiceSettings.similarityBoost,
                                    style: voiceSettings.style
                                }
                            })
                        });

                        if (response.ok) {
                            const blob = await response.blob();
                            const url = URL.createObjectURL(blob);
                            const audio = new Audio(url);
                            audio.play();
                            showToast('음성 재생 중...', 'success');
                        } else {
                            throw new Error('음성 테스트 실패');
                        }
                    } catch (error) {
                        showToast('음성 테스트 실패', 'error');
                    }
                };

                const showToast = (message, type = 'info') => {
                    setToast({ message, type });
                    setTimeout(() => setToast(null), 5000);
                };

                // 프로젝트 저장
                const saveProject = () => {
                    if (!projectName.trim()) {
                        showToast('프로젝트 이름을 입력해주세요', 'error');
                        return;
                    }

                    const project = {
                        id: Date.now(),
                        name: projectName,
                        date: new Date().toISOString(),
                        data: {
                            script,
                            scenes,
                            overallFeedback,
                            suggestions,
                            imageStyle,
                            customStylePrefix,
                            aspectRatio,
                            aiModel
                        }
                    };

                    const updated = [...savedProjects, project];
                    setSavedProjects(updated);
                    localStorage.setItem('savedProjects', JSON.stringify(updated));
                    setProjectName('');
                    setShowProjectModal(false);
                    showToast('프로젝트가 저장되었습니다', 'success');
                };

                // 프로젝트 불러오기
                const loadProject = (project) => {
                    const { data } = project;
                    setScript(data.script);
                    setScenes(data.scenes);
                    setOverallFeedback(data.overallFeedback);
                    setSuggestions(data.suggestions);
                    setImageStyle(data.imageStyle);
                    setCustomStylePrefix(data.customStylePrefix);
                    setAspectRatio(data.aspectRatio);
                    setAiModel(data.aiModel);
                    setShowProjectModal(false);
                    showToast('프로젝트가 불러와졌습니다', 'success');
                };

                // 프로젝트 삭제
                const deleteProject = (projectId) => {
                    const updated = savedProjects.filter(p => p.id !== projectId);
                    setSavedProjects(updated);
                    localStorage.setItem('savedProjects', JSON.stringify(updated));
                    showToast('프로젝트가 삭제되었습니다', 'success');
                };

                // 전체 다운로드 (ZIP)
                const downloadAllAssets = async () => {
                    if (scenes.length === 0) {
                        showToast('다운로드할 장면이 없습니다', 'error');
                        return;
                    }

                    try {
                        showToast('ZIP 파일 생성 중...', 'info');
                        const zip = new JSZip();

                        // 이미지 다운로드
                        for (const scene of scenes) {
                            if (scene.imageUrl) {
                                try {
                                    const response = await fetch(scene.imageUrl);
                                    const blob = await response.blob();
                                    zip.file(\`scene_\${scene.id}_image.jpg\`, blob);
                                } catch (error) {
                                    console.error('Image download error:', scene.id, error);
                                }
                            }
                        }

                        // 영상 다운로드
                        for (const scene of scenes) {
                            if (scene.videoUrl) {
                                try {
                                    const response = await fetch(scene.videoUrl);
                                    const blob = await response.blob();
                                    zip.file(\`scene_\${scene.id}_video.mp4\`, blob);
                                } catch (error) {
                                    console.error('Video download error:', scene.id, error);
                                }
                            }
                        }

                        // 대본 텍스트 파일
                        const scriptText = scenes.map((s, i) => \`[장면 \${i + 1}]\\n\${s.text}\\n\`).join('\\n');
                        zip.file('script.txt', scriptText);

                        // ZIP 생성 및 다운로드
                        const content = await zip.generateAsync({ type: 'blob' });
                        saveAs(content, 'jihye-studio-project.zip');
                        showToast('ZIP 파일이 다운로드되었습니다', 'success');
                    } catch (error) {
                        console.error('ZIP download error:', error);
                        showToast('ZIP 다운로드 실패', 'error');
                    }
                };

                // 이미지만 다운로드
                const downloadImages = async () => {
                    const images = scenes.filter(s => s.imageUrl);
                    if (images.length === 0) {
                        showToast('다운로드할 이미지가 없습니다', 'error');
                        return;
                    }

                    try {
                        showToast('이미지 ZIP 생성 중...', 'info');
                        const zip = new JSZip();

                        for (const scene of images) {
                            const response = await fetch(scene.imageUrl);
                            const blob = await response.blob();
                            zip.file(\`scene_\${scene.id}_image.jpg\`, blob);
                        }

                        const content = await zip.generateAsync({ type: 'blob' });
                        saveAs(content, 'jihye-studio-images.zip');
                        showToast(\`\${images.length}개 이미지 다운로드 완료\`, 'success');
                    } catch (error) {
                        showToast('이미지 다운로드 실패', 'error');
                    }
                };

                // 영상만 다운로드
                const downloadVideos = async () => {
                    const videos = scenes.filter(s => s.videoUrl);
                    if (videos.length === 0) {
                        showToast('다운로드할 영상이 없습니다', 'error');
                        return;
                    }

                    try {
                        showToast('영상 ZIP 생성 중...', 'info');
                        const zip = new JSZip();

                        for (const scene of videos) {
                            const response = await fetch(scene.videoUrl);
                            const blob = await response.blob();
                            zip.file(\`scene_\${scene.id}_video.mp4\`, blob);
                        }

                        const content = await zip.generateAsync({ type: 'blob' });
                        saveAs(content, 'jihye-studio-videos.zip');
                        showToast(\`\${videos.length}개 영상 다운로드 완료\`, 'success');
                    } catch (error) {
                        showToast('영상 다운로드 실패', 'error');
                    }
                };

                // 자막 SRT 생성 및 다운로드
                const downloadSubtitles = () => {
                    if (scenes.length === 0) {
                        showToast('자막을 생성할 장면이 없습니다', 'error');
                        return;
                    }

                    try {
                        let srtContent = '';
                        let startTime = 0;

                        scenes.forEach((scene, index) => {
                            const duration = scene.duration || 5; // 기본 5초
                            const endTime = startTime + duration;

                            srtContent += \`\${index + 1}\\n\`;
                            srtContent += \`\${formatSrtTime(startTime)} --> \${formatSrtTime(endTime)}\\n\`;
                            srtContent += \`\${scene.text}\\n\\n\`;

                            startTime = endTime;
                        });

                        const blob = new Blob([srtContent], { type: 'text/plain;charset=utf-8' });
                        saveAs(blob, 'jihye-studio-subtitles.srt');
                        showToast('자막 파일 다운로드 완료', 'success');
                    } catch (error) {
                        showToast('자막 생성 실패', 'error');
                    }
                };

                // SRT 시간 포맷 변환
                const formatSrtTime = (seconds) => {
                    const hours = Math.floor(seconds / 3600);
                    const minutes = Math.floor((seconds % 3600) / 60);
                    const secs = Math.floor(seconds % 60);
                    const ms = Math.floor((seconds % 1) * 1000);
                    
                    return \`\${String(hours).padStart(2, '0')}:\${String(minutes).padStart(2, '0')}:\${String(secs).padStart(2, '0')},\${String(ms).padStart(3, '0')}\`;
                };

                // 완성 영상 합성 (FFmpeg.wasm)
                const composeVideo = async () => {
                    // 영상 또는 이미지가 있는지 확인
                    const hasMedia = scenes.some(s => s.videoUrl || s.imageUrl);
                    if (!hasMedia) {
                        showToast('합성할 영상이나 이미지가 없습니다', 'error');
                        return;
                    }

                    try {
                        setIsComposing(true);
                        setComposingProgress(10);
                        showToast('FFmpeg 로딩 중...', 'info');

                        // FFmpeg 초기화
                        const { FFmpeg } = FFmpegWASM;
                        const { fetchFile } = FFmpegUtil;
                        const ffmpeg = new FFmpeg();

                        ffmpeg.on('progress', ({ progress }) => {
                            setComposingProgress(Math.round(progress * 100));
                        });

                        await ffmpeg.load({
                            coreURL: 'https://unpkg.com/@ffmpeg/core@0.12.6/dist/umd/ffmpeg-core.js',
                        });

                        setComposingProgress(20);
                        showToast('미디어 파일 다운로드 중...', 'info');

                        // 각 장면의 미디어 파일 준비
                        for (let i = 0; i < scenes.length; i++) {
                            const scene = scenes[i];
                            const filename = \`scene_\${i}.mp4\`;

                            if (scene.videoUrl) {
                                // 영상이 있으면 영상 사용
                                await ffmpeg.writeFile(filename, await fetchFile(scene.videoUrl));
                            } else if (scene.imageUrl) {
                                // 이미지만 있으면 이미지를 5초 영상으로 변환
                                const imgFilename = \`image_\${i}.jpg\`;
                                await ffmpeg.writeFile(imgFilename, await fetchFile(scene.imageUrl));
                                await ffmpeg.exec(['-loop', '1', '-i', imgFilename, '-t', '5', '-pix_fmt', 'yuv420p', filename]);
                            }

                            setComposingProgress(20 + (i / scenes.length) * 40);
                        }

                        setComposingProgress(60);
                        showToast('영상 합성 중...', 'info');

                        // concat 파일 생성
                        let concatContent = '';
                        for (let i = 0; i < scenes.length; i++) {
                            concatContent += \`file 'scene_\${i}.mp4'\\n\`;
                        }
                        await ffmpeg.writeFile('concat.txt', concatContent);

                        // 영상 합치기
                        await ffmpeg.exec(['-f', 'concat', '-safe', '0', '-i', 'concat.txt', '-c', 'copy', 'output.mp4']);

                        setComposingProgress(90);
                        showToast('최종 영상 생성 중...', 'info');

                        // 결과 파일 읽기
                        const data = await ffmpeg.readFile('output.mp4');
                        const blob = new Blob([data.buffer], { type: 'video/mp4' });
                        const url = URL.createObjectURL(blob);

                        setFinalVideoUrl(url);
                        setShowFinalVideo(true);
                        setComposingProgress(100);
                        showToast('완성 영상이 생성되었습니다!', 'success');
                    } catch (error) {
                        console.error('Video composition error:', error);
                        showToast('영상 합성 실패: ' + error.message, 'error');
                    } finally {
                        setIsComposing(false);
                    }
                };

                // 드래그앤드롭 핸들러
                const handleDragStart = (index) => {
                    setDraggedIndex(index);
                };

                const handleDragOver = (e, index) => {
                    e.preventDefault();
                    if (draggedIndex === null || draggedIndex === index) return;

                    const newScenes = [...scenes];
                    const draggedScene = newScenes[draggedIndex];
                    newScenes.splice(draggedIndex, 1);
                    newScenes.splice(index, 0, draggedScene);

                    setScenes(newScenes);
                    setDraggedIndex(index);
                };

                const handleDragEnd = () => {
                    setDraggedIndex(null);
                };

                // 캐릭터 이미지 업로드
                const handleCharacterImageUpload = (e) => {
                    const file = e.target.files[0];
                    if (!file) return;

                    // 이미지 파일 체크
                    if (!file.type.startsWith('image/')) {
                        showToast('이미지 파일만 업로드 가능합니다', 'error');
                        return;
                    }

                    // 파일 크기 체크 (10MB)
                    if (file.size > 10 * 1024 * 1024) {
                        showToast('파일 크기는 10MB 이하여야 합니다', 'error');
                        return;
                    }

                    const reader = new FileReader();
                    reader.onload = (event) => {
                        setCharacterImageUrl(event.target.result);
                        setCharacterImage(file);
                        showToast('캐릭터 이미지가 업로드되었습니다', 'success');
                    };
                    reader.readAsDataURL(file);
                };

                // 캐릭터 이미지 삭제
                const deleteCharacterImage = () => {
                    setCharacterImageUrl('');
                    setCharacterImage(null);
                    setUseCharacter(false);
                    showToast('캐릭터 이미지가 삭제되었습니다', 'success');
                };

                // 검수 대본 생성
                const generateDraftScript = async () => {
                    if (!ideaKeyword.trim()) {
                        showToast('주제나 키워드를 입력해주세요', 'error');
                        return;
                    }

                    if (!apiKeys.gemini) {
                        showToast('Gemini API 키를 먼저 설정해주세요. 좌측 하단 설정 버튼을 클릭하세요.', 'error');
                        return;
                    }

                    setGeneratingDraft(true);
                    try {
                        const response = await fetch('/api/generate-draft-script', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ keyword: ideaKeyword, geminiApiKey: apiKeys.gemini })
                        });

                        const result = await response.json();
                        
                        if (result.success) {
                            setDraftScript(result.data.script);
                            setFinalScript(result.data.script);
                            showToast('검수 대본이 생성되었습니다!', 'success');
                        } else {
                            showToast(result.error || '대본 생성 실패', 'error');
                        }
                    } catch (error) {
                        console.error('Draft script generation error:', error);
                        showToast('서버 연결 오류', 'error');
                    } finally {
                        setGeneratingDraft(false);
                    }
                };

                // 최종 대본 적용 (영상 제작 페이지로 이동)
                const applyFinalScript = () => {
                    setScript(finalScript);
                    setCurrentPage('video-production');
                    showToast('대본이 영상 제작 페이지에 적용되었습니다', 'success');
                };

                const analyzeScript = async () => {
                    if (!script.trim()) {
                        showToast('대본을 입력해주세요', 'error');
                        return;
                    }

                    if (!apiKeys.gemini) {
                        showToast('Gemini API 키를 먼저 설정해주세요. 좌측 하단 설정 버튼을 클릭하세요.', 'error');
                        return;
                    }

                    setLoading(true);
                    try {
                        const response = await fetch('/api/analyze-script', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ script, geminiApiKey: apiKeys.gemini })
                        });

                        const result = await response.json();
                        
                        if (result.success) {
                            setScenes(result.data.scenes.map(scene => ({
                                ...scene,
                                imageUrl: null,
                                videoUrl: null,
                                imageLoading: false,
                                videoLoading: false,
                                videoJobId: null
                            })));
                            setOverallFeedback(result.data.overallFeedback);
                            setSuggestions(result.data.suggestions || []);
                            showToast('대본 분석이 완료되었습니다!', 'success');
                        } else {
                            showToast(result.error || '분석 실패', 'error');
                        }
                    } catch (error) {
                        showToast('서버 연결 오류', 'error');
                        console.error(error);
                    } finally {
                        setLoading(false);
                    }
                };

                const generateImage = async (sceneId) => {
                    const scene = scenes.find(s => s.id === sceneId);
                    if (!scene) return;

                    if (!apiKeys.replicate) {
                        showToast('Replicate API 키를 먼저 설정해주세요. 좌측 하단 설정 버튼을 클릭하세요.', 'error');
                        return;
                    }

                    setScenes(prev => prev.map(s => 
                        s.id === sceneId ? { ...s, imageLoading: true } : s
                    ));

                    try {
                        // 스타일 프리픽스 결정
                        const stylePrefix = imageStyle === 'custom' 
                            ? customStylePrefix 
                            : STYLE_PRESETS[imageStyle];

                        const response = await fetch('/api/generate-image', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ 
                                prompt: scene.imagePrompt,
                                sceneId,
                                stylePrefix,
                                aspectRatio,
                                model: aiModel,
                                replicateApiKey: apiKeys.replicate,
                                ...(useCharacter && characterImageUrl && {
                                    characterImage: characterImageUrl,
                                    characterDescription,
                                    characterStrength
                                })
                            })
                        });

                        const result = await response.json();
                        
                        if (result.success) {
                            setScenes(prev => prev.map(s => 
                                s.id === sceneId ? { ...s, imageUrl: result.data.imageUrl, imageLoading: false } : s
                            ));
                            showToast(\`이미지 생성 완료! (\${result.data.generationTime}초 소요)\`, 'success');
                        } else {
                            throw new Error(result.error);
                        }
                    } catch (error) {
                        showToast('이미지 생성 실패', 'error');
                        setScenes(prev => prev.map(s => 
                            s.id === sceneId ? { ...s, imageLoading: false } : s
                        ));
                    }
                };

                const generateAllImages = async () => {
                    for (const scene of scenes) {
                        if (!scene.imageUrl) {
                            await generateImage(scene.id);
                            await new Promise(resolve => setTimeout(resolve, 1000));
                        }
                    }
                };

                const generateVideo = async (sceneId) => {
                    const scene = scenes.find(s => s.id === sceneId);
                    if (!scene || !scene.imageUrl) {
                        showToast('먼저 이미지를 생성해주세요', 'warning');
                        return;
                    }

                    if (!apiKeys.replicate) {
                        showToast('Replicate API 키를 먼저 설정해주세요. 좌측 하단 설정 버튼을 클릭하세요.', 'error');
                        return;
                    }

                    setScenes(prev => prev.map(s => 
                        s.id === sceneId ? { ...s, videoLoading: true } : s
                    ));

                    try {
                        const response = await fetch('/api/generate-video', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ 
                                imageUrl: scene.imageUrl,
                                prompt: scene.text,
                                sceneId,
                                replicateApiKey: apiKeys.replicate
                            })
                        });

                        const result = await response.json();
                        
                        if (result.success) {
                            setScenes(prev => prev.map(s => 
                                s.id === sceneId ? { ...s, videoJobId: result.data.jobId } : s
                            ));
                            showToast('영상 생성이 시작되었습니다 (2-5분 소요)', 'info');
                            pollVideoStatus(result.data.jobId, sceneId);
                        } else {
                            throw new Error(result.error);
                        }
                    } catch (error) {
                        showToast('영상 생성 시작 실패', 'error');
                        setScenes(prev => prev.map(s => 
                            s.id === sceneId ? { ...s, videoLoading: false } : s
                        ));
                    }
                };

                const pollVideoStatus = async (jobId, sceneId) => {
                    const interval = setInterval(async () => {
                        try {
                            const response = await fetch(\`/api/check-status/\${jobId}\`);
                            const result = await response.json();

                            if (result.success && result.data.status === 'completed') {
                                setScenes(prev => prev.map(s => 
                                    s.id === sceneId ? { 
                                        ...s, 
                                        videoUrl: result.data.videoUrl, 
                                        videoLoading: false,
                                        videoJobId: null
                                    } : s
                                ));
                                showToast('영상 생성 완료!', 'success');
                                clearInterval(interval);
                            } else if (result.data.status === 'failed') {
                                showToast('영상 생성 실패', 'error');
                                setScenes(prev => prev.map(s => 
                                    s.id === sceneId ? { ...s, videoLoading: false, videoJobId: null } : s
                                ));
                                clearInterval(interval);
                            }
                        } catch (error) {
                            console.error('Polling error:', error);
                        }
                    }, 10000); // 10초마다 체크
                };

                const generateVoice = async () => {
                    const fullScript = scenes.map(s => s.text).join(' ');
                    
                    if (!fullScript) {
                        showToast('장면이 없습니다', 'warning');
                        return;
                    }

                    if (!apiKeys.elevenlabs) {
                        showToast('ElevenLabs API 키를 먼저 설정해주세요. 좌측 하단 설정 버튼을 클릭하세요.', 'error');
                        return;
                    }

                    try {
                        showToast('음성 생성 중...', 'info');
                        const response = await fetch('/api/generate-voice', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ 
                                text: fullScript,
                                voiceId: voiceSettings.voiceId,
                                voiceSettings: {
                                    stability: voiceSettings.stability,
                                    similarity_boost: voiceSettings.similarityBoost,
                                    style: voiceSettings.style
                                },
                                elevenlabsApiKey: apiKeys.elevenlabs
                            })
                        });

                        if (response.ok) {
                            const blob = await response.blob();
                            const url = URL.createObjectURL(blob);
                            const a = document.createElement('a');
                            a.href = url;
                            a.download = 'voice.mp3';
                            a.click();
                            showToast('음성 파일이 다운로드되었습니다!', 'success');
                        } else {
                            throw new Error('Voice generation failed');
                        }
                    } catch (error) {
                        showToast('음성 생성 실패', 'error');
                    }
                };

                return (
                    <div className="max-w-7xl mx-auto">
                        {/* Toast */}
                        {toast && (
                            <div className={\`toast \${toast.type === 'error' ? 'border-red-500' : toast.type === 'success' ? 'border-green-500' : 'border-purple-500'}\`}>
                                <div className="flex items-center gap-3">
                                    <i className={\`fas fa-\${toast.type === 'error' ? 'exclamation-circle text-red-400' : toast.type === 'success' ? 'check-circle text-green-400' : 'info-circle text-purple-400'}\`}></i>
                                    <span>{toast.message}</span>
                                </div>
                            </div>
                        )}

                        {/* 좌측 사이드바 */}
                        <div className={'fixed left-0 top-0 h-screen bg-gradient-to-b from-gray-900 to-gray-950 border-r border-gray-800 transition-all duration-300 z-50 flex flex-col ' + (sidebarCollapsed ? 'w-16' : 'w-64')}>
                            {/* 사이드바 헤더 */}
                            <div className="p-4 border-b border-gray-800 flex items-center justify-between flex-shrink-0">
                                {!sidebarCollapsed && (
                                    <div className="flex items-center gap-2">
                                        <i className="fas fa-video text-purple-400 text-xl"></i>
                                        <span className="font-bold text-white">지혜스튜디오</span>
                                    </div>
                                )}
                                <button
                                    onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
                                    className="text-gray-400 hover:text-white transition-all p-2"
                                >
                                    <i className={'fas fa-' + (sidebarCollapsed ? 'angle-right' : 'angle-left')}></i>
                                </button>
                            </div>

                            {/* 메뉴 항목 */}
                            <div className="p-4 space-y-2 flex-1 overflow-y-auto">
                                {[
                                    { icon: 'file-alt', label: '대본 생성', id: 'script-gen', page: 'script-gen' },
                                    { icon: 'magic', label: '제목/내용 생성', id: 'title-gen', page: 'title-gen' },
                                    { icon: 'film', label: '영상 제작', id: 'video-production', page: 'video-production' },
                                    { icon: 'image', label: '썸네일 제작', id: 'thumbnail', page: 'thumbnail' },
                                    { icon: 'palette', label: '비주얼 프롬프트', id: 'visual-prompt', page: 'visual-prompt' }
                                ].map(item => (
                                    <button
                                        key={item.id}
                                        onClick={() => setCurrentPage(item.page)}
                                        className={'w-full text-left p-3 rounded-lg transition-all flex items-center gap-3 ' + (currentPage === item.page ? 'bg-purple-600 text-white' : 'text-gray-300 hover:text-white hover:bg-gray-800/50')}
                                        title={item.label}
                                    >
                                        <i className={'fas fa-' + item.icon + ' text-lg'}></i>
                                        {!sidebarCollapsed && <span>{item.label}</span>}
                                    </button>
                                ))}
                            </div>

                            {/* 하단 고정 버튼들 */}
                            <div className="p-4 border-t border-gray-800 bg-gray-900 space-y-2 flex-shrink-0">
                                {/* 새 창 열기 */}
                                <button
                                    onClick={() => {
                                        if (confirm('현재 작업을 초기화하고 새 프로젝트를 시작하시겠습니까?')) {
                                            setScript('');
                                            setScenes([]);
                                            setOverallFeedback('');
                                            setSuggestions([]);
                                            setFinalVideoUrl('');
                                            setIdeaKeyword('');
                                            setDraftScript('');
                                            setFinalScript('');
                                            setCurrentPage('script-gen');
                                            showToast('새 프로젝트가 시작되었습니다', 'success');
                                        }
                                    }}
                                    className="w-full bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-700 hover:to-emerald-700 text-white p-3 rounded-lg font-semibold transition-all flex items-center justify-center gap-2"
                                    title="새 창 열기"
                                >
                                    <i className="fas fa-plus-circle text-lg"></i>
                                    {!sidebarCollapsed && <span>새 창 열기</span>}
                                </button>

                                {/* 설정 */}
                                <button
                                    onClick={(e) => {
                                        e.preventDefault();
                                        e.stopPropagation();
                                        console.log('설정 버튼 클릭됨, showSettings를 true로 설정');
                                        setShowSettings(true);
                                    }}
                                    className="w-full bg-gray-700 hover:bg-gray-600 text-white p-3 rounded-lg font-semibold transition-all flex items-center justify-center gap-2"
                                    title="설정"
                                >
                                    <i className="fas fa-cog text-lg"></i>
                                    {!sidebarCollapsed && <span>설정</span>}
                                </button>

                                {/* 브라우저로 열기 */}
                                <button
                                    onClick={() => window.open(window.location.href, '_blank')}
                                    className="w-full bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white p-3 rounded-lg font-semibold transition-all flex items-center justify-center gap-2"
                                    title="브라우저로 열기"
                                >
                                    <i className="fas fa-external-link-alt text-lg"></i>
                                    {!sidebarCollapsed && <span>브라우저로 열기</span>}
                                </button>
                            </div>
                        </div>

                        {/* 메인 컨텐츠 (사이드바만큼 왼쪽 마진 추가) */}
                        <div className={'transition-all duration-300 min-h-screen p-6 ' + (sidebarCollapsed ? 'ml-16' : 'ml-64')}>
                            {/* Header */}
                            <div className="text-center mb-8 relative">
                                <h1 className="text-5xl font-bold mb-3 bg-gradient-to-r from-purple-400 to-indigo-400 bg-clip-text text-transparent">
                                    <i className="fas fa-video mr-3"></i>
                                    지혜스튜디오 v5.1
                                </h1>
                                <p className="text-gray-400">AI 기반 유튜브 영상 제작 솔루션</p>
                                
                                {/* 상단 버튼들 */}
                                <div className="absolute top-0 right-0 flex gap-2">
                                    {/* 프로젝트 저장 버튼 */}
                                    <button
                                        onClick={() => setShowProjectModal(true)}
                                        className="bg-gray-800 hover:bg-gray-700 text-white p-3 rounded-lg transition-all"
                                        title="프로젝트 관리"
                                    >
                                        <i className="fas fa-folder text-xl"></i>
                                    </button>
                                </div>
                            </div>

                        {/* 페이지 컨텐츠 */}
                        {currentPage === 'script-gen' && (
                            <>
                                {/* 대본 생성 페이지 */}
                                <div className="card rounded-xl p-6 mb-6">
                                    <h2 className="text-2xl font-bold mb-6 flex items-center gap-2">
                                        <i className="fas fa-lightbulb text-yellow-400"></i>
                                        1단계: 아이디어 확산 (검수 대본)
                                    </h2>
                                    
                                    <div className="mb-4">
                                        <label className="block text-sm font-semibold mb-2 text-gray-300">
                                            주제 / 키워드
                                        </label>
                                        <input
                                            type="text"
                                            value={ideaKeyword}
                                            onChange={(e) => setIdeaKeyword(e.target.value)}
                                            placeholder="예: 워렌 버핏의 투자 철학, 조선왕조실록 미스터리"
                                            className="w-full p-4 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 placeholder-gray-500 focus:outline-none focus:border-purple-500"
                                        />
                                    </div>

                                    <button
                                        onClick={generateDraftScript}
                                        disabled={generatingDraft || !ideaKeyword.trim()}
                                        className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white py-4 rounded-lg font-bold text-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                    >
                                        {generatingDraft ? (
                                            <>
                                                <i className="fas fa-spinner fa-spin mr-2"></i>
                                                검수 대본 생성 중...
                                            </>
                                        ) : (
                                            <>
                                                <i className="fas fa-magic mr-2"></i>
                                                검수 대본 생성
                                            </>
                                        )}
                                    </button>
                                </div>

                                {draftScript && (
                                    <div className="card rounded-xl p-6 mb-6">
                                        <h2 className="text-2xl font-bold mb-6 flex items-center gap-2">
                                            <i className="fas fa-file-alt text-green-400"></i>
                                            2단계: 시나리오 완성 (최종 대본)
                                        </h2>
                                        
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                검수 대본 (수정 가능)
                                            </label>
                                            <textarea
                                                value={finalScript}
                                                onChange={(e) => setFinalScript(e.target.value)}
                                                className="w-full p-4 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500 min-h-[400px]"
                                                placeholder="생성된 대본을 수정하세요..."
                                            />
                                        </div>

                                        <button
                                            onClick={applyFinalScript}
                                            disabled={!finalScript.trim()}
                                            className="w-full bg-gradient-to-r from-green-600 to-teal-600 hover:from-green-700 hover:to-teal-700 text-white py-4 rounded-lg font-bold text-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                        >
                                            <i className="fas fa-check mr-2"></i>
                                            영상 제작으로 이동
                                        </button>
                                    </div>
                                )}
                            </>
                        )}

                        {/* 제목/내용 생성 페이지 */}
                        {currentPage === 'title-gen' && (
                            <>
                                <div className="card rounded-xl p-6 mb-6">
                                    <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
                                        <i className="fas fa-magic text-purple-400"></i>
                                        유튜브 성장 전략 (Growth Hacker)
                                    </h2>
                                    <p className="text-gray-400 mb-6">
                                        알고리즘이 사랑하는 제목, 설명, 썸네일 전략을 제안받으세요.
                                    </p>

                                    {/* 분석 대상 상태 박스 */}
                                    <div className="mb-6 p-4 bg-gray-800 rounded-lg border-2 border-gray-700">
                                        <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
                                            <i className="fas fa-file-alt text-blue-400"></i>
                                            분석 대상
                                        </h3>
                                        {!script || script.trim() === '' ? (
                                            <div className="text-center py-8">
                                                <i className="fas fa-exclamation-triangle text-yellow-500 text-4xl mb-3"></i>
                                                <p className="text-gray-400 text-lg">
                                                    분석할 대본이 없습니다. 대본을 먼저 생성하세요.
                                                </p>
                                                <button
                                                    onClick={() => setCurrentPage('script-gen')}
                                                    className="mt-4 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white py-2 px-6 rounded-lg font-semibold transition-all"
                                                >
                                                    <i className="fas fa-arrow-left mr-2"></i>
                                                    대본 생성으로 이동
                                                </button>
                                            </div>
                                        ) : (
                                            <div>
                                                <div className="flex items-center gap-2 mb-2">
                                                    <i className="fas fa-check-circle text-green-500"></i>
                                                    <span className="text-green-500 font-semibold">대본이 준비되었습니다</span>
                                                </div>
                                                <div className="bg-gray-900/50 p-4 rounded-lg max-h-40 overflow-y-auto">
                                                    <p className="text-gray-300 text-sm whitespace-pre-wrap">
                                                        {script.substring(0, 200)}...
                                                    </p>
                                                </div>
                                                <p className="text-gray-500 text-sm mt-2">
                                                    총 {script.length}자
                                                </p>
                                            </div>
                                        )}
                                    </div>

                                    {/* 전략 분석 버튼 */}
                                    <button
                                        onClick={() => {
                                            if (!script || script.trim() === '') {
                                                showToast('대본을 먼저 생성해주세요', 'error');
                                                return;
                                            }
                                            showToast('전략 분석 기능은 곧 제공됩니다', 'info');
                                        }}
                                        disabled={!script || script.trim() === ''}
                                        className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white py-4 rounded-lg font-bold text-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                                    >
                                        <i className="fas fa-rocket mr-2"></i>
                                        전략 분석 및 메타데이터 생성 시작
                                    </button>
                                </div>

                                {/* 분석 결과 섹션 (추후 구현) */}
                                <div className="card rounded-xl p-6">
                                    <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                                        <i className="fas fa-chart-line text-green-400"></i>
                                        분석 결과
                                    </h3>
                                    <div className="text-center py-12 text-gray-500">
                                        <i className="fas fa-hourglass-half text-4xl mb-3"></i>
                                        <p>전략 분석 버튼을 클릭하여 시작하세요</p>
                                    </div>
                                </div>
                            </>
                        )}

                        {currentPage === 'video-production' && (
                            <>
                        {/* 상단 액션 버튼 */}
                        <div className="flex gap-3 mb-6">
                            <button
                                onClick={() => {
                                    // 직접 첨부 기능 (추후 구현)
                                    showToast('직접 첨부 기능은 곧 제공됩니다', 'info');
                                }}
                                className="flex-1 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white py-3 px-6 rounded-lg font-bold transition-all"
                            >
                                <i className="fas fa-upload mr-2"></i>
                                ✨ 직접 첨부
                            </button>
                            <button
                                onClick={() => {
                                    if (confirm('모든 작업 내용을 초기화하시겠습니까?')) {
                                        setScript('');
                                        setScenes([]);
                                        setOverallFeedback('');
                                        setSuggestions([]);
                                        setFinalVideoUrl('');
                                        showToast('초기화되었습니다', 'success');
                                    }
                                }}
                                className="bg-red-600 hover:bg-red-700 text-white py-3 px-6 rounded-lg font-bold transition-all"
                            >
                                <i className="fas fa-redo mr-2"></i>
                                🔄 초기화
                            </button>
                        </div>

                        {/* 최종 대본 입력 */}
                        <div className="card rounded-xl p-6 mb-6">
                            <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                                <i className="fas fa-file-alt text-purple-400"></i>
                                최종 대본
                            </h2>
                            <textarea
                                value={script}
                                onChange={(e) => setScript(e.target.value)}
                                className="w-full p-4 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500 min-h-[200px]"
                                placeholder="[대본 생성] 탭에서 만든 대본을 적용하거나 직접 입력하세요."
                            />
                        </div>

                        {/* Image Style Settings */}
                        <div className="card rounded-xl p-6 mb-6">
                            <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                                <i className="fas fa-palette text-purple-400"></i>
                                이미지 스타일 설정
                            </h2>
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                {/* 스타일 선택 */}
                                <div>
                                    <label className="block text-sm font-semibold mb-2 text-gray-300">
                                        <i className="fas fa-brush mr-2"></i>스타일
                                    </label>
                                    <select
                                        value={imageStyle}
                                        onChange={(e) => setImageStyle(e.target.value)}
                                        className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                    >
                                        <option value="photorealistic">🎬 실사 (Photorealistic)</option>
                                        <option value="anime">🎨 애니메이션 (Anime/Cartoon)</option>
                                        <option value="stickman">✏️ 스틱맨 (Simple Stickman)</option>
                                        <option value="illustration">🖼️ 일러스트 (Illustration)</option>
                                        <option value="custom">⚙️ 커스텀 (직접 입력)</option>
                                    </select>
                                </div>

                                {/* 비율 선택 */}
                                <div>
                                    <label className="block text-sm font-semibold mb-2 text-gray-300">
                                        <i className="fas fa-crop-alt mr-2"></i>이미지 비율
                                    </label>
                                    <select
                                        value={aspectRatio}
                                        onChange={(e) => setAspectRatio(e.target.value)}
                                        className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                    >
                                        <option value="16:9">16:9 (가로)</option>
                                        <option value="9:16">9:16 (세로)</option>
                                        <option value="1:1">1:1 (정사각형)</option>
                                        <option value="4:3">4:3 (클래식)</option>
                                        <option value="3:4">3:4 (포트레이트)</option>
                                    </select>
                                </div>

                                {/* AI 모델 선택 */}
                                <div>
                                    <label className="block text-sm font-semibold mb-2 text-gray-300">
                                        <i className="fas fa-robot mr-2"></i>AI 모델
                                    </label>
                                    <select
                                        value={aiModel}
                                        onChange={(e) => setAiModel(e.target.value)}
                                        className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                    >
                                        <option value="nanobanana-pro">🌟 Nanobanana Pro (고품질 실사 + 캐릭터)</option>
                                        <option value="nanobanana">📸 Nanobanana (실사 + 캐릭터)</option>
                                        <option value="flux-pro">🏆 FLUX 1.1 Pro (최고 품질)</option>
                                        <option value="flux-dev">💎 FLUX Dev (고품질 무료)</option>
                                        <option value="flux-schnell">⚡ FLUX Schnell (빠름)</option>
                                        <option value="recraft-v3">✨ Recraft V3 (초고품질)</option>
                                    </select>
                                </div>
                            </div>

                            {/* 커스텀 스타일 입력 */}
                            {imageStyle === 'custom' && (
                                <div className="mt-4">
                                    <label className="block text-sm font-semibold mb-2 text-gray-300">
                                        <i className="fas fa-code mr-2"></i>커스텀 스타일 프롬프트 프리픽스
                                    </label>
                                    <input
                                        type="text"
                                        value={customStylePrefix}
                                        onChange={(e) => setCustomStylePrefix(e.target.value)}
                                        placeholder="예: watercolor painting, soft colors, artistic, "
                                        className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                    />
                                    <p className="text-xs text-gray-500 mt-2">
                                        💡 팁: 이 텍스트가 AI 생성 프롬프트 앞에 붙습니다. 끝에 쉼표와 공백을 추가하세요.
                                    </p>
                                </div>
                            )}

                            {/* 캐릭터 설정 */}
                            <div className="mt-6 p-4 bg-gray-800/50 rounded-lg border border-gray-700">
                                <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                                    <i className="fas fa-user-circle text-blue-400"></i>
                                    캐릭터 일관성 설정
                                    {(aiModel === 'nanobanana' || aiModel === 'nanobanana-pro') && (
                                        <span className="text-xs bg-blue-500/20 text-blue-300 px-2 py-1 rounded">지원됨</span>
                                    )}
                                </h3>

                                {/* 캐릭터 이미지 업로드 */}
                                <div className="mb-4">
                                    <label className="block text-sm font-semibold mb-2 text-gray-300">
                                        <i className="fas fa-upload mr-2"></i>캐릭터 참조 이미지
                                    </label>
                                    
                                    {characterImageUrl ? (
                                        <div className="flex gap-4 items-start">
                                            <div className="w-32 h-32 rounded-lg overflow-hidden border-2 border-purple-500">
                                                <img src={characterImageUrl} alt="Character" className="w-full h-full object-cover" />
                                            </div>
                                            <div className="flex-1">
                                                <button
                                                    onClick={deleteCharacterImage}
                                                    className="bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-lg font-semibold transition-all mb-2"
                                                >
                                                    <i className="fas fa-trash mr-2"></i>
                                                    캐릭터 삭제
                                                </button>
                                                <p className="text-sm text-gray-400">
                                                    <i className="fas fa-check-circle text-green-400 mr-1"></i>
                                                    캐릭터 이미지가 업로드되었습니다
                                                </p>
                                            </div>
                                        </div>
                                    ) : (
                                        <label className="block cursor-pointer">
                                            <input
                                                type="file"
                                                accept="image/*"
                                                onChange={handleCharacterImageUpload}
                                                className="hidden"
                                            />
                                            <div className="border-2 border-dashed border-gray-600 rounded-lg p-8 text-center hover:border-purple-500 transition-all">
                                                <i className="fas fa-cloud-upload-alt text-4xl text-gray-500 mb-2"></i>
                                                <p className="text-gray-400">클릭하여 캐릭터 이미지 업로드</p>
                                                <p className="text-xs text-gray-600 mt-1">PNG, JPG (최대 10MB)</p>
                                            </div>
                                        </label>
                                    )}
                                </div>

                                {/* 캐릭터 설명 */}
                                <div className="mb-4">
                                    <label className="block text-sm font-semibold mb-2 text-gray-300">
                                        <i className="fas fa-comment-dots mr-2"></i>캐릭터 설명 (선택)
                                    </label>
                                    <input
                                        type="text"
                                        value={characterDescription}
                                        onChange={(e) => setCharacterDescription(e.target.value)}
                                        placeholder="예: 60대 한국 할아버지, 흰머리, 안경"
                                        className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                    />
                                    <p className="text-xs text-gray-500 mt-2">
                                        💡 캐릭터의 특징을 설명하면 더 정확한 결과를 얻을 수 있습니다
                                    </p>
                                </div>

                                {/* 캐릭터 일관성 강도 */}
                                {characterImageUrl && (
                                    <>
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-sliders-h mr-2"></i>일관성 강도: {characterStrength.toFixed(2)}
                                            </label>
                                            <input
                                                type="range"
                                                min="0"
                                                max="1"
                                                step="0.05"
                                                value={characterStrength}
                                                onChange={(e) => setCharacterStrength(parseFloat(e.target.value))}
                                                className="w-full"
                                            />
                                            <div className="flex justify-between text-xs text-gray-500 mt-1">
                                                <span>낮음 (자유로움)</span>
                                                <span>높음 (정확함)</span>
                                            </div>
                                        </div>

                                        {/* 캐릭터 사용 체크박스 */}
                                        <div className="flex items-center gap-2">
                                            <input
                                                type="checkbox"
                                                id="useCharacter"
                                                checked={useCharacter}
                                                onChange={(e) => setUseCharacter(e.target.checked)}
                                                className="w-4 h-4"
                                            />
                                            <label htmlFor="useCharacter" className="text-sm text-gray-300 cursor-pointer">
                                                <i className="fas fa-magic mr-2 text-purple-400"></i>
                                                모든 장면에 이 캐릭터 사용
                                            </label>
                                        </div>

                                        {/* 모델 지원 안내 */}
                                        {(aiModel !== 'nanobanana' && aiModel !== 'nanobanana-pro') && (
                                            <div className="mt-3 p-3 bg-yellow-900/20 border border-yellow-700/50 rounded-lg">
                                                <p className="text-yellow-300 text-sm">
                                                    <i className="fas fa-exclamation-triangle mr-2"></i>
                                                    현재 선택된 모델은 캐릭터 일관성을 완벽히 지원하지 않습니다. Nanobanana 또는 Nanobanana Pro 모델을 사용하세요.
                                                </p>
                                            </div>
                                        )}
                                    </>
                                )}
                            </div>

                            {/* 자막 설정 */}
                            <div className="mt-6 p-4 bg-gray-800/50 rounded-lg border border-gray-700">
                                <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                                    <i className="fas fa-closed-captioning text-green-400"></i>
                                    자막 설정
                                </h3>

                                {/* 자막 사용 여부 */}
                                <div className="mb-4 flex items-center gap-2">
                                    <input
                                        type="checkbox"
                                        id="subtitleEnabled"
                                        checked={subtitleEnabled}
                                        onChange={(e) => setSubtitleEnabled(e.target.checked)}
                                        className="w-4 h-4"
                                    />
                                    <label htmlFor="subtitleEnabled" className="text-sm text-gray-300 cursor-pointer">
                                        <i className="fas fa-eye mr-2 text-green-400"></i>
                                        자막 사용
                                    </label>
                                </div>

                                {subtitleEnabled && (
                                    <>
                                        {/* 폰트 크기 */}
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-text-height mr-2"></i>폰트 크기: {subtitleStyle.fontSize}px
                                            </label>
                                            <input
                                                type="range"
                                                min="16"
                                                max="48"
                                                step="2"
                                                value={subtitleStyle.fontSize}
                                                onChange={(e) => setSubtitleStyle({...subtitleStyle, fontSize: parseInt(e.target.value)})}
                                                className="w-full"
                                            />
                                            <div className="flex justify-between text-xs text-gray-500 mt-1">
                                                <span>작음</span>
                                                <span>큼</span>
                                            </div>
                                        </div>

                                        {/* 폰트 색상 */}
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-palette mr-2"></i>폰트 색상
                                            </label>
                                            <div className="flex gap-2 items-center">
                                                <input
                                                    type="color"
                                                    value={subtitleStyle.fontColor}
                                                    onChange={(e) => setSubtitleStyle({...subtitleStyle, fontColor: e.target.value})}
                                                    className="w-12 h-12 rounded cursor-pointer"
                                                />
                                                <input
                                                    type="text"
                                                    value={subtitleStyle.fontColor}
                                                    onChange={(e) => setSubtitleStyle({...subtitleStyle, fontColor: e.target.value})}
                                                    className="flex-1 p-2 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                                />
                                            </div>
                                        </div>

                                        {/* 배경 색상 */}
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-fill mr-2"></i>배경 색상
                                            </label>
                                            <div className="flex gap-2 items-center">
                                                <input
                                                    type="color"
                                                    value={subtitleStyle.backgroundColor}
                                                    onChange={(e) => setSubtitleStyle({...subtitleStyle, backgroundColor: e.target.value})}
                                                    className="w-12 h-12 rounded cursor-pointer"
                                                />
                                                <input
                                                    type="text"
                                                    value={subtitleStyle.backgroundColor}
                                                    onChange={(e) => setSubtitleStyle({...subtitleStyle, backgroundColor: e.target.value})}
                                                    className="flex-1 p-2 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                                />
                                            </div>
                                        </div>

                                        {/* 배경 투명도 */}
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-adjust mr-2"></i>배경 투명도: {(subtitleStyle.backgroundOpacity * 100).toFixed(0)}%
                                            </label>
                                            <input
                                                type="range"
                                                min="0"
                                                max="1"
                                                step="0.1"
                                                value={subtitleStyle.backgroundOpacity}
                                                onChange={(e) => setSubtitleStyle({...subtitleStyle, backgroundOpacity: parseFloat(e.target.value)})}
                                                className="w-full"
                                            />
                                            <div className="flex justify-between text-xs text-gray-500 mt-1">
                                                <span>투명</span>
                                                <span>불투명</span>
                                            </div>
                                        </div>

                                        {/* 위치 */}
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-arrows-alt-v mr-2"></i>자막 위치
                                            </label>
                                            <select
                                                value={subtitleStyle.position}
                                                onChange={(e) => setSubtitleStyle({...subtitleStyle, position: e.target.value})}
                                                className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                            >
                                                <option value="top">상단</option>
                                                <option value="middle">중앙</option>
                                                <option value="bottom">하단</option>
                                            </select>
                                        </div>

                                        {/* 폰트 패밀리 */}
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-font mr-2"></i>폰트
                                            </label>
                                            <select
                                                value={subtitleStyle.fontFamily}
                                                onChange={(e) => setSubtitleStyle({...subtitleStyle, fontFamily: e.target.value})}
                                                className="w-full p-3 bg-gray-900/50 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                            >
                                                <option value="Arial">Arial</option>
                                                <option value="'Noto Sans KR', sans-serif">Noto Sans KR</option>
                                                <option value="'Nanum Gothic', sans-serif">나눔고딕</option>
                                                <option value="'Malgun Gothic', sans-serif">맑은 고딕</option>
                                            </select>
                                        </div>

                                        {/* 미리보기 */}
                                        <div className="p-4 bg-gray-900 rounded-lg text-center">
                                            <p className="text-xs text-gray-500 mb-2">자막 미리보기</p>
                                            <div 
                                                style={{
                                                    fontSize: subtitleStyle.fontSize + 'px',
                                                    color: subtitleStyle.fontColor,
                                                    backgroundColor: subtitleStyle.backgroundColor,
                                                    opacity: subtitleStyle.backgroundOpacity,
                                                    fontFamily: subtitleStyle.fontFamily,
                                                    padding: '8px 16px',
                                                    borderRadius: '4px',
                                                    display: 'inline-block'
                                                }}
                                            >
                                                안녕하세요. 지혜스튜디오입니다.
                                            </div>
                                        </div>
                                    </>
                                )}
                            </div>

                            {/* 현재 설정 미리보기 */}
                            <div className="mt-4 p-3 bg-purple-500/10 border border-purple-500/30 rounded-lg">
                                <p className="text-sm text-purple-300">
                                    <i className="fas fa-info-circle mr-2"></i>
                                    <strong>현재 설정:</strong> {imageStyle === 'custom' ? '커스텀' : imageStyle} 스타일, {aspectRatio} 비율, {
                                        aiModel === 'flux-1.1-pro' ? 'FLUX 1.1 Pro (최고 품질)' :
                                        aiModel === 'flux-dev' ? 'FLUX Dev (고품질)' :
                                        aiModel === 'flux-schnell' ? 'FLUX Schnell (빠름)' :
                                        aiModel === 'recraft-v3' ? 'Recraft V3 (초고품질)' :
                                        'SDXL (안정적)'
                                    } 모델
                                </p>
                            </div>
                        </div>

                        {/* Main Layout */}
                        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
                            {/* Left: Script Input */}
                            <div className="card rounded-xl p-6">
                                <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
                                    <i className="fas fa-file-alt text-purple-400"></i>
                                    대본 입력
                                </h2>
                                <textarea
                                    value={script}
                                    onChange={(e) => setScript(e.target.value)}
                                    className="w-full h-96 p-4 bg-gray-900/50 border border-gray-700 rounded-lg resize-none focus:outline-none focus:border-purple-500 text-gray-200"
                                    placeholder="유튜브 영상 대본을 입력하세요...&#10;&#10;예시:&#10;안녕하세요 여러분! 오늘은 AI 기술의 미래에 대해 이야기해보겠습니다.&#10;최근 인공지능 기술이 급속도로 발전하면서..."
                                />
                                <button
                                    onClick={analyzeScript}
                                    disabled={loading}
                                    className="w-full mt-4 btn-primary text-white py-3 px-6 rounded-lg font-semibold flex items-center justify-center gap-2 transition-all disabled:opacity-50"
                                >
                                    {loading ? (
                                        <>
                                            <div className="spinner"></div>
                                            <span>분석 중...</span>
                                        </>
                                    ) : (
                                        <>
                                            <i className="fas fa-brain"></i>
                                            <span>AI 분석 시작</span>
                                        </>
                                    )}
                                </button>
                            </div>

                            {/* Right: Feedback */}
                            <div className="card rounded-xl p-6">
                                <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
                                    <i className="fas fa-lightbulb text-yellow-400"></i>
                                    AI 피드백
                                </h2>
                                {overallFeedback ? (
                                    <div className="space-y-4">
                                        <div className="bg-gray-900/50 p-4 rounded-lg border border-gray-700">
                                            <p className="text-gray-300 leading-relaxed">{overallFeedback}</p>
                                        </div>
                                        {suggestions.length > 0 && (
                                            <div>
                                                <h3 className="font-semibold mb-2 text-purple-300">개선 제안</h3>
                                                <ul className="space-y-2">
                                                    {suggestions.map((suggestion, idx) => (
                                                        <li key={idx} className="flex items-start gap-2 text-gray-400">
                                                            <i className="fas fa-check-circle text-green-400 mt-1"></i>
                                                            <span>{suggestion}</span>
                                                        </li>
                                                    ))}
                                                </ul>
                                            </div>
                                        )}
                                    </div>
                                ) : (
                                    <div className="h-full flex items-center justify-center text-gray-500">
                                        <div className="text-center">
                                            <i className="fas fa-comments text-6xl mb-4 opacity-20"></i>
                                            <p>대본을 분석하면 AI 피드백이 표시됩니다</p>
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>

                        {/* Scenes Grid */}
                        {scenes.length > 0 && (
                            <>
                                <div className="flex justify-between items-center mb-6">
                                    <h2 className="text-2xl font-bold flex items-center gap-2">
                                        <i className="fas fa-film text-purple-400"></i>
                                        장면 목록 ({scenes.length}개)
                                    </h2>
                                    <button
                                        onClick={generateAllImages}
                                        className="btn-primary text-white py-2 px-4 rounded-lg font-semibold flex items-center gap-2 transition-all"
                                    >
                                        <i className="fas fa-images"></i>
                                        <span>전체 이미지 생성</span>
                                    </button>
                                </div>

                                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">
                                    {scenes.map((scene, index) => (
                                        <div 
                                            key={scene.id} 
                                            className={\`card rounded-xl p-4 transition-all cursor-move \${draggedIndex === index ? 'opacity-50' : ''}\`}
                                            draggable
                                            onDragStart={() => handleDragStart(index)}
                                            onDragOver={(e) => handleDragOver(e, index)}
                                            onDragEnd={handleDragEnd}
                                        >
                                            <div className="mb-3 flex justify-between items-center">
                                                <span className="bg-purple-500/20 text-purple-300 px-3 py-1 rounded-full text-sm font-semibold">
                                                    장면 {scene.id}
                                                </span>
                                                <i className="fas fa-grip-vertical text-gray-600"></i>
                                            </div>

                                            {/* Image Preview */}
                                            <div className="mb-3 bg-gray-900/50 rounded-lg aspect-video flex items-center justify-center overflow-hidden">
                                                {scene.imageLoading ? (
                                                    <div className="spinner"></div>
                                                ) : scene.imageUrl ? (
                                                    <img src={scene.imageUrl} alt={\`Scene \${scene.id}\`} className="w-full h-full object-cover" />
                                                ) : (
                                                    <i className="fas fa-image text-gray-600 text-4xl"></i>
                                                )}
                                            </div>

                                            {/* Video Preview */}
                                            {scene.videoUrl && (
                                                <div className="mb-3 bg-gray-900/50 rounded-lg aspect-video overflow-hidden">
                                                    <video src={scene.videoUrl} controls className="w-full h-full object-cover"></video>
                                                </div>
                                            )}

                                            {/* Text */}
                                            <p className="text-sm text-gray-300 mb-3 line-clamp-3">{scene.text}</p>

                                            {/* Feedback */}
                                            {scene.feedback && (
                                                <div className="mb-3 p-2 bg-yellow-500/10 border border-yellow-500/30 rounded text-xs text-yellow-300">
                                                    <i className="fas fa-exclamation-triangle mr-1"></i>
                                                    {scene.feedback}
                                                </div>
                                            )}

                                            {/* Actions */}
                                            <div className="flex gap-2">
                                                <button
                                                    onClick={() => generateImage(scene.id)}
                                                    disabled={scene.imageLoading}
                                                    className="flex-1 bg-purple-600 hover:bg-purple-700 text-white py-2 px-3 rounded-lg text-sm font-semibold transition-all disabled:opacity-50"
                                                >
                                                    <i className="fas fa-image mr-1"></i>
                                                    {scene.imageUrl ? '재생성' : '이미지 생성'}
                                                </button>
                                                <button
                                                    onClick={() => generateVideo(scene.id)}
                                                    disabled={scene.videoLoading || !scene.imageUrl}
                                                    className="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-3 rounded-lg text-sm font-semibold transition-all disabled:opacity-50"
                                                >
                                                    <i className="fas fa-video mr-1"></i>
                                                    {scene.videoLoading ? '생성 중...' : '영상 변환'}
                                                </button>
                                            </div>
                                        </div>
                                    ))}
                                </div>

                                {/* Bottom Actions */}
                                <div className="space-y-4">
                                    {/* 영상 합성 버튼 */}
                                    <div className="card rounded-xl p-6">
                                        <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                                            <i className="fas fa-film text-purple-400"></i>
                                            최종 영상 제작
                                        </h3>
                                        <button
                                            onClick={composeVideo}
                                            disabled={isComposing}
                                            className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white py-4 px-6 rounded-lg font-bold flex items-center justify-center gap-3 transition-all disabled:opacity-50 text-lg"
                                        >
                                            {isComposing ? (
                                                <>
                                                    <div className="spinner"></div>
                                                    <span>영상 합성 중... {composingProgress}%</span>
                                                </>
                                            ) : (
                                                <>
                                                    <i className="fas fa-magic"></i>
                                                    <span>🎬 완성 영상 합성하기</span>
                                                </>
                                            )}
                                        </button>
                                        {isComposing && (
                                            <div className="mt-4">
                                                <div className="w-full bg-gray-700 rounded-full h-3 overflow-hidden">
                                                    <div 
                                                        className="bg-gradient-to-r from-purple-500 to-indigo-500 h-full transition-all duration-300"
                                                        style={{ width: composingProgress + '%' }}
                                                    ></div>
                                                </div>
                                                <p className="text-sm text-gray-400 mt-2 text-center">
                                                    {composingProgress < 20 ? 'FFmpeg 초기화 중...' :
                                                     composingProgress < 60 ? '미디어 파일 준비 중...' :
                                                     composingProgress < 90 ? '영상 합성 중...' :
                                                     '최종 처리 중...'}
                                                </p>
                                            </div>
                                        )}
                                    </div>

                                    {/* 개별 다운로드 버튼들 */}
                                    <div className="card rounded-xl p-6">
                                        <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
                                            <i className="fas fa-download text-green-400"></i>
                                            개별 다운로드
                                        </h3>
                                        <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
                                            <button
                                                onClick={downloadImages}
                                                className="bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-lg font-semibold flex flex-col items-center gap-2 transition-all"
                                            >
                                                <i className="fas fa-image text-2xl"></i>
                                                <span className="text-sm">이미지</span>
                                            </button>
                                            <button
                                                onClick={downloadVideos}
                                                className="bg-indigo-600 hover:bg-indigo-700 text-white py-3 px-4 rounded-lg font-semibold flex flex-col items-center gap-2 transition-all"
                                            >
                                                <i className="fas fa-video text-2xl"></i>
                                                <span className="text-sm">영상 클립</span>
                                            </button>
                                            <button
                                                onClick={generateVoice}
                                                className="bg-purple-600 hover:bg-purple-700 text-white py-3 px-4 rounded-lg font-semibold flex flex-col items-center gap-2 transition-all"
                                            >
                                                <i className="fas fa-microphone text-2xl"></i>
                                                <span className="text-sm">음성 생성</span>
                                            </button>
                                            <button
                                                onClick={downloadSubtitles}
                                                className="bg-green-600 hover:bg-green-700 text-white py-3 px-4 rounded-lg font-semibold flex flex-col items-center gap-2 transition-all"
                                            >
                                                <i className="fas fa-closed-captioning text-2xl"></i>
                                                <span className="text-sm">자막 SRT</span>
                                            </button>
                                            <button
                                                onClick={downloadAllAssets}
                                                className="bg-gray-600 hover:bg-gray-700 text-white py-3 px-4 rounded-lg font-semibold flex flex-col items-center gap-2 transition-all"
                                            >
                                                <i className="fas fa-archive text-2xl"></i>
                                                <span className="text-sm">전체 ZIP</span>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </>
                        )}

                        {/* 완성 영상 미리보기 모달 */}
                        {showFinalVideo && (
                            <div className="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center z-50 p-4" onClick={() => setShowFinalVideo(false)}>
                                <div className="bg-gray-900 rounded-xl p-6 max-w-4xl w-full" onClick={(e) => e.stopPropagation()}>
                                    <div className="flex justify-between items-center mb-4">
                                        <h2 className="text-2xl font-bold flex items-center gap-2">
                                            <i className="fas fa-film text-purple-400"></i>
                                            완성 영상 미리보기
                                        </h2>
                                        <button
                                            onClick={() => setShowFinalVideo(false)}
                                            className="text-gray-400 hover:text-white text-2xl"
                                        >
                                            <i className="fas fa-times"></i>
                                        </button>
                                    </div>
                                    <div className="aspect-video bg-black rounded-lg overflow-hidden mb-4">
                                        <video src={finalVideoUrl} controls className="w-full h-full"></video>
                                    </div>
                                    <div className="flex gap-3">
                                        <button
                                            onClick={() => {
                                                const a = document.createElement('a');
                                                a.href = finalVideoUrl;
                                                a.download = 'jihye-studio-final-video.mp4';
                                                a.click();
                                                showToast('완성 영상 다운로드 시작', 'success');
                                            }}
                                            className="flex-1 bg-purple-600 hover:bg-purple-700 text-white py-3 px-6 rounded-lg font-semibold flex items-center justify-center gap-2 transition-all"
                                        >
                                            <i className="fas fa-download"></i>
                                            <span>영상 다운로드</span>
                                        </button>
                                        <button
                                            onClick={() => setShowFinalVideo(false)}
                                            className="bg-gray-700 hover:bg-gray-600 text-white py-3 px-6 rounded-lg font-semibold transition-all"
                                        >
                                            닫기
                                        </button>
                                    </div>
                                </div>
                            </div>
                        )}
                        
                        {/* 프로젝트 관리 모달 */}
                        {showProjectModal && (
                            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" onClick={() => setShowProjectModal(false)}>
                                <div className="bg-gray-900 rounded-xl p-6 max-w-3xl w-full mx-4 max-h-[90vh] overflow-y-auto" onClick={(e) => e.stopPropagation()}>
                                    {/* 모달 헤더 */}
                                    <div className="flex justify-between items-center mb-6">
                                        <h2 className="text-2xl font-bold flex items-center gap-2">
                                            <i className="fas fa-folder text-purple-400"></i>
                                            프로젝트 관리
                                        </h2>
                                        <button
                                            onClick={() => setShowProjectModal(false)}
                                            className="text-gray-400 hover:text-white text-2xl"
                                        >
                                            <i className="fas fa-times"></i>
                                        </button>
                                    </div>

                                    {/* 프로젝트 저장 */}
                                    <div className="mb-6 p-4 bg-gray-800 rounded-lg">
                                        <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
                                            <i className="fas fa-save text-green-400"></i>
                                            현재 프로젝트 저장
                                        </h3>
                                        <div className="flex gap-2">
                                            <input
                                                type="text"
                                                value={projectName}
                                                onChange={(e) => setProjectName(e.target.value)}
                                                placeholder="프로젝트 이름 입력..."
                                                className="flex-1 p-3 bg-gray-900 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                            />
                                            <button
                                                onClick={saveProject}
                                                className="bg-purple-600 hover:bg-purple-700 text-white py-3 px-6 rounded-lg font-semibold transition-all"
                                            >
                                                <i className="fas fa-save mr-2"></i>
                                                저장
                                            </button>
                                        </div>
                                    </div>

                                    {/* 저장된 프로젝트 목록 */}
                                    <div>
                                        <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
                                            <i className="fas fa-list text-blue-400"></i>
                                            저장된 프로젝트 ({savedProjects.length}개)
                                        </h3>
                                        {savedProjects.length === 0 ? (
                                            <div className="text-center py-8 text-gray-500">
                                                <i className="fas fa-inbox text-4xl mb-3"></i>
                                                <p>저장된 프로젝트가 없습니다</p>
                                            </div>
                                        ) : (
                                            <div className="space-y-3">
                                                {savedProjects.map((project) => (
                                                    <div key={project.id} className="bg-gray-800 rounded-lg p-4 flex justify-between items-center hover:bg-gray-700 transition-all">
                                                        <div className="flex-1">
                                                            <h4 className="font-semibold text-white mb-1">{project.name}</h4>
                                                            <p className="text-sm text-gray-400">
                                                                <i className="fas fa-calendar mr-1"></i>
                                                                {new Date(project.date).toLocaleString('ko-KR')}
                                                            </p>
                                                            <p className="text-sm text-gray-500 mt-1">
                                                                <i className="fas fa-film mr-1"></i>
                                                                {project.data.scenes.length}개 장면
                                                            </p>
                                                        </div>
                                                        <div className="flex gap-2">
                                                            <button
                                                                onClick={() => loadProject(project)}
                                                                className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg font-semibold transition-all"
                                                            >
                                                                <i className="fas fa-folder-open mr-1"></i>
                                                                불러오기
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    if (confirm('정말 삭제하시겠습니까?')) {
                                                                        deleteProject(project.id);
                                                                    }
                                                                }}
                                                                className="bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-lg font-semibold transition-all"
                                                            >
                                                                <i className="fas fa-trash"></i>
                                                            </button>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            </div>
                        )}
                        
                        </>
                        )}

                        {/* Footer */}
                        <div className="footer">
                            © 2026 지혜스튜디오랩. All Rights Reserved.
                        </div>
                        </div> {/* 메인 컨텐츠 닫기 */}

                        {/* 설정 모달 - 전체 앱에서 접근 가능 */}
                        {showSettings && (
                            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-[100]" onClick={() => setShowSettings(false)}>
                                <div className="bg-gray-900 rounded-xl p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto" onClick={(e) => e.stopPropagation()}>
                                    {/* 모달 헤더 */}
                                    <div className="flex justify-between items-center mb-6">
                                        <h2 className="text-2xl font-bold flex items-center gap-2">
                                            <i className="fas fa-cog text-purple-400"></i>
                                            설정
                                        </h2>
                                        <button
                                            onClick={() => setShowSettings(false)}
                                            className="text-gray-400 hover:text-white text-2xl"
                                        >
                                            <i className="fas fa-times"></i>
                                        </button>
                                    </div>

                                    {/* API 키 입력 섹션 */}
                                    <div className="space-y-6">
                                        <h3 className="text-lg font-semibold text-purple-300 flex items-center gap-2">
                                            <i className="fas fa-key"></i>
                                            API 키 설정
                                        </h3>

                                        {/* Gemini API */}
                                        <div>
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-brain mr-2 text-blue-400"></i>Gemini API 키
                                                {apiKeys.gemini && <i className="fas fa-check-circle text-green-400 ml-2"></i>}
                                                {!apiKeys.gemini && <i className="fas fa-times-circle text-red-400 ml-2"></i>}
                                            </label>
                                            <div className="flex gap-2">
                                                <div className="flex-1 relative">
                                                    <input
                                                        type={showApiKeys.gemini ? "text" : "password"}
                                                        value={apiKeys.gemini}
                                                        onChange={(e) => setApiKeys({...apiKeys, gemini: e.target.value})}
                                                        placeholder="AIzaSy..."
                                                        className="w-full p-3 bg-gray-800 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                                    />
                                                    <button
                                                        onClick={() => setShowApiKeys({...showApiKeys, gemini: !showApiKeys.gemini})}
                                                        className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white"
                                                    >
                                                        <i className={\`fas fa-\${showApiKeys.gemini ? 'eye-slash' : 'eye'}\`}></i>
                                                    </button>
                                                </div>
                                                <a
                                                    href="https://makersuite.google.com/app/apikey"
                                                    target="_blank"
                                                    className="bg-gray-700 hover:bg-gray-600 text-white py-3 px-4 rounded-lg font-semibold transition-all whitespace-nowrap"
                                                >
                                                    <i className="fas fa-external-link-alt mr-1"></i>
                                                    발급
                                                </a>
                                            </div>
                                            <p className="text-xs text-gray-500 mt-1">대본 분석 및 AI 피드백에 사용됩니다</p>
                                        </div>

                                        {/* Replicate API */}
                                        <div>
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-image mr-2 text-green-400"></i>Replicate API 키
                                                {apiKeys.replicate && <i className="fas fa-check-circle text-green-400 ml-2"></i>}
                                                {!apiKeys.replicate && <i className="fas fa-times-circle text-red-400 ml-2"></i>}
                                            </label>
                                            <div className="flex gap-2">
                                                <div className="flex-1 relative">
                                                    <input
                                                        type={showApiKeys.replicate ? "text" : "password"}
                                                        value={apiKeys.replicate}
                                                        onChange={(e) => setApiKeys({...apiKeys, replicate: e.target.value})}
                                                        placeholder="r8_..."
                                                        className="w-full p-3 bg-gray-800 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                                    />
                                                    <button
                                                        onClick={() => setShowApiKeys({...showApiKeys, replicate: !showApiKeys.replicate})}
                                                        className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white"
                                                    >
                                                        <i className={\`fas fa-\${showApiKeys.replicate ? 'eye-slash' : 'eye'}\`}></i>
                                                    </button>
                                                </div>
                                                <a
                                                    href="https://replicate.com/account/api-tokens"
                                                    target="_blank"
                                                    className="bg-gray-700 hover:bg-gray-600 text-white py-3 px-4 rounded-lg font-semibold transition-all whitespace-nowrap"
                                                >
                                                    <i className="fas fa-external-link-alt mr-1"></i>
                                                    발급
                                                </a>
                                            </div>
                                            <p className="text-xs text-gray-500 mt-1">이미지 및 영상 생성에 사용됩니다</p>
                                        </div>

                                        {/* ElevenLabs API */}
                                        <div>
                                            <label className="block text-sm font-semibold mb-2 text-gray-300">
                                                <i className="fas fa-microphone mr-2 text-purple-400"></i>ElevenLabs API 키
                                                {apiKeys.elevenlabs && <i className="fas fa-check-circle text-green-400 ml-2"></i>}
                                                {!apiKeys.elevenlabs && <i className="fas fa-times-circle text-red-400 ml-2"></i>}
                                            </label>
                                            <div className="flex gap-2">
                                                <div className="flex-1 relative">
                                                    <input
                                                        type={showApiKeys.elevenlabs ? "text" : "password"}
                                                        value={apiKeys.elevenlabs}
                                                        onChange={(e) => setApiKeys({...apiKeys, elevenlabs: e.target.value})}
                                                        placeholder="sk_..."
                                                        className="w-full p-3 bg-gray-800 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:border-purple-500"
                                                    />
                                                    <button
                                                        onClick={() => setShowApiKeys({...showApiKeys, elevenlabs: !showApiKeys.elevenlabs})}
                                                        className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white"
                                                    >
                                                        <i className={\`fas fa-\${showApiKeys.elevenlabs ? 'eye-slash' : 'eye'}\`}></i>
                                                    </button>
                                                </div>
                                                <a
                                                    href="https://elevenlabs.io/app/settings/api-keys"
                                                    target="_blank"
                                                    className="bg-gray-700 hover:bg-gray-600 text-white py-3 px-4 rounded-lg font-semibold transition-all whitespace-nowrap"
                                                >
                                                    <i className="fas fa-external-link-alt mr-1"></i>
                                                    발급
                                                </a>
                                            </div>
                                            <p className="text-xs text-gray-500 mt-1">음성(나레이션) 생성에 사용됩니다</p>
                                        </div>

                                        {/* 안내 메시지 */}
                                        <div className="bg-blue-900/20 border border-blue-700/50 rounded-lg p-4">
                                            <p className="text-blue-300 text-sm">
                                                <i className="fas fa-shield-alt mr-2"></i>
                                                API 키는 브라우저(localStorage)에만 저장됩니다. 서버로 전송되지 않아 안전합니다.
                                            </p>
                                        </div>
                                    </div>

                                    {/* 취소/저장 버튼 */}
                                    <div className="flex gap-3 mt-6 pt-6 border-t border-gray-700">
                                        <button
                                            onClick={() => setShowSettings(false)}
                                            className="flex-1 bg-gray-700 hover:bg-gray-600 text-white py-3 px-6 rounded-lg font-semibold transition-all"
                                        >
                                            <i className="fas fa-times mr-2"></i>
                                            취소
                                        </button>
                                        <button
                                            onClick={() => {
                                                setShowSettings(false);
                                                showToast('설정이 저장되었습니다', 'success');
                                            }}
                                            className="flex-1 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white py-3 px-6 rounded-lg font-semibold transition-all"
                                        >
                                            <i className="fas fa-save mr-2"></i>
                                            저장
                                        </button>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                );
            }

            ReactDOM.render(<App />, document.getElementById('root'));
        </script>
    </body>
    </html>
  `)
})

export default app
