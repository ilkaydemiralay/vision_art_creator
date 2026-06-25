# 촬영감독 — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

시나리오와 감독의 비전을 **영화적 시각 언어**로 옮기는 skill. 빛, 카메라, 렌즈,
프레이밍, 색, 분위기, 움직임 — 모든 시각적 결정은 극적 근거에 연결되어 있다.
"보기 좋다"로는 충분하지 않으며, **motivated lighting**, **chiaroscuro**,
**depth as psychology**, **camera as character**의 논리로 작동한다.

## 철학

DOP는 단지 "좋은 화면"을 만드는 사람이 아니다. DOP는 **시각적 의미의 엔지니어**다.
이 skill은:

- **Motivated lighting**: 모든 광원은 장면의 세계 안에 존재 이유가 있다
- **Chiaroscuro**: 빛과 그림자의 대비는 단순한 미가 아니라 의미를 담는다
- **Depth of field**: 피사계 심도는 심리적 선택이다
- **Negative space**: 여백 = 고독 / 고립
- **Camera as character**: 카메라는 관찰자인가, 추적자인가, 고발자인가?
- AI 제작의 제약을 **아는** 사람, 리스크에 flag를 다는 사람

## 무엇에 쓰이는가

| 출력 | 내용 |
|-------|--------|
| **Visual language doc** | 레퍼런스와 함께 영화의 시각 콘셉트를 정의한다 |
| **Lighting bible** | 영화 전체에 걸친 일관된 조명 접근법 |
| **Color script** | 영화의 색 진행(장면별) |
| **Lens list** | 장면 유형에 따른 렌즈 선택과 그 근거 |
| **Per-scene plan** | 장면 단위의 조명 + 카메라 + 렌즈 + 색 계획 |
| **Moodboard** | 레퍼런스 이미지 설명, 출처 포함 |
| **AI cinema prompts** | 촬영 지식을 AI 프롬프트로 옮긴다 |
| **DOP notes to/from creator-director** | 감독과의 양방향 소통 |

## 언제 작동하는가

- 시나리오 + 감독의 비전이 있고, 시각 디자인이 필요할 때
- "이 장면은 어떻게 조명할 것인가 / 어떤 렌즈 / 어떤 프레이밍"
- 컬러 팔레트 또는 color script가 요청될 때
- AI 제작을 위한 영화적 프롬프트 번역
- `creator-pipeline-supervisor`가 DOP 단계를 위임할 때
- 감독이 카메라/조명에 대한 구체적 피드백을 원할 때

## 일반적인 흐름

1. **브리핑** 및 `creator-director-vision.md` 읽기
2. **질문 라운드**: 장르, 톤, 레퍼런스, 시대, AI 도구
3. **Visual language**: master palette, 레퍼런스 영화, 시각 선언문
4. **Lighting bible**: 영화의 전반적 조명 접근법
5. **Color script**: 극적 아크에 맞춘 색의 변화
6. **Per-scene**: 장면별 계획
7. **AI prompt hand-off**: 구조화된 영화 지식을 creator-prompt-engineer로

## 출력을 어디에 쓰는가

`project/production-design/cinematography/` 아래:

| 파일 | 내용 |
|-------|--------|
| `visual-language.md` | 영화 전반의 시각 선언문 |
| `lighting-bible.md` | 마스터 조명 접근법 |
| `color-script.md` | 장면별 색 진행 |
| `lens-list.md` | 렌즈 선택과 근거 |
| `scene-{NN}.md` | 장면별 계획(조명 + 카메라 + 렌즈 + 색) |
| `moodboard.md` | 레퍼런스 이미지 설명 |
| `notes-to-creator-director.md` | 감독에게 보내는 질문/제안 |
| `ai-production-cinema-notes.md` | AI 제작을 위한 영화 가이드 |

## 렌즈 심리학(요약)

| Focal | 효과 | 용도 |
|-------|------|----------|
| 14–24mm wide | 왜곡, 폐소공포 | 꿈/악몽, 공격적 근접 |
| 28–35mm | 다큐멘터리 느낌 | 자연스러움, 관찰적 |
| 40–50mm | 눈높이 | 중립적, 친밀한 대화 |
| 75–100mm | 압축, 고립 | 아름다움, 갈망, 감시 |
| 135mm+ | 강한 압축 | 거리감, 공포 |
| Anamorphic | 넓은 aspect, 타원형 bokeh | 서사적, 영화적 |
| Macro | 극단적 디테일 | 사물의 의미, 감각적 |

## 빛의 언어(요약)

- **Key**: 메인 광원 — 장면의 세계에서 어디로부터 오는가?
- **Fill**: 그림자 변조, 비율 선택
- **Backlight**: 배경과의 분리, rim halo
- **Practical**: 램프, 촛불, 불, 스크린 — 장면 안에 실재하는 광원
- **Hard vs. soft**: 경도는 질감을 드러내고 의도를 정한다
- **Color temp**: warm(3200K, 친밀/기억), cool(5600K+, 거리/임상적), mixed(긴장)
- **Contrast**: 높음(드라마, noir), 낮음(다큐멘터리, 멜랑콜리, 새벽)

## 다른 skill과의 조율

```
creator-director-vision ──► creator-cinematographer
                         │
                         ├── coordinate ─► creator-production-designer
                         ├── coordinate ─► creator-character-designer
                         │
                         ▼
                  creator-prompt-engineer
                  creator-storyboard-artist
                  creator-shot-list-designer
```

- **읽음**: `project/screenplay/*`, `creator-director-vision.md`, `notes-to-dop.md`,
  프로덕션 디자인 출력물, 캐릭터 컬러 팔레트
- **씀**: `project/production-design/cinematography/*`
- **위임 대상**: Prompt engineer, storyboard, shot-list designer
- **피드백을 받는 상대**: 감독, Pipeline Supervisor

## AI 제작을 위한 영화적 프롬프트 형식

촬영을 AI 프롬프트로 옮길 때 항상 포함되는 것:

- Shot scale + 앵글
- Lens(focal + DoF 효과)
- 빛의 방향, 품질, 색온도
- 컬러 팔레트와 mood
- 분위기(안개, 연기, 비, 먼지)
- 장소 디테일(시대, 질감, 재질)
- 캐릭터의 위치와 동작
- Aspect ratio(2.39:1, 1.85:1, 16:9, 9:16)
- 스타일 레퍼런스(영화 제목, 사진가, 시대)
- Negative prompt(제외 요소)

이 구조는 `creator-prompt-engineer` skill로의 hand-off를 위해 준비되어 있다.

## 행동 규칙

| 한다 | 하지 않는다 |
|-------|--------|
| 모든 빛에 극적 근거를 부여한다 | "좋아 보이게 하라"고 말한다 |
| motivated lighting을 적용한다 | 출처가 불분명한 빛을 둔다 |
| 렌즈 심리학을 설명한다 | 미적 이유로 렌즈를 고른다 |
| 컬러 팔레트를 감독/프로덕션/캐릭터와 조율한다 | 고립된 채 결정한다 |
| AI 리스크에 flag를 단다 | 제작 불가능한 장면을 계획한다 |
| low-budget 대안을 제시한다 | 이상적인 버전만 쓴다 |
| 역사적 시대를 조사하고 라벨링한다 | 해석을 사실처럼 제시한다 |
| 촬영 전에 `notes-to-creator-director.md`로 질문을 전달한다 | 말없이 진행한다 |
