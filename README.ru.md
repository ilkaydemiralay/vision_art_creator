# vision_art_creator

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Русский** · [日本語](README.ja.md) · [한국어](README.ko.md)

> Набор навыков для кинопроизводства с помощью ИИ для [Claude Code](https://claude.com/claude-code) и [OpenAI Codex](https://github.com/openai/codex).

`vision_art_creator` объединяет **11 навыков `creator-*`**, которые охватывают
каждый отдел кинопроизводства — от сценария до финального монтажа — в одном
репозитории. Установите его на любой машине с помощью `git clone` +
`./install.sh`.

> Навыки спроектированы так, чтобы ссылаться друг на друга
> (`creator-pipeline-supervisor` управляет остальными). Рекомендуется
> устанавливать их все вместе.

---

## Демо: *Before She Leaves*

Сцена длиной 26 секунд, созданная с этим набором и Higgsfield (референсы Nano Banana Pro, клипы Seedance 2.0), и 30-секундный ролик о создании, показывающий записанный граф: ответственных, хеши и согласования. Два агента, Claude Code и OpenAI Codex, работали с одними и теми же файлами навыков. Все кадры созданы ИИ.

| Фильм (26 с) | Как это сделано (30 с) |
|---|---|
| [![Фильм (26 с)](docs/media/demo-film.jpg)](https://github.com/ilkaydemiralay/vision_art_creator/releases/download/v1.2.0/before-she-leaves-film.mp4) | [![Как это сделано (30 с)](docs/media/demo-making-of.jpg)](https://github.com/ilkaydemiralay/vision_art_creator/releases/download/v1.2.0/before-she-leaves-making-of.mp4) |

---

## Установка

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

Используете OpenAI Codex? Установите навыки в его каталог и перезапустите Codex:

```bash
./install.sh --codex   # ~/.agents/skills/
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

## Режим записанного графа (необязательный, экспериментальный)

Начиная с v1.1.0 пакет содержит необязательный, проверяемый машиной рабочий процесс для одной сцены. `creator-pipeline-supervisor` может вести препродакшн как граф из 12 узлов: каждый артефакт записывается со своим хешем SHA-256, каждое одобрение привязано к точным входным данным, которые оно проверило, а ревизия перезапускает только затронутые узлы.

- Процесс: `workflows/single-scene.v1.json`. Контракт: `skills/creator-pipeline-supervisor/references/graph-workflow.md`.
- JSON-схемы в `schemas/`, валидатор только для чтения в `scripts/validate_graph.py`, тесты в `tests/`.
- Готовый текстовый пилот на 15 секунд и три плана в `examples/single-scene/`: v00 останавливается на конфликте дизайна, v01 его решает, v02 меняет цвет одного реквизита.

Для обычного использования навыков Python не нужен. Запуск валидатора (Python 3.10+):

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/validate_graph.py validate --manifest path/to/manifest.json
```

Ограничения: это только текстовый пилот одного автора. Параллельная работа отделов, генерация медиа, монтаж и стоимость не проверялись. Личность одобряющего и метки времени указывает оператор, они не подписаны. Заметки по дизайну и результатам находятся в `docs/` (на турецком).

---

## Обновление

```bash
cd ~/projects/vision_art_creator
git pull
```

Поскольку навыки подключены через символические ссылки, дополнительных
действий не требуется.

Изменения каждой версии описаны в [CHANGELOG.md](CHANGELOG.md). **v1.1.0:** `creator-cinematographer` и `creator-storyboard-artist` теперь хранят черновики промптов в своих папках; итоговые промпты в `project/prompts/` пишет только `creator-prompt-engineer`.

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
