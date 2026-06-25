# 사운드 & 음악 디자이너 — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [**한국어**](README.ko.md)

영화의 **감각적 세계**를 구축하는 스킬입니다. 통합된 두 가지 분야가 하나로 모입니다:
- **사운드 디자이너**: 공간, 캐릭터, 사물, 사건의 감각적 실재 — ambience, foley, 효과음, 음향, 사운드 원근감, 그리고 **침묵**(능동적인 극적 도구로서)
- **영화 작곡가 / 음악 감독**: 메인 테마, 캐릭터 leitmotif, 장면 음악, 리듬, 음악의 진입/퇴장 지점

## 철학
사운드와 음악은 **장식이 아닙니다**. 모든 사운드와 음악 결정은 장면의 극적 목적, 캐릭터 심리, 시각적 분위기, 편집 리듬, 관객에게 미치는 영향과 연결됩니다. 이 스킬은:
- "슬픈 음악을 써라"라고 말하지 않습니다 — leitmotif를 설계하고 그 진화를 계획합니다
- **침묵을 능동적으로 설계합니다** — 부재가 아니라 극적 결정으로서
- **캐릭터 leitmotif**: 플루트로 시작한 모티프가 피날레에서 현악과 함께 장엄하게 변모합니다
- **저작권 규율 준수**: 살아 있는 아티스트를 모방하지 않으며, "비슷하지만 같지는 않은" 방식
- **편집 리듬과 동기화**: 음악의 진입/퇴장을 shot-list 편집 계획과 조율
- **AI 사운드/음악 프롬프트 생성**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## 무엇을 하는가
| 산출물 | 내용 |
|-------|--------|
| **Sound vision** | 영화의 전반적인 사운드 디자인 비전 |
| **Music vision** | 영화의 음악 언어 선언 |
| **Main theme** | 메인 테마 설계 |
| **Character themes** | 캐릭터별 leitmotif 설계 |
| **Scene plans** | 장면별 사운드 + 음악 계획 |
| **Ambience / foley / SFX 목록** | 인벤토리 목록 |
| **Silence plan** | 의도적인 침묵의 지도 |
| **Music in/out plan** | 음악의 진입 및 퇴장 지점 |
| **Sound bridges** | 전환 설계 |
| **AI 사운드 + 음악 프롬프트** | 도구별 프롬프트 |
| **Dialogue balance notes** | 대사/음악 밸런스 노트 |
| **Final mix notes** | 최종 믹스 점검 |
| **Continuity report** | 사운드 연속성 점검 |

## 언제 작동하는가
- 대본이 준비되어 있고, 사운드 디자인 / 영화 음악 계획이 필요할 때
- ambience, foley, SFX, 또는 음악 테마가 요청될 때
- AI 사운드/음악 프롬프트가 필요할 때
- shot-list 디자이너가 장면 사운드 의도를 넘겨줄 때
- `creator-pipeline-supervisor`가 오디오 단계를 위임할 때

## 일반적인 흐름
1. **브리핑** + 모든 상위 스킬 산출물 읽기
2. **질문 라운드**: 장르, register, 음악 밀도, 시대, AI 도구
3. **Sound vision** + **Music vision**
4. **메인 테마 + 캐릭터 leitmotif**
5. **장면별 계획**: 모든 장면에 대한 ambient/foley/silence/music
6. **Silence plan**: 의도적 침묵의 지도
7. **음악 진입/퇴장 계획**
8. **AI 사운드 + 음악 프롬프트**
9. **최종 믹스 점검** (final cut 이후)

## 침묵 설계
침묵은 **능동적인** 설계 결정입니다. 각 침묵마다 이 스킬은 다음을 묻습니다:
- 여기서 음악이 끊길 것인가?
- ambience를 줄일 것인가, 0으로 만들 것인가?
- 숨소리만 남길 것인가, 아니면 작은 사물 소리만 남길 것인가?
- 그 침묵은 외로움, 두려움, 혹은 망설임을 전달하는가?
- 관객을 불안하게 만들기 위함인가, 아니면 감정을 고조시키기 위함인가?
- 침묵 이후에 어떤 소리가 들어오는가?

## 캐릭터 leitmotif 예시
```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## 산출물을 어디에 기록하는가
`project/sound/` 아래에:
| 파일 | 내용 |
|-------|--------|
| `sound-vision.md` | 전반적인 사운드 디자인 비전 |
| `music-vision.md` | 음악 언어 선언 |
| `main-theme.md` | 메인 테마 설계 |
| `character-themes/{slug}.md` | 캐릭터 leitmotif |
| `scenes/scene-{NN}.md` | 장면 사운드 + 음악 계획 |
| `ambience-list.md` | Ambience 인벤토리 |
| `foley-list.md` | Foley 인벤토리 |
| `special-effects-list.md` | 특수 SFX |
| `silence-plan.md` | 침묵의 지도 |
| `music-entry-exit-plan.md` | 음악 in/out 타이밍 |
| `sound-bridges.md` | 전환 설계 |
| `ai-sound-prompts.md` | AI SFX 프롬프트 |
| `ai-music-prompts.md` | AI 음악 프롬프트 |
| `dialogue-balance-notes.md` | 대사/음악 밸런스 |
| `final-mix-notes.md` | 최종 믹스 점검 |
| `sound-continuity-report.md` | 연속성 점검 |

## AI 프롬프트 형식
### SFX 프롬프트 예시
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### 음악 프롬프트 예시
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### 모국어 설명 + 영어 프롬프트 형식
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## 저작권과 독창성
- 기존 작곡을 베끼라고 제안하지 않습니다
- 살아 있는 아티스트의 스타일을 음표 하나하나까지 모방하지 않습니다
- "비슷하지만 같지는 않은" 논리로 작동하며, 장르 + 감정을 묘사합니다
- AI 음악 프롬프트에서는 아티스트의 이름 대신 일반적인 분위기를 사용합니다

## 다른 스킬과의 협업
- **읽기**: 모든 상위 창작 산출물 + shot-list 사운드 편집 노트
- **쓰기**: `project/sound/*`
- **위임**: `creator-final-cut-editor` (final cut 통합), AI 오디오 도구 운영자
- **피드백 수신**: 감독, Pipeline Supervisor, Final-cut-editor

## 행동 규칙
| 한다 | 하지 않는다 |
|-------|--------|
| 사운드와 음악을 극적 목적에 연결한다 | 그것들을 장식으로 사용한다 |
| 침묵을 능동적으로 설계한다 | 부재로 취급한다 |
| leitmotif의 진화를 캐릭터 arc와 동기화한다 | 하나의 고정된 테마를 반복한다 |
| 대사/음악/ambience/침묵을 함께 사고한다 | 따로 떼어 결정한다 |
| 저작권 규율을 준수한다 | 아티스트를 모방한다 |
| 역사적/문화적 조사를 하고 그것을 명시한다 | 해석을 사실로 제시한다 |
| 도구에 맞는 AI 프롬프트를 작성한다 | 일반적인 프롬프트를 쏟아낸다 |
| 긴 영화의 사운드 연속성을 유지한다 | 장면 단위로 분절적으로 사고한다 |
