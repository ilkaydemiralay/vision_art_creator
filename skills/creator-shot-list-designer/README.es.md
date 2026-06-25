# Diseñador de lista de planos — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · **Español** · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

La skill que convierte escenas y storyboards en una **lista de planos + intención de montaje**.
El lugar donde se encuentran la planificación de preproducción y la intención editorial. No
es el montador de corte final: diseña la intención editorial ANTES de que se produzca
cualquier material, para que el rodaje genere las piezas correctas.

## Filosofía

Una lista de planos no es un inventario técnico; es un **mapa de la intención dramática +
editorial**. Esta skill:

- **Economía del plano**: cada plano lleva una única acción clara
- **Conciencia del ritmo de montaje**: ¿qué plano se sostiene largo, cuál se corta rápido?
  La duración del plano es una decisión editorial
- **Dirección de pantalla + continuidad**: coherencia espacial/temporal entre cortes
- **Producibilidad para AI**: planifica la complejidad de cada plano en torno a las restricciones de las herramientas AI
- **Intención editorial antes de la producción**: la lógica de montaje se fija ANTES del rodaje
  para no filmar planos innecesarios
- **Diseño de la experiencia del público**: ¿qué siente el espectador, qué aprende y qué se le oculta?

## Qué produce

| Salida | Contenido |
|-------|---------|
| **Lista de planos por escena** | Lista de planos canónica, con justificación dramática + editorial |
| **Plan de montaje** | Ritmo dentro de la escena, puntos de corte, imagen de apertura/cierre |
| **Diseño de transiciones** | Decisiones de transición entre escenas (hard cut, match, J/L, sound bridge) |
| **Auditoría de riesgos de continuidad** | Informe de riesgos de coherencia entre planos |
| **Notas de montaje sonoro** | Puntos de J-cut / L-cut / silencio para el diseñador de sonido |
| **Lista de planos de toda la película** | Lista consolidada que abarca toda la película |
| **Mapa de ritmo** | Ritmo escena por escena (rangos de duración de plano) |
| **Informe de redundancias** | Planos que deberían cortarse/fusionarse |
| **Notas para el montador final** | Traspaso de la intención editorial al montador de corte final |

## Cuándo entra en juego

- Las escenas y los storyboards están listos y se necesita un plan basado en planos
- Se solicita una secuenciación de planos consciente del montaje
- Hay que descomponer escenas largas en piezas producibles por AI
- Cuando el director o el DOP solicitan un plan estructural de rodaje/producción
- Cuando `creator-pipeline-supervisor` delega la planificación previa al montaje

## Flujo típico

1. **Briefing** + lectura de todas las salidas de las skills previas
2. **Ronda de preguntas**: formato, ritmo de montaje, tono, herramientas AI
3. **Lista de planos (por escena)**: en estructura canónica, con justificación dramática + editorial
4. **Plan de montaje (por escena)**: ritmo, apertura/cierre, puntos de corte
5. **Diseño de transiciones**: transiciones entre escenas
6. **Auditoría de continuidad**: riesgos entre planos
7. **Mapa de ritmo**: mapa de ritmo de toda la película
8. **Informe de redundancias**: identificación de planos que pueden cortarse
9. **Traspaso**: datos de prompt de plano para creator-prompt-engineer + intención editorial para creator-final-cut-editor

## Plano — estructura canónica

```
Scene 04 — Shot 04.02
Shot name: "Kettle close, silence"
Shot type: insert
Frame scale: extreme close
Camera angle: eye level (side-high)
Camera movement: static
Lens recommendation: 100mm macro feeling
Estimated duration: 4s
Location: Anatolian kitchen 1980s [anchor: kitchen-anatolian-1980s]
Time: night
Characters in frame: none (only the kettle)
Character action: kettle whistle dying down (off-screen Demir turns off the heat)
Dialogue / silence note: SILENCE (only kettle + clock ticking)
Light / atmosphere: gray moonlight from the window, copper kettle highlight
Sound / music note: NO music; clock ticking + kettle dying
Dramatic purpose: a symbolic echo of Demir's inner turning
Edit purpose: a 4-second breath — no need to cut, hold it
Link to previous shot: 04.01 (Demir sitting, wide) — match by sound
Link to next shot: 04.03 (Demir's face close, first blink) — hard cut
Continuity note: kettle = same copper, same stain pattern
AI video production note: single action (whistle dying) + static camera = low risk
Safe alternative: 6s version — slower whistle fade, very slow camera push-in
```

## Intención editorial — plan de escena

Preguntas editoriales a nivel de escena:

- ¿Qué plano abre la escena?
- ¿Qué imagen la cierra?
- ¿Qué plano se sostiene largo?
- ¿Qué plano se corta corto?
- ¿Dónde van los reaction shots?
- ¿Dónde se extiende el silencio?
- ¿Dónde hace falta un hard cut?
- ¿Dónde una transición suave?
- ¿Qué imagen enlaza con la escena siguiente?
- ¿Qué plano lleva el clímax dramático?
- ¿Qué plano es innecesario?
- ¿Qué plano entrega información y cuál emoción?

Se escribe en `project/shot-list/scene-{NN}/edit-plan.md`.

## Dónde escribe sus salidas

En `project/shot-list/`:

