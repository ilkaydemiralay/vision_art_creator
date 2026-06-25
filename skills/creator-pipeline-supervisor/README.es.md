# Supervisor de Pipeline y Continuidad — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

El **orchestrator** y el **supervisor de continuidad** de un proyecto de cine
con IA. Se combinan dos disciplinas integradas:

- **Pipeline supervisor**: qué skill se ejecuta y cuándo, dónde vive el estado
  compartido, cómo se ciclan las revisiones, cómo se rastrean las versiones,
  cómo se hace el ship del proyecto
- **Continuity supervisor**: audita la coherencia de personaje, vestuario,
  localización, prop, luz, color, sonido, tiempo y dirección de montaje escena
  por escena y departamento por departamento — detecta contradicciones a
  tiempo, solicita correcciones

## Filosofía

El pipeline-supervisor no es una "checklist tool". Piensa como una combinación
de **unit production manager + script supervisor**. Mantiene todo el proyecto
en la cabeza y no deja que el trabajo de ningún departamento se desvíe de la
intención coherente de la película. Esta skill:

- **Mantiene una única fuente de verdad**: `bible/continuity-bible.md` gobierna
  todo
- **Production status table** siempre actualizada — la respuesta a "qué debo
  hacer ahora"
- **Disciplina de locked anchor**: ADN del personaje + master reference de la
  localización + style block — entra verbatim en cada prompt
- **Cross-skill arbitration**: cuando dos departamentos entran en conflicto,
  transmite ambas posturas, presenta opciones referidas a la visión del
  director y escala al usuario
- **Gestión del revision loop**: cuando una skill downstream encuentra un
  problema upstream, hace cascade en orden canónico
- **Risk register**: seguimiento proactivo del riesgo, control de la mitigación
- **Ship gate**: no dice "listo" sin una auditoría de delivery-readiness

## Qué produce

| Salida | Contenido |
|--------|-----------|
| **Project bible** | Canon del proyecto de alto nivel |
| **Style bible** | Canon de estilo cross-skill |
| **Continuity bible** | Única fuente de verdad de continuidad |
| **Prompt blocks** | Locked prompt blocks consolidados |
| **Production status table** | Matriz de estado skill × escena |
| **Risk register** | Log de riesgo + severity + mitigación |
| **Continuity audit reports** | Auditorías por dominio |
| **Revision request manifests** | Solicitudes de revisión cross-skill |
| **Prompt consistency report** | Auditoría pre-generación |
| **AI generation error summary** | Auditoría post-generación |
| **Final QC report** | Auditoría de todo el proyecto |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | Historial de decisiones con fecha |

## Cuándo interviene

- Se inicia un nuevo proyecto de cine con IA
- Se solicita una auditoría de consistencia cross-skill en un proyecto en curso
- Ante la pregunta "qué hago ahora" (la respuesta viene del production status)
- Cuando una cuestión de continuidad o pipeline cruza el límite de una skill
- Se solicita una auditoría de delivery-readiness
- Cuestión de estructura de carpetas / file organization
- Cuando una revisión debe hacer cascade a skills dependientes

## Cuándo NO interviene

- Trabajos creativos de una sola skill (que el specialist trabaje solo)
- Generación simple de un único shot
- Cuestiones puramente técnicas fuera de la producción cinematográfica

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

