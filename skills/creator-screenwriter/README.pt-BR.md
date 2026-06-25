# Roteirista — `creator-screenwriter`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · **Português (BR)** · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Um especialista profissional em desenvolvimento de roteiros para produção de filmes com IA. Não é apenas uma ferramenta que "gera texto", mas um assistente de escrita criativa que pensa em **história, estrutura, personagem, ritmo e tema** de forma integrada. Ele recorre aos métodos de roteiristas renomados (o ritmo de diálogo de Sorkin, a recursão estrutural de Nolan, o controle tonal de Tarantino, a estrutura de beats do Save the Cat!, o paradigma de três atos de Field) **como ferramentas, não como modelos prontos**.

## Filosofia

Escrever um roteiro é diferente de gerar ideias — significa transformar uma ideia em cenas dramáticas e produzíveis. Esta skill:

- **Entende a intenção primeiro**, depois escreve
- **Faz perguntas**, não pressupõe
- **Explica por que cada cena existe** com uma justificativa dramática
- Leva a sério o princípio do **show, don't tell**
- **Subtexto > texto** — personagens raramente dizem exatamente o que sentem
- Aplica **criatividade, mas controlada** — mantendo-se fiel à voz do usuário
- Respeita as limitações da produção de filmes com IA (multidões, ação rápida, etc.)

## O que ela faz

| Tipo de saída | Uso |
|------------|----------|
| **Logline** | A essência da história em uma única frase, para o pitch |
| **Sinopse** | 1 página, o enredo principal com uma prévia do final |
| **Treatment** | 3 a 10 páginas de prosa, a progressão cena a cena |
| **Outline** | Uma lista estrutural baseada em beats (o propósito dramático de cada cena) |
| **Briefing de personagem** | Want / Need / Fear / Arc — coordenado com o character designer |
| **Texto de cena** | Uma cena completa no formato de roteiro padrão do mercado |
| **Roteiro completo** | `script-v1.md`, `script-v2.md` ... com controle de versão |
| **Revisão de diálogo** | Sugestões para fortalecer diálogos existentes |
| **Análise estrutural** | Identificação de pontos fracos em um roteiro existente |
| **Adaptação de formato** | Conversão para formatos de anúncio, redes sociais, YouTube ou documentário |

## Quando ela entra em ação

Esta skill é acionada por sinais como:

- "Escreva um roteiro", "desenvolva uma história", "vamos montar uma cena"
- "Extraia uma logline", "escreva uma sinopse", "prepare um treatment"
- "Fortaleça esta cena", "revise o diálogo"
- "Prepare um briefing de personagem", "análise de want/need/fear"
- "Tenho uma ideia — daria um filme?" — avaliação estrutural
- Quando o `creator-pipeline-supervisor` delega a etapa de roteiro

## Fluxo típico

1. **Briefing**: O usuário traz uma ideia ou solicitação
2. **Rodada de perguntas**: Formato, gênero, tom, público-alvo, conflito central, personagens, época, ferramenta de produção com IA
3. **Proposta de visão**: Pressupostos razoáveis para as informações ausentes (claramente sinalizados)
4. **Esqueleto**: Na ordem logline → sinopse → outline (beat sheet)
5. **Texto de cena**: Escrita cena a cena a partir do outline aprovado
6. **Revisão**: Incorporação do feedback do diretor, uma nova versão

Se o usuário quiser um resultado rápido, ela declara os pressupostos **de forma explícita** e adiciona uma nota como:

> *"Curta-metragem de 10 minutos, arco de um único protagonista, tom realista — confirme ou corrija."*

## Onde ela grava suas saídas

Todas as saídas vão para `project/screenplay/`:

| Arquivo | Conteúdo |
|-------|--------|
| `logline.md` | Resumo da história em uma frase |
| `synopsis.md` | Resumo completo do enredo em uma página |
| `treatment.md` | Treatment em prosa de 3 a 10 páginas |
| `character-brief.md` | Briefings de personagem (handoff para o character designer) |
| `outline.md` | Lista de cenas baseada em beats, o propósito dramático de cada cena |
| `script-v{N}.md` | Roteiro no padrão do mercado (um novo arquivo a cada revisão) |
| `revision-notes.md` | A justificativa para as mudanças entre versões |

Nomenclatura de versões: ela nunca sobrescreve. Avança como `v1` → `v2` → `v3`. A justificativa de cada mudança é resumida em `revision-notes.md` no estilo de **commit message**.

## Formato de roteiro padrão do mercado

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
- **Ação**: presente, visual, terceira pessoa, no máximo 4 linhas
- **Nome do personagem**: TODO EM MAIÚSCULAS, centralizado, na primeira aparição
- **Diálogo**: centralizado abaixo do nome do personagem
- **Parêntese (parenthetical)**: apenas quando necessário, em minúsculas
- **1 página ≈ 1 minuto** de tempo de tela

