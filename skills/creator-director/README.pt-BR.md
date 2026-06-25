# Diretor — `creator-director`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · **Português (BR)** · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

O **líder criativo** da produção de filmes com IA. A skill que lê e interpreta
o roteiro, questiona por que cada cena existe, dá direção de atuação, conecta
as decisões de câmera/luz/som à intenção dramática e unifica todos os departamentos
sob uma única visão cinematográfica. Ela não escreve o roteiro em si, nem decompõe
cenas em quadros por conta própria — ela **dirige** o trabalho que os outros fazem.

## Filosofia

Dirigir não é uma habilidade técnica, mas **pensamento dramático holístico**. Esta skill:

- Faz disso uma obsessão: nunca perder **a emoção central do filme** cena a cena
- Usa **verbos jogáveis** (playable verbs): em vez de "fique triste", diga "convença", "esconda", "defenda"
- **Mise-en-scène** e **proxêmica** — a composição e a distância carregam significado
- **Subtexto**: não o que os personagens dizem, mas por que dizem — é isso que importa
- **DNA do personagem + Verdade Visual de Base (Visual Ground Truth)**: estabelece âncoras de
  personagem e locação para a consistência da IA
- **Toda decisão de direção carrega uma justificativa dramática** — "fica bonito" não basta

## O que ela faz

| Saída | Conteúdo |
|--------|--------|
| **Documento de visão (Vision document)** | A emoção central do filme, tema, ritmo, tom de atuação, mundo visual |
| **Direction Sheet (por cena)** | O propósito dramático da cena, subtexto, direção de atuação, abordagem de câmera |
| **Notas de atuação** | Por personagem: o que sente ao entrar, o que quer, como demonstra |
| **Acompanhamento do arco do personagem** | Mapa da transformação do personagem ao longo do filme, cenas de virada |
| **Auditoria de tom** | Relatório de consistência tonal entre todas as cenas, rupturas e sugestões de revisão |
| **Notas para o creator-screenwriter** | Feedback estrutural/dramático — por que uma cena é fraca, como fortalecê-la |
| **Notas para o DOP** | Comentários específicos sobre decisões de câmera/luz/lente (não vagos) |
| **Notas para o editor** | Notas sobre ritmo, corte, montagem paralela, transições |
| **Guia de produção com IA** | Quais cenas são arriscadas, abordagens alternativas |

## Quando ela entra em ação

- Quando há um roteiro em mãos e se deseja **uma visão criativa**
- "Como esta cena deve ser filmada", "o que ela deve transmitir", "o que está forte e o que está fraco"
- Verificar a consistência tonal ao longo do filme
- Quando o DOP ou o designer de personagens precisa de um árbitro para uma decisão criativa
- Quando o `creator-pipeline-supervisor` delega a fase de direção
- Quando o roteirista solicita feedback estrutural antes de fazer uma revisão

## Fluxo típico

### Novo projeto
1. **Briefing**: Roteiro, tratamento ou ideia de história
2. **Rodada de perguntas**: Assunto central, emoção-alvo, registro tonal, referências, formato, ferramentas de IA
3. **Documento de visão**: O arcabouço filosófico/dramático do filme → `project/continuity/creator-director-vision.md`
4. **Passagem cena a cena**: Uma Direction Sheet para cada cena
5. **Coordenação entre skills**: Notas específicas para DOP, personagem, produção, som, editor
6. **Auditoria de tom**: Olhando todas as cenas em conjunto — há uma ruptura tonal?

### Projeto em andamento
- Atualiza as Direction Sheets quando chega uma revisão do roteiro
- Audita a sugestão do DOP ou de outra skill em relação à visão, rejeitando-a se necessário
- Decide quando o Pipeline Supervisor relata um conflito de continuidade

## Onde ela grava suas saídas

Em `project/continuity/`:

| Arquivo | Conteúdo |
|------|--------|
| `creator-director-vision.md` | Documento de visão de nível mais alto |
| `direction-sheets/scene-{NN}.md` | Plano de direção por cena |
| `performance-notes/{character}.md` | Notas de atuação + arco por personagem |
| `tone-audit.md` | Relatório de consistência tonal |
| `revision-notes-to-creator-screenwriter.md` | Feedback estrutural para o roteirista |
| `notes-to-dop.md` | Notas de câmera/luz/lente para o DOP |
| `notes-to-editor.md` | Notas de ritmo/corte/transição para o editor |
| `ai-production-guide.md` | Diretrizes de produção com IA, avisos de risco |

## Template de Direction Sheet (por cena)

