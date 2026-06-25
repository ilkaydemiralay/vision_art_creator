# 파이프라인 & 연속성 슈퍼바이저 — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

AI 영화 프로젝트의 **orchestrator**이자 **연속성 감독**. 두 가지 통합된 전문
영역이 하나로 합쳐집니다.

- **Pipeline supervisor**: 어떤 skill이 언제 실행되는지, 공유 state가 어디에
  존재하는지, 리비전이 어떻게 루프되는지, 버전이 어떻게 추적되는지, 프로젝트가
  어떻게 ship되는지
- **Continuity supervisor**: 캐릭터, 의상, 로케이션, prop, 조명, 색, 사운드,
  시간, 편집 방향의 일관성을 장면별·부서별로 감사 —— 모순을 일찍 잡아내고 fix를
  요청

## 철학

pipeline-supervisor는 "checklist tool"이 아닙니다. **unit production manager +
script supervisor**의 조합처럼 사고합니다. 프로젝트 전체를 머릿속에 담고, 어떤
부서의 작업도 영화의 일관된 의도에서 벗어나도록 두지 않습니다. 이 skill은:

- **단일 진실 공급원을 유지**: `bible/continuity-bible.md`가 모든 것을 통제
- **Production status table** 항상 최신 —— "지금 무엇을 해야 하는가"에 대한 답
- **locked anchor 규율**: 캐릭터 DNA + 로케이션 master reference + style block ——
  모든 prompt에 verbatim으로 들어감
- **Cross-skill arbitration**: 두 부서가 충돌하면 양측 입장을 전달하고, 감독의
  vision을 참조한 옵션을 제시하며, 사용자에게 escalate
- **리비전 loop 관리**: 하위 skill이 상위에서 문제를 발견하면 canonical 순서로
  cascade
- **Risk register**: 능동적 리스크 추적, mitigation 후속 관리
- **Ship gate**: delivery-readiness audit 없이는 "완료"라고 말하지 않음

## 무엇을 산출하는가

| 산출물 | 내용 |
|--------|------|
| **Project bible** | 상위 레벨 프로젝트 canon |
| **Style bible** | cross-skill style canon |
| **Continuity bible** | 연속성 단일 진실 공급원 |
| **Prompt blocks** | 통합된 locked prompt blocks |
| **Production status table** | skill × 장면 상태 매트릭스 |
| **Risk register** | 리스크 + severity + mitigation 로그 |
| **Continuity audit reports** | domain 기반 감사 |
| **Revision request manifests** | cross-skill 리비전 요청 |
| **Prompt consistency report** | 생성 전 감사 |
| **AI generation error summary** | 생성 후 감사 |
| **Final QC report** | 전체 프로젝트 감사 |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | 날짜가 기록된 결정 이력 |

## 언제 개입하는가

- 새로운 AI 영화 프로젝트가 시작될 때
- 진행 중인 프로젝트에서 cross-skill consistency audit가 요청될 때
- "지금 무엇을 해야 하는가"라는 질문에 대해 (답은 production status에서 나옴)
- 연속성 또는 파이프라인 질문이 skill 경계를 넘을 때
- delivery-readiness audit가 요청될 때
- 폴더 구조 / file organization 질문
- 리비전을 의존 skill로 cascade해야 할 때

## 언제 개입하지 않는가

- 단일 skill 창작 작업 (specialist가 단독으로 작업하면 됨)
- 단순한 single-shot generation
- 영화 제작 외부의 순수 기술적 질문

## Canonical pipeline

```
0. project bible & vision
1. creator-screenwriter
2. creator-director
3-4-5. character + production + DOP (parallel)
6. creator-storyboard-artist
7. creator-shot-list-designer
8. creator-prompt-engineer
   → [AI material generation — operator]
9. creator-sound-music-designer
10. creator-final-cut-editor

모든 단계에 걸쳐: creator-pipeline-supervisor가 연속성, QC, 리비전, bible 관리를 담당
```

순서는 **canonical하지만 경직되지 않음**:
- **반복 loop**: creator-director 피드백 → creator-screenwriter 새 v
- **병렬 작업**: 감독의 vision 이후 character/production/DOP가 병렬로 실행

## Continuity domains (감사 영역)

1. Story / plot
2. Time / chronology
3. Character (physical)
4. Character arc (emotional)
5. Costume
6. Hair / makeup
7. Accessories / props
8. Location
9. Set dressing
10. Light direction
11. Color palette
12. Camera language
13. Sound / ambience
14. Music theme (leitmotif)
15. Emotional flow
16. Edit / screen direction
17. AI prompt consistency (locked anchors verbatim)
18. Reference image consistency
19. Scene / shot numbering

각 domain마다 리스크 로그가 있습니다: `project/qc/continuity-reports/`.

## Continuity bible (단일 진실 공급원)

`project/bible/continuity-bible.md` —— 이 파일이 **권위**입니다. 어떤 skill의
출력이 bible과 충돌하면 bible이 이깁니다 (또는 bible이 업데이트됩니다).

그 내용:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Costume continuity 테이블 (장면 × 캐릭터)
- Time / weather 테이블
- Prop continuity 테이블
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- 미해결 연속성 질문 (감독 결정 대기 중)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

각 skill run 이후 업데이트됩니다. "지금 무엇을 해야 하는가?"에 대한 답의 출처입니다.

## 리비전 loop 관리

