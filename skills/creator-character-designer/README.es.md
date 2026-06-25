# Diseñador de Personajes — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Una skill que eleva al personaje más allá de la tríada **nombre + edad +
apariencia** y lo diseña como un **ser coherente**. Produce función dramática,
psicología, biografía, lenguaje corporal, vestuario, props, perfil de casting y
una **biblioteca de expresiones codificada con FACS Action Units**. Establece los
anclajes de «Character DNA» que preservan la consistencia del personaje a lo largo
de la producción de cine con IA de formato largo.

## Filosofía

Un personaje no se genera al azar: deriva de las necesidades del guion, de la
visión del director y del mundo visual del DOP. Esta skill:

- **Cada personaje es la respuesta a una pregunta dramática** — de lo contrario, sugiere eliminarlo
- Establece obligatoriamente el cuarteto **Want / Need / Fear / Wound** para cada personaje principal
- **FACS Action Units**: en lugar de decir «triste», dice AU1+AU4+AU15 —
  los modelos de IA y los animadores interpretan el código anatómico de forma más consistente
- **Character DNA**: define rasgos ancla bloqueados para la consistencia de la IA
- **Visual distinction audit**: cuando hay varios personajes, audita las distinciones de silueta, color y energía

## Para qué sirve

| Salida | Contenido |
|--------|-----------|
| **Character sheet** | Ficha del personaje — psicología, vestuario, props, FACS, AI prompt |
| **Costume bible** | Variaciones de vestuario y continuidad en toda la película |
| **Props list** | Los objetos personales del personaje y sus usos dramáticos |
| **FACS expression library** | 3–5 expresiones distintivas por personaje, codificadas con AU |
| **Casting brief** | El perfil buscado en un actor (no propone nombres, define rasgos) |
| **AI prompts** | Base prompt + variaciones de escena para una referencia de personaje consistente |
| **Arc tracker** | Transformación del personaje coordinada con el arc tracking del director |
| **Continuity notes** | Continuidad de vestuario/props escena por escena |

## Cuándo entra en acción

- El guion está listo y hay que desarrollar los personajes
- «Prepara una character sheet», «diseña un vestuario», «redacta un perfil de casting»
- Se necesita una referencia de personaje consistente para cine con IA
- Cuando el director o `creator-pipeline-supervisor` delega la etapa de personajes
- Cuando se cuestiona la distinción visual de los personajes existentes

## Uso de FACS — por qué y cómo

El **Facial Action Coding System (Ekman & Friesen, 1978)** es la codificación
anatómica de los músculos faciales. Una Action Unit (AU) = un movimiento muscular
específico.

### ¿Por qué lo usa esta skill?

- **Los generadores de IA** interpretan de forma inconsistente entradas abstractas como «happy face»;
  «AU6 + AU12 (Duchenne smile)» da un resultado más fiable
- **Los equipos de animación/VFX** comparten un único conjunto de referencia mediante códigos AU
- **La expresión distintiva del personaje** puede archivarse — por ejemplo, «Demir
  carga su duelo reprimido con AU4 + AU17 (ceño fruncido, barbilla elevada, sin AU15)»

### Combinaciones de AU comunes

| Expresión | AU |
|-----------|-----|
| Duchenne smile (felicidad genuina) | AU6 + AU12 |
| Polite smile (falsa/social) | AU12 sola |
| Tristeza | AU1 + AU4 + AU15 |
| Ira | AU4 + AU5 + AU7 + AU23 |
| Miedo | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| Asco | AU9 + AU15 + AU16 |
| Sorpresa | AU1 + AU2 + AU5B + AU26 |
| Desprecio (asimétrico) | AU12 (unilateral) + AU14 |
| Duelo reprimido | AU4 + AU17 (sin AU15) |
| Calma tensa | AU7 + AU23 + AU24 |

## Plantilla de character sheet (resumen)

```
Character: Demir
Role: Protagonist
Want: babasının arşivini bulup yakmak
Need: kendisini babadan ayırmadan da yaşayabileceğini görmek
Fear: babasının tüm kötü yanlarına dönüşmek
Wound: 14 yaşında bir gece babasının onu fark etmemesi
Visual identity: lacivert ağır kumaş palto, traşsız, sol elinin
                 üstünde küçük yanık izi
Signature expressions:
  - Bastırılmış yas: AU4 + AU17 (mutfak sahnesinde kettle önünde)
  - Reddediş: AU14 + AU24 (kuzeniyle konuşma)
  - Saklı acı: AU1 + AU4, gözler kaçıyor (cenaze sonrası)
Continuity anchors: yanık izi, palto, traşsız, ses tonu — sessiz, alçak
AI base prompt: "...same character across all scenes..."
```

