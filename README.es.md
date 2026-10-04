# vision_art_creator

[English](README.md) · [中文](README.zh.md) · **Español** · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> Un paquete de skills de producción cinematográfica con IA para [Claude Code](https://claude.com/claude-code).

`vision_art_creator` reúne **11 skills `creator-*`** que cubren todos los
departamentos de una producción cinematográfica —desde el guion hasta el
montaje final— en un único repositorio. Instálalo en cualquier máquina con
`git clone` + `./install.sh`.

> Las skills están diseñadas para hacer referencia unas a otras
> (`creator-pipeline-supervisor` orquesta el resto). Se recomienda instalarlas
> todas juntas.

---

## Instalación

```bash
git clone https://github.com/ilkaydemiralay/vision_art_creator.git ~/projects/vision_art_creator
cd ~/projects/vision_art_creator
./install.sh
```

`install.sh` crea un **enlace simbólico** para cada skill en
`~/.claude/skills/<skill-name>` que apunta de vuelta a este repositorio. La
ventaja: para actualizar basta con un simple `git pull` —no hace falta
reinstalar.

### Opciones

```bash
./install.sh --target /path/to/skills   # instalar en otro directorio de skills
./install.sh --force                    # sobrescribir nombres existentes
./uninstall.sh                          # eliminar los enlaces simbólicos
```

`uninstall.sh` solo elimina los enlaces simbólicos que apuntan a este
repositorio —deja intactos los enlaces externos y los directorios reales (a
menos que se use `--force`).

### Verificación

Tras la instalación, reinicia Claude Code y escribe:

```
/creator-pipeline-supervisor
```

Comprueba que las 11 skills `creator-*` aparecen en la lista de skills.

---

## Qué incluye el paquete

| Skill | Resumen |
|---|---|
| `creator-pipeline-supervisor` | Orquesta toda la producción, secuencia los departamentos, garantiza la continuidad, ejecuta el control de calidad y genera el informe de preparación para la entrega. |
| `creator-director` | Traduce el guion en una visión de dirección unificada: dirección de escena, interpretación, blocking, control tonal. |
| `creator-screenwriter` | Escritura y revisión de guiones, tratamientos, loglines, escaletas y diálogos. |
| `creator-character-designer` | Diseña al personaje como un todo integrado: psicología, biografía, identidad visual, vestuario, atrezo, expresiones codificadas con FACS. |
| `creator-production-designer` | Construye el mundo de la película: localizaciones, decorados, atrezo, atmósfera de época, lenguaje de color y materiales, anclas de continuidad. |
| `creator-cinematographer` | Diseña el lenguaje visual: luz, cámara, óptica, encuadre, color, atmósfera, movimiento. |
| `creator-storyboard-artist` | Visualiza las escenas viñeta a viñeta: escalas de plano, ángulos, blocking, composición, prompts de IA. |
| `creator-shot-list-designer` | Convierte escenas y storyboards en una lista de planos técnica, dividida en fragmentos producibles por IA. |
| `creator-sound-music-designer` | El mundo sonoro de la película: atmósfera, foley, efectos de sonido, banda sonora, leitmotivs, plan musical escena por escena, prompts de audio para IA. |
| `creator-prompt-engineer` | Convierte la salida de cada departamento en prompts coherentes para GPT Image 2.0, Nano Banana, Sora, Veo, Runway, Kling, Higgsfield y más. |
| `creator-final-cut-editor` | Ensambla los planos, el audio, la música y los gráficos generados por IA en una película terminada: rough/fine/final cut, triaje de errores de IA, formatos de entrega. |

La definición completa de cada skill se encuentra en su propio archivo `SKILL.md`.

---

## Cómo funciona

El paquete funciona sobre un **estado compartido basado en el sistema de
archivos**. Todas las skills leen y escriben en un árbol `project/` común
(`bible/`, `screenplay/`, `characters/`, `storyboards/`, `prompts/`, `cuts/`,
`qc/`, …). `creator-pipeline-supervisor` mantiene los archivos canónicos (las
"biblias" del proyecto y de continuidad) y audita la salida de cada
departamento contrastándola con ellos.

El pipeline canónico:

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

La secuencia es canónica pero no rígida: el feedback del director puede volver
a activar al guionista, y los departamentos de personaje/producción/fotografía
suelen ejecutarse en paralelo una vez fijada la visión de dirección.

---

## Modo de grafo registrado (opcional, experimental)

Desde la v1.1.0, el paquete incluye un flujo de trabajo opcional y verificable por máquina para una sola escena. `creator-pipeline-supervisor` puede ejecutar la preproducción como un grafo de 12 nodos: cada artefacto se registra con su hash SHA-256, cada aprobación queda vinculada a las entradas exactas que revisó y una revisión solo vuelve a ejecutar los nodos afectados.

- Flujo: `workflows/single-scene.v1.json`. Contrato: `skills/creator-pipeline-supervisor/references/graph-workflow.md`.
- Esquemas JSON en `schemas/`, un validador de solo lectura en `scripts/validate_graph.py` y pruebas en `tests/`.
- Un piloto de texto completo de 15 segundos y tres planos en `examples/single-scene/`: v00 se detiene en un conflicto de diseño, v01 lo resuelve y v02 cambia el color de un objeto.

El uso normal de las skills no requiere Python. Para ejecutar el validador (Python 3.10+):

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-graph.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/validate_graph.py validate --manifest path/to/manifest.json
```

Límites: es un piloto solo de texto escrito por un único autor. No se probaron departamentos en paralelo, generación de medios, montaje ni costes. La identidad de quien aprueba y las marcas de tiempo las declara el operador; no están firmadas. Las notas de diseño y resultados están en `docs/` (en turco).

---

## Actualización

```bash
cd ~/projects/vision_art_creator
git pull
```

Como las skills están enlazadas simbólicamente, no se necesita ningún paso
adicional.

Consulta [CHANGELOG.md](CHANGELOG.md) para ver qué cambió en cada versión. **v1.1.0:** `creator-cinematographer` y `creator-storyboard-artist` guardan ahora sus borradores de prompts en sus propias carpetas; solo `creator-prompt-engineer` escribe los prompts finales en `project/prompts/`.

---

## Desarrollo

1. Edita una skill en el repositorio (`skills/creator-*/SKILL.md`).
2. Prueba el cambio en Claude Code —al ser un enlace simbólico, surte efecto
   de inmediato.
3. Haz commit + push.

Para añadir una nueva skill creator:

```bash
mkdir -p skills/creator-new-skill
# write SKILL.md and README.md
./install.sh   # create the symlink for the new skill
```

---

## Traducciones

Este README y el `README.md` de cada skill están disponibles en 12 idiomas
(consulta el selector de idiomas en la parte superior). Los archivos de
instrucciones `SKILL.md` se mantienen en inglés de forma deliberada: Claude
responde en el idioma del usuario en tiempo de ejecución, y un único conjunto
de instrucciones canónico evita nombres de skill duplicados.

---

## Licencia

[MIT](LICENSE) © 2026 İlkay Demiralay.
