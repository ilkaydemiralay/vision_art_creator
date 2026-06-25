# Designer de Som e Música — `creator-sound-music-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [**Português (BR)**](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

O skill que constrói o **mundo sensorial** do filme. Duas disciplinas integradas se unem:
- **Sound designer**: a realidade sensorial de espaços, personagens, objetos e eventos — ambience, foley, efeitos, acústica, perspectiva sonora e **silêncio** (como ferramenta dramática ativa)
- **Compositor de cinema / supervisor musical**: tema principal, leitmotifs de personagens, música de cena, ritmo, pontos de entrada/saída da música

## Filosofia
Som e música **não são decoração**. Cada decisão de som e música está ligada ao propósito dramático da cena, à psicologia do personagem, à atmosfera visual, ao ritmo de edição e ao impacto sobre a audiência. Este skill:
- Não diz "use uma música triste" — ele projeta leitmotifs e planeja sua evolução
- **Projeta o silêncio de forma ativa** — não como ausência, mas como decisão dramática
- **Leitmotifs de personagens**: um motivo que começa numa flauta se transforma em algo épico com cordas no final
- **Disciplinado quanto a direitos autorais**: não imita artistas vivos, "parecido, mas não igual"
- **Em sincronia com o ritmo de edição**: entrada/saída da música coordenada com o plano de edição do shot-list
- **Geração de prompts de som/música por IA**: Suno, Udio, ElevenLabs SFX, Stable Audio, Runway Audio

## O que ele faz
| Saída | Conteúdo |
|-------|----------|
| **Visão sonora** | A visão geral de sound design do filme |
| **Visão musical** | O manifesto da linguagem musical do filme |
| **Tema principal** | Design do tema principal |
| **Temas de personagens** | Design de leitmotif por personagem |
| **Planos de cena** | Plano de som + música cena a cena |
| **Listas de ambience / foley / SFX** | Listas de inventário |
| **Plano de silêncio** | Um mapa deliberado do silêncio |
| **Plano de entrada/saída da música** | Pontos de entrada e saída da música |
| **Pontes sonoras** | Design de transição |
| **Prompts de som + música por IA** | Prompts específicos por ferramenta |
| **Notas de balanço de diálogo** | Notas de balanço entre diálogo/música |
| **Notas de mix final** | Auditoria do final mix |
| **Relatório de continuidade** | Verificação de continuidade sonora |

## Quando ele entra em ação
- Há um roteiro em mãos e é preciso um plano de sound design / música de cinema
- São solicitados ambience, foley, SFX ou temas musicais
- São necessários prompts de som/música por IA
- Quando o shot-list designer repassa a intenção sonora da cena
- Quando o `creator-pipeline-supervisor` delega a etapa de áudio

## Fluxo típico
1. **Briefing** + leitura de todas as saídas dos skills anteriores
2. **Rodada de perguntas**: gênero, register, densidade musical, época, ferramentas de IA
3. **Visão sonora** + **Visão musical**
4. **Tema principal + leitmotifs de personagens**
5. **Plano por cena**: ambient/foley/silêncio/música para cada cena
6. **Plano de silêncio**: um mapa do silêncio deliberado
7. **Plano de entrada/saída da música**
8. **Prompts de som + música por IA**
9. **Auditoria do mix final** (após o final cut)

## Design do silêncio
O silêncio é uma decisão de design **ativa**. Para cada silêncio, o skill pergunta:
- A música vai cortar aqui?
- A ambience é atenuada ou zerada?
- Vai restar apenas uma respiração, ou o som de um pequeno objeto?
- O silêncio transmite solidão, medo ou hesitação?
- Ele está ali para inquietar a audiência ou para intensificar a emoção?
- Qual som entra depois do silêncio?

