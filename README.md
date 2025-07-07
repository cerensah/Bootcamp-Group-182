## Takım İsmi:
Bootcamp Group 182

## Takım Üyeleri:
Ayşe Ceren Şahin

## Ürün Açıklaması:
Öğrenciler tarafından sorulan matematik problemlerini çözüp nasıl çözdüğünü özetleyen bir chatbot

## Ürün Özellikleri:

### Solver'ın çözebildiği konular: 
1. Basit dört işlem
2. Geometrik şekillerin alan ve çevre hesaplaması
3. Basit tek bilinmeyenli denklemler
4. Basit problemler

### Ürün Tech Stack:
- Tokenizer ve Model Train için: Google FLAN-T5 Pre-trained Model
- Soru/cevap çiftlerini tutmak için: Excel
- (Sprint 2&3'te) Web tabanlı uygulama geliştirme için: FastAPI

## Ürün İsmi:
Math Solver & Tutor

## Hedef Kitle:
Matematik problemleri çözmeye yeni başlayan ilkokul öğrencileri 

## Product Backlog Url:
[Notion Link](https://www.notion.so/Math-Solver-Tutor-Product-Backlog-22938967824d8077a2aadf84cb9cf02f?source=copy_link)

## Sprint 1 - Total 100 puan:

- 20 puan - LLM trainlemek adına soru ve cevaplarından oluşan excel dosyası oluşturma
- 50 puan - pre-trained model ve tokenizer ile data training
- 30 puan - karşılıklı konuşan chatbot'un başlangıcı


### Ürün Durumu ve Board Screenshot:
  ![Durum](https://github.com/cerensah/Bootcamp-Group-182/blob/main/urunDurumu.png)
  ![BacklogSS](https://github.com/cerensah/Bootcamp-Group-182/blob/main/backlog.png)
### Sprint Review:
  - Sprint için planan aşamalar tamamlandı. Chatbot'a sorular sorularak test edildi. İngilizce dil seçeneği beğenildi, Türkçe de eklenmesine karar verildi.
  - Sprint Review Katılımcıları: Ceren Şahin
       
### Sprint Retrospective:
  - Henüz data sayısı az olduğu için yanlış cevaplar verdiği not edildi. 4 işlem soruları için ekstra bir fonksiyon yazılarak yanlış cevaplar doğruları ile override edildi.
  - Alakasız bir soru sorulduğunda uyarı verme ve hedef kitle çocuk olduğu için kelime filtresi eklenebileceği düşünüldü.

## Sprint 2 ve 3 için planlar (Total 250 puan):

- 50 puan - Excel dosyasındaki soru ve cevapları arttırmak. Ayrıca data çeşitliğini arttırarak farklı dillerde (türkçe, ingilizce ve belki fransızca) çalışmasını sağlamak
- 50 puan - Model fine-tuning ile cevapların kalitesini düzeltmek
- 80 puan - Web tabanlı bir uygulama yaparak chat'i daha erişilebilir yapmak.
- 70 puan (vakit kalırsa) - yazıyla soru sormaya ek olarak resim yükleyerek soru sorma özelliği getirmek
