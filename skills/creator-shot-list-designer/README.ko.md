# 샷 리스트 디자이너 — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · **한국어**

씬과 스토리보드를 **샷 리스트 + 편집 의도**로 전환하는 스킬.
프리프로덕션 기획과 편집 의도가 한데 모이는 지점이다. 이것은
파이널 컷 에디터가 아니다 — 어떤 소재가 제작되기 전에 편집 의도를
설계하여, 촬영이 올바른 조각들을 만들어내도록 한다.

## 철학

샷 리스트는 기술 목록이 아니라 **극적 + 편집 의도의 지도**다. 이 스킬은:

- **샷 경제성**: 모든 샷은 하나의 명확한 액션을 담는다
- **편집 리듬 인식**: 어떤 샷을 길게 가져가고, 어떤 샷을 빠르게 cut할 것인가?
  샷 지속 시간은 편집상의 결정이다
- **스크린 디렉션 + 연속성**: cut 전반에 걸친 공간적/시간적 일관성
- **AI 제작 가능성**: AI 도구의 제약을 고려하여 단일 샷의 복잡도를 기획한다
- **제작 이전의 편집 의도**: 불필요한 샷을 촬영하지 않도록 촬영 전에
  편집 로직을 확정한다
- **관객 경험 설계**: 관객은 무엇을 느끼고, 무엇을 알게 되며, 무엇이 감춰지는가?

## 산출물

| 산출물 | 내용 |
|-------|---------|
| **씬별 샷 리스트** | 정본 샷 리스트, 극적 + 편집상의 근거 포함 |
| **편집 계획** | 씬 내 페이싱, cut 지점, 오프닝/클로징 이미지 |
| **트랜지션 설계** | 씬 간 트랜지션 결정 (hard cut, match, J/L, sound bridge) |
| **연속성 리스크 감사** | 샷 전반의 일관성 리스크 보고서 |
| **사운드 편집 노트** | 사운드 디자이너를 위한 J-cut / L-cut / 침묵 지점 |
| **영화 전체 샷 리스트** | 영화 전체를 아우르는 통합 리스트 |
| **리듬 맵** | 씬별 페이싱 (샷 지속 시간 범위) |
| **중복 보고서** | cut/병합해야 할 샷 |
| **파이널 에디터 노트** | 파이널 컷 에디터에게 넘기는 편집 의도 |

## 언제 등장하는가

- 씬과 스토리보드가 준비되었고 샷 기반 계획이 필요할 때
- 편집을 고려한 샷 시퀀싱이 요청될 때
- 긴 씬을 AI로 제작 가능한 조각으로 나눠야 할 때
- 감독이나 DOP가 구조적 촬영/제작 계획을 요청할 때
- `creator-pipeline-supervisor`가 편집 전 기획을 위임할 때

## 일반적인 흐름

1. **브리핑** + 모든 상위 스킬 산출물 읽기
2. **질문 라운드**: 포맷, 편집 리듬, 톤, AI 도구
3. **샷 리스트 (씬별)**: 정본 구조로, 극적 + 편집상의 근거 포함
4. **편집 계획 (씬별)**: 페이싱, 오프닝/클로징, cut 지점
5. **트랜지션 설계**: 씬 간 트랜지션
6. **연속성 감사**: 샷 전반의 리스크
7. **리듬 맵**: 영화 전체 페이싱 맵
8. **중복 보고서**: cut 가능한 샷 식별
9. **인계**: creator-prompt-engineer를 위한 샷 프롬프트 데이터 + creator-final-cut-editor를 위한 편집 의도

