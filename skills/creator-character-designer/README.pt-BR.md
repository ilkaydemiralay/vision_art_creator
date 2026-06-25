# Designer de Personagens — `creator-character-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Uma skill que eleva o personagem para além da tríade **nome + idade + aparência**
e o projeta como um **ser coerente**. Produz função dramática, psicologia,
biografia, linguagem corporal, figurino, props, perfil de elenco e uma
**biblioteca de expressões codificada com FACS Action Units**. Estabelece as
âncoras de "Character DNA" que preservam a consistência do personagem ao longo da
produção de filmes com IA de formato longo.

## Filosofia

Um personagem não é gerado ao acaso — ele deriva das necessidades do roteiro, da
visão do diretor e do mundo visual do DOP. Esta skill:

- **Cada personagem é a resposta a uma pergunta dramática** — caso contrário, sugere cortar o personagem
- Estabelece obrigatoriamente o quarteto **Want / Need / Fear / Wound** para cada personagem principal
- **FACS Action Units**: em vez de dizer "triste", diz AU1+AU4+AU15 —
  modelos de IA e animadores interpretam o código anatômico de forma mais consistente
- **Character DNA**: define traços-âncora travados para a consistência da IA
- **Visual distinction audit**: quando há vários personagens, audita as distinções de silhueta, cor e energia

## Para que serve

| Saída | Conteúdo |
|-------|----------|
| **Character sheet** | Ficha do personagem — psicologia, figurino, prop, FACS, AI prompt |
| **Costume bible** | Variações de figurino e continuidade em todo o filme |
| **Props list** | Os objetos pessoais do personagem e seus usos dramáticos |
| **FACS expression library** | 3–5 expressões características por personagem, codificadas com AU |
| **Casting brief** | O perfil buscado em um ator (não sugere nomes, define traços) |
| **AI prompts** | Base prompt + variações de cena para uma referência consistente de personagem |
| **Arc tracker** | Transformação do personagem coordenada com o arc tracking do diretor |
| **Continuity notes** | Continuidade de figurino/props cena a cena |

## Quando entra em ação

- O roteiro está pronto e os personagens precisam ser desenvolvidos
- "Prepare uma character sheet", "projete um figurino", "redija um perfil de elenco"
- É necessária uma referência consistente de personagem para filme com IA
- Quando o diretor ou o `creator-pipeline-supervisor` delega a etapa de personagens
- Quando a distinção visual dos personagens existentes é questionada

## Uso do FACS — por que e como

O **Facial Action Coding System (Ekman & Friesen, 1978)** é a codificação
anatômica dos músculos faciais. Uma Action Unit (AU) = um movimento muscular
específico.

### Por que esta skill o utiliza?

- **Geradores de IA** interpretam de forma inconsistente entradas abstratas como "happy face";
  "AU6 + AU12 (Duchenne smile)" produz um resultado mais confiável
- **Equipes de animação/VFX** compartilham um único conjunto de referência por meio de códigos AU
- **A expressão característica do personagem** pode ser arquivada — por exemplo, "Demir
  carrega seu luto reprimido com AU4 + AU17 (sobrancelha franzida, queixo erguido, sem AU15)"

### Combinações comuns de AU

| Expressão | AU |
|-----------|-----|
| Duchenne smile (felicidade genuína) | AU6 + AU12 |
| Polite smile (falsa/social) | AU12 sozinha |
| Tristeza | AU1 + AU4 + AU15 |
| Raiva | AU4 + AU5 + AU7 + AU23 |
| Medo | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 |
| Nojo | AU9 + AU15 + AU16 |
| Surpresa | AU1 + AU2 + AU5B + AU26 |
| Desprezo (assimétrico) | AU12 (unilateral) + AU14 |
| Luto reprimido | AU4 + AU17 (sem AU15) |
| Calma tensa | AU7 + AU23 + AU24 |

## Modelo de character sheet (resumo)

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

## Onde escreve suas saídas

Em `project/characters/{character-slug}/`:

