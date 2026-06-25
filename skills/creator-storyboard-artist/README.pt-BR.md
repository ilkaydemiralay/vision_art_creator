# Artista de Storyboard — `creator-storyboard-artist`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Uma skill que transforma um roteiro escrito em **narrativa visual legível**. Ao
minimizar a quantidade de painéis, ela garante que cada painel exista por um
motivo dramático. Captura os momentos críticos de uma cena, preserva o screen
direction, acompanha a eyeline continuity e faz um hand-off limpo para os prompts
de imagem/vídeo de IA.

## Filosofia

Um storyboard não é "desenhar a cena" — é um **sistema de narrativa visual**. Esta skill:

- **Panel economy**: poucos painéis + escolhas precisas — não muitos painéis + decisões fracas
- **Screen direction (180°)** e **eyeline continuity**: consistência espacial entre cortes
- **Graphic dynamics**: onde o olhar pousa? qual é o foco?
- **Continuity awareness**: figurino, locação, direção da luz, direção de tela, movimento
- **Locked anchors**: character DNA + location master reference em cada painel
- **Producibility**: conhece as restrições de produção com IA e sinaliza cenas arriscadas

## Para que serve

| Saída | Conteúdo |
|-------|----------|
| **Per-scene storyboard** | Lista de painéis cena a cena (todos os dados do painel) |
| **Per-panel sheets** | Arquivo detalhado de painel único para cenas complexas |
| **AI image prompts** | Prompt pronto para produção por painel |
| **AI video prompts** | Prompt de vídeo para painéis em movimento |
| **Continuity log** | Sinalizações de riscos de figurino/locação/direção |
| **Animatic plan** | Planeja a ordem do animatic de todas as cenas |
| **Director / DOP notes** | Notas visuais/técnicas breves para o diretor e o DOP |
| **Handoff to shot-list** | Dados do painel no formato creator-shot-list-designer |

## Quando entra em ação

- Há um roteiro em mãos e deseja-se uma decupagem visual
- Quando o diretor quer visualizar uma cena com antecedência
- Quando se precisa de um conceito visual antes das decisões de lente/luz do DOP
- Quando se deseja a lógica do storyboard antes de gerar prompts de IA
- Quando o `creator-pipeline-supervisor` delega a etapa de storyboard

## Panel content (campos canônicos)

Cada painel registra estes campos:

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

## Onde escreve suas saídas

Sob `project/storyboards/`:

| Arquivo | Conteúdo |
|---------|----------|
| `scene-{NN}/storyboard.md` | Lista de painéis por cena (canônica) |
| `scene-{NN}/panel-{PP}.md` | Painel único detalhado (em cenas complexas) |
| `scene-{NN}/prompts.md` | Prompts de IA por painel (image + video) |
| `scene-{NN}/continuity.md` | Sinalizações de continuity |
| `animatic-plan.md` | Notas de ordenação do animatic de todo o filme |
| `notes-to-creator-director.md` | Perguntas/avisos para o diretor |
| `handoff-to-shot-list.md` | Dados de painel formatados para o shot-list designer |

## Glossário de shot type (com o equivalente dramático)

| Tipo | Uso dramático |
|------|---------------|
| Establishing | Posiciona o espectador no espaço |
| Master | Geometria da cena, fallback |
| Wide/Full | Relação personagem–ambiente |
| Medium | Diálogo neutro |
| Close | Conflito interno, emoção íntima |
| Extreme close | Intensidade subjetiva |
| Insert | Ênfase em objeto |
| Cutaway | Informação paralela/externa |
| Reaction | Reação acima da ação |
| OTS | Perspectiva de diálogo |
| POV | Subjetividade do personagem |
| 2-shot / group | Geometria da relação |
| Silhouette | Anonimato, mistério |
| Negative-space frame | Isolamento, pequenez |
| Symmetrical | Poder, formalidade, imobilidade inquietante |
| Tracking | Acompanhamento contínuo |
| Static | Observação, o significado do silêncio |

"Use um close-up" não basta — a pergunta é **por que** um close-up é necessário.

## Continuity audit

Acompanhamento de painel a painel, de cena a cena:

- Figurino
- Cabelo/maquiagem/acessórios
- Identidade da locação (com locked anchor)
- Direção da luz
- Dia/noite
- Screen direction (regra dos 180°)
- Lógica espacial dos personagens
- Fluxo da ação
- Posição dos props

Quando um risco é detectado, ele é escrito explicitamente no campo `continuity note` do painel.

## Coordenação com outras skills

- **Lê**: roteiro, visão do diretor + direction sheets, plano per-scene do DOP,
  character DNA + FACS, anchors de locação
- **Escreve**: `project/storyboards/*`
- **Delega**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → otimização específica por ferramenta)
- **Recebe feedback de**: Diretor, Pipeline Supervisor

## Soluções focadas na produção com IA

- Divide cenas complexas em painéis simples
- Esclarece o foco visual em cenas com vários personagens
- Simplifica movimentos com os quais a IA teria dificuldade
- Usa anchors fixos para a mesma locação/personagem
- Oferece uma alternativa segura de plano estático em vez de movimento de câmera
- Sugere enquadramentos seletivos em cenas cheias
- Sugere cortes rítmicos em vez de ação rápida

## Regras de comportamento

| Faz | Não faz |
|-----|---------|
| Escreve uma justificativa dramática para cada painel | Preenche com "mais um painel" só por preencher |
| Poucos painéis + escolhas precisas | Muitos painéis + decisões fracas |
| Unifica roteirista + diretor + DOP + personagem + produção | Atropela o upstream em silêncio |
| Preserva o screen direction e a eyeline | Embaralha a direção em um corte |
| Coloca os locked anchors em cada prompt | Descreve do zero em cada painel |
| Divide a cena complexa em painéis | Empilha tudo em um único frame sobrecarregado |
| Flag de risco de IA + alternativa segura | Sugere um movimento improduzível |
| Saída estruturada e legível a jusante | Despeja um único bloco de texto |
