# Designer de lista de planos — `creator-shot-list-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · **Português (BR)** · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A skill que transforma cenas e storyboards em uma **lista de planos + intenção de edição**.
O lugar onde o planejamento de pré-produção e a intenção editorial se encontram. Ela não
é a editora de corte final — ela projeta a intenção editorial ANTES de qualquer material ser
produzido, para que a filmagem gere as peças certas.

## Filosofia

Uma lista de planos não é um inventário técnico; é um **mapa da intenção dramática +
editorial**. Esta skill:

- **Economia de planos**: cada plano carrega uma única ação clara
- **Consciência do ritmo de edição**: qual plano é sustentado por mais tempo, qual é cortado
  rapidamente? A duração do plano é uma decisão editorial
- **Direção de tela + continuidade**: consistência espacial/temporal através dos cortes
- **Producibilidade para AI**: planeja a complexidade de cada plano em torno das restrições das ferramentas de AI
- **Intenção editorial antes da produção**: a lógica da edição é definida ANTES da filmagem
  para que planos desnecessários não sejam filmados
- **Design da experiência do público**: o que o espectador sente, aprende, e o que é omitido?

## O que ela produz

| Saída | Conteúdo |
|-------|---------|
| **Lista de planos por cena** | Lista de planos canônica, com justificativa dramática + editorial |
| **Plano de edição** | Ritmo dentro da cena, pontos de corte, imagem de abertura/fechamento |
| **Design de transições** | Decisões de transição entre cenas (hard cut, match, J/L, sound bridge) |
| **Auditoria de riscos de continuidade** | Relatório de riscos de consistência entre planos |
| **Notas de edição de som** | Pontos de J-cut / L-cut / silêncio para o sound designer |
| **Lista de planos de todo o filme** | Lista consolidada cobrindo o filme inteiro |
| **Mapa de ritmo** | Ritmo cena a cena (faixas de duração dos planos) |
| **Relatório de redundância** | Planos que devem ser cortados/fundidos |
| **Notas para a editora final** | Transferência da intenção editorial para a editora de corte final |

## Quando ela entra em cena

- Cenas e storyboards estão prontos, e é necessário um plano baseado em planos
- É solicitado um sequenciamento de planos consciente da edição
- Cenas longas precisam ser divididas em peças producíveis por AI
- Quando o diretor ou o DOP solicita um plano estrutural de filmagem/produção
- Quando o `creator-pipeline-supervisor` delega o planejamento de pré-edição

## Fluxo típico

1. **Briefing** + leitura de todas as saídas das skills anteriores
2. **Rodada de perguntas**: formato, ritmo de edição, tom, ferramentas de AI
3. **Lista de planos (por cena)**: em estrutura canônica, com justificativa dramática + editorial
4. **Plano de edição (por cena)**: ritmo, abertura/fechamento, pontos de corte
5. **Design de transições**: transições entre cenas
6. **Auditoria de continuidade**: riscos entre planos
7. **Mapa de ritmo**: mapa de ritmo de todo o filme
8. **Relatório de redundância**: identificação de planos cortáveis
9. **Transferência**: dados de prompt de planos para o creator-prompt-engineer + intenção editorial para o creator-final-cut-editor

## Plano — estrutura canônica

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

## Intenção editorial — plano da cena

Perguntas editoriais no nível da cena:

- Qual plano abre a cena?
- Qual imagem a fecha?
- Qual plano é sustentado por mais tempo?
- Qual plano é cortado curto?
- Onde vão os reaction shots?
- Onde o silêncio se estende?
- Onde é necessário um hard cut?
- Onde há uma transição suave?
- Qual imagem conecta com a próxima cena?
- Qual plano carrega o pico dramático?
- Qual plano é desnecessário?
- Qual plano entrega informação, qual entrega emoção?

Escrito em `project/shot-list/scene-{NN}/edit-plan.md`.

## Onde ela escreve suas saídas

Em `project/shot-list/`:

| Arquivo | Conteúdo |
|-------|---------|
| `scene-{NN}/shot-list.md` | Lista de planos da cena |
| `scene-{NN}/edit-plan.md` | Intenção de edição + ritmo |
| `scene-{NN}/transitions.md` | Decisões de transição |
| `scene-{NN}/continuity-risks.md` | Auditoria de continuidade |
| `scene-{NN}/sound-edit-notes.md` | Transferência para o sound designer |
| `film-shot-list.md` | Lista consolidada de todo o filme |
| `rhythm-map.md` | Mapa de ritmo |
| `redundancy-report.md` | Planos cortáveis |
| `ai-production-shot-guide.md` | Guia de restrições das ferramentas de AI |
| `final-editor-notes.md` | Intenção para a editora de corte final |

