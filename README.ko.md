# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · **한국어**

> [Claude Code](https://claude.com/claude-code)를 위한 AI 영화 제작 스킬 팩.

`vision_art_creator`는 영화 제작의 모든 부서를 아우르는 **11개의 `creator-*`
스킬**을 — 시나리오에서 최종 편집본까지 — 하나의 저장소에 묶어 제공합니다.
`git clone` + `./install.sh`만으로 어떤 머신에든 설치할 수 있습니다.

> 이 스킬들은 서로를 참조하도록 설계되어 있습니다
> (`creator-pipeline-supervisor`가 나머지를 총괄합니다). 모두 함께
> 설치하는 것을 권장합니다.

---

## 설치

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh`는 각 스킬에 대해 이 저장소를 가리키는 **심링크**를
`~/.claude/skills/<skill-name>` 아래에 생성합니다. 장점은, 업데이트할 때
간단한 `git pull`만으로 충분하다는 것입니다 — 재설치가 필요 없습니다.

### 옵션

```bash
./install.sh --target /path/to/skills   # 다른 스킬 디렉터리에 설치
./install.sh --force                    # 기존 이름 덮어쓰기
./uninstall.sh                          # 심링크 제거
```

`uninstall.sh`는 이 저장소를 가리키는 심링크만 제거합니다 — 외부 링크와
실제 디렉터리는 (`--force`가 아닌 한) 그대로 둡니다.

### 확인

설치 후 Claude Code를 재시작하고 다음을 입력하세요:

```
/creator-pipeline-supervisor
```

11개의 `creator-*` 스킬이 모두 스킬 목록에 나타나는지 확인하세요.

---

## 팩 구성

| 스킬 | 요약 |
|---|---|
| `creator-pipeline-supervisor` | 제작 전반을 총괄하며, 부서 작업의 순서를 정하고, 연속성을 강제하며, QC를 실행하고, 납품 준비 보고서를 작성합니다. |
| `creator-director` | 시나리오를 일관된 연출 비전으로 변환합니다: 장면 연출, 연기, 블로킹, 톤 조절. |
| `creator-screenwriter` | 시나리오, 트리트먼트, 로그라인, 장면 개요, 대사를 집필하고 수정합니다. |
| `creator-character-designer` | 캐릭터를 통합된 전체로 설계합니다: 심리, 약력, 시각적 정체성, 의상, 소품, FACS 코딩된 표정. |
| `creator-production-designer` | 영화의 세계를 구축합니다: 로케이션, 세트, 소품, 시대 분위기, 색/재질 언어, 연속성 앵커. |
| `creator-cinematographer` | 시각 언어를 설계합니다: 빛, 카메라, 렌즈, 프레이밍, 색, 분위기, 움직임. |
| `creator-storyboard-artist` | 장면을 패널 단위로 시각화합니다: 샷 스케일, 앵글, 블로킹, 구도, AI 프롬프트. |
| `creator-shot-list-designer` | 장면과 스토리보드를 기술적 샷 리스트로 전환하고, AI로 제작 가능한 단위로 쪼갭니다. |
| `creator-sound-music-designer` | 영화의 음향 세계를 다룹니다: 분위기, 폴리, SFX, 스코어, 라이트모티프, 장면별 음악 계획, AI 오디오 프롬프트. |
| `creator-prompt-engineer` | 각 부서의 산출물을 GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield 등을 위한 일관된 프롬프트로 변환합니다. |
| `creator-final-cut-editor` | AI로 생성된 샷/오디오/음악/그래픽을 완성된 영화로 조립합니다: 러프/파인/파이널 컷, AI 오류 분류, 납품 포맷. |

각 스킬의 전체 정의는 각자의 `SKILL.md` 파일에 담겨 있습니다.

---

## 작동 방식

이 팩은 **파일시스템 기반 공유 상태**로 동작합니다. 모든 스킬은 공통의
`project/` 트리(`bible/`, `screenplay/`, `characters/`, `storyboards/`,
`prompts/`, `cuts/`, `qc/` 등)에서 읽고 씁니다.
`creator-pipeline-supervisor`는 정본 파일(프로젝트 및 연속성 "바이블")을
유지하고, 모든 부서의 산출물을 그에 비추어 점검합니다.

정본 파이프라인:

```
0. project bible & vision
1. creator-screenwriter        → screenplay
2. creator-director            → vision, direction sheets, arcs
3-4-5. creator-character-designer + creator-production-designer
        + creator-cinematographer        (run in parallel)
6. creator-storyboard-artist   → panels with prompts
7. creator-shot-list-designer  → shot list + edit plan
8. creator-prompt-engineer     → tool-fit image + video prompts
   → [AI material generation — operator]
9. creator-sound-music-designer → sound + score plan
10. creator-final-cut-editor   → rough → fine → final cut → delivery

Throughout: creator-pipeline-supervisor enforces continuity, runs QC,
manages revision loops, and holds the bibles.
```

이 순서는 정본이되 경직된 것은 아닙니다: 감독의 피드백이 작가를 다시
가동시킬 수 있고, 연출 비전이 정해지면 캐릭터/프로덕션/촬영은 보통
병렬로 진행됩니다.

---

## 업데이트

```bash
cd ~/projects/vision_art_creator
git pull
```

스킬들이 심링크로 연결되어 있기 때문에 별도의 단계가 필요하지 않습니다.

---

## 개발

1. 저장소에서 스킬을 편집합니다(`skills/creator-*/SKILL.md`).
2. Claude Code에서 변경을 테스트합니다 — 심링크이므로 즉시
   적용됩니다.
3. 커밋 + 푸시합니다.

새 creator 스킬을 추가하려면:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## 번역

이 README와 각 스킬의 `README.md`는 12개 언어로 제공됩니다(상단의 언어
선택기 참조). `SKILL.md` 지시 파일은 의도적으로 영어로 유지합니다 —
Claude는 런타임에 사용자의 언어로 응답하며, 단일 정본 지시 세트는
중복된 스킬 이름을 방지하기 때문입니다.

---

## 라이선스

[MIT](LICENSE) © 2026 İlkay Demiralay.