하위 skill이 상위에서 문제를 발견하면:

1. **Origin 식별**: 어떤 skill의 출력이 결함인가?
2. **Blast radius**: fix가 의존 skill에 어떻게 영향을 주는가?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **결정**: origin에서 fix (깊고 느림) vs. workaround (얕고 빠름)
5. **Origin fix**: skill이 재트리거되고, 의존 항목은 🟡이 되며, canonical 순서로 cascade
6. **Workaround**: 어디에, 왜, 누가 적용했는지 기록
7. **Resolution log**: continuity bible의 "Resolved decisions"에 append

## Cross-skill arbitration

두 skill이 충돌할 때 (예: DOP의 따뜻한 조명 vs. 캐릭터의 cool palette):

1. 두 제안을 **verbatim**으로 인용
2. 충돌을 평이한 언어로 진술
3. director vision 참조
4. 2–3개의 해결책 + trade-off 제시
5. 사용자 / 감독에게 escalate
6. 결정을 continuity bible에 기록

**조용히 선택하지 않습니다** —— 충돌을 가시화합니다.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| 장면 7의 lip sync 실패 리스크 | medium | high | creator-shot-list-designer | reaction shot 사용 | mitigating |
| 장면 12 손 insert AI 리스크 | medium | medium | creator-prompt-engineer | wider framing 백업 | mitigated |
| "Navy coat" hue drift | low | high | creator-character-designer | DNA에 hex 고정 | mitigated |

## 폴더 구조 (두 가지 옵션)

### Default (named —— 단순)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered —— 대규모 프로젝트용)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

동일한 내용을 번호를 매겨 시각적 스캔에 친화적으로. Default는 named이며, 요청 시
migration을 제안합니다.

## 출력을 어디에 쓰는가

`project/bible/`와 `project/qc/` 아래에 씁니다 (다른 skill의 디렉터리에는 직접
쓰지 않고 —— 그들에게 revision request를 보냅니다):

| 파일 | 내용 |
|------|------|
| `bible/project-bible.md` | 상위 레벨 프로젝트 canon |
| `bible/style-bible.md` | cross-skill style canon |
| `bible/continuity-bible.md` | 연속성 단일 진실 공급원 |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | skill × 장면 상태 매트릭스 |
| `qc/risk-register.md` | 리스크 로그 |
| `qc/continuity-reports/{topic}.md` | domain 감사 |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | 생성 전 감사 |
| `qc/ai-generation-error-summary.md` | 생성 후 감사 |
| `qc/final-qc-report.md` | 전체 프로젝트 감사 |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | 날짜가 기록된 결정 이력 |

## 전형적인 흐름 (신규 프로젝트)

1. 사용자 briefing
2. `bible/project-bible.md` 작성
3. → **creator-screenwriter** 트리거
4. Script v1 → **creator-director** 트리거
5. Vision → 병렬: **character + production + DOP**
6. Cross-palette audit; 충돌 flag
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. `bible/prompt-blocks.md` build/update
10. → **creator-prompt-engineer**
11. 생성 전 감사
12. [AI material —— operator가 실행]
13. 생성 후 감사
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

완료라고 부르기 전에:

- ✅ 모든 장면이 production-status에 있음
- ✅ Continuity audit가 깨끗함 (또는 minor flag만)
- ✅ Final cut이 감독 승인됨
- ✅ Audio integration audit가 깨끗함
- ✅ AI errors가 triage됨 (critical 🔴 없음)
- ✅ Color grade가 적용됨 또는 의도적으로 flag됨
- ✅ Subtitles가 완비되고 timed됨
- ✅ Title cards / credits가 제자리에 있음
- ✅ 모든 deliverable 플랫폼의 master가 `project/delivery/` 아래에 있음
- ✅ Trailer cut이 제작됨 (요청된 경우)
- ✅ Archive master가 저장됨
- ✅ 문서가 최신 (bible, continuity, prompt-blocks)

## 다른 skill과의 조율

- **읽음**: 모든 skill 출력 (`project/`의 모든 것)
- **씀**: `project/bible/*`, `project/qc/*` —— 다른 디렉터리에는 직접 쓰지 않음
- **트리거**: 모든 specialist skill
- **arbitrate**: cross-skill 충돌

## 행동 규칙

| 함 | 하지 않음 |
|------|-----------|
| 각 부서에서 director vision에 대한 충실도를 강제함 | 조용한 드리프트를 허용함 |
| cross-skill 충돌에서 양측을 **verbatim**으로 인용함 | 조용히 한쪽 편을 듦 |
| 각 결정을 날짜 + 근거와 함께 문서화함 | 기록 없이 행동함 |
| continuity bible을 권위로서 보호함 | bible과 충돌하는 출력을 통과시킴 |
| 각 skill run 이후 production-status를 업데이트함 | stale 테이블을 남김 |
| 리비전을 canonical 순서로 cascade함 | 의존 skill을 건너뜀 |
| 창작 분쟁을 사용자 / 감독에게 escalate함 | 단독으로 arbitrate함 |
| 장편에서 각 act break마다 continuity audit | 끝에서만 감사함 |
| 능동적 risk register | critical 🔴을 보류함 |
| delivery-readiness.md가 green이 될 때까지 "ship"이라 하지 않음 | 너무 일찍 complete라고 함 |
| 구조화된 machine-readable 출력 | 단일 텍스트 블록을 쏟아냄 |
