# Diretor de Arte — `creator-production-designer`

[English](README.md) · [中文](README.zh.md) · [Español](README.es.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [Português (BR)](README.pt-BR.md) · [Türkçe](README.tr.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

O skill que constrói o **mundo** do filme: locações, cenários, props, atmosfera
de época, linguagem de cor e de materiais. Em vez de dizer "uma vila bonita",
ele projeta no nível da textura da parede, do material do piso, da densidade do
mobiliário, das superfícies que afetam a luz e das marcas de desgaste. Ele
estabelece as master references que mantêm a **consistência de locação** ao
longo de uma produção de cinema com IA de formato longo.

## Filosofia

Um espaço não é um pano de fundo — é um **instrumento narrativo**. Este skill:

- **World bible** primeiro — depois per-location, depois per-scene (top-down)
- **Master reference**: um bloco de prompt de IA travado para cada locação
  principal — para conseguir produzir a mesma casa mesmo 50 cenas depois
- **Design do vivido**: rachaduras, manchas, desbotamento pelo sol, desgaste,
  marcas de reparo
- **Class-coded design**: cada material/cor fala da classe social
- **Coordinated palette**: pensada junto com a iluminação do DOP e o figurino do
  personagem
- **Period research**: pesquisa com fontes quando se exige precisão
  histórica/cultural

## Para que serve

| Saída | Conteúdo |
|-------|--------|
| **World bible** | As regras gerais do mundo do filme (época, classe, arquitetura, materiais) |
| **Color & texture bible** | Paleta de cores, linguagem de materiais, padrões de desgaste |
| **Location dossier** | Um documento abrangente para cada locação principal (travado + variações) |
| **Master reference (AI)** | O bloco de prompt de IA fixo da identidade de uma locação |
| **Props inventory** | Objetos de cena, com suas funções dramáticas |
| **Per-scene plan** | Direção de arte cena a cena (dressing, props, fontes de luz) |
| **Continuity log** | Verificação de consistência de locação entre cenas |
| **Period research** | Pesquisa histórica/cultural com fontes |
| **Notes to DOP / creator-director** | Comunicação bidirecional |

## Quando entra em ação

- Roteiro em mãos, design de mundo / locação / cenário necessário
- "Como este espaço deve parecer", "set dressing", "lista de props"
- Referência de locação consistente para produção com IA
- Pesquisa de época (histórica, cultural, regional)
- Quando o `creator-pipeline-supervisor` delega a fase de direção de arte

## Fluxo típico

1. **Briefing** + leitura de `creator-director-vision.md` + DOP visual-language
2. **Rodada de perguntas**: época, geografia, tom, classe, ferramentas de IA
3. **World bible**: as regras gerais do mundo do filme
4. **Color & texture bible**: linguagem de materiais e de cor
5. **Major locations**: um dossier para cada locação principal
6. **Master references**: blocos de prompt travados para a consistência com IA
7. **Per-scene sheets**: set dressing cena a cena + notas de props
8. **Continuity audit**: a mesma locação é consistente em cenas diferentes?

## Onde escreve suas saídas

Sob `project/production-design/` (excluindo cinematography — isso é do DOP):

| Arquivo | Conteúdo |
|-------|--------|
| `world-bible.md` | As regras do mundo do filme |
| `color-texture-bible.md` | Linguagem de cor + materiais |
| `locations/{slug}/location-doc.md` | Dossier per-location |
| `locations/{slug}/master-reference.md` | Base prompt de IA travado |
| `props/{slug}.md` ou `props-list.md` | Inventário de props |
| `scenes/scene-{NN}.md` | Plano de direção de arte cena a cena |
| `continuity-notes.md` | Log de verificação de consistência de locação |
| `period-research.md` | Pesquisa de época com fontes |
| `notes-to-creator-director.md` | Perguntas/sugestões ao diretor |
| `notes-to-creator-cinematographer.md` | Coordenação de superfície/profundidade/luz com o DOP |

## Modelo de location dossier (resumo)

```
Location: Demir'in dedesinin köy evi mutfağı
Function in story: Demir'in babayı ilk kez bir mekânda hisseder
Period: 1980'ler doğu Anadolu kırsalı
Architectural style: tek katlı kerpiç, ahşap kiriş tavan, kireçli duvar
Color palette: kireç beyazı, bakır, yanmış toprak, kömür siyahı
Texture: kireç ufalı duvar, ahşap çatlamış, bakır pas yeşili, demir tencere is izi
Walls: kireç boyalı, alt 1m'de toz/duman izi
Floor: ham ahşap, eskimiş
Doors / windows: ahşap kanat pencere, dışarısı çıplak ağaç
Furniture: ahşap masa (4 kişilik), iki sandalye, bakır kapaklı dolap
Decorative: duvarda tek bir solmuş aile fotoğrafı
Daily-use items: bakır kettle, demir tencere, tahta kaşıklar, kil testi
Lived-in level: yıllarca yaşanmış, son 2 hafta dokunulmamış (toz tabakası)
Light-affecting surfaces: kireç (matt, ışık yutar), bakır (kontur), pencere (tek kaynak)
Camera framing points: pencere ışığı kettle'ı tarayan açı; masa ekseni
Continuity anchors: pencere konumu, masa, dolap, fotoğraf — KİLİTLİ
AI master reference prompt: "...same kitchen across all scenes..."
Variations: gündüz, gece, fırtınalı, yeni temizlenmiş (final sahnede)
```

## Master reference (para a consistência com IA)

Escreve-se um **bloco de base prompt travado** para cada locação principal:

```
{kitchen-anatolian-1980s}: small one-room kitchen in an Eastern Anatolian
village house, single small window on the east wall with bare tree branches
visible outside, lime-washed walls with soot stain along the lower meter, raw
wooden floorboards, one wooden table center, two chairs, a copper-lidded
cabinet on the north wall, copper kettle on a small iron stove, a single faded
family photograph framed on the west wall — soft natural side light, dust in
the air, period-accurate 1980s Eastern Anatolia, no modern objects, --ar 2.39:1
```

Esse bloco é repetido literalmente em todos os prompts de cena, com a variação
específica da cena adicionada por cima.

## Coordenação com outros skills

- **Cinematographer**:
  - Como as superfícies se relacionam com a luz (matte, glossy, transparent)
  - Primeiro plano/plano médio/fundo para escalonar a profundidade
  - A paleta de cores funciona com a iluminação planejada?
  - Espelhos, vidro e superfícies brilhantes são um problema para a câmera?
- **Director**:
  - A locação serve ao tema central?
  - O tom do mundo combina com a visão?
  - Há locações que devem ser "signature/iconic"?
- **Character-designer**:
  - O figurino é lido corretamente dentro da paleta da locação?
  - Os objetos pessoais encontram lugar dentro do dressing?
  - A classe social é consistente tanto pelo figurino quanto pelo espaço?
- **Storyboard / shot-list**: notas dos pontos de enquadramento
- **Prompt-engineer**: hand-off da master reference + prompts de variação

## Reads / writes

- **Reads**: roteiro, visão do diretor, DOP visual-language, paletas de personagem
- **Writes**: `project/production-design/*` (excluindo cinematography)

## Soluções voltadas à produção com IA

- Produzir muitas cenas com poucas locações
- Mostrar a mesma locação de forma diferente variando ângulo/luz/clima
- Controlar a densidade do dressing — para que a IA não fique sobrecarregada
- Simplificar espaços complexos com os quais a IA teria dificuldade
- Consistência por meio de imagens de referência fixas
- Produção antecipada da "master reference"
- Reutilizar objetos do dressing (coerência do mundo)
- Reduzir o detalhe desnecessário para destacar o objeto dramático

## Regras de comportamento

| Faz | Não faz |
|-------|--------|
| Projeta o espaço como instrumento narrativo | Diz "um quarto bonito" |
| Liga cada decisão de dressing à época/personagem/tema | Faz escolhas estéticas isoladas |
| Pergunta quando falta informação | Inventa em silêncio |
| Pesquisa os detalhes culturais e os rotula | Apresenta interpretação como fato |
| Garante a consistência com IA via master reference | Descreve do zero em cada cena |
| Coordena a paleta com o DOP + os personagens | Decide isoladamente |
| Esclarece a posse prop-de-personagem / prop-de-locação | Conflita com o designer de personagens |
| Entrega um arquivo estruturado e downstream-readable | Despeja um único bloco de texto |
| Oferece alternativas para locações de risco para a IA | Força um detalhe que não pode ser produzido |
