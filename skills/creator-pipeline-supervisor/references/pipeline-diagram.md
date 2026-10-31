# Pipeline diagram

Visual form of the canonical sequence described in SKILL.md.

```
                 ┌────────────────────────────────┐
                 │  0. Project bible & vision     │
                 │  - logline, scope, format      │
                 │  - working language            │
                 │  - AI tools targeted           │
                 └──────────────┬─────────────────┘
                                │
                                ▼
            ┌─────────────────────────────────────────┐
            │  1. creator-screenwriter                        │
            │  → screenplay (logline → script v01)    │
            └─────────────┬───────────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────────┐
            │  2. creator-director                            │
            │  → vision, direction sheets, arcs       │
            └──┬──────────┬───────────┬────────┬──────┘
               │          │           │        │
               ▼          ▼           ▼        ▼
   ┌──────────┐  ┌─────────────────┐  ┌────────────────┐
   │ 3. char- │  │ 4. production-  │  │ 5. cinemato-   │
   │ designer │  │    designer     │  │    grapher     │
   └────┬─────┘  └────────┬────────┘  └────────┬───────┘
        │                 │                    │
        └────────┬────────┴────────┬───────────┘
                 │                 │
                 ▼                 ▼
            ┌─────────────────────────────────────────┐
            │  6. creator-storyboard-artist                   │
            │  → panels with prompts                  │
            └─────────────┬───────────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────────┐
            │  7. creator-shot-list-designer                  │
            │  → shot list + edit plan + transitions  │
            └─────────────┬───────────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────────┐
            │  8. creator-prompt-engineer                     │
            │  → tool-fit image + video prompts       │
            └─────────────┬───────────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────────┐
            │  AI material generation (operator)      │
            │  → images, videos, audio                │
            └─────────────┬───────────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────────┐
            │  9. creator-sound-music-designer                │
            │  → sound + score plan and AI audio      │
            └─────────────┬───────────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────────┐
            │  10. creator-final-cut-editor                   │
            │  → rough → fine → final cut → delivery  │
            └─────────────────────────────────────────┘

  creator-pipeline-supervisor monitors all stages, enforces continuity,
  runs cross-cutting QC, manages revision loops, holds the bible.
```
