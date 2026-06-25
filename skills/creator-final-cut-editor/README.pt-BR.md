# Editor de Corte Final — `creator-final-cut-editor`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · **Português (BR)** · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

A skill que transforma os resultados da produção em IA em um **filme finalizado**. O fim
da pré-produção / o início da pós-produção. Depois que o material foi produzido,
ela gerencia o fluxo rough cut → fine cut → final cut → entrega; faz a triagem dos erros
de geração da IA, audita a continuidade, verifica a integração de áudio/música e
produz masters prontos para entrega.

**Diferença em relação ao shot-list-designer**: o shot list projeta a intenção editorial
ANTES da filmagem; o creator-final-cut-editor EXECUTA o corte sobre o material
de fato.

## Filosofia

O corte final **não é um sequenciamento técnico** — é a construção da
totalidade cinematográfica. Esta skill:

- **Uma justificativa dramática para cada corte** — "fica bom" não basta
- **Ritmo em múltiplas escalas**: dentro de um plano, dentro de uma cena, ao longo de todo o filme
- **Triagem de erros da IA**: qual erro quebra o corte, qual pode ser escondido, qual pode permanecer
- **Design da experiência do público**: o que o espectador sente, aprende e leva consigo
- **Disciplina de entrega**: YouTube ≠ festival ≠ Instagram ≠ arquivo
- **Versionamento**: gerencia separadamente cortes rough/fine/final + festival/social/trailer

## O que ela faz

| Resultado | Conteúdo |
|-------|---------|
| **Avaliação de material** | Por plano: utilizável / revisar / regerar / cortar |
| **Plano de rough cut** | Primeiro sequenciamento bruto, lista de material faltante |
| **Plano de fine cut** | Pontos de corte, durações dos planos, silêncio |
| **Plano de final cut** | Prontidão final + checklist de entrega |
| **Verificação final por cena** | Auditoria detalhada cena a cena |
| **Relatório do filme inteiro** | Relatório de corte final para o filme inteiro |
| **Relatório de erros da IA** | Erros de geração + classificação de severidade |
| **Auditoria de integração de áudio** | Feedback para o sound designer |
| **Notas de color grade** | Diretrizes de correção de cor |
| **EDL** | Edit Decision List legível por NLE |
| **Manifesto de versões** | Versões de corte festival/social/trailer |
| **Especificações de entrega** | Configurações de exportação específicas por plataforma |
| **Plano de trailer** | Plano de corte de teaser/trailer |

## Quando ela entra em ação

- Os planos de vídeo em IA foram produzidos, a edição está começando
- É necessário o planejamento de rough/fine/final cut
- É solicitada uma auditoria de erros da IA
- Serão produzidos múltiplos cortes (festival, social, trailer)
- Preparação da exportação para entrega
- Quando o `creator-pipeline-supervisor` delega a fase de pós-produção

## Fluxo típico

1. **Avaliação de material** — cada plano é categorizado (✅🟡🟠🔴)
2. **Rough cut v01** — ordem da história, sequência dramática básica
3. **Fine cut v01** — pontos de corte, ritmo, silêncio
4. **Auditoria de integração de som** — feedback para o creator-sound-music-designer
5. **Relatório de erros da IA** — classificação crítico/médio/menor
6. **Notas de color grade** — se necessário
7. **Verificação de legendas / títulos / gráficos**
8. **Final cut v01** — checklist de prontidão
9. **Exportação para entrega** — versão específica por plataforma

## Matriz de triagem de erros da IA

| Severidade | Definição | Ação |
|----------|------------|--------|
| 🔴 Crítico | Não pode entrar no corte final | Regerar (sinalizar ao creator-prompt-engineer) |
| 🟡 Médio | Escondido via trim/crop/cor/som | Solução editorial |
| ✅ Menor | Não incomoda o espectador | Pode permanecer |

Verificados: distorção de rosto, erros de mão/dedos, lip-sync, mudanças de figurino,
perda de acessórios, deriva de locação, inconsistência na direção da luz, movimento
artificial de câmera, flicker, warping, morphing, objetos derretendo, colapso de
fundo, anacronismo, aparência plástica.

## Formato de verificação final por cena

```
Scene 04 — "Mutfak / Cenaze Sonrası"
Target duration: 90s
Current duration: 102s
Dramatic purpose: Demir'in iç dönüşümünün ilk anı
Core emotion: Bastırılmış yas

Shots used: 04.01, 04.02, 04.03, 04.05, 04.06
Shots cut: 04.04 (gereksiz reaction, ritim düşürüyor)
Shots shortened: 04.05 (8s → 5s — wide hold gereksiz uzun)
Shots lengthened: 04.02 (4s → 6s — kettle hold dramatik nefes)
Cut points:
  - 04.01 → 04.02: sound bridge (kettle ıslığı önce)
  - 04.02 → 04.03: hard cut (kettle sessizleşmesi → Demir close)
Transitions:
  - Scene → next: dissolve (sabah ışığına geçiş)
Reaction shot usage: 04.03 (Demir close) — yas kırılma anı
Silence usage: 04.02'de 4 saniye saatin tıkırtısı dışında hiç ses yok
Music usage: YOK — yönetmen direktifi
Ambience / foley notes: kettle, saat tıkırtı, dış rüzgâr çok kısık
Visual continuity notes: ✅ kostüm, ışık yönü, kettle leke pattern hepsi tutarlı
AI error audit:
  - 04.02 kettle buharı warping (🟡 orta) — sound design ile maskelenecek
  - 04.03 Demir göz sol kenar microflicker (🟡 orta) — color grade düzeltir
Color / light notes: 04.05'in white balance hafif sıcak — match için -100K
Subtitle / graphic notes: YOK
Final decision: 🟡 küçük revizyon (1 shot kes, 1 kısalt, 1 uzat)
Revision rationale: ritim 12s düşürülerek dramatik yoğunluk artar
```

