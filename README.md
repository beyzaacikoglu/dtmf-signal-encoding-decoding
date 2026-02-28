# DTMF Signal Encoding & Decoding with FFT

Bu projede, DTMF benzeri bir yöntem kullanılarak metin sinyal biçiminde
kodlanmış, frekans alanında (FFT) analiz edilmiş ve tekrar çözümlenmiştir.
Amaç, zaman domeni – frekans domeni ilişkisini ve iki baskın frekansın
karakterleri nasıl temsil ettiğini göstermektir.

---

## 📌 Proje İçeriği

Proje üç ana aşamadan oluşmaktadır:

1. **Kodlama (Encoding)**
   - Girilen metindeki her karakter, iki farklı sinüs frekansının toplamı ile temsil edilmiştir.
   - Oluşturulan sinyal `.wav` formatında kaydedilmiştir.

2. **Frekans Analizi (FFT)**
   - Kodlanan sinyalin zaman domeni grafiği çizilmiştir.
   - FFT uygulanarak frekans domeninde iki baskın tepe noktası gözlemlenmiştir.

3. **Çözme (Decoding)**
   - FFT sonucunda elde edilen frekanslar, karakter–frekans tablosu ile eşleştirilerek
     orijinal metin başarıyla geri elde edilmiştir.

---

## 📁 Dosya Yapısı
