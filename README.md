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
- Web tabanlı uygulama geliştirme için: Gradio
- Image-to-text çeviri için: Tesseract OCR

## Ürün İsmi:
Math Solver & Tutor

## Hedef Kitle:
Matematik problemleri çözmeye yeni başlayan ilkokul öğrencileri 

## Product Backlog Url:
[Notion Link](https://www.notion.so/Math-Solver-Tutor-Product-Backlog-22938967824d8077a2aadf84cb9cf02f?source=copy_link)

### Sprint 1 - Total 100 puan:
<details>

<summary> Sprint 1 - Detaylar İçin Tıklayın </summary>


<br/>


- 20 puan - LLM trainlemek adına soru ve cevaplarından oluşan excel dosyası oluşturma
- 50 puan - pre-trained model ve tokenizer ile data training
- 30 puan - karşılıklı konuşan chatbot'un başlangıcı


### Ürün Durumu ve Board Screenshot:

  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/urunDurumu.png" width="750" />
  <br>
  <em> Terminal üzerinden prompt ile soru sorma.</em>
</p>


<br/>


  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/urunDurumu.png" width="750" />
  <br>
  <em> Sprint 1 Backlog.</em>
</p>

### Sprint Review:
  - Sprint için planan aşamalar tamamlandı. Chatbot'a sorular sorularak test edildi. İngilizce dil seçeneği beğenildi, Türkçe de eklenmesine karar verildi.
  - Sprint Review Katılımcıları: Ceren Şahin
       
### Sprint Retrospective:
  - Henüz data sayısı az olduğu için yanlış cevaplar verdiği not edildi. 4 işlem soruları için ekstra bir fonksiyon yazılarak yanlış cevaplar doğruları ile override edildi.
  - Alakasız bir soru sorulduğunda uyarı verme ve hedef kitle çocuk olduğu için kelime filtresi eklenebileceği düşünüldü.

</details>

### Sprint 2 - Total 150 puan:
<details>

<summary> Sprint 2 - Detaylar İçin Tıklayın </summary>

<br/>

- 20 puan - Daha çeşitli soru oluşturmak ve soru sayısını arttırarak cevap kalitesini yükseltmek

- 20 puan - Türkçe dil seçeneği eklenmesi
  
- 50 puan - Gradio yardımı ile web-tabanlı app yapımı
  
- 60 puan - Tesseract OCR ile Gradio üzerinden yüklenilen soru fotoğraflarının algılanması


### Ürün Durumu ve Board Screenshot:

  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/urunSprint2.png" width="750" />
  <br>
  <em> Yazılı prompt ile soru sorma.</em>
</p>


<br/>


  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/urunSprint_resimAlgilama.png" width="750" />
  <br>
  <em> Resim yükleme ile soru sorma. Aşağıda görülen "if 2x + 5 = 11, what is x?" fotoğrafından Tesseract ile soru algılanıyor ve cevap veriliyor.</em>
</p>


<br/>


  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/backlog_sprint2.png" width="750" />
  <br>
  <em> Sprint 2 Backlog.</em>
</p>


### Sprint Review:
  - Türkçe dil desteği dışındaki planan aşamalar tamamlandı. Gradio ile web tabanlı uygulama çalıştırılıp yazılı prompt ve foto prompt test edildi.
  - Sprint Review Katılımcıları: Ceren Şahin
       
### Sprint Retrospective:
  - Data sayısının artması ile cevap kalitesinin arttığı görüldü ancak hala yetersiz olduğuna karar verildi.
  - Daha kaliteli cevaplar için WolframAlpha ve benzeri bir bilgi motoru framework'e eklenebilir
  - El yazısı ile bir soru yüklendiğinde Tesseract'in algılamada zorlandığı görüldü. Kontrast arttırma ve fotoğraf keskinleştirme gibi filtreler koyarak algılama yükseltilebilir.

</details>

</details>

### Sprint 3 - Total 130 puan:
<details>

<summary> Sprint 3 - Detaylar İçin Tıklayın </summary>

<br/>

- 80 puan - Wolfram Alpha API eklenmesi ile cevap kalitesinin arttırılması 
  
- 50 puan - Filtreler ile yüklenilen fotoğrafların kaltesinini arttırılması

- 10 puan - Matematik dışındaki sorulara cevap vermemesi için kelime filtesi eklenmesi


### Ürün Durumu ve Board Screenshot:

  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/sprint3_urunDurumu.png" width="750" />
  <br>
  <em> Yazılı prompt ile Wolfram Alpha'ya soru sorma.</em>
</p>


<br/>


  <p align="center">
  <img src="https://github.com/cerensah/Bootcamp-Group-182/blob/main/backlog3.png" width="750" />
  <br>
  <em> Sprint 3 Backlog.</em>
</p>


### Sprint Review:
  - Wolfram Alpha ile cevap kalitesi yükseldiği görüldü

  - Sprint Review Katılımcıları: Ceren Şahin
       
### Sprint Retrospective:
  - Wolfram Alpha eklenilmesi ile kendi kendime yaptığım LLM'in yetersiz kaldığı görüldü ve Wolfram ile tamamlanmaya karar verildi. Ayrıca daha çeşitli matematik sorularına da cevap verebildiği görüldü. 
  - Uygulama HugginFace Spaces'e eklenmeye çalışıldı ancak error'ler çözülemedi (https://huggingface.co/spaces/acsah00/MathSolver)

</details>