| Arquivo | Conteúdo |
|---------|----------|
| `character-sheet.md` | A ficha canônica do personagem |
| `costume-bible.md` | Todas as variações de figurino + continuidade |
| `props.md` | Os objetos do personagem, uso dramático |
| `facs-expressions.md` | Biblioteca de expressões características, codificada com AU |
| `casting-brief.md` | Perfil do ator / base para um AI face prompt |
| `ai-prompts.md` | Base prompt + variação cena a cena |
| `arc-tracker.md` | Sincronização com o arc tracking do diretor |
| `continuity-notes.md` | Continuidade de figurino/props cena a cena |

Há também um `cast-list.md` no diretório superior — uma lista que resume todos os personagens.

## Visual distinction audit

Quando há mais de um personagem, a skill executa estas verificações:

- Distinção de silhueta (altura, postura, forma do figurino)
- Distinção de mundo cromático (ou contraste deliberado)
- Distinção de registro de energia
- Distinção de padrão de fala
- Distinção de presença em tela (tipo foreground / background)

Se dois personagens "se confundem", ela reporta e sugere uma revisão.

## Consistência de IA (Character DNA)

Para gerar o mesmo personagem em 50 cenas com o mesmo rosto/figurino:

1. **Base prompt** — traços-chave (formato do rosto, cabelo, marca distintiva) fixos
2. **Anchor descriptors** — 2–3 deles se repetem em cada prompt de cena
3. **Expressão via FACS** — codificada com AU, não com adjetivos
4. **Produção precoce da character sheet** — imagens de referência front/side/back/close
5. **Referência no prompt de cena**: "consistent with `characters/demir/sheet.png`"

## Coordenação com outras skills

- **Lê**:
  - `project/screenplay/character-brief.md`
  - `project/continuity/creator-director-vision.md`
  - `project/continuity/performance-notes/*`
  - `project/production-design/cinematography/visual-language.md`
  - `project/production-design/world-bible.md`
- **Escreve**: `project/characters/*`
- **Delega para**: Engenheiro de prompt, storyboard, DOP (coordenação de paleta)
- **Recebe feedback de**: Diretor, Pipeline Supervisor

## Abordagem de design de figurino

O figurino narra o personagem — não é apenas "o que ele veste":

- Peça principal + sua função
- Tecido: pesado, macio, rígido, fibroso
- Cor: harmonia/contraste com a paleta
- Desgaste / novidade / dano / sinais de reparo
- Precisão de época
- Relação com o estado de espírito do personagem
- Efeito sobre a mobilidade
- Interação com a luz (fosco, brilhante, transparente, que retém poeira)

Para cada cena principal, uma nota de continuidade de figurino: ele muda dentro da
cena, muda entre cenas, por quê?

## Abordagem dos props

Props são ferramentas narrativas — não decorativas:

- Nome + função
- Relação com o personagem
- Aparência, material, cor, condição
- Significado para o personagem (lembrança, identidade, relação)
- Uso dramático (prenúncio, payoff, revelação)
- Como a câmera o vê (close, detalhe, de passagem)
- Continuidade (onde está em cada cena)

A propriedade personagem-prop / locação-prop é esclarecida e coordenada com o
**creator-production-designer**.

## Regras de comportamento

| Faz | Não faz |
|-----|---------|
| Gera um personagem com uma justificativa dramática | Diz "precisamos de mais um personagem" |
| Vincula cada escolha visual ao arc / função / tema | Faz escolhas estéticas isoladas |
| Faz perguntas quando falta informação | Inventa em silêncio |
| Pesquisa o detalhe cultural | Apresenta um palpite como fato |
| Define expressões com códigos FACS AU | Usa adjetivos como "triste" |
| Executa um visual distinction audit | Deixa dois personagens se confundirem |
| Incorpora continuity anchors nos AI prompts | Descreve do zero em cada cena |
| Esclarece a propriedade personagem-prop | Sobrepõe-se ao designer de produção |
| Entrega arquivos estruturados e downstream-readable | Despeja um único bloco de texto |