## Onde ela grava seus resultados

Em `project/cuts/`:

| Arquivo | Conteúdo |
|-------|---------|
| `material-evaluation.md` | Categoria de cada plano |
| `rough-cut/v{NN}.md` | Plano de rough cut |
| `fine-cut/v{NN}.md` | Plano de fine cut |
| `final-cut/v{NN}.md` | Plano de final cut + prontidão |
| `scene-{NN}/final-check.md` | Detalhe cena a cena |
| `final-cut-report.md` | Auditoria do filme inteiro |
| `ai-error-report.md` | Relatório de erros da IA |
| `audio-integration-report.md` | Auditoria de integração de áudio |
| `color-grade-notes.md` | Correção de cor |
| `subtitle-titles-graphics.md` | Legendas/títulos |
| `transitions.md` | Decisões de transição |
| `edit-decision-list.md` | EDL |
| `versions/{cut-name}.md` | Manifesto de versões |
| `delivery/{platform}.md` | Especificações de exportação por plataforma |
| `trailer-plan.md` | Plano de trailer/teaser |

## Gestão de versões

| Versão | Duração | Objetivo |
|----------|----------|------|
| Rough Cut v01 | ~115% do alvo | Primeiro teste de fluxo da história |
| Rough Cut v02 | ~108% | Integração das peças faltantes |
| Fine Cut | ~102% | Travar ritmo e emoção |
| Director's Cut | 100% do alvo | Aprovação total do diretor |
| Final Cut | 100% | Pronto para entrega |
| Festival Cut | 100% | Formato de festival |
| YouTube Cut | 100% ou encurtado | Algoritmo do YouTube |
| Trailer Cut | 30s–2 min | Marketing |
| Social Cut | 9:16 curto | Reels, TikTok |

Para cada versão: nome, duração, alterações, cenas removidas/adicionadas, mudanças
de áudio, justificativa da revisão, status de aprovação.

## Exemplo de especificações de entrega

| Plataforma | Proporção | Resolução | FPS | Áudio |
|----------|--------|------------|-----|-------|
| Master YouTube 16:9 | 16:9 | 3840×2160 (4K) ou 1920×1080 | 24/25 | AAC 320kbps estéreo |
| Master de festival | 2.39:1 ou 16:9 | 4K | 24 | WAV 48kHz 24-bit estéreo + 5.1 |
| Instagram Reels | 9:16 | 1080×1920 | 30 | AAC estéreo |
| TikTok | 9:16 | 1080×1920 | 30 | AAC estéreo |
| Web comprimido | 16:9 | 1920×1080 | 24/25 | AAC 192kbps |
| Master de arquivo | original | máxima | original | WAV master |

## Lógica do corte de trailer

Um trailer **não é uma miniatura do filme** — ele tem sua própria lógica editorial:

- Os 6–10 visuais mais fortes
- Lista de exclusão de spoilers
- Gancho → contexto → ameaça/conflito → teaser do clímax → escuridão → tagline
- Construção musical (diferente do filme, mais direta)
- Ritmo de cortes rápidos (diferente do filme)
- Apresentações de personagens comprimidas
- Uma imagem de impacto final — **fora** do contexto do filme
- Versão curta 9:16 para redes sociais

## Coordenação com outras skills

- **Lê**: todos os resultados criativos a montante + o `final-editor-notes.md` do shot-list
- **Grava**: `project/cuts/*`
- **Dá feedback a**:
  - **creator-sound-music-designer**: solicitações de correção de áudio
  - **creator-prompt-engineer**: solicitações de regeração
  - **creator-pipeline-supervisor**: escalonamento de continuidade
- **Obtém aprovação de**: Diretor (aprovação final), Pipeline Supervisor

## Regras de comportamento

| Faz | Não faz |
|-------|---------|
| Uma justificativa dramática para cada corte | Fazer mero sequenciamento técnico |
| Sinaliza claramente cenas/planos desnecessários | Mantê-los por apego |
| Avalia os erros da IA pela experiência do espectador | Perfeccionismo abstrato/técnico |
| Considera diálogo + música + ambiência + silêncio em conjunto | Auditar isoladamente |
| Fiel à visão do diretor | Conflitar com o ego editorial |
| Disciplinado quanto à duração-alvo | Estourar o limite |
| Pergunta ao usuário antes de uma grande mudança | Cortar em silêncio |
| Acompanha múltiplas versões | Misturá-las em um único arquivo |
| Entrega adequada a cada plataforma | Entregar um único master |
| Não dirá "concluído" sem um checklist de prontidão para entrega | Declarar concluído cedo demais |
