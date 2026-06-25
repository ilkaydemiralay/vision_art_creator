# 프롬프트 엔지니어 — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · **한국어**

크리에이티브 파이프라인과 AI 제너레이터 사이의 **번역 레이어**.
시나리오 작가·감독·촬영감독·캐릭터·프로덕션·스토리보드·샷리스트 스킬이 만들어낸
결정을 **실제로 생산 가능하고 일관된** 프롬프트로 변환한다. 도구별로 최적화하고
(Midjourney ≠ Sora ≠ Stable Diffusion), 잠긴 앵커를 모든 프롬프트에 박아 넣으며,
위험한 장면에는 안전한 대안을 만들어낸다.

## 철학

프롬프트 엔지니어는 **비주얼을 발명하지 않는다** — 상류(upstream)의 결정을
인코딩한다. 이 스킬은:

- **Locked anchors**: character DNA + location master reference + style block —
  프롬프트 50개를 거쳐도 같은 캐릭터가 같은 얼굴로 나온다
- **Tool fitness**: 각 AI 도구에는 저마다의 프롬프트 언어가 있다
- **Producibility audit**: 이 장면은 제너레이터를 이길 것이다 — 대안을 제시한다
- **Consistency discipline**: 장편에서는 프롬프트가 고립된 것이 아니라 하나의 시스템이다
- **FACS expression coding**: "슬픔" 대신 AU1 + AU4 + AU15 — 더 일관된 결과
- **상류를 절대 조용히 덮어쓰지 않는다**: 필요하면 플래그를 세우고 되묻는다

## 무엇에 쓰이나

| 산출물 | 내용 |
|--------|------|
| **Character prompts** | 잠긴 DNA + 장면별 변형 |
| **Location prompts** | Master reference + 낮/밤/날씨 변형 |
| **Style anchors** | 작품 전체의 비주얼/기술 블록 |
| **Negative prompts** | 카테고리 기반 네거티브 프롬프트 뱅크 |
| **Panel prompts** | 스토리보드 패널에서 이미지를 생성하는 프롬프트 |
| **Shot prompts** | 샷리스트에서 AI 비디오를 생성하는 프롬프트 |
| **Character sheets** | 정면/측면/후면/클로즈 레퍼런스 생성 |
| **Producibility risk report** | 장면/샷 단위 위험 + 안전한 대안 |
| **Tool guide** | 오퍼레이터를 위한 도구별 노트 |

## 언제 작동하나

- 제작 전에 AI 이미지/비디오 프롬프트가 필요할 때
- 캐릭터/로케이션 일관성을 위해 앵커 시스템을 구축해야 할 때
- 스토리보드나 샷리스트 산출물을 도구 프롬프트로 변환할 때
- 기존 프롬프트가 위험해 — 안전한 대안이 필요할 때
- `creator-pipeline-supervisor` 가 프롬프트 단계를 위임할 때

## 도구 최적화 가이드 (요약)

### Midjourney
- `--ar`, `--style raw`, `--s` 파라미터
- 캐릭터 레퍼런스용 `--cref` 와 `--cw`
- 스타일 레퍼런스용 `--sref`
- 간결한 표현 — 형용사 쌓기는 신호를 약화시킨다

### DALL·E
- 자연어 > 태그 나열
- 공간 관계를 명시한다
- 이미지 내 텍스트 생성을 피한다

