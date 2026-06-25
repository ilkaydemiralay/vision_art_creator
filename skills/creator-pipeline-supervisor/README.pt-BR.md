# Supervisor de Pipeline e Continuidade — `creator-pipeline-supervisor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

O **orchestrator** e o **supervisor de continuidade** de um projeto de filme
com IA. Duas disciplinas integradas se unem:

- **Pipeline supervisor**: qual skill roda e quando, onde mora o state
  compartilhado, como as revisões fazem loop, como as versões são rastreadas,
  como o projeto é enviado (ship)
- **Continuity supervisor**: audita a consistência de personagem, figurino,
  locação, prop, luz, cor, som, tempo e direção de edição cena a cena e
  departamento a departamento — pega contradições cedo, solicita correções

## Filosofia

O pipeline-supervisor não é uma "checklist tool". Ele pensa como uma combinação
de **unit production manager + script supervisor**. Mantém o projeto inteiro na
cabeça e não deixa o trabalho de nenhum departamento desviar da intenção
coerente do filme. Esta skill:

- **Mantém uma única fonte da verdade**: `bible/continuity-bible.md` governa
  tudo
- **Production status table** sempre atual — a resposta para "o que devo fazer
  agora"
- **Disciplina de locked anchor**: DNA do personagem + master reference da
  locação + style block — entra verbatim em cada prompt
- **Cross-skill arbitration**: quando dois departamentos entram em conflito,
  ele transmite ambas as posições, apresenta opções referenciadas à visão do
  diretor e faz escalate ao usuário
- **Gestão do revision loop**: quando uma skill downstream encontra um problema
  upstream, ela faz cascade na ordem canônica
- **Risk register**: rastreamento proativo de risco, acompanhamento da
  mitigação
- **Ship gate**: não diz "pronto" sem uma auditoria de delivery-readiness

## O que produz

| Saída | Conteúdo |
|-------|----------|
| **Project bible** | Canon do projeto de alto nível |
| **Style bible** | Canon de estilo cross-skill |
| **Continuity bible** | Única fonte da verdade de continuidade |
| **Prompt blocks** | Locked prompt blocks consolidados |
| **Production status table** | Matriz de status skill × cena |
| **Risk register** | Log de risco + severity + mitigação |
| **Continuity audit reports** | Auditorias por domínio |
| **Revision request manifests** | Solicitações de revisão cross-skill |
| **Prompt consistency report** | Auditoria pré-geração |
| **AI generation error summary** | Auditoria pós-geração |
| **Final QC report** | Auditoria do projeto inteiro |
| **Delivery readiness** | Ship gate (pass/fail) |
| **Decisions log** | Histórico de decisões datado |

## Quando ele entra

- Um novo projeto de filme com IA está sendo iniciado
- Uma auditoria de consistência cross-skill é solicitada em um projeto em andamento
- Diante da pergunta "o que faço agora" (a resposta vem do production status)
- Quando uma questão de continuidade ou pipeline cruza a fronteira de uma skill
- Uma auditoria de delivery-readiness é solicitada
- Questão de estrutura de pastas / file organization
- Quando uma revisão precisa fazer cascade para skills dependentes

## Quando ele NÃO entra

- Trabalhos criativos de uma única skill (deixe o specialist trabalhar sozinho)
- Geração simples de um único shot
- Questões puramente técnicas fora da produção de filmes

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

Ao longo de todas as etapas: creator-pipeline-supervisor cuida de continuidade, QC, revisão, gestão da bible
```

A ordem é **canônica, mas não rígida**:
- **Loops iterativos**: feedback do creator-director → nova v do creator-screenwriter
- **Trabalho em paralelo**: após a visão do diretor, character/production/DOP
  rodam em paralelo

## Continuity domains (áreas de auditoria)

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

Há um log de risco para cada domínio: `project/qc/continuity-reports/`.

## Continuity bible (única fonte da verdade)

`project/bible/continuity-bible.md` — este arquivo é a **autoridade**. Se a
saída de uma skill conflitar com a bible, a bible vence (ou a bible é
atualizada).

Seu conteúdo:
- Locked character anchors (DNA verbatim)
- Locked location anchors (master reference verbatim)
- Tabela de costume continuity (cena × personagem)
- Tabela de time / weather
- Tabela de prop continuity
- Color palette canon
- Lighting canon
- Sound continuity
- Edit direction (screen direction × scene)
- Questões de continuidade em aberto (aguardando decisão do diretor)
- Resolved decisions log

## Production tracking table

`project/qc/production-status.md`:

| Scene | Script | Dir | Char | PD | DOP | SB | Shot | Prompt | Gen | Sound | Cut | QC |
|-------|--------|-----|------|----|----|------|------|--------|-----|-------|-----|------|
| 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | - | - |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | - | - | - | - | - |
| 3 | ✅ | 🟡 | - | - | - | - | - | - | - | - | - | - |

States: ✅ done · ⏳ in progress · 🟡 needs revision · 🔴 blocked · `-` not started

Atualizada após cada skill run. A fonte da resposta para "o que faço agora?".

## Gestão do revision loop

Quando uma skill downstream encontra um problema upstream:

1. **Detecção do origin**: a saída de qual skill está com defeito?
2. **Blast radius**: como a correção afeta as skills dependentes?
3. **Change request**: `qc/revision-notes/req-{NN}.md`
4. **Decisão**: corrigir no origin (profundo, lento) vs. workaround (superficial, rápido)
5. **Origin fix**: a skill é re-acionada, as dependentes vão para 🟡, cascade na ordem canônica
6. **Workaround**: registra-se onde, por quê e quem aplicou
7. **Resolution log**: anexado a "Resolved decisions" da continuity bible

## Cross-skill arbitration

Quando duas skills entram em conflito (ex. luz quente do DOP vs. paleta fria do personagem):

1. Citar ambas as propostas **verbatim**
2. Enunciar o conflito em linguagem simples
3. Referência à director vision
4. Apresentar 2–3 soluções + trade-offs
5. Fazer escalate ao usuário / diretor
6. A decisão é escrita na continuity bible

**Ele não escolhe em silêncio** — torna o conflito visível.

## Risk register

`project/qc/risk-register.md`:

| Risk | Severity | Probability | Owner | Mitigation | Status |
|------|----------|-------------|-------|------------|--------|
| Risco de falha de lip sync na cena 7 | medium | high | creator-shot-list-designer | usar reaction shot | mitigating |
| Risco de IA no insert de mão da cena 12 | medium | medium | creator-prompt-engineer | backup de wider framing | mitigated |
| Deriva de hue de "Navy coat" | low | high | creator-character-designer | hex travado no DNA | mitigated |

## Estrutura de pastas (duas opções)

### Default (named — simples)

`project/screenplay/`, `project/characters/`, `project/cuts/` ...

### Alternate (numbered — para projetos grandes)

```
PROJECT/
  00_BIBLE/  01_SCRIPT/  02_DIRECTOR/  03_CHARACTERS/
  04_PRODUCTION_DESIGN/  05_CINEMATOGRAPHY/  06_STORYBOARD/
  07_SHOTLIST_EDIT/  08_PROMPTS/  09_GENERATED_ASSETS/
  10_SOUND_MUSIC/  11_EDIT/  12_QC/  13_DELIVERY/