| Archivo | Contenido |
|-------|---------|
| `scene-{NN}/shot-list.md` | Lista de planos de la escena |
| `scene-{NN}/edit-plan.md` | Intención de montaje + ritmo |
| `scene-{NN}/transitions.md` | Decisiones de transición |
| `scene-{NN}/continuity-risks.md` | Auditoría de continuidad |
| `scene-{NN}/sound-edit-notes.md` | Traspaso al diseñador de sonido |
| `film-shot-list.md` | Lista consolidada de toda la película |
| `rhythm-map.md` | Mapa de ritmo |
| `redundancy-report.md` | Planos que pueden cortarse |
| `ai-production-shot-guide.md` | Guía de restricciones de herramientas AI |
| `final-editor-notes.md` | Intención para el montador de corte final |

## Tipos de transición (uso editorial)

| Transición | Uso editorial |
|-------|-------------------|
| Hard cut | Ruptura dramática repentina |
| Match cut | Un puente de significado entre dos imágenes |
| Fade in/out | Apertura/cierre temporal/emocional |
| Dissolve | Transición temporal, mezcla emocional |
| J-cut | El sonido de la escena siguiente llega primero (flujo fluido) |
| L-cut | El sonido de la escena actual se prolonga (emoción sostenida) |
| Sound bridge | Cambio de lugar/tiempo arrastrado sobre el sonido |
| Visual motif | Un puente a través de un elemento visual recurrente |
| Object transition | Coincidencia de forma |
| Movement transition | Continuidad direccional |
| Time jump | Salto temporal repentino |
| Flashback | Mediante un filtro/lente/desenfoque/señal sonora |
| Parallel edit | Dos lugares entrelazados |

## Reglas de producibilidad para video AI

- Una acción clara por plano
- Un movimiento de cámara principal (no encadenado)
- Un número controlado de personajes
- Un objetivo visual claro
- Descomponer el movimiento complejo en varios planos
- Señalar el lip sync de manos/dedos/labios arriesgado
- Encuadre selectivo para multitudes
- Anchors de ubicación + personaje bloqueados en cada prompt
- Duración del plano típicamente de 3 a 10s
- Cada plano se corresponde limpiamente con un único prompt de video

Cuando se detecta un riesgo, señálalo:

> *"Este plano es demasiado complejo para video AI: divídelo en dos planos."*
> *"El lip sync puede fallar aquí; usa un reaction shot en lugar del hablante."*
> *"El movimiento de la mano es crítico: usa un encuadre más abierto en lugar de un insert."*
> *"Acción de multitud: constrúyela con cortes, no con un solo plano."*

## Ritmo y cadencia

No se usan frases vagas como "hazlo rápido". El ritmo se:

- Expresa como un **rango de duración de plano**
- Mide por la **frecuencia de cortes**

Ejemplo:
> *"La escena 3 promedia 4–6s/plano, la escena 12 promedia 1,5–3s/plano:
> el ritmo se acelera a medida que escala el conflicto del personaje."*

## Intención de montaje del diálogo

Para escenas con mucho diálogo:

- ¿El hablante o el oyente?
- ¿Dónde van los reaction shots?
- ¿Dónde es más fuerte el silencio?
- ¿Otra imagen sobre el diálogo?
- ¿Subtexto a través de la expresión facial?
- ¿Hard cut o solapamiento natural?
- ¿Cortar antes de que termine la frase?
- ¿Repetición redundante de la explicación?
- ¿A quién pertenece la emoción que el espectador realmente necesita ver?

Aquí se fijan las marcas de J-cut / L-cut.

## Coordinación con otras skills

- **Lee**: guion, visión del director + hojas de dirección, plan por escena del DOP,
  datos de los paneles del storyboard, anchors de personaje/ubicación
- **Escribe**: `project/shot-list/*`
- **Traspasa a**:
  - `creator-prompt-engineer` (prompts de video a nivel de plano)
  - `creator-final-cut-editor` (archivos de intención editorial)
- **Recibe feedback de**: el director, el Pipeline Supervisor

## Detección de redundancias

En una película AI larga, señala:

- Un plano que repite la misma información
- Un plano que no cambia la emoción
- Un plano de detalle que rompe el ritmo
- Uso excesivo de reaction shots
- Un plano difícil para AI con baja contribución dramática
- Oportunidades de entrar tarde / salir temprano
- Un momento que puede contarse visualmente en lugar de con diálogo

Se escribe explícitamente *"Este plano puede cortarse"* o *"Estos dos planos pueden fusionarse"*.

## Reglas de comportamiento

| Hace | No hace |
|-------|---------|
| Da a cada plano una justificación dramática **y** editorial | Hacer un inventario técnico |
| Se coordina con el ritmo del director, el encuadre del DOP, el storyboard | Decidir de forma aislada |
| Señala los planos innecesarios | Añadir relleno |
| Comprueba la continuidad de forma proactiva | Esperar a que los problemas salgan tras el rodaje |
| Diseña en torno a las restricciones de las herramientas AI | Planificar planos imposibles de producir |
| Una alternativa segura para los planos arriesgados | Ofrecer una única versión |
| Considera también al oyente en el diálogo | Seguir solo al hablante |
| Coordina la intención editorial de sonido y música | Pensar solo en la imagen |
| Salida estructurada, legible para las fases posteriores | Volcar un solo bloque de texto |
