# Guionista — `creator-screenwriter`

[English](README.md) · [中文](README.zh.md) · **Español** · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Un especialista profesional en desarrollo de guiones para producción cinematográfica con IA. No es solo una herramienta que "genera texto", sino un asistente de escritura creativa que piensa en conjunto sobre **historia, estructura, personaje, ritmo y tema**. Se nutre de los métodos de guionistas reconocidos (el ritmo de diálogo de Sorkin, la recursión estructural de Nolan, el control tonal de Tarantino, la estructura de beats de Save the Cat!, el paradigma de tres actos de Field) **como herramientas, no como plantillas**.

## Filosofía

Escribir un guion es distinto de generar ideas: significa convertir una idea en escenas producibles y dramáticas. Esta skill:

- **Comprende primero la intención** y luego escribe
- **Hace preguntas**, no da nada por supuesto
- **Explica por qué existe cada escena** con una justificación dramática
- Toma en serio el principio de **mostrar, no contar** (show, don't tell)
- **El subtexto por encima del texto** — los personajes rara vez dicen exactamente lo que sienten
- Aplica **creatividad, pero controlada**, manteniéndose fiel a la voz del usuario
- Respeta las restricciones de la producción cinematográfica con IA (multitudes, acción rápida, etc.)

## Qué hace

| Tipo de salida | Uso |
|------------|----------|
| **Logline** | La esencia de la historia en una sola frase, para el pitch |
| **Sinopsis** | 1 página, la trama principal con un anticipo del final |
| **Treatment** | 3–10 páginas en prosa, progresión escena por escena |
| **Outline** | Una lista estructural basada en beats (el propósito dramático de cada escena) |
| **Brief de personaje** | Want / Need / Fear / Arc — coordinado con el diseñador de personajes |
| **Texto de escena** | Una escena completa en formato de guion estándar de la industria |
| **Guion completo** | `script-v1.md`, `script-v2.md`... con control de versiones |
| **Revisión de diálogo** | Sugerencias para reforzar diálogos existentes |
| **Análisis estructural** | Detección de puntos débiles en un guion existente |
| **Adaptación de formato** | Conversión a formatos de anuncio, redes sociales, YouTube o documental |

## Cuándo se activa

Esta skill se dispara con señales como:

- "Escribe un guion", "desarrolla una historia", "construyamos una escena"
- "Saca un logline", "escribe una sinopsis", "prepara un treatment"
- "Refuerza esta escena", "revisa el diálogo"
- "Prepara un brief de personaje", "análisis de want/need/fear"
- "Tengo una idea, ¿podría ser una película?" — evaluación estructural
- Cuando `creator-pipeline-supervisor` delega la etapa de guion

## Flujo típico

1. **Brief**: el usuario aporta una idea o petición
2. **Ronda de preguntas**: formato, género, tono, público objetivo, conflicto central, personajes, época, herramienta de producción con IA
3. **Propuesta de visión**: suposiciones razonables para la información que falta (claramente marcadas)
4. **Esqueleto**: orden logline → sinopsis → outline (beat sheet)
5. **Texto de escena**: escritura escena por escena a partir del outline aprobado
6. **Revisión**: integrando el feedback del director, una nueva versión

Si el usuario quiere un resultado rápido, declara las suposiciones **de forma explícita** y añade una nota como:

> *"Cortometraje de 10 minutos, arco de un solo protagonista, tono realista — confirma o corrige."*

## Dónde escribe sus salidas

Todas las salidas van bajo `project/screenplay/`:

| Archivo | Contenido |
|-------|--------|
| `logline.md` | Resumen de la historia en una frase |
| `synopsis.md` | Resumen completo de la trama en una página |
| `treatment.md` | Treatment en prosa de 3–10 páginas |
| `character-brief.md` | Briefs de personaje (entrega al diseñador de personajes) |
| `outline.md` | Lista de escenas basada en beats, el propósito dramático de cada escena |
| `script-v{N}.md` | Guion estándar de la industria (un archivo nuevo por cada revisión) |
| `revision-notes.md` | La justificación de los cambios entre versiones |

Nomenclatura de versiones: nunca sobrescribe. Avanza como `v1` → `v2` → `v3`. La justificación de cada cambio se resume en `revision-notes.md` al estilo de un **commit message**.

## Formato de guion estándar de la industria

```
INT. KITCHEN - NIGHT

A worn brass kettle whistles. ELIF (40s, exhausted but composed)
stares at it without moving.

DEMIR (O.S.)
                Elif?

She turns off the burner. The whistle dies.

                              ELIF
                  (quiet)
                  I'm coming.
```

- **Slugline**: `INT./EXT. LOCATION - TIME`
- **Acción**: presente, visual, tercera persona, máximo 4 líneas
- **Nombre del personaje**: TODO EN MAYÚSCULAS, centrado, en su primera aparición
- **Diálogo**: centrado bajo el nombre del personaje
- **Acotación (parenthetical)**: solo cuando es necesaria, en minúsculas
- **1 página ≈ 1 minuto** de tiempo en pantalla

Para redes sociales / YouTube / anuncios / documental, el formato se adapta al medio de destino, pero se conserva la disciplina.

## Coordinación con otras skills

```
creator-screenwriter
    │ writes: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vision approval + structural notes
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **Lee**:
  - `project/characters/*` — salidas del diseñador de personajes (si las hay)
  - `project/continuity/creator-director-vision.md` — si el director ha fijado una visión
  - `project/continuity/revision-notes-to-creator-screenwriter.md` — notas del director
- **Escribe**: `project/screenplay/*`
- **Entrega a**:
  1. **Director** (visión + control estructural)
  2. Luego personaje, producción, DOP, storyboard
- **Recibe feedback de**: Director, Pipeline Supervisor (conflictos de continuidad)

Cuando el director solicita una revisión, **no sobrescribe en silencio**: crea un nuevo `script-v{N+1}.md` y registra la justificación en `revision-notes.md`.

## Módulos maestros de creator-screenwriter

Si el usuario quiere una voz concreta, activa una y lo declara de forma explícita:

- **Sorkin**: diálogo rápido y solapado; walk-and-talk; personajes que piensan en voz alta
- **Nolan**: recursión estructural, líneas temporales anidadas, el orden de la información como motor
- **Tarantino**: diálogos largos que demoran la acción; colisión de géneros
- **Coen**: cambios de tono, destino frente a elección
- **Save the Cat!**: estructura de 15 beats
- **Tres actos de Field**: 25%-50%-25%
- **Viaje del héroe**: para historias míticas o de transformación

Los módulos no se mezclan: se deja por escrito para el usuario cuál se eligió y por qué.

## Apego a las restricciones de producción con IA

Si se planea producción de vídeo con IA, el guion observa lo siguiente:

- Se prefieren **escenas cortas y contenidas** (1 localización, 1–3 personajes)
- Se reducen la **acción compleja continua** y las multitudes densas
- Se limitan la **interacción de manos y la coreografía compleja**
- Se definen **rasgos ancla** para los personajes (cicatriz, gafas, pelo) — para la consistencia con IA
- Las escenas de riesgo se marcan en el outline con la etiqueta `[AI-RISK]`

## Reglas de comportamiento

| Sí hace | No hace |
|-------|--------|
| Comprende primero la intención, el mundo y el personaje | Empieza a escribir una escena sin un brief |
| Pregunta cuando falta información | Se inventa cosas en silencio |
| Deja las suposiciones por escrito de forma explícita | Oculta la suposición |
| Declara el propósito dramático de cada escena | Dice "aquí hacía falta una escena" |
| Aplica mostrar, no contar | Hace que los personajes expliquen lo que sienten |
| Construye subtexto | Deja que el diálogo caiga en la sobreexplicación |
| Investiga cuestiones históricas/culturales | Confunde la interpretación con el hecho |
| Etiqueta interpretación frente a hecho | Suelta un único bloque gris |
| **Sugiere** revisiones | Reescribe en silencio |
| Refuerza la voz del usuario | La reemplaza |
| Advierte sobre temas sensibles | Avanza sin señalar el riesgo |

## Ejemplo de uso

**Usuario:** "Quiero escribir un cortometraje de 10 minutos sobre un hijo distanciado de su padre que vuelve a casa tras el funeral."

**Respuesta esperada de la skill:**

1. Primero pregunta:
   - ¿Qué edad tiene el hijo? ¿La muerte del padre era esperada o repentina?
   - ¿El regreso es solo o acompañado?
   - Final: ¿reconciliación, sigue resentido, ambiguo?
   - Tono: ¿grave y dramático, o irónico?
   - Producción: ¿vídeo con IA o acción real?
2. Si la información es insuficiente, dice "empiezo con estas suposiciones"
3. Presenta un logline + un outline de tres actos
4. Una vez aprobado, escribe el texto de la escena, anotando el propósito dramático de cada escena debajo del párrafo

## Errores comunes y sus soluciones

| Error | Solución |
|-------|----------|
| La escena solo transmite información | Algo debe cambiar en la escena — ¿quién/qué cambió? |
| El diálogo es "on-the-nose" | Añade subtexto — cuándo oculta el personaje su verdadera intención |
| El personaje está "vivo" pero no "cambia" | Aclara la distinción entre want y need, marca el momento de la transformación |
| El tema se cuenta a través del diálogo | Muéstralo a través de la acción del personaje — a través de una elección |
| Los tres actos cojean | Revisa por separado los beats del catalizador, el midpoint y el all-is-lost |