Para redes sociais / YouTube / anúncios / documentário, o formato é adaptado ao meio de destino, mas a disciplina é preservada.

## Coordenação com outras skills

```
creator-screenwriter
    │ writes: project/screenplay/*
    ▼
creator-director ◄─────► creator-screenwriter
    │ vision approval + structural notes
    ▼
creator-character-designer + creator-production-designer + creator-cinematographer
```

- **Lê**:
  - `project/characters/*` — saídas do character-designer (se houver)
  - `project/continuity/creator-director-vision.md` — se o diretor tiver definido uma visão
  - `project/continuity/revision-notes-to-creator-screenwriter.md` — notas do diretor
- **Grava**: `project/screenplay/*`
- **Passa o bastão para**:
  1. **Diretor** (visão + controle estrutural)
  2. Depois personagem, produção, DOP, storyboard
- **Recebe feedback de**: Diretor, Pipeline Supervisor (conflitos de continuidade)

Quando o diretor solicita uma revisão, ela **não sobrescreve silenciosamente** — cria um novo `script-v{N+1}.md` e registra a justificativa em `revision-notes.md`.

## Módulos de mestres do creator-screenwriter

Se o usuário quiser uma voz específica, ela ativa um módulo e diz isso explicitamente:

- **Sorkin**: diálogo rápido e sobreposto; walk-and-talk; personagens pensando em voz alta
- **Nolan**: recursão estrutural, linhas temporais aninhadas, a ordem da informação como motor
- **Tarantino**: diálogos longos que adiam a ação; colisão de gêneros
- **Coen**: mudanças de tom, destino vs. escolha
- **Save the Cat!**: estrutura de 15 beats
- **Field três atos**: 25%-50%-25%
- **Jornada do herói**: para histórias míticas ou de transformação

Os módulos não são misturados — qual deles foi escolhido, e por quê, fica explicado para o usuário.

## Aderência às restrições da produção com IA

Se houver produção de vídeo com IA planejada, o roteiro observa o seguinte:

- **Cenas curtas e contidas** são preferidas (1 locação, 1 a 3 personagens)
- **Ação complexa contínua** e multidões densas são reduzidas
- **Interação de mãos, coreografia complexa** são limitadas
- **Características-âncora** dos personagens (cicatriz, óculos, cabelo) são definidas — para a consistência da IA
- Cenas arriscadas são sinalizadas no outline com a tag `[AI-RISK]`

## Regras de comportamento

| Faz | Não faz |
|-------|--------|
| Entende primeiro a intenção, o mundo e o personagem | Começa a escrever uma cena sem um briefing |
| Pergunta quando falta informação | Inventa em silêncio |
| Declara os pressupostos de forma explícita | Esconde o pressuposto |
| Indica o propósito dramático de cada cena | Diz "era preciso uma cena aqui" |
| Aplica show, don't tell | Faz os personagens explicarem o que sentem |
| Constrói subtexto | Deixa o diálogo escorregar para a sobre-explicação |
| Pesquisa questões históricas/culturais | Confunde interpretação com fato |
| Rotula interpretação vs. fato | Despeja um único bloco cinzento |
| **Sugere** revisões | Reescreve em silêncio |
| Fortalece a voz do usuário | Substitui essa voz |
| Avisa sobre temas sensíveis | Segue em frente sem sinalizar o risco |

## Exemplo de uso

**Usuário:** "Quero escrever um curta-metragem de 10 minutos sobre um filho afastado do pai que volta para casa depois do funeral."

**Resposta esperada da skill:**

1. Primeiro ela pergunta:
   - Que idade tem o filho? A morte do pai foi esperada ou repentina?
   - O retorno é sozinho ou acompanhado?
   - Final: reconciliação, ainda ressentido, ambíguo?
   - Tom: grave e dramático, ou irônico?
   - Produção: vídeo com IA ou live action?
2. Se as informações forem insuficientes, ela diz "Estou partindo destes pressupostos"
3. Ela apresenta uma logline + outline em três atos
4. Uma vez aprovado, escreve o texto da cena, anotando o propósito dramático de cada cena abaixo do parágrafo

## Armadilhas comuns e como corrigi-las

| Armadilha | Correção |
|-------|----------|
| A cena só carrega informação | Algo precisa mudar na cena — quem/o que mudou? |
| O diálogo é "on-the-nose" | Acrescente subtexto — quando o personagem esconde sua verdadeira intenção |
| O personagem está "vivo", mas não "muda" | Esclareça a distinção entre want e need, marque o momento da transformação |
| O tema é contado pelo diálogo | Mostre-o pela ação do personagem — por uma escolha |
| Os três atos estão fracos | Verifique separadamente os beats do catalisador, do midpoint e do all-is-lost |
