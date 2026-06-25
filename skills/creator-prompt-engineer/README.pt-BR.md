# Engenheiro de Prompts — `creator-prompt-engineer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · **Português (BR)** · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A **camada de tradução** entre o pipeline criativo e os geradores de IA.
Transforma as decisões produzidas pelas skills de roteirista, diretor, DOP,
personagens, produção, storyboard e lista de planos em prompts **realmente
produzíveis e consistentes**. Otimiza por ferramenta (Midjourney ≠ Sora ≠
Stable Diffusion), embute os anchors travados em cada prompt e gera alternativas
seguras para cenas arriscadas.

## Filosofia

O engenheiro de prompts **não inventa imagens** — ele codifica as decisões do
upstream. Esta skill:

- **Locked anchors**: character DNA + location master reference + style block —
  mesmo depois de 50 prompts o mesmo personagem sai com o mesmo rosto
- **Tool fitness**: cada ferramenta de IA tem sua própria linguagem de prompt
- **Producibility audit**: esta cena vai derrubar o gerador — proponha uma alternativa
- **Consistency discipline**: para um longa-metragem, os prompts são um sistema, não algo isolado
- **FACS expression coding**: AU1 + AU4 + AU15 em vez de "triste" — resultados mais consistentes
- **Nunca sobrescreve o upstream em silêncio**: sinaliza e devolve a pergunta quando preciso

## Para que serve

| Saída | Conteúdo |
|-------|----------|
| **Character prompts** | DNA travado + variação cena a cena |
| **Location prompts** | Master reference + variação dia/noite/clima |
| **Style anchors** | Bloco visual/técnico do filme inteiro |
| **Negative prompts** | Banco de prompts negativos por categoria |
| **Panel prompts** | Prompt de geração de imagem a partir de um painel de storyboard |
| **Shot prompts** | Prompt de geração de vídeo IA a partir da lista de planos |
| **Character sheets** | Geração de referência frente/lado/costas/close |
| **Producibility risk report** | Risco no nível de cena/plano + alternativa segura |
| **Tool guide** | Notas específicas por ferramenta para o operador |

## Quando entra em ação

- São necessários prompts de imagem/vídeo IA antes da produção
- É preciso montar um sistema de anchors para a consistência de personagem/locação
- Uma saída de storyboard ou lista de planos será convertida em prompts de ferramenta
- Um prompt existente é arriscado — quer-se uma alternativa segura
- Quando `creator-pipeline-supervisor` delega a etapa de prompts

## Guia de otimização por ferramenta (resumo)

### Midjourney
- Parâmetros `--ar`, `--style raw`, `--s`
- `--cref` e `--cw` para referência de personagem
- `--sref` para referência de estilo
- Redação compacta — empilhar adjetivos enfraquece o sinal

### DALL·E
- Linguagem natural > despejo de tags
- Escreva as relações espaciais
- Evite gerar texto dentro da imagem

### Stable Diffusion (SDXL / SD3)
- Positive + negative separados
- Notas de LoRA / reference / seed para a consistência do personagem
- Termos importantes no começo (token weight)

### Runway / Kling / Sora / Veo / Luma / Higgsfield
- Um único movimento de câmera principal
- Número de personagens controlado
- Opening + closing frame claros
- Duração curta (3–10s típico)
- Limites específicos por ferramenta:
  - Sora 2: ~20s
  - Kling 3.0: subject binding para consistência
  - Veo: motion fidelity forte
  - Runway Gen-3/4: o movimento faz sentido, lip sync fraco

## Sistema de anchors travados (para um longa-metragem)

### Character DNA block

Copiado **literalmente** de `project/characters/{slug}/ai-prompts.md`:

```
{character-demir}: middle-aged man, late 40s, weary but composed face,
short dark hair, three-day stubble, small scar on left eyebrow, small burn
mark on the back of his left hand, navy heavy wool coat, dark wool sweater
underneath, controlled posture, low and quiet energy
```

### Location anchor block

