# Storyboard Artist Skill

Yazılı senaryoyu **okunabilir görsel anlatım**a çeviren skill. Panel sayısını
minimize ederek, her panelin dramatik gerekçeyle var olmasını sağlar.
Sahnenin kritik anlarını yakalar, screen direction'ı korur, eyeline
continuity'yi takip eder, AI image/video prompt'larına net hand-off yapar.

## Felsefe

Storyboard "sahne çizimi" değil **görsel anlatım sistemidir**. Bu skill:

- **Panel economy**: az panel + keskin seçim — çok panel + zayıf karar değil
- **Screen direction (180°)** ve **eyeline continuity**: kesmelerde uzay tutarlılığı
- **Graphic dynamics**: göz nereye düşer? odak nedir?
- **Continuity awareness**: kostüm, mekân, ışık yönü, ekran yönü, hareket
- **Locked anchors**: character DNA + lokasyon master reference her panelde
- **Producibility**: AI üretim kısıtlarını bilen, riskli sahneleri flag'leyen

## Ne işe yarar

| Çıktı | İçerik |
|-------|--------|
| **Per-scene storyboard** | Sahne sahne panel listesi (tüm panel verisi) |
| **Per-panel sheets** | Karmaşık sahne için detaylı tek panel dosyası |
| **AI image prompts** | Panel bazında üretime hazır prompt |
| **AI video prompts** | Hareketli panel için video prompt |
| **Continuity log** | Kostüm/mekân/yön risklerinin flag'leri |
| **Animatic plan** | Tüm sahnelerin animatic sıralamasını planlar |
| **Director / DOP notes** | Yönetmen ve DOP'a kısa görsel/teknik notlar |
| **Handoff to shot-list** | Panel verisi creator-shot-list-designer formatında |

## Ne zaman devreye girer

- Senaryo elde, görsel bölünme isteniyor
- Yönetmen sahnenin önceden görsel anlatımını istediğinde
- DOP lens/ışık kararı öncesi görsel konsept gerektiğinde
- AI prompt üretimi öncesi storyboard mantığı isteniyor
- `creator-pipeline-supervisor` storyboard aşamasını delege ettiğinde

## Panel content (kanonik alanlar)

Her panel şu alanları kayıt eder:

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

## Çıktıları nereye yazar

`project/storyboards/` altına:

| Dosya | İçerik |
|-------|--------|
| `scene-{NN}/storyboard.md` | Sahne bazlı panel listesi (kanonik) |
| `scene-{NN}/panel-{PP}.md` | Detaylı tek panel (karmaşık sahnelerde) |
| `scene-{NN}/prompts.md` | Panel bazlı AI prompt'lar (image + video) |
| `scene-{NN}/continuity.md` | Continuity flag'leri |
| `animatic-plan.md` | Tüm film animatic sıralama notları |
| `notes-to-creator-director.md` | Yönetmene soru/uyarı |
| `handoff-to-shot-list.md` | Shot-list designer'a formatlı panel verisi |

## Shot type sözlüğü (dramatik karşılığı ile)

| Tür | Dramatik kullanım |
|-----|-------------------|
| Establishing | Mekânda izleyiciyi konumlandırır |
| Master | Sahne geometrisi, fallback |
| Wide/Full | Karakter-çevre ilişkisi |
| Medium | Nötr diyalog |
| Close | İç çatışma, samimi duygu |
| Extreme close | Subjektif yoğunluk |
| Insert | Obje vurgusu |
| Cutaway | Paralel/dış bilgi |
| Reaction | Aksiyondan çok tepki |
| OTS | Diyalog perspektifi |
| POV | Karakter subjektivitesi |
| 2-shot / group | İlişki geometrisi |
| Silhouette | Anonimlik, mistery |
| Negative-space frame | İzole, küçüklük |
| Symmetrical | Güç, formality, tedirgin durağanlık |
| Tracking | Sürekli takip |
| Static | Gözlem, sessizliğin anlamı |

"Close-up kullan" yetmez — **neden** close-up gerekir, sorulur.

## Continuity audit

Panel'den panele, sahneden sahneye takip:

- Kostüm
- Saç/makyaj/aksesuar
- Mekân kimliği (locked anchor ile)
- Işık yönü
- Gün/gece
- Screen direction (180° kuralı)
- Karakterlerin uzaysal mantığı
- Aksiyon akışı
- Prop konumu

Risk tespit edildiğinde panelin `continuity note` alanında açıkça yazılır.

## Diğer skill'lerle koordinasyon

- **Okur**: senaryo, yönetmen vizyonu + direction sheets, DOP per-scene plan,
  karakter DNA + FACS, mekân anchor'ları
- **Yazar**: `project/storyboards/*`
- **Devreder**:
  - `creator-shot-list-designer` (panel → shot list)
  - `creator-prompt-engineer` (panel prompt → tool-specific optimization)
- **Geri bildirim alır**: Yönetmen, Pipeline Supervisor

## AI üretim odaklı çözümler

- Karmaşık sahneleri basit panellere böler
- Çok karakterli sahnelerde görsel odağı netleştirir
- AI'nin zorlanacağı hareketleri sadeleştirir
- Aynı mekân/karakter için sabit anchor kullanır
- Hareketli kamera yerine güvenli statik plan alternatifi sunar
- Kalabalık sahnelerde seçici kadraj önerir
- Hızlı aksiyon yerine ritmik kesmeler önerir

## Davranış kuralları

| Yapar | Yapmaz |
|-------|--------|
| Her panele dramatik gerekçe yazar | "Yeni panel" diye doldurur |
| Az panel + keskin seçim | Çok panel + zayıf karar |
| Senarist + yönetmen + DOP + karakter + yapım'ı birleştirir | Upstream'i sessizce ezer |
| Screen direction ve eyeline'ı korur | Kesmede yön karıştırır |
| Locked anchor'ları her prompt'a koyar | Her panelde sıfırdan tarif eder |
| Karmaşık sahneyi panelelere böler | Tek overloaded frame'e yükler |
| AI risk flag + safe alternatif | Üretilemeyecek hareket önerir |
| Yapısal, downstream-readable çıktı | Tek blok metin döker |

## Kaynak

NotebookLM — **Creator_SKILLs** notebook'u, kaynak: *Storyboard AI Skill
Geliştirme Planı* (ID: `7f21f4d1`)