## Dónde escribe sus salidas

Bajo `project/characters/{character-slug}/`:

| Archivo | Contenido |
|---------|-----------|
| `character-sheet.md` | La ficha canónica del personaje |
| `costume-bible.md` | Todas las variaciones de vestuario + continuidad |
| `props.md` | Los objetos del personaje, uso dramático |
| `facs-expressions.md` | Biblioteca de expresiones distintivas, codificada con AU |
| `casting-brief.md` | Perfil del actor / base para un AI face prompt |
| `ai-prompts.md` | Base prompt + variación escena por escena |
| `arc-tracker.md` | Sincronización con el arc tracking del director |
| `continuity-notes.md` | Continuidad de vestuario/props escena por escena |

Además, en el directorio superior hay un `cast-list.md` — una lista que resume todos los personajes.

## Visual distinction audit

Cuando hay más de un personaje, la skill ejecuta estas comprobaciones:

- Distinción de silueta (altura, postura, forma del vestuario)
- Distinción de mundo cromático (o contraste deliberado)
- Distinción de registro de energía
- Distinción de patrón de habla
- Distinción de presencia en pantalla (tipo foreground / background)

Si dos personajes «se confunden» entre sí, lo reporta y sugiere una revisión.

## Consistencia de IA (Character DNA)

Para generar el mismo personaje en 50 escenas con el mismo rostro/vestuario:

1. **Base prompt** — rasgos clave (forma del rostro, cabello, marca distintiva) fijos
2. **Anchor descriptors** — 2–3 de ellos se repiten en cada prompt de escena
3. **Expresión mediante FACS** — codificada con AU, no con adjetivos
4. **Producción temprana de la character sheet** — imágenes de referencia front/side/back/close
5. **Referencia en el prompt de escena**: «consistent with `characters/demir/sheet.png`»

## Coordinación con otras skills

- **Lee**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **Escribe**: `project/characters/*`
- **Delega en**: Ingeniero de prompts, storyboard, DOP (coordinación de paleta)
- **Recibe feedback de**: Director, Pipeline Supervisor

## Enfoque del diseño de vestuario

El vestuario narra al personaje — no es solo «lo que lleva puesto»:

- Pieza principal + su función
- Tejido: pesado, suave, rígido, fibroso
- Color: armonía/contraste con la paleta
- Desgaste / novedad / daño / señales de reparación
- Precisión de época
- Relación con el estado de ánimo del personaje
- Efecto sobre la movilidad
- Interacción con la luz (mate, brillante, transparente, que atrapa el polvo)

Para cada escena principal, una nota de continuidad de vestuario: ¿cambia dentro de
la escena, cambia entre escenas, por qué?

## Enfoque de los props

Los props son herramientas narrativas — no decorativas:

- Nombre + función
- Relación con el personaje
- Apariencia, material, color, estado
- Significado para el personaje (recuerdo, identidad, relación)
- Uso dramático (anticipación, pago, revelación)
- Cómo lo ve la cámara (primer plano, detalle, de paso)
- Continuidad (dónde está en cada escena)

Se aclara la propiedad personaje-prop / locación-prop y se coordina con
**creator-production-designer**.

## Reglas de comportamiento

| Hace | No hace |
|------|---------|
| Genera un personaje con una justificación dramática | Dice «necesitamos un personaje más» |
| Vincula cada elección visual al arc / función / tema | Toma decisiones estéticas aisladas |
| Hace preguntas cuando falta información | Inventa en silencio |
| Investiga el detalle cultural | Presenta una conjetura como un hecho |
| Define expresiones con códigos FACS AU | Usa adjetivos como «triste» |
| Ejecuta un visual distinction audit | Deja que dos personajes se confundan |
| Incrusta continuity anchors en los AI prompts | Describe desde cero en cada escena |
| Aclara la propiedad personaje-prop | Se solapa con el diseñador de producción |
| Entrega archivos estructurados y downstream-readable | Vuelca un único bloque de texto |
