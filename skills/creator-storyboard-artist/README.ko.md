# 스토리보드 아티스트 — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

작성된 시나리오를 **읽을 수 있는 시각적 서사**로 바꾸는 스킬. 패널 수를
최소화함으로써 각 패널이 극적인 이유를 가지고 존재하도록 보장한다. 장면의
결정적인 순간을 포착하고, screen direction을 유지하며, eyeline continuity를
추적하고, AI image/video prompt로 깔끔하게 hand-off한다.

## 철학

스토리보드는 "장면 작화"가 아니라 **시각적 서사 시스템**이다. 이 스킬은:

- **Panel economy**: 적은 패널 + 날카로운 선택 — 많은 패널 + 약한 결정이 아니라
- **Screen direction(180°)** 및 **eyeline continuity**: 컷 사이의 공간적 일관성
- **Graphic dynamics**: 시선은 어디에 떨어지는가? 초점은 무엇인가?
- **Continuity awareness**: 의상, 로케이션, 빛의 방향, 화면 방향, 움직임
- **Locked anchors**: 모든 패널에서의 character DNA + location master reference
- **Producibility**: AI 생성 제약을 알고 위험한 장면을 flag하는

## 무엇에 쓰이는가

| 출력 | 내용 |
|------|------|
| **Per-scene storyboard** | 장면별 패널 목록(전체 패널 데이터) |
| **Per-panel sheets** | 복잡한 장면을 위한 상세 단일 패널 파일 |
| **AI image prompts** | 패널별 생성 가능한 prompt |
| **AI video prompts** | 움직이는 패널을 위한 video prompt |
| **Continuity log** | 의상/로케이션/방향 위험의 flag |
| **Animatic plan** | 모든 장면의 animatic 순서를 계획 |
| **Director / DOP notes** | 감독과 DOP에게 보내는 간결한 시각적/기술적 메모 |
| **Handoff to shot-list** | creator-shot-list-designer 형식의 패널 데이터 |

## 언제 작동하는가

- 시나리오가 손에 있고 시각적 분할이 필요할 때
- 감독이 장면을 사전에 시각화하고자 할 때
- DOP의 렌즈/조명 결정 전에 시각적 콘셉트가 필요할 때
- AI prompt 생성 전에 스토리보드 논리가 필요할 때
- `creator-pipeline-supervisor`가 스토리보드 단계를 위임할 때

## Panel content(정규 필드)

각 패널은 다음 필드를 기록한다:

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## 출력을 어디에 쓰는가

`project/storyboards/` 아래:

| 파일 | 내용 |
|------|------|
| `scene-{NN}/storyboard.md` | 장면 기반 패널 목록(정규) |
| `scene-{NN}/panel-{PP}.md` | 상세 단일 패널(복잡한 장면에서) |
| `scene-{NN}/prompts.md` | 패널별 AI prompt(image + video) |
| `scene-{NN}/continuity.md` | Continuity flag |
| `animatic-plan.md` | 전체 영화의 animatic 순서 메모 |
| `notes-to-creator-director.md` | 감독에게 보내는 질문/경고 |
| `handoff-to-shot-list.md` | shot-list designer를 위한 형식화된 패널 데이터 |

## Shot type 용어집(극적 대응 포함)

| 유형 | 극적 용도 |
|------|-----------|
| Establishing | 공간 안에서 관객을 위치시킨다 |
| Master | 장면 기하, fallback |
| Wide/Full | 캐릭터–환경 관계 |
| Medium | 중립적 대화 |
| Close | 내적 갈등, 친밀한 감정 |
| Extreme close | 주관적 강도 |
| Insert | 사물 강조 |
| Cutaway | 병렬/외부 정보 |
| Reaction | 액션보다 반응 |
| OTS | 대화 시점 |
| POV | 캐릭터의 주관성 |
| 2-shot / group | 관계 기하 |
| Silhouette | 익명성, 미스터리 |
| Negative-space frame | 고립, 작음 |
| Symmetrical | 힘, 격식, 불안한 정지 |
| Tracking | 지속적인 추적 |
| Static | 관찰, 침묵의 의미 |

"close-up을 써라"로는 충분치 않다 — **왜** close-up이 필요한지가 질문된다.

## Continuity audit

패널에서 패널로, 장면에서 장면으로 추적:

- 의상
- 헤어/메이크업/액세서리
- 로케이션 정체성(locked anchor와 함께)
- 빛의 방향
- 낮/밤
- Screen direction(180° 규칙)
- 캐릭터의 공간적 논리
- 액션 흐름
- prop 위치

위험이 감지되면 패널의 `continuity note` 필드에 명시적으로 기록된다.

## 다른 스킬과의 협업

- **읽는다**: 시나리오, 감독의 비전 + direction sheets, DOP의 per-scene plan,
  character DNA + FACS, 로케이션 anchor
- **쓴다**: `project/storyboards/*`
- **위임한다**:
  - `creator-shot-list-designer`(panel → shot list)
  - `creator-prompt-engineer`(panel prompt → 도구별 최적화)
- **피드백을 받는다**: 감독, Pipeline Supervisor

## AI 생성에 초점을 맞춘 해법

- 복잡한 장면을 단순한 패널로 분할한다
- 다수 캐릭터 장면에서 시각적 초점을 명확히 한다
- AI가 어려워할 움직임을 단순화한다
- 동일한 로케이션/캐릭터에 고정 anchor를 사용한다
- 카메라 움직임 대신 안전한 정적 샷 대안을 제시한다
- 붐비는 장면에서 선택적 프레이밍을 제안한다
- 빠른 액션 대신 리듬감 있는 컷을 제안한다

## 행동 규칙

| 한다 | 하지 않는다 |
|------|-------------|
| 각 패널에 극적 근거를 쓴다 | 채우려고 "패널 하나 더"를 넣는다 |
| 적은 패널 + 날카로운 선택 | 많은 패널 + 약한 결정 |
| 시나리오 작가 + 감독 + DOP + 캐릭터 + 제작을 통합한다 | upstream을 조용히 덮어쓴다 |
| screen direction과 eyeline을 유지한다 | 컷에서 방향을 뒤섞는다 |
| locked anchor를 모든 prompt에 넣는다 | 각 패널에서 처음부터 다시 기술한다 |
| 복잡한 장면을 패널로 분할한다 | 단일 과부하 frame에 몰아넣는다 |
| AI 위험 flag + 안전한 대안 | 생성 불가능한 움직임을 제안한다 |
| 구조화되고 하류에서 읽을 수 있는 출력 | 단일 텍스트 블록을 쏟아낸다 |