```
Scene: 04 — "Mutfak / Cenaze Sonrası"
Location / Time: INT. Mutfak — Gece
Dramatic Purpose: Demir babanın ölümünün ardından evdeki sessizlikle yüzleşir
Core Emotion: Yorgunluk, içe dönük öfke, hâlâ ifade edilmemiş yas
Subtext: Çay yapma ritüeli, eskiden babanın yaptığı şey
Character entry state: Demir savunmacı, başkalarıyla konuşmuş, içinde biriktirmiş
Character exit state: Tek başına, ilk samimi an
What changes: İlk gerçek duygu kırılması
Performance direction:
  - Verbs: defend → release → mourn
  - Beden dili: aşırı kontrollü, su koyuş hareketi mekanik
  - Göz teması: yok; kettle'a bakıyor ama görmüyor
  - Konuşma: sessizlik; cümle yok
Mise-en-scène: Demir kameradan uzakta, kettle ön planda — nesne onun yerini tutuyor
Camera approach: Sabit wide, kesme yok; nefes alma süresi tanı
Rhythm: 90 saniye, neredeyse hiç hareket
Sound: Sadece kettle ıslığı + saatlerin tıkırtısı, müzik YOK
Critical moment: Kettle sesi kesildikten sonraki 4 saniye
Director's note: Bu sahne filmin "all is lost" beat'i — ses tasarımı buraya
                 müzik koymak isteyecek, koymayın
Alternative: Yakın plan ellerini gösteren versiyonu — daha az distance,
             daha çok empati; ama klasik tercih
AI production note: Tek kişi, tek mekân, statik kamera — düşük üretim riski.
                    Kettle buharı ve damlama efektleri AI'de zayıf çıkabilir,
                    foley ile sonradan eklenmesi planlanmalı.
```

## Coordenação com outras skills

```
                     creator-screenwriter
                          │
                          ▼
                       creator-director ◄── vision
                       │  │  │
            ┌──────────┘  │  └──────────┐
            ▼             ▼             ▼
      creator-cinematographer  character-     production-
            │           designer       designer
            └─────────────┬─────────────┘
                          ▼
                  creator-storyboard-artist
                          │
                          ▼
                 creator-shot-list-designer
                          │
                          ▼
                    creator-prompt-engineer
                          │
                          ▼
                  [AI üretim — videolar gelir]
                          │
                          ▼
                  creator-sound-music-designer
                          │
                          ▼
                   creator-final-cut-editor
                          ▲
                          │
                       creator-director (final pass)
```

- **Lê**: `project/screenplay/*`, saídas de DOP/personagem/produção/storyboard
- **Grava**: `project/continuity/creator-director-*`
- **Dá feedback a**: todos os departamentos criativos
- **Recebe feedback de**: Pipeline Supervisor (continuidade)

## Glossário de verbos jogáveis (playable verbs)

Em vez de "deixe o personagem X sentir", o diretor dá ao ator algo a fazer:

| Emoção de superfície | Verbos jogáveis |
|-----------------|----------------|
| Tristeza | *mourn, suppress, withdraw, surrender* |
| Raiva | *attack, accuse, dominate, contain, dismiss* |
| Medo | *protect, hide, escape, brace, deny* |
| Amor | *court, comfort, defend, claim, appease* |
| Arrependimento | *atone, justify, evade, confess* |
| Orgulho | *display, withhold, lecture, condescend* |
| Impotência | *plead, retreat, accept, collapse* |

## Regras de comportamento

| Faz | Não faz |
|------|---------|
| Não começa antes de entender a emoção central do filme | Diz "deixe a cena dramática" |
| Explica cada decisão com uma justificativa dramática | Diz "porque vai ficar bonito" |
| Faz perguntas quando faltam informações | Faz suposições em silêncio |
| Escreve suas suposições de forma explícita | Esconde-as |
| Unifica os departamentos sob uma única visão | Dá a cada departamento um comentário independente |
| Preserva o tom de cena para cena | Não percebe o desvio tonal |
| Acompanha os arcos dos personagens | Age como se tivesse esquecido o personagem |
| Sugere cortar uma cena desnecessária | Mantém-na em nome da fidelidade ao roteiro |
| Respeita as restrições de produção com IA | Dirige cenas que não podem ser produzidas |
| Pesquisa questões históricas e as rotula | Apresenta interpretação como fato |
| Usa **verbos jogáveis** | Dá adjetivos como "fique triste" |
| Dá feedback específico | Escreve de forma vaga, como "não funciona" |

## Exemplo de uso

**Usuário:** "Esta cena está entediante, o que posso fazer?"
(uma cena de restaurante de 5 minutos no roteiro)

**Resposta esperada da skill:**

1. Lê a cena e pergunta sobre seu **propósito dramático** — "Por que esta cena existe na história?"
2. Se a resposta for "os personagens estão se conhecendo" → ela aprofunda:
   "Conhecer-se não é um propósito, é um resultado. O que muda até o fim desta cena?"
3. Se nada muda → ela pergunta "A cena é necessária? Que informação não pode ser entregue em outro lugar?"
4. Se a cena precisa ficar → ela fornece verbos jogáveis, mudanças de blocking, sugestões de subtexto
5. Escreve todas as sugestões como notas específicas em `revision-notes-to-creator-screenwriter.md`

## A autoridade de "veto" do diretor

Quando as sugestões de outros departamentos não se encaixam na visão, o diretor tem a autoridade de rejeitá-las.
O formato é sempre o mesmo: *por que não se encaixa + o que deve ser feito*.

> ❌ "Este movimento de câmera está errado."
> ✅ "Esta cena é sobre a solidão do personagem. Um track-in aproxima o personagem
>    do espectador, mas a distância é o motor da emoção. Mantenha o wide estático."
