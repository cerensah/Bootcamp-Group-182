# Maths Problem Solver & Tutor

## Proje Üyeleri:
Ayşe Ceren Şahin

## Proje Konusu:
Öğrenciler tarafından sorulan matematik problemlerini çözüp nasıl çözdüğünü özetleyen bir chatbot. Çözebildiği konular: 
1. Basit dört işlem
2. Geometrik şekillerin alan ve çevre hesaplaması
3. Basit tek bilinmeyenli denklemler
4. Basit problemler

## Tech Stack:
- Tokenizer ve Model Train için: Google FLAN-T5 Pre-trained Model
- Soru/cevap çiftlerini tutmak için: Excel
- (Sprint 2&3'te) Web tabanlı uygulama geliştirme için: FastAPI

## Sprint 1 - Total 100 puan:

- 20 puan - LLM trainlemek adına soru ve cevaplarından oluşan excel dosyası oluşturma
- 50 puan - pre-trained model ve tokenizer ile data training
- 30 puan - karşılıklı konuşan chatbot'un başlangıcı. Eğer cevap hallucation yüzünden yanlış ise doğru cevap ile override etmek

## Sprint 2 ve 3 için planlar (Total 250 puan):

- 50 puan - Excel dosyasındaki soru ve cevapları arttırmak. Ayrıca data çeşitliğini arttırarak farklı dillerde (türkçe, ingilizce ve belki fransızca) çalışmasını sağlamak
- 50 puan - Model fine-tuning ile cevapların kalitesini düzeltmek
- 80 puan - Web tabanlı bir uygulama yaparak chat'i daha erişilebilir yapmak.
- 70 puan (vakit kalırsa) - yazıyla soru sormaya ek olarak resim yükleyerek soru sorma özelliği getirmek