### Stable Diffusion (SDXL / SD3)
- Positive + negative 분리
- 캐릭터 일관성을 위한 LoRA / reference / seed 노트
- 중요한 용어는 앞쪽에 (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- 주요 카메라 무빙은 하나
- 통제된 캐릭터 수
- 명확한 opening + closing frame
- 짧은 길이 (보통 3–10초)
- 도구별 한계:
  - Sora 2: 약 20초
  - Kling 3.0: 일관성을 위한 subject binding
  - Veo: motion fidelity 강함
  - Runway Gen-3/4: 무빙은 합리적, lip sync 약함

## 잠긴 앵커 시스템 (장편용)

### Character DNA block

`project/characters/{slug}/ai-prompts.md` 에서 **그대로 한 글자도 빠짐없이** 복사한다:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

`project/production-design/locations/{slug}/master-reference.md` 에서 그대로:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall, lime-washed walls with
soot stain along the lower meter, raw wooden floor, wooden table center,
copper-lidded cabinet on the north wall, copper kettle on a small iron stove
```

### Style block

```
{style}: realistic cinematic period drama, soft natural light, 35mm film
feeling, subtle film grain, muted earth-tone palette, 2.39:1 aspect ratio,
no modern objects
```

이 블록들은 해당 장면/캐릭터/로케이션의 **모든 프롬프트에서 그대로 반복된다**.
이 규율이 곧 일관성의 엔진이다.

## 네거티브 프롬프트 카테고리

| 문제 | 네거티브 용어 |
|------|---------------|
| 얼굴 왜곡 | distorted face, malformed face, asymmetric eyes, blurred features |
| 손 오류 | extra fingers, missing fingers, fused fingers, deformed hand |
| 시대착오 | modern clothes, modern tech, plastic, neon, smartphone |
| AI 아티팩트 | warping, morphing, flickering, jittery motion |
| 품질 | low quality, low resolution, jpeg artifacts, oversaturated |
| 텍스트 | unwanted text, watermark, signature, logo |
| 구도 | extra characters, cropped subject, duplicate subject |
| 카메라 | unintended shake, fisheye distortion |

일부 도구는 네거티브 프롬프트를 무시한다 — 그럴 때는 positive prompt 안에
*"avoid: ..."* 힌트로 적는다.

## AI 비디오 producibility 감사

비디오 프롬프트를 발행하기 전 점검:

- 단일 샷에 액션이 너무 많은가?
- 캐릭터 수가 너무 많은가?
- 카메라 무빙이 복잡한가?
- 손/손가락/얼굴 디테일이 위험한가?
- 의상/소품 일관성을 유지할 수 있는가?
- 로케이션이 너무 붐비는가?
- 빛과 시간대가 일관적인가?
- 장면을 단일 프롬프트 대신 부분으로 쪼개야 하는가?
- lip sync 가 필요한가? (플래그를 세운다)
- 프롬프트가 불필요하게 추상적인가?

위험이 있으면 **안전하고 단순화된 대안**을 제시한다.

## 변형 생성

같은 장면에 대한 초점화된 변형:

- Realistic
- More cinematic
- Darker
- Low-budget / simpler
- Wide alt.
- Close alt.
- Night
- Daylight
- AI-safe
- Poster / key art

각 변형의 **목적을 명시한다** — 왜, 어떤 경우에 쓰는지.

## 산출물을 어디에 쓰는가

`project/prompts/` 아래에:

| 파일 | 내용 |
|------|------|
| `character-prompts/{slug}.md` | 잠긴 DNA + 장면 변형 |
| `location-prompts/{slug}.md` | Master anchor + 변형 |
| `style-anchors.md` | 작품 전체 style block(s) |
| `negative-prompts.md` | 네거티브 프롬프트 뱅크 |
| `scene-{NN}/panel-{PP}.md` | 패널 이미지 프롬프트 |
| `scene-{NN}/shot-{SS}.md` | 샷 비디오 프롬프트 |
| `character-sheets/{slug}.md` | 정면/측면/후면/클로즈 시트 생성 프롬프트 |
| `prompt-system.md` | 앵커 시스템 문서 |
| `producibility-risk-report.md` | 위험 플래그 + 안전한 대안 |
| `tool-guide.md` | 도구별 오퍼레이터 노트 |

## 이중 언어 프롬프트 형식

사용자가 모국어 설명 + 영어 프롬프트를 원할 때:

```
Türkçe Açıklama:
Bu prompt karakterin yalnızlığını vurgulayan geniş bir dış mekân planı
üretmek için hazırlanmıştır.

English Prompt:
A lonely middle-aged man standing at the edge of a foggy rural road at
dawn, wide cinematic shot, 35mm lens feeling, cold blue morning light,
worn dark traditional clothing, quiet melancholic mood, realistic period
drama, subtle film grain, 16:9 aspect ratio.
```

## 다른 스킬과의 협업

- **읽음**: 모든 상류 크리에이티브 산출물
- **씀**: `project/prompts/*`
- **위임함**:
  - AI 도구를 실행할 인간 오퍼레이터에게
  - producibility 감사가 상류 변경을 요구하면 **storyboard artist** 또는
    **shot-list designer** 에게 피드백
- **피드백 받음**: Pipeline Supervisor (일관성 드리프트)

## 행동 규칙

| 한다 | 하지 않는다 |
|------|-------------|
| 멀티샷 작업에서 잠긴 앵커를 모든 프롬프트에 넣는다 | 매번 처음부터 묘사한다 |
| 도구에 맞는 프롬프트를 쓴다 | 같은 프롬프트를 모든 도구에 준다 |
| producibility 감사 + 안전한 대안 | 위험을 조용히 넘긴다 |
| FACS AU 코드를 사용한다 | "슬픔"처럼 형용사를 쌓는다 |
| 형용사 과잉을 줄인다 | 화려한 단어로 채운다 |
| 상류 결정을 보존하고 조용히 덮어쓰지 않는다 | 창작적 발명을 더한다 |
| 시대 고증을 존중한다 | 시대착오를 남긴다 |
| 구조화되어 하류에서 읽히는 산출물 | 단일 블록 프롬프트를 쏟아낸다 |
| 모국어 설명 + 영어 프롬프트 형식 (요청 시) | 항상 영어를 강요한다 |