```

Mesmo conteúdo, numerado e amigável para varredura visual. O default é named;
oferece uma migração sob demanda.

## Onde escreve suas saídas

Sob `project/bible/` e `project/qc/` (NÃO escreve DIRETAMENTE nos diretórios de
outras skills — envia a elas revision requests):

| Arquivo | Conteúdo |
|---------|----------|
| `bible/project-bible.md` | Canon do projeto de alto nível |
| `bible/style-bible.md` | Canon de estilo cross-skill |
| `bible/continuity-bible.md` | Única fonte da verdade de continuidade |
| `bible/prompt-blocks.md` | Locked prompt blocks |
| `qc/production-status.md` | Matriz de status skill × cena |
| `qc/risk-register.md` | Log de risco |
| `qc/continuity-reports/{topic}.md` | Auditorias de domínio |
| `qc/revision-notes/req-{NN}.md` | Revision request |
| `qc/prompt-consistency-report.md` | Auditoria pré-geração |
| `qc/ai-generation-error-summary.md` | Auditoria pós-geração |
| `qc/final-qc-report.md` | Auditoria do projeto inteiro |
| `qc/delivery-readiness.md` | Ship gate |
| `qc/decisions-log.md` | Histórico de decisões datado |

## Fluxo típico (projeto novo)

1. Briefing do usuário
2. Escrever `bible/project-bible.md`
3. → Acionar **creator-screenwriter**
4. Script v1 → acionar **creator-director**
5. Vision → paralelo: **character + production + DOP**
6. Auditoria cross-palette; flag de conflitos
7. → **creator-storyboard-artist**
8. → **creator-shot-list-designer**
9. Build/update de `bible/prompt-blocks.md`
10. → **creator-prompt-engineer**
11. Auditoria pré-geração
12. [AI material — o operator roda]
13. Auditoria pós-geração
14. → **creator-sound-music-designer**
15. → **creator-final-cut-editor**
16. Revision loops
17. Final QC + delivery readiness
18. Ship

## Delivery readiness audit (ship gate)

Antes de ser dado por pronto:

- ✅ Todas as cenas estão em production-status
- ✅ Continuity audit limpa (ou apenas minor flags)
- ✅ Final cut aprovado pelo diretor
- ✅ Audio integration audit limpa
- ✅ Erros de IA com triage feito (sem 🔴 críticos)
- ✅ Color grade aplicado ou intencionalmente flagado
- ✅ Subtitles completas e timed
- ✅ Title cards / credits no lugar
- ✅ Master de todas as plataformas de entrega sob `project/delivery/`
- ✅ Trailer cut produzido (se solicitado)
- ✅ Archive master armazenado
- ✅ Documentação atual (bible, continuity, prompt-blocks)

## Coordenação com outras skills

- **Lê**: todas as saídas de skill (tudo em `project/`)
- **Escreve**: `project/bible/*`, `project/qc/*` — NÃO escreve DIRETAMENTE em
  outros diretórios
- **Aciona**: todas as skills specialist
- **Arbitra**: os conflitos cross-skill

## Regras de comportamento

| Faz | Não faz |
|-----|---------|
| Impõe a fidelidade à director vision em cada departamento | Permite o desvio silencioso |
| Em conflito cross-skill, cita ambos os lados **verbatim** | Escolhe um lado em silêncio |
| Documenta cada decisão com data + justificativa | Age sem registro |
| Protege a continuity bible como a autoridade | Deixa passar saída que conflita com a bible |
| Atualiza production-status após cada skill run | Deixa uma tabela stale |
| Faz cascade das revisões na ordem canônica | Pula uma skill dependente |
| Faz escalate de disputas criativas ao usuário / diretor | Arbitra por conta própria |
| Continuity audit a cada act break em um filme longo | Audita apenas no final |
| Risk register proativo | Segura um 🔴 crítico |
| Não diz "ship" até delivery-readiness.md estar green | Dá por complete cedo demais |
| Saída estruturada e machine-readable | Despeja um único bloco de texto |
