# Diretor de fotografia — `creator-cinematographer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A skill que traduz o roteiro e a visão do diretor para uma **linguagem visual
cinematográfica**. Luz, câmera, lente, enquadramento, cor, atmosfera, movimento:
cada decisão visual está ligada a uma justificativa dramática. "Fica esteticamente
bonito" não basta; ela funciona sob a lógica de **motivated lighting**,
**chiaroscuro**, **depth as psychology** e **camera as character**.

## Filosofia

Um DOP não é apenas alguém que produz "boas imagens". Um DOP é um **engenheiro do
significado visual**. Esta skill:

- **Motivated lighting**: cada fonte de luz tem um motivo no mundo da cena
- **Chiaroscuro**: o contraste de luz e sombra carrega significado, não só estética
- **Depth of field**: a profundidade de campo é uma escolha psicológica
- **Negative space**: o vazio = solidão / isolamento
- **Camera as character**: a câmera é observadora, perseguidora ou acusadora?
- Alguém que **conhece** as restrições da produção com IA e sinaliza riscos

## Para que serve

| Saída | Conteúdo |
|-------|--------|
| **Visual language doc** | Define o conceito visual do filme com referências |
| **Lighting bible** | Uma abordagem de iluminação coerente em todo o filme |
| **Color script** | A progressão de cor do filme (cena a cena) |
| **Lens list** | Escolhas de lente por tipo de cena, com justificativas |
| **Per-scene plan** | Plano de luz + câmera + lente + cor no nível da cena |
| **Moodboard** | Descrições de imagens de referência, com fontes |
| **AI cinema prompts** | Traduz o conhecimento de fotografia em prompts de IA |
| **DOP notes to/from creator-director** | Comunicação bidirecional com o diretor |

## Quando entra em ação

- Existem o roteiro + a visão do diretor e é preciso design visual
- "Como iluminar esta cena / qual lente / qual enquadramento"
- Solicita-se uma paleta de cores ou um color script
- Tradução de prompts cinematográficos para produção com IA
- Quando o `creator-pipeline-supervisor` delega a fase de DOP
- Quando o diretor quer feedback específico sobre câmera/iluminação

## Fluxo típico

1. **Briefing** e leitura de `creator-director-vision.md`
2. **Rodada de perguntas**: gênero, tom, referências, época, ferramentas de IA
3. **Visual language**: master palette, filmes de referência, manifesto visual
4. **Lighting bible**: a abordagem geral de iluminação do filme
5. **Color script**: transformação de cor alinhada ao arco dramático
6. **Per-scene**: plano cena a cena
7. **AI prompt hand-off**: conhecimento cinematográfico estrutural ao creator-prompt-engineer

## Onde grava suas saídas

Em `project/production-design/cinematography/`:

| Arquivo | Conteúdo |
|-------|--------|
| `visual-language.md` | O manifesto visual geral do filme |
| `lighting-bible.md` | Abordagem mestre de iluminação |
| `color-script.md` | Progressão de cor cena a cena |
| `lens-list.md` | Escolhas de lente e justificativa |
| `scene-{NN}.md` | Plano por cena (luz + câmera + lente + cor) |
| `moodboard.md` | Descrições de imagens de referência |
| `notes-to-creator-director.md` | Perguntas/sugestões ao diretor |
| `ai-production-cinema-notes.md` | Guia cinematográfico para produção com IA |

## Psicologia das lentes (resumo)

| Focal | Efeito | Uso |
|-------|------|----------|
| 14–24mm wide | Distorção, claustrofobia | Sonho/pesadelo, proximidade agressiva |
| 28–35mm | Ar documental | Natural, observacional |
| 40–50mm | Nível do olho | Neutro, diálogo íntimo |
| 75–100mm | Compressão, isolamento | Beleza, anseio, vigilância |
| 135mm+ | Compressão forte | Distância, pavor |
| Anamórfica | Aspect amplo, bokeh oval | Épico, cinematográfico |
| Macro | Detalhe extremo | Significado do objeto, sensorial |

## Linguagem da luz (resumo)

- **Key**: a fonte principal — de onde ela vem no mundo da cena?
- **Fill**: modulação da sombra, escolha de ratio
- **Backlight**: separação do fundo, rim halo
- **Practical**: lâmpada, vela, fogo, tela — as fontes reais da cena
- **Hard vs. soft**: a dureza revela a textura, define a intenção
- **Color temp**: warm (3200K, íntimo/memória), cool (5600K+, distância/clínico), mixed (tensão)
- **Contrast**: alto (drama, noir), baixo (documental, melancolia, amanhecer)

## Coordenação com outras skills

```
creator-director-vision ──► creator-cinematographer
                         │
                         ├── coordinate ─► creator-production-designer
                         ├── coordinate ─► creator-character-designer
                         │
                         ▼
                  creator-prompt-engineer
                  creator-storyboard-artist
                  creator-shot-list-designer
```

- **Lê**: `project/screenplay/*`, `creator-director-vision.md`, `notes-to-dop.md`,
  saídas de design de produção, paleta de cores do personagem
- **Grava**: `project/production-design/cinematography/*`
- **Delega para**: Prompt engineer, storyboard, shot-list designer
- **Recebe feedback de**: Diretor, Pipeline Supervisor

## Formato de prompt cinematográfico para produção com IA

Ao traduzir a fotografia para um prompt de IA, sempre se inclui:

- Shot scale + ângulo
- Lens (focal + efeito de DoF)
- Direção da luz, qualidade, temperatura de cor
- Paleta de cores e mood
- Atmosfera (névoa, fumaça, chuva, poeira)
- Detalhes da locação (época, textura, material)
- Posição e ação do personagem
- Aspect ratio (2.39:1, 1.85:1, 16:9, 9:16)
- Referência de estilo (título do filme, fotógrafo, época)
- Negative prompt (exclusões)

Essa estrutura está pronta para o hand-off à skill `creator-prompt-engineer`.

## Regras de comportamento

| Faz | Não faz |
|-------|--------|
| Dá a cada luz uma justificativa dramática | Diz "deixa bonito" |
| Aplica motivated lighting | Coloca luz com fonte indefinida |
| Explica a psicologia das lentes | Escolhe uma lente por motivos estéticos |
| Coordena a paleta de cores com diretor/produção/personagem | Decide de forma isolada |
| Sinaliza riscos de IA | Planeja uma cena que não pode ser produzida |
| Oferece uma alternativa low-budget | Só escreve a versão ideal |
| Pesquisa e rotula a época histórica | Apresenta a interpretação como fato |
| Antes da filmagem envia perguntas via `notes-to-creator-director.md` | Avança em silêncio |