## 샷 — 정본 구조

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, silence"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (side-high)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: night
Characters in frame: none (only the kettle)
Character action: kettle whistle dying down (off-screen Demir turns off the heat)
Dialogue / silence note: SILENCE (only kettle + clock ticking)
Light / atmosphere: gray moonlight from the window, copper kettle highlight
Sound / music note: NO music; clock ticking + kettle dying
Dramatic purpose: a symbolic echo of Demir's inner turning
Edit purpose: a 4-second breath — no need to cut, hold it
Link to previous shot: 04.01 (Demir sitting, wide) — match by sound
Link to next shot: 04.03 (Demir's face close, first blink) — hard cut
Continuity note: kettle = same copper, same stain pattern
AI video production note: single action (whistle dying) + static camera = low risk
Safe alternative: 6s version — slower whistle fade, very slow camera push-in
```

## 편집 의도 — 씬 계획

씬 단위 편집 질문:

- 어떤 샷으로 씬을 연다?
- 어떤 이미지로 씬을 닫는다?
- 어떤 샷을 길게 가져가는가?
- 어떤 샷을 짧게 cut하는가?
- 리액션 샷은 어디에 들어가는가?
- 침묵은 어디서 늘어지는가?
- hard cut이 필요한 곳은 어디인가?
- 부드러운 트랜지션은 어디인가?
- 어떤 이미지가 다음 씬으로 이어지는가?
- 어떤 샷이 극적 정점을 담는가?
- 어떤 샷이 불필요한가?
- 어떤 샷이 정보를 전달하고, 어떤 샷이 감정을 전달하는가?

`project/shot-list/scene-{NN}/edit-plan.md` 아래에 작성된다.

## 산출물을 쓰는 위치

`project/shot-list/` 아래:

| 파일 | 내용 |
|-------|---------|
| `scene-{NN}/shot-list.md` | 씬 샷 리스트 |
| `scene-{NN}/edit-plan.md` | 편집 의도 + 페이싱 |
| `scene-{NN}/transitions.md` | 트랜지션 결정 |
| `scene-{NN}/continuity-risks.md` | 연속성 감사 |
| `scene-{NN}/sound-edit-notes.md` | 사운드 디자이너 인계 |
| `film-shot-list.md` | 영화 전체 통합 리스트 |
| `rhythm-map.md` | 페이싱 맵 |
| `redundancy-report.md` | cut 가능한 샷 |
| `ai-production-shot-guide.md` | AI 도구 제약 가이드 |
| `final-editor-notes.md` | 파이널 컷 에디터를 위한 의도 |

## 트랜지션 유형 (편집상의 용도)

| 트랜지션 | 편집상의 용도 |
|-------|-------------------|
| Hard cut | 갑작스러운 극적 단절 |
| Match cut | 두 이미지 사이의 의미의 다리 |
| Fade in/out | 시간적/감정적 열고 닫음 |
| Dissolve | 시간 전환, 감정의 혼합 |
| J-cut | 다음 씬의 사운드가 먼저 도착 (매끄러운 흐름) |
| L-cut | 현재 씬의 사운드가 연장 (유지되는 감정) |
| Sound bridge | 사운드로 이어지는 장소/시간의 변화 |
| Visual motif | 반복되는 비주얼을 통한 다리 |
| Object transition | 형태 매칭 |
| Movement transition | 방향의 연속성 |
| Time jump | 갑작스러운 시간 도약 |
| Flashback | 필터/렌즈/블러/사운드 큐를 통해 |
| Parallel edit | 두 장소의 교차 편집 |

## AI 비디오 제작 가능성 규칙

- 샷당 하나의 명확한 액션
- 하나의 주된 카메라 무브먼트 (연결하지 않음)
- 통제된 수의 캐릭터
- 명확한 비주얼 타깃
- 복잡한 움직임은 멀티 샷으로 분할
- 위험한 손/손가락/lip sync에 플래그
- 군중은 선택적 프레이밍
- 모든 프롬프트에 잠긴 location + 캐릭터 anchor
- 샷 지속 시간은 보통 3–10s
- 각 샷은 단일 비디오 프롬프트로 깔끔하게 매핑

리스크가 감지되면 플래그를 단다:

> *"이 샷은 AI 비디오에 너무 복잡하다 — 두 개의 샷으로 분할하라."*
> *"여기서 lip sync가 실패할 수 있다; 말하는 인물 대신 리액션 샷을 쓰라."*
> *"손의 움직임이 결정적이다 — insert 대신 더 넓은 프레임을 쓰라."*
> *"군중 액션 — 단일 샷이 아니라 cut으로 구성하라."*

## 리듬과 페이싱

"빠르게 해줘" 같은 모호한 표현은 쓰지 않는다. 페이싱은:

- **샷 지속 시간 범위**로 표현되고
- **cut 빈도**로 측정된다

예시:
> *"씬 3은 샷당 평균 4–6s, 씬 12는 샷당 평균 1.5–3s —
> 캐릭터 갈등이 고조됨에 따라 페이스가 빨라진다."*

## 대사 편집 의도

대사가 많은 씬의 경우:

- 말하는 사람인가, 듣는 사람인가?
- 리액션 샷은 어디에 들어가는가?
- 침묵이 더 강한 곳은 어디인가?
- 대사 위에 다른 이미지를 얹을까?
- 표정으로 표현되는 서브텍스트?
- hard cut인가, 자연스러운 오버랩인가?
- 문장이 끝나기 전에 cut할까?
- 설명의 불필요한 반복?
- 관객이 정말로 봐야 하는 감정은 누구에게 있는가?

J-cut / L-cut 마커가 여기서 설정된다.

## 다른 스킬과의 협업

- **읽기**: 대본, 감독의 비전 + 디렉션 시트, DOP 씬별 계획,
  스토리보드 패널 데이터, 캐릭터/location anchor
- **쓰기**: `project/shot-list/*`
- **인계 대상**:
  - `creator-prompt-engineer` (샷 단위 비디오 프롬프트)
  - `creator-final-cut-editor` (편집 의도 파일)
- **피드백 수신처**: 감독, 파이프라인 슈퍼바이저

## 중복 감지

긴 AI 영화에서는 다음에 플래그를 단다:

- 같은 정보를 반복하는 샷
- 감정을 바꾸지 않는 샷
- 리듬을 떨어뜨리는 디테일 샷
- 리액션 샷의 과도한 사용
- 극적 기여도가 낮은데 AI로 어려운 샷
- late-in / early-out 기회
- 대사 대신 비주얼로 전달할 수 있는 순간

*"이 샷은 cut할 수 있다"* 또는 *"이 두 샷은 병합할 수 있다"*라고 명시적으로 쓴다.

## 행동 규칙

| 한다 | 하지 않는다 |
|-------|---------|
| 모든 샷에 극적 **그리고** 편집상의 근거를 부여한다 | 기술 목록을 만든다 |
| 감독의 리듬, DOP 프레이밍, 스토리보드와 협업한다 | 고립되어 결정한다 |
| 불필요한 샷에 플래그를 단다 | 채우기용 샷을 추가한다 |
| 연속성을 선제적으로 점검한다 | 촬영 후 문제가 드러나기를 기다린다 |
| AI 도구 제약을 고려하여 설계한다 | 제작 불가능한 샷을 기획한다 |
| 위험한 샷에 안전한 대안을 둔다 | 단일 버전만 제공한다 |
| 대사에서 듣는 사람도 고려한다 | 말하는 사람만 따라간다 |
| 사운드와 음악의 편집 의도를 조율한다 | 그림만 생각한다 |
| 구조화되어 후속 단계가 읽을 수 있는 산출물 | 텍스트 한 덩어리를 쏟아낸다 |