## Exemplo de leitmotif de personagem
```
Karakter: Demir
Müzikal duygu: bastırılmış yas + içsel kararlılık
Ana enstrüman: solo cello (başlangıç) → cello + ney (orta) → cello + yaylı
                grup (final)
Tempo: 60–66 BPM (slow heart)
Ton: minör, kromatik geçişler
Ritim: rubato, neredeyse zamansız
Motifin evrimi:
  - Sahne 1–5: solo cello, kısa 5-notalı motif, sessizlik aralıkları geniş
  - Sahne 6–12: ney ekleniyor — nefes katmanı
  - Sahne 13–18: yaylı grup açılıyor — toplum, geçmiş, anlam
  - Sahne 19 (final): tek cello, ilk motifin yarısı — kırılma
```

## Onde ele grava suas saídas
Em `project/sound/`:
| Arquivo | Conteúdo |
|---------|----------|
| `sound-vision.md` | Visão geral de sound design |
| `music-vision.md` | Manifesto da linguagem musical |
| `main-theme.md` | Design do tema principal |
| `character-themes/{slug}.md` | Leitmotif de personagem |
| `scenes/scene-{NN}.md` | Plano de som + música da cena |
| `ambience-list.md` | Inventário de ambience |
| `foley-list.md` | Inventário de foley |
| `special-effects-list.md` | SFX especiais |
| `silence-plan.md` | Mapa do silêncio |
| `music-entry-exit-plan.md` | Timing de entrada/saída da música |
| `sound-bridges.md` | Design de transição |
| `ai-sound-prompts.md` | Prompts de SFX por IA |
| `ai-music-prompts.md` | Prompts de música por IA |
| `dialogue-balance-notes.md` | Balanço entre diálogo/música |
| `final-mix-notes.md` | Auditoria do final mix |
| `sound-continuity-report.md` | Verificação de continuidade |

## Formato de prompt de IA
### Exemplo de prompt de SFX
```
Old wooden door slowly creaking open in a quiet rural house interior,
close perspective, dry wooden texture, subtle room reverb, tense and
restrained mood, no music, no voices, 4 seconds.
```
### Exemplo de prompt de música
```
Slow cinematic period drama cue, melancholic and restrained, solo cello
with soft ney-like woodwind texture, sparse low percussion, warm but
somber atmosphere, gradual emotional rise, no modern drums, no pop
rhythm, 60 seconds.
```
### Formato de descrição no idioma nativo + prompt em inglês
```
Türkçe Açıklama:
Bu sahnede müzik duyguyu açıkça anlatmamalı; karakterin içindeki
bastırılmış pişmanlığı alttan desteklemeli.

English Music Prompt:
Minimal cinematic drama score, restrained emotional tension, solo cello
and soft ambient drone, slow tempo, subtle rise, intimate and sorrowful,
no strong melody, no percussion, 45 seconds.
```

## Direitos autorais e originalidade
- Não sugere copiar composições existentes
- Não imita o estilo de um artista vivo nota por nota
- Trabalha com a lógica "parecido, mas não igual", descrevendo gênero + emoção
- Em prompts de música por IA, usa a atmosfera geral em vez do nome de um artista

## Coordenação com outros skills
- **Lê**: todas as saídas criativas anteriores + notas de edição sonora do shot-list
- **Grava**: `project/sound/*`
- **Delega para**: `creator-final-cut-editor` (integração do final cut), o operador da ferramenta de áudio por IA
- **Recebe feedback de**: Diretor, Pipeline Supervisor, Final-cut-editor

## Regras de comportamento
| Faz | Não faz |
|-----|---------|
| Liga som e música ao propósito dramático | Usa-os como decoração |
| Projeta o silêncio de forma ativa | Trata-o como ausência |
| Sincroniza a evolução do leitmotif com o arco do personagem | Repete um único tema fixo |
| Pensa diálogo/música/ambience/silêncio em conjunto | Decide de forma isolada |
| É disciplinado quanto a direitos autorais | Imita artistas |
| Faz pesquisa histórica/cultural e a rotula | Apresenta interpretação como fato |
| Escreve prompts de IA adequados à ferramenta | Despeja prompts genéricos |
| Preserva a continuidade sonora de um filme longo | Pensa cena a cena e de forma desconexa |
