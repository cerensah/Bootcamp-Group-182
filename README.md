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

- 40 puan - LLM trainlemek adına soru ve cevaplarından oluşan excel dosyası oluşturma
- 60 puan - basit bir transformer kurarak matematik sorularına cevap verecek bir LLM oluşturmak

## Sprint 2 ve 3 için planlar (Total 250 puan):

- 50 puan - Excel dosyasındaki soru ve cevapları arttırmak. Ayrıca data çeşitliğini arttırarak farklı dillerde (türkçe, ingilizce ve belki fransızca) çalışmasını sağlamak
- 50 puan - Transformer'da trainlenen seti kullanarak, kullanıcının karşılıklı sohbet edebileceği bir bot kurmak
- 80 puan - Web tabanlı bir uygulama yaparak chat'i daha erişilebilir yapmak.
- 70 puan (vakit kalırsa) - yazıyla soru sormaya ek olarak resim yükleyerek soru sorma özelliği getirmek
