# 캐릭터 디자이너 — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

캐릭터를 **이름 + 나이 + 외모**라는 삼요소에서 끌어올려 **통합된 하나의 존재**로
설계하는 스킬. 극적 기능, 심리, 전기, 보디랭귀지, 의상, props, 캐스팅 프로필, 그리고
**FACS Action Unit으로 코드화된 표정 라이브러리**를 생성합니다. 장편 AI 영화 제작
전반에 걸쳐 캐릭터 일관성을 지켜 주는 "Character DNA" 앵커를 구축합니다.

## 철학

캐릭터는 무작위로 생성되지 않습니다 — 각본의 필요, 감독의 비전, DOP의 시각적
세계에서 비롯됩니다. 이 스킬은:

- **모든 캐릭터는 어떤 극적 질문에 대한 답이다** — 그렇지 않으면 그 캐릭터를 잘라낼 것을 제안한다
- 모든 주요 캐릭터에 대해 **Want / Need / Fear / Wound** 4요소를 필수로 구축한다
- **FACS Action Units**: "슬프다"라고 말하는 대신 AU1+AU4+AU15라고 표현한다 —
  AI 모델과 애니메이터는 해부학적 코드를 더 일관되게 해석한다
- **Character DNA**: AI 일관성을 위해 잠긴 앵커 특징을 정의한다
- **Visual distinction audit**: 캐릭터가 여럿일 때 실루엣, 색상, 에너지의 구분을 점검한다

## 무엇에 쓰이는가

| 산출물 | 내용 |
|--------|------|
| **Character sheet** | 캐릭터 파일 — 심리, 의상, prop, FACS, AI prompt |
| **Costume bible** | 영화 전체에 걸친 의상 변형과 연속성 |
| **Props list** | 캐릭터의 개인 소지품과 그 극적 용도 |
| **FACS expression library** | 캐릭터별 3~5개의 시그니처 표정, AU 코드화 |
| **Casting brief** | 배우에게서 찾는 프로필 (이름은 제안하지 않고 특징을 정의) |
| **AI prompts** | 일관된 캐릭터 레퍼런스를 위한 base prompt + 장면 변형 |
| **Arc tracker** | 감독의 arc tracking과 조율된 캐릭터 변화 |
| **Continuity notes** | 장면별 의상/prop 연속성 |

## 언제 작동하는가

- 각본이 준비되어 캐릭터를 발전시키려 할 때
- "character sheet를 준비해 줘", "의상을 디자인해 줘", "캐스팅 프로필을 뽑아 줘"
- AI 영화를 위해 일관된 캐릭터 레퍼런스가 필요할 때
- 감독 또는 `creator-pipeline-supervisor`가 캐릭터 단계를 위임할 때
- 기존 캐릭터들의 시각적 구분이 문제로 제기될 때

## FACS 활용 — 왜, 그리고 어떻게

**Facial Action Coding System (Ekman & Friesen, 1978)** 은 얼굴 근육의 해부학적
코드화입니다. Action Unit(AU) = 특정한 근육 움직임.

### 이 스킬은 왜 이것을 사용하는가?

- **AI 생성기**는 "happy face" 같은 추상적 입력을 일관성 없게 해석한다;
  "AU6 + AU12 (Duchenne smile)"가 더 신뢰할 수 있는 결과를 낸다
- **애니메이션/VFX 팀**은 AU 코드를 통해 단일 레퍼런스 세트를 공유한다
- **캐릭터의 시그니처 표정**은 문서화할 수 있다 — 예를 들어 "Demir는 억눌린
  슬픔을 AU4 + AU17(이마를 찌푸리고, 턱을 들고, AU15 없음)로 짊어진다"

### 흔한 AU 조합

| 표정 | AU |
|------|-----|
| Duchenne smile (진짜 행복) | AU6 + AU12 |
| Polite smile (가짜/사교적) | AU12 단독 |
| 슬픔 | AU1 + AU4 + AU15 |
| 분노 | AU4 + AU5 + AU7 + AU23 |
| 공포 | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| 혐오 | AU9 + AU15 + AU16 |
| 놀람 | AU1 + AU2 + AU5B + AU26 |
| 경멸 (비대칭) | AU12 (한쪽) + AU14 |
| 억눌린 비탄 | AU4 + AU17 (AU15 없음) |
| 긴장된 평정 | AU7 + AU23 + AU24 |

## character sheet 템플릿 (요약)

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## 산출물을 어디에 기록하는가