Literalmente de `project/production-design/locations/{slug}/master-reference.md`:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall, lime-washed walls with
soot stain along the lower meter, raw wooden floor, wooden table center,
copper-lidded cabinet on the north wall, copper kettle on a small iron stove
```

### Style block

```
{style}: realistic cinematic period drama, soft natural light, 35mm film
feeling, subtle film grain, muted earth-tone palette, 2.39:1 aspect ratio,
no modern objects
```

Esses blocos são **repetidos literalmente em cada prompt** daquela cena/personagem/locação.
Essa disciplina é o motor da consistência.

## Categorias de prompt negativo

| Problema | Termo negativo |
|----------|----------------|
| Distorção facial | distorted face, malformed face, asymmetric eyes, blurred features |
| Erro de mão | extra fingers, missing fingers, fused fingers, deformed hand |
| Anacronismo | modern clothes, modern tech, plastic, neon, smartphone |
| Artefato de IA | warping, morphing, flickering, jittery motion |
| Qualidade | low quality, low resolution, jpeg artifacts, oversaturated |
| Texto | unwanted text, watermark, signature, logo |
| Composição | extra characters, cropped subject, duplicate subject |
| Câmera | unintended shake, fisheye distortion |

Algumas ferramentas ignoram o prompt negativo — nesse caso escreva-o dentro do
positive prompt como uma dica *"avoid: ..."*.

## Auditoria de producibilidade de vídeo IA

Verificações antes de emitir um prompt de vídeo:

- Muita ação em um único plano?
- Personagens demais?
- O movimento de câmera é complexo?
- O detalhe de mão/dedos/rosto é arriscado?
- A consistência de figurino/adereço pode ser mantida?
- A locação está cheia demais?
- Luz e horário estão consistentes?
- A cena deveria ser dividida em partes em vez de um único prompt?
- É preciso lip sync? (sinalize)
- O prompt é desnecessariamente abstrato?

Havendo risco, ela dá uma **alternativa segura e simplificada**.

## Geração de variações

Variações focadas para a mesma cena:

- Realistic
- More cinematic
- Darker
- Low-budget / simpler
- Wide alt.
- Close alt.
- Night
- Daylight
- AI-safe
- Poster / key art

O **propósito de cada variação é registrado** — por que e em qual situação é usada.

## Onde grava suas saídas

Em `project/prompts/`:

| Arquivo | Conteúdo |
|---------|----------|
| `character-prompts/{slug}.md` | DNA travado + variações de cena |
| `location-prompts/{slug}.md` | Master anchor + variações |
| `style-anchors.md` | Style block(s) do filme inteiro |
| `negative-prompts.md` | Banco de prompts negativos |
| `scene-{NN}/panel-{PP}.md` | Prompts de imagem de painel |
| `scene-{NN}/shot-{SS}.md` | Prompts de vídeo de plano |
| `character-sheets/{slug}.md` | Prompts de geração de sheet frente/lado/costas/close |
| `prompt-system.md` | Documentação do sistema de anchors |
| `producibility-risk-report.md` | Sinalizações de risco + alternativa segura |
| `tool-guide.md` | Notas para o operador específicas por ferramenta |

## Formato de prompt bilíngue

Quando o usuário quer uma explicação na língua nativa + um prompt em inglês:

```
Türkçe Açıklama:
Bu prompt karakterin yalnızlığını vurgulayan geniş bir dış mekân planı
üretmek için hazırlanmıştır.

English Prompt:
A lonely middle-aged man standing at the edge of a foggy rural road at
dawn, wide cinematic shot, 35mm lens feeling, cold blue morning light,
worn dark traditional clothing, quiet melancholic mood, realistic period
drama, subtle film grain, 16:9 aspect ratio.
```

## Coordenação com outras skills

- **Lê**: todas as saídas criativas do upstream
- **Grava**: `project/prompts/*`
- **Delega**:
  - ao operador humano que vai rodar as ferramentas de IA
  - feedback ao **storyboard artist** ou ao **shot-list designer** se a
    auditoria de producibilidade exigir mudar o upstream
- **Recebe feedback**: Pipeline Supervisor (deriva de consistência)

## Regras de comportamento

| Faz | Não faz |
|-----|---------|
| Coloca os locked anchors em cada prompt em trabalho multi-plano | Descreve do zero a cada vez |
| Escreve prompts adequados à ferramenta | Dá o mesmo prompt a toda ferramenta |
| Auditoria de producibilidade + alternativa segura | Passa por cima do risco em silêncio |
| Usa códigos FACS AU | Empilha adjetivos como "triste" |
| Reduz o excesso de adjetivos | Enche com palavras rebuscadas |
| Preserva a decisão do upstream, sem sobrescrever em silêncio | Adiciona invenção criativa |
| Respeita a pesquisa de época | Deixa anacronismos |
| Saída estruturada, legível a jusante | Despeja um prompt em bloco único |
| Formato de explicação na língua nativa + prompt em inglês (se pedido) | Impõe o inglês sempre |
