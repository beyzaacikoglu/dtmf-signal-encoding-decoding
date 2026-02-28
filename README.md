# DTMF Signal Encoding & Decoding with FFT

Bu projede, DTMF benzeri bir frekans tabanlı yöntem kullanılarak metin sinyal biçiminde
kodlanmış, frekans alanında (FFT) analiz edilmiş ve tekrar çözümlenmiştir.
Amaç; zaman domeni, frekans domeni ve iki baskın frekansın karakterleri nasıl temsil ettiğini
uygulamalı olarak göstermektir.

---

## Proje Özeti

Çalışma üç ana aşamadan oluşmaktadır:

1. **Kodlama (Encoding)**
   - Girilen metindeki her karakter, iki farklı sinüs frekansının toplamı ile temsil edilmiştir.
   - Oluşturulan sinyal `.wav` formatında kaydedilmiştir.

2. **Frekans Analizi (FFT)**
   - Kodlanan sinyalin zaman domeni grafiği çizilmiştir.
   - FFT uygulanarak frekans domeninde her karakter için iki baskın tepe noktası gözlemlenmiştir.

3. **Çözme (Decoding)**
   - FFT sonucunda elde edilen frekanslar, karakter–frekans eşleme tablosu ile karşılaştırılarak
     orijinal metin başarıyla geri elde edilmiştir.

---

## Dosya Yapısı
dtmf-signal-encoding-decoding/
│
├── dtmf_encode.py # Metni sinyal olarak kodlar ve encoded.wav oluşturur
├── dtmf_decode.py # encoded.wav dosyasını çözerek metni geri elde eder
├── plots.py # Zaman domeni ve FFT grafiklerini üretir
├── encoded.wav # Kodlanmış ses sinyali
├── zaman_domeni.png # Zaman domeni grafiği
└── fft.png # FFT grafiği (iki baskın frekans tepe noktası)




---

## Kullanım

### 1) Kodlama
```bash
python dtmf_encode.py
Kullanıcıdan metin alınır, encoded.wav dosyası oluşturulur ve ses çalınır.


2) Grafiklerin Oluşturulması
python plots.py
Zaman domeni ve FFT grafikleri otomatik olarak PNG formatında kaydedilir.

3) Çözme
python dtmf_decode.py
Kodlanan ses dosyası çözülür ve orijinal metin terminalde gösterilir.

Sonuçlar

Zaman domeninde sinyalin yapısı açıkça gözlemlenmiştir.

FFT grafiğinde her karakter için iki baskın frekans tepe noktası net olarak görülmüştür.

Çözme aşamasında metin hatasız şekilde geri elde edilmiştir.

Bu sonuçlar, frekans tabanlı sinyal kodlama ve çözme işleminin başarıyla
gerçekleştirildiğini göstermektedir.