## Tipos de transição (uso editorial)

| Transição | Uso editorial |
|-------|-------------------|
| Hard cut | Ruptura dramática súbita |
| Match cut | Uma ponte de significado entre duas imagens |
| Fade in/out | Abertura/fechamento temporal/emocional |
| Dissolve | Transição de tempo, fusão emocional |
| J-cut | O som da próxima cena chega primeiro (fluxo suave) |
| L-cut | O som da cena atual é estendido (emoção sustentada) |
| Sound bridge | Mudança de lugar/tempo conduzida pelo som |
| Motivo visual | Uma ponte por meio de um elemento visual recorrente |
| Transição por objeto | Combinação de forma |
| Transição por movimento | Continuidade direcional |
| Salto temporal | Pulo súbito no tempo |
| Flashback | Por meio de filtro/lente/desfoque/deixa sonora |
| Edição paralela | Dois lugares entrelaçados |

## Regras de producibilidade de vídeo por AI

- Uma ação clara por plano
- Um movimento de câmera principal (não encadeado)
- Um número controlado de personagens
- Um alvo visual claro
- Quebrar movimentos complexos em múltiplos planos
- Sinalizar riscos de mão/dedos/lip sync
- Enquadramento seletivo para multidões
- Anchors de locação + personagem travados em cada prompt
- Duração do plano tipicamente de 3 a 10s
- Cada plano mapeia limpamente para um único prompt de vídeo

Quando um risco é detectado, sinalize-o:

> *"Este plano é complexo demais para vídeo por AI — divida-o em dois planos."*
> *"O lip sync pode falhar aqui; use um reaction shot em vez de quem fala."*
> *"O movimento da mão é crítico — use um enquadramento mais aberto em vez de um insert."*
> *"Ação de multidão — construa com cortes, não com um único plano."*

## Ritmo e cadência

Frases vagas como "deixa rápido" não são usadas. O ritmo é:

- Expresso como uma **faixa de duração de plano**
- Medido pela **frequência de cortes**

Exemplo:
> *"A cena 3 tem em média 4–6s/plano, a cena 12 tem em média 1.5–3s/plano —
> o ritmo acelera à medida que o conflito do personagem escala."*

## Intenção de edição de diálogo

Para cenas com muito diálogo:

- Quem fala ou quem escuta?
- Onde vão os reaction shots?
- Onde o silêncio é mais forte?
- Outra imagem sobre o diálogo?
- Subtexto através da expressão facial?
- Hard cut vs. sobreposição natural?
- Cortar antes da frase terminar?
- Repetição redundante de explicação?
- Em quem está a emoção que o espectador realmente precisa ver?

Os marcadores de J-cut / L-cut são definidos aqui.

## Coordenação com outras skills

- **Lê**: roteiro, visão do diretor + fichas de direção, plano por cena do DOP,
  dados dos painéis de storyboard, anchors de personagem/locação
- **Escreve**: `project/shot-list/*`
- **Transfere para**:
  - `creator-prompt-engineer` (prompts de vídeo no nível do plano)
  - `creator-final-cut-editor` (arquivos de intenção editorial)
- **Recebe feedback de**: Diretor, Pipeline Supervisor

## Detecção de redundância

Em um filme longo feito por AI, sinalize:

- Um plano que repete a mesma informação
- Um plano que não muda a emoção
- Um plano de detalhe que derruba o ritmo
- Uso excessivo de reaction shots
- Um plano difícil para AI com baixa contribuição dramática
- Oportunidades de late-in / early-out
- Um momento que pode ser contado visualmente em vez de no diálogo

*"Este plano pode ser cortado"* ou *"Estes dois planos podem ser fundidos"* é escrito explicitamente.

## Regras de comportamento

| Faz | Não faz |
|-------|---------|
| Dá a cada plano uma justificativa dramática **e** editorial | Fazer um inventário técnico |
| Coordena com o ritmo do diretor, o enquadramento do DOP, o storyboard | Decidir isoladamente |
| Sinaliza planos desnecessários | Adicionar enchimento |
| Verifica a continuidade de forma proativa | Esperar que os problemas apareçam após a filmagem |
| Projeta em torno das restrições das ferramentas de AI | Planejar planos não producíveis |
| Uma alternativa segura para planos arriscados | Fornecer uma única versão |
| Considera também quem escuta no diálogo | Seguir apenas quem fala |
| Coordena a intenção editorial de som e música | Pensar apenas na imagem |
| Saída estruturada, legível pelas etapas seguintes | Despejar um único bloco de texto |
