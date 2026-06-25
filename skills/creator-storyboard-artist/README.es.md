# Artista de Storyboard — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Una skill que convierte un guion escrito en **narrativa visual legible**. Al
minimizar la cantidad de paneles, garantiza que cada panel exista por una razón
dramática. Captura los momentos críticos de una escena, preserva el screen
direction, sigue la eyeline continuity y hace un hand-off limpio a los prompts
de imagen/vídeo de IA.

## Filosofía

Un storyboard no es "dibujar la escena" — es un **sistema de narrativa visual**. Esta skill:

- **Panel economy**: pocos paneles + decisiones precisas — no muchos paneles + decisiones débiles
- **Screen direction (180°)** y **eyeline continuity**: coherencia espacial entre cortes
- **Graphic dynamics**: ¿dónde cae la mirada? ¿cuál es el foco?
- **Continuity awareness**: vestuario, localización, dirección de la luz, dirección de pantalla, movimiento
- **Locked anchors**: character DNA + location master reference en cada panel
- **Producibility**: conoce las restricciones de producción con IA y marca las escenas riesgosas

## Para qué sirve

| Salida | Contenido |
|--------|-----------|
| **Per-scene storyboard** | Lista de paneles escena por escena (todos los datos del panel) |
| **Per-panel sheets** | Archivo detallado de un solo panel para escenas complejas |
| **AI image prompts** | Prompt listo para producción por panel |
| **AI video prompts** | Prompt de vídeo para paneles en movimiento |
| **Continuity log** | Marcas de riesgos de vestuario/localización/dirección |
| **Animatic plan** | Planifica el orden del animatic de todas las escenas |
| **Director / DOP notes** | Notas visuales/técnicas breves para el director y el DOP |
| **Handoff to shot-list** | Datos del panel en formato creator-shot-list-designer |

## Cuándo entra en acción

- Hay un guion en mano y se desea un desglose visual
- Cuando el director quiere visualizar una escena por anticipado
- Cuando se necesita un concepto visual antes de las decisiones de lente/luz del DOP
- Cuando se desea la lógica del storyboard antes de generar prompts de IA
- Cuando `creator-pipeline-supervisor` delega la etapa de storyboard

## Panel content (campos canónicos)

Cada panel registra estos campos:

```
Scene 04 — Panel 04.03
Shot type: medium close
Camera angle: eye level
Frame: Demir merkez-sağ; kettle ön plan-sol; arka plan
       dolap soft-focus; sağ kenar negatif alan açık
Lens feeling: 50mm (eye-equivalent, samimi)
Character position: Demir sandalyede, omuzlar düşmüş, eller masada
Character movement: yok — duraksama
Camera movement: static
Setting / dressing: kireçli mutfak — pencere doğu, kettle ateşte
Light / atmosphere: pencereden yumuşak gri sabah, mum yok
Emotional emphasis: bastırılmış yas; ilk gerçek duygu kırılması
Dialogue / action note: sessizlik; kettle ıslığı
Dramatic justification: Demir'in iç çatışmasını yüzeye getiren ilk an
Transition to next panel: J-cut — kettle sesi devam ederken Panel 4.04 başlar
AI image prompt: [tam prompt]
AI video prompt: [tam prompt, 6s]
Continuity note: palto sahne başında; ceket askıda; kettle aktif
```

## Dónde escribe sus salidas

Bajo `project/storyboards/`:

| Archivo | Contenido |
|---------|-----------|
| `scene-{NN}/storyboard.md` | Lista de paneles por escena (canónica) |
| `scene-{NN}/panel-{PP}.md` | Panel único detallado (en escenas complejas) |
| `scene-{NN}/prompts.md` | Prompts de IA por panel (image + video) |
| `scene-{NN}/continuity.md` | Marcas de continuity |
| `animatic-plan.md` | Notas de orden del animatic de toda la película |
| `notes-to-creator-director.md` | Preguntas/avisos para el director |
| `handoff-to-shot-list.md` | Datos de panel formateados para el shot-list designer |

## Glosario de shot type (con su equivalente dramático)

| Tipo | Uso dramático |
|------|---------------|
| Establishing | Sitúa al espectador en el espacio |
| Master | Geometría de la escena, fallback |
| Wide/Full | Relación personaje–entorno |
| Medium | Diálogo neutro |
| Close | Conflicto interno, emoción íntima |
| Extreme close | Intensidad subjetiva |
| Insert | Énfasis en un objeto |
| Cutaway | Información paralela/externa |
| Reaction | Reacción por encima de la acción |
| OTS | Perspectiva de diálogo |
| POV | Subjetividad del personaje |
| 2-shot / group | Geometría de la relación |
| Silhouette | Anonimato, misterio |
| Negative-space frame | Aislamiento, pequeñez |
| Symmetrical | Poder, formalidad, quietud inquietante |
| Tracking | Seguimiento continuo |
| Static | Observación, el significado del silencio |

"Usa un close-up" no basta — la pregunta es **por qué** se necesita un close-up.

## Continuity audit

Seguimiento de panel a panel, de escena a escena:

- Vestuario
- Pelo/maquillaje/accesorios
- Identidad de la localización (con locked anchor)
- Dirección de la luz
- Día/noche
- Screen direction (regla de los 180°)
- Lógica espacial de los personajes
- Flujo de la acción
- Posición de los props

Cuando se detecta un riesgo, se escribe explícitamente en el campo `continuity note` del panel.

## Coordinación con otras skills

- **Lee**: guion, visión del director + direction sheets, plan per-scene del DOP,
  character DNA + FACS, anchors de localización
- **Escribe**: `project/storyboards/*`
- **Delega**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → optimización específica por herramienta)
- **Recibe feedback de**: Director, Pipeline Supervisor

## Soluciones enfocadas a la producción con IA

- Divide escenas complejas en paneles simples
- Aclara el foco visual en escenas con varios personajes
- Simplifica los movimientos con los que la IA tendría dificultades
- Usa anchors fijos para la misma localización/personaje
- Ofrece una alternativa segura de plano estático en lugar de movimiento de cámara
- Sugiere encuadres selectivos en escenas con mucha gente
- Sugiere cortes rítmicos en lugar de acción rápida

## Reglas de comportamiento

| Hace | No hace |
|------|---------|
| Escribe una justificación dramática para cada panel | Rellena con "otro panel" por rellenar |
| Pocos paneles + decisiones precisas | Muchos paneles + decisiones débiles |
| Unifica guionista + director + DOP + personaje + producción | Pasa por encima del upstream en silencio |
| Preserva el screen direction y la eyeline | Confunde la dirección en un corte |
| Pone los locked anchors en cada prompt | Vuelve a describir desde cero en cada panel |
| Divide la escena compleja en paneles | La carga en un único frame sobrecargado |
| Flag de riesgo de IA + alternativa segura | Sugiere un movimiento improducible |
| Salida estructurada y legible aguas abajo | Vuelca un único bloque de texto |