`project/characters/{character-slug}/` 아래에:

| 파일 | 내용 |
|------|------|
| `character-sheet.md` | 정전(正典) 캐릭터 파일 |
| `costume-bible.md` | 모든 의상 변형 + 연속성 |
| `props.md` | 캐릭터의 소지품, 극적 용도 |
| `facs-expressions.md` | 시그니처 표정 라이브러리, AU 코드화 |
| `casting-brief.md` | 배우 프로필 / AI face prompt의 기초 |
| `ai-prompts.md` | Base prompt + 장면별 변형 |
| `arc-tracker.md` | 감독의 arc tracking과 sync |
| `continuity-notes.md` | 장면별 의상/prop 연속성 |

또한 상위 디렉터리에는 `cast-list.md`가 있습니다 — 모든 캐릭터를 요약한 목록.

## Visual distinction audit

캐릭터가 둘 이상일 때, 스킬은 다음 점검을 수행합니다:

- 실루엣 구분 (키, 자세, 의상 형태)
- 색채 세계 구분 (또는 의도적 대비)
- 에너지 register 구분
- 말투 패턴 구분
- 화면 존재감 구분 (foreground / background 유형)

두 캐릭터가 서로 "뒤섞이면" 이를 보고하고 수정을 제안합니다.

## AI 일관성 (Character DNA)

50개 장면에 걸쳐 동일한 얼굴/의상으로 같은 캐릭터를 생성하기 위해:

1. **Base prompt** — 핵심 특징(얼굴형, 머리카락, 식별 표식)을 고정
2. **Anchor descriptors** — 그중 2~3개가 모든 장면 prompt에서 반복 등장
3. **FACS를 통한 표정** — 형용사가 아니라 AU 코드화
4. **이른 character sheet 제작** — front/side/back/close 레퍼런스 이미지
5. **장면 prompt 내 참조**: "consistent with `characters/demir/sheet.png`"

## 다른 스킬과의 조율

- **읽음**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **씀**: `project/characters/*`
- **위임함**: 프롬프트 엔지니어, storyboard, DOP (팔레트 조율)
- **피드백 받음**: 감독, Pipeline Supervisor

## 의상 디자인 접근법

의상은 캐릭터를 이야기한다 — 단지 "입고 있는 것"이 아니다:

- 주요 아이템 + 그 기능
- 원단: 무겁고, 부드럽고, 뻣뻣하고, 섬유질의
- 색상: 팔레트와의 조화/대비
- 낡음 / 새것 / 손상 / 수선의 흔적
- 시대 정확성
- 캐릭터의 심정과의 관계
- 운동성에 미치는 영향
- 빛과의 상호작용 (무광, 광택, 투명, 먼지를 머금는)

각 메인 장면마다 의상 연속성 노트: 장면 안에서 바뀌는가, 장면 사이에서 바뀌는가,
왜?

## props 접근법

props는 이야기의 도구다 — 장식이 아니다:

- 이름 + 기능
- 캐릭터와의 관계
- 외관, 재질, 색상, 상태
- 캐릭터에게의 의미 (유품, 정체성, 관계)
- 극적 용도 (복선, payoff, 폭로)
- 카메라가 그것을 어떻게 보는가 (클로즈업, 디테일, 스쳐 지나감)
- 연속성 (각 장면에서 그것이 어디 있는가)

캐릭터-prop / 로케이션-prop 소유권을 명확히 하고, **creator-production-designer**
와 조율합니다.

## 행동 규칙

| 한다 | 하지 않는다 |
|------|-------------|
| 극적 근거와 함께 캐릭터를 생성한다 | "캐릭터가 하나 더 필요해"라고 말한다 |
| 모든 시각적 선택을 arc / 기능 / 테마에 연결한다 | 고립된 미적 선택을 한다 |
| 정보가 부족하면 질문한다 | 조용히 지어낸다 |
| 문화적 디테일을 조사한다 | 추측을 사실처럼 제시한다 |
| FACS AU 코드로 표정을 정의한다 | "슬프다" 같은 형용사를 쓴다 |
| visual distinction audit를 수행한다 | 두 캐릭터를 서로 뒤섞이게 둔다 |
| continuity anchors를 AI prompts에 심는다 | 매 장면 처음부터 묘사한다 |
| 캐릭터-prop 소유권을 명확히 한다 | 프로덕션 디자이너와 겹친다 |
| 구조화된 downstream-readable 파일을 전달한다 | 한 덩어리 텍스트를 쏟아낸다 |
