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

// 1. 대본 분석 (Gemini)
app.post('/api/analyze-script', async (c) => {
  try {
    const { script } = await c.req.json()
    
    if (!script) {
      return c.json({ error: '대본을 입력해주세요' }, 400)
    }

    const genAI = new GoogleGenerativeAI(c.env.GEMINI_API_KEY || '')
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
      model = 'flux-1.1-pro' 
    } = await c.req.json()
    
    if (!prompt) {
      return c.json({ error: '프롬프트를 입력해주세요' }, 400)
    }

    const replicate = new Replicate({
      auth: c.env.REPLICATE_API_TOKEN || ''
    })

    // 품질 향상 키워드 추가
    const qualityEnhancement = 'masterpiece, best quality, highly detailed, sharp focus, professional photography, '
    
    // 네거티브 프롬프트
    const negativePrompt = 'low quality, blurry, distorted, disfigured, bad anatomy, wrong proportions, watermark, text, logo, ugly, duplicate, '

    // 최종 프롬프트 생성
    const finalPrompt = `${qualityEnhancement}${stylePrefix}${prompt}`

    console.log('Generating image with model:', model)
    console.log('Final prompt:', finalPrompt)

    // 모델별 설정
    const modelConfigs: Record<string, any> = {
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
    const { imageUrl, prompt, sceneId } = await c.req.json()
    
    if (!imageUrl) {
      return c.json({ error: '이미지 URL을 입력해주세요' }, 400)
    }

    const replicate = new Replicate({
      auth: c.env.REPLICATE_API_TOKEN || ''
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
    const { text, voiceId = '21m00Tcm4TlvDq8ikWAM' } = await c.req.json()
    
    if (!text) {
      return c.json({ error: '텍스트를 입력해주세요' }, 400)
    }

    // API 키 확인
    const apiKey = c.env.ELEVENLABS_API_KEY
    if (!apiKey) {
      console.error('ElevenLabs API key not found')
      return c.json({ 
        error: 'ElevenLabs API 키가 설정되지 않았습니다',
        details: 'API_SETUP.md 파일을 참고하여 .dev.vars에 ELEVENLABS_API_KEY를 설정해주세요.\n\n1. https://elevenlabs.io/app/settings/api-keys 에서 API 키 발급\n2. .dev.vars 파일에 ELEVENLABS_API_KEY=your_key 추가\n3. 서버 재시작 (pm2 restart youtube-studio)'
      }, 400)
    }

    console.log('Generating voice with ElevenLabs...')
    console.log('Text length:', text.length, 'characters')
    console.log('Voice ID:', voiceId)

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
            stability: 0.5,
            similarity_boost: 0.75,
            style: 0.0,
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
                const [script, setScript] = useState('');
                const [scenes, setScenes] = useState([]);
                const [overallFeedback, setOverallFeedback] = useState('');
                const [suggestions, setSuggestions] = useState([]);
                const [loading, setLoading] = useState(false);
                const [toast, setToast] = useState(null);
                
                // 이미지 스타일 설정
                const [imageStyle, setImageStyle] = useState('photorealistic');
                const [customStylePrefix, setCustomStylePrefix] = useState('');
                const [aspectRatio, setAspectRatio] = useState('16:9');
                const [aiModel, setAiModel] = useState('flux-pro');

                const showToast = (message, type = 'info') => {
                    setToast({ message, type });
                    setTimeout(() => setToast(null), 5000);
                };

                const analyzeScript = async () => {
                    if (!script.trim()) {
                        showToast('대본을 입력해주세요', 'error');
                        return;
                    }

                    setLoading(true);
                    try {
                        const response = await fetch('/api/analyze-script', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ script })
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
                                model: aiModel
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
                                sceneId 
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

                    try {
                        showToast('음성 생성 중...', 'info');
                        const response = await fetch('/api/generate-voice', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ text: fullScript })
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

                        {/* Header */}
                        <div className="text-center mb-8">
                            <h1 className="text-5xl font-bold mb-3 bg-gradient-to-r from-purple-400 to-indigo-400 bg-clip-text text-transparent">
                                <i className="fas fa-video mr-3"></i>
                                지혜스튜디오 v5.1
                            </h1>
                            <p className="text-gray-400">AI 기반 유튜브 영상 제작 솔루션</p>
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
                                    {scenes.map((scene) => (
                                        <div key={scene.id} className="card rounded-xl p-4 transition-all">
                                            <div className="mb-3">
                                                <span className="bg-purple-500/20 text-purple-300 px-3 py-1 rounded-full text-sm font-semibold">
                                                    장면 {scene.id}
                                                </span>
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
                                <div className="card rounded-xl p-6 flex flex-wrap gap-4 justify-center">
                                    <button
                                        onClick={generateVoice}
                                        className="btn-primary text-white py-3 px-6 rounded-lg font-semibold flex items-center gap-2 transition-all"
                                    >
                                        <i className="fas fa-microphone"></i>
                                        <span>전체 음성 생성</span>
                                    </button>
                                    <button
                                        className="bg-gray-700 hover:bg-gray-600 text-white py-3 px-6 rounded-lg font-semibold flex items-center gap-2 transition-all"
                                    >
                                        <i className="fas fa-download"></i>
                                        <span>전체 다운로드</span>
                                    </button>
                                </div>
                            </>
                        )}
                        
                        {/* Footer */}
                        <div className="footer">
                            © 2026 지혜스튜디오랩. All Rights Reserved.
                        </div>
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
