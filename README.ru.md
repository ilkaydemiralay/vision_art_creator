# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Русский** · [日本語](README.ja.md) · [한국어](README.ko.md)

> Набор навыков для кинопроизводства с помощью ИИ для [Claude Code](https://claude.com/claude-code).

`vision_art_creator` объединяет **11 навыков `creator-*`**, которые охватывают
каждый отдел кинопроизводства — от сценария до финального монтажа — в одном
репозитории. Установите его на любой машине с помощью `git clone` +
`./install.sh`.

> Навыки спроектированы так, чтобы ссылаться друг на друга
> (`creator-pipeline-supervisor` управляет остальными). Рекомендуется
> устанавливать их все вместе.

---

## Установка

```bash
git clone https://github.com/<your-username>/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh` создаёт **символическую ссылку** для каждого навыка в
`~/.claude/skills/<skill-name>`, указывающую обратно в этот репозиторий.
Преимущество: для обновления достаточно простого `git pull` — переустановка
не требуется.

### Параметры

```bash
./install.sh --target /path/to/skills   # установить в другой каталог навыков
./install.sh --force                    # перезаписать существующие имена
./uninstall.sh                          # удалить символические ссылки
```

`uninstall.sh` удаляет только те символические ссылки, которые ведут в этот
репозиторий — он не трогает сторонние ссылки и реальные каталоги (если не
указан `--force`).

### Проверка

После установки перезапустите Claude Code и введите:

```
/creator-pipeline-supervisor
```

Убедитесь, что все 11 навыков `creator-*` появились в списке навыков.

---

## Что входит в набор

| Навык | Описание |
|---|---|
| `creator-pipeline-supervisor` | Управляет всем производством, выстраивает последовательность работы отделов, обеспечивает преемственность, проводит контроль качества и формирует отчёт о готовности к сдаче. |
| `creator-director` | Превращает сценарий в единое режиссёрское видение: режиссура сцен, актёрская игра, мизансцена, контроль тональности. |
| `creator-screenwriter` | Написание и редактирование сценариев, тритментов, логлайнов, поэпизодных планов и диалогов. |
| `creator-character-designer` | Проектирует персонажа как единое целое: психология, биография, визуальная идентичность, костюм, реквизит, мимика с кодировкой FACS. |
| `creator-production-designer` | Создаёт мир фильма: локации, декорации, реквизит, атмосферу эпохи, язык цвета и материалов, опорные точки преемственности. |
| `creator-cinematographer` | Разрабатывает визуальный язык: свет, камеру, оптику, кадрирование, цвет, атмосферу, движение. |
| `creator-storyboard-artist` | Визуализирует сцены панель за панелью: крупности планов, ракурсы, мизансцену, композицию, промпты для ИИ. |
| `creator-shot-list-designer` | Превращает сцены и раскадровки в технический shot list, разбитый на производимые ИИ фрагменты. |
| `creator-sound-music-designer` | Звуковой мир фильма: атмосфера, foley, SFX, музыка, лейтмотивы, поэпизодный музыкальный план, промпты для ИИ-аудио. |
| `creator-prompt-engineer` | Преобразует результаты каждого отдела в согласованные промпты для GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield и других. |
| `creator-final-cut-editor` | Собирает сгенерированные ИИ кадры/аудио/музыку/графику в готовый фильм: rough/fine/final cut, разбор ошибок ИИ, форматы сдачи. |

Полное определение каждого навыка находится в его собственном файле `SKILL.md`.

---

## Как это работает

Набор работает на основе **общего состояния через файловую систему**. Все
навыки читают из общего дерева `project/` и пишут в него (`bible/`,
`screenplay/`, `characters/`, `storyboards/`, `prompts/`, `cuts/`, `qc/`, …).
`creator-pipeline-supervisor` поддерживает канонические файлы (проектную
«библию» и «библию» преемственности) и сверяет с ними результаты работы
каждого отдела.

Канонический конвейер:

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

Последовательность канонична, но не жёстко фиксирована: отзыв режиссёра может
заново запустить сценариста, а отделы персонажей/производственного дизайна/
операторской работы обычно работают параллельно после того, как
режиссёрское видение определено.

---

## Обновление

```bash
cd ~/projects/vision_art_creator
git pull
```

Поскольку навыки подключены через символические ссылки, дополнительных
действий не требуется.

---

## Разработка

1. Отредактируйте навык в репозитории (`skills/creator-*/SKILL.md`).
2. Проверьте изменение в Claude Code — поскольку это символическая ссылка,
   оно вступает в силу немедленно.
3. Зафиксируйте изменения (commit) и отправьте (push).

Чтобы добавить новый навык creator:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## Переводы

Этот README и `README.md` каждого навыка доступны на 12 языках (см. переключатель
языков вверху). Файлы инструкций `SKILL.md` намеренно оставлены на английском
языке — Claude отвечает на языке пользователя во время выполнения, а единый
канонический набор инструкций позволяет избежать дублирования имён навыков.

---

## Лицензия

[MIT](LICENSE) © 2026 İlkay Demiralay.