A lo largo de todas las etapas: creator-pipeline-supervisor gestiona continuidad, QC, revisión, gestión de la bible
```

El orden es **canónico pero no rígido**:
- **Loops iterativos**: feedback de creator-director → nueva v de creator-screenwriter
- **Trabajo en paralelo**: tras la visión del director, character/production/DOP
  corren en paralelo

## Continuity domains (áreas de auditoría)

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

Hay un log de riesgo para cada dominio: `project/qc/continuity-reports/`.

## Continuity bible (única fuente de verdad)

`project/bible/continuity-bible.md` — este archivo es la **autoridad**. Si la
salida de una skill entra en conflicto con la bible, gana la bible (o se
actualiza la bible).

Su contenido:
- Locked character anchors (ADN verbatim)
- Locked location anchors (master reference verbatim)
- Tabla de costume continuity (escena × personaje)
- Tabla de time / weather
- Tabla de prop continuity
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Preguntas de continuidad abiertas (a la espera de una decisión del director)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Se actualiza tras cada skill run. La fuente de la respuesta a "¿qué hago ahora?"

## Gestión del revision loop

Cuando una skill downstream encuentra un problema upstream:

1. **Detección del origin**: ¿la salida de qué skill es defectuosa?
2. **Blast radius**: ¿cómo afecta la corrección a las skills dependientes?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **Decisión**: corregir en el origin (profundo, lento) vs. workaround (superficial, rápido)
5. **Origin fix**: la skill se re-dispara, las dependientes pasan a 🟡, cascade en orden canónico
6. **Workaround**: se registra dónde, por qué y quién lo aplicó
7. **Resolution log**: se añade a "Resolved decisions" de la continuity bible

## Cross-skill arbitration

Cuando dos skills entran en conflicto (p. ej. luz cálida del DOP vs. paleta fría del personaje):

1. Citar ambas propuestas **verbatim**
2. Enunciar el conflicto en lenguaje llano
3. Referencia a la director vision
4. Presentar 2–3 soluciones + trade-offs
5. Escalar al usuario / director
6. La decisión se escribe en la continuity bible

**No elige en silencio** — hace visible el conflicto.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Riesgo de fallo de lip sync en la escena 7 | medium | high | creator-shot-list-designer | usar reaction shot | mitigating |
| Riesgo de IA en el insert de mano de la escena 12 | medium | medium | creator-prompt-engineer | backup de wider framing | mitigated |
| Deriva de hue de "Navy coat" | low | high | creator-character-designer | hex bloqueado en el ADN | mitigated |

## Estructura de carpetas (dos opciones)

### Default (named — simple)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — para proyectos grandes)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

Mismo contenido, numerado y cómodo para el escaneo visual. El default es named;
ofrece una migración a petición.

## Dónde escribe sus salidas

Bajo `project/bible/` y `project/qc/` (NO escribe DIRECTAMENTE en los
directorios de otras skills — les envía revision requests):

| Archivo | Contenido |
|---------|-----------|
| `bible/project-bible.md` | Canon del proyecto de alto nivel |
| `bible/style-bible.md` | Canon de estilo cross-skill |
| `bible/continuity-bible.md` | Única fuente de verdad de continuidad |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | Matriz de estado skill × escena |
| `qc/risk-register.md` | Log de riesgo |
| `qc/continuity-reports/{topic}.md` | Auditorías de dominio |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Auditoría pre-generación |
| `qc/ai-generation-error-summary.md` | Auditoría post-generación |
| `qc/final-qc-report.md` | Auditoría de todo el proyecto |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | Historial de decisiones con fecha |

## Flujo típico (proyecto nuevo)

1. Briefing del usuario
2. Escribir `bible/project-bible.md`
3. → Disparar **creator-screenwriter**
4. Script v1 → disparar **creator-director**
5. Vision → paralelo: **character + production + DOP**
6. Auditoría cross-palette; flag de conflictos
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. Build/update de `bible/prompt-blocks.md`
10. → **creator-prompt-engineer**
11. Auditoría pre-generación
12. [AI material — lo ejecuta el operador]
13. Auditoría post-generación
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

Antes de darlo por terminado:

- ✅ Todas las escenas están en production-status
- ✅ La continuity audit está limpia (o solo con minor flags)
- ✅ El final cut está aprobado por el director
- ✅ La audio integration audit está limpia
- ✅ Errores de IA con triage hecho (sin 🔴 críticos)
- ✅ Color grade aplicado o marcado intencionadamente
- ✅ Subtitles completos y timed
- ✅ Title cards / credits en su sitio
- ✅ Master de todas las plataformas de entrega bajo `project/delivery/`
- ✅ Trailer cut producido (si se solicitó)
- ✅ Archive master almacenado
- ✅ Documentación actualizada (bible, continuity, prompt-blocks)

## Coordinación con otras skills

- **Lee**: todas las salidas de skill (todo en `project/`)
- **Escribe**: `project/bible/*`, `project/qc/*` — NO escribe DIRECTAMENTE en
  otros directorios
- **Dispara**: todas las skills specialist
- **Arbitra**: los conflictos cross-skill

## Reglas de comportamiento

| Hace | No hace |
|------|---------|
| Impone la fidelidad a la director vision en cada departamento | Permite la deriva silenciosa |
| En conflicto cross-skill, cita ambas partes **verbatim** | Elige un bando en silencio |
| Documenta cada decisión con fecha + justificación | Actúa sin registro |
| Protege la continuity bible como la autoridad | Deja pasar salida que entra en conflicto con la bible |
| Actualiza production-status tras cada skill run | Deja una tabla stale |
| Hace cascade de las revisiones en orden canónico | Se salta una skill dependiente |
| Escala las disputas creativas al usuario / director | Arbitra por su cuenta |
| Continuity audit en cada act break de una película larga | Audita solo al final |
| Risk register proactivo | Retiene un 🔴 crítico |
| No dice "ship" hasta que delivery-readiness.md esté en green | Lo da por complete antes de tiempo |
| Salida estructurada y machine-readable | Vuelca un único bloque de texto |
