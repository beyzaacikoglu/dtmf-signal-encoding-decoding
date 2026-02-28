# DTMF Encode/Decode Tool

Bu küçük Python projesi, verilen bir metni DTMF tabanlı çift frekans tonlarına çevirir, bu ses dosyasını çözer ve frekans/tüsn elde etmek için grafikler üretir.

## İçerik

- `dtmf_encode.py` – Metni DTMF tonlarına dönüştürüp `encoded.wav` olarak kaydeder ve çalar.
- `dtmf_decode.py` – `encoded.wav` dosyasını analiz ederek metni geri çıkarır.
- `plots.py` – Zaman domeni ve FFT grafiğini hesaplar. Artık `report.png` adında tek bir rapor oluşturur ve çözülen metni başlıkta gösterir.
- `run_all.py` – Üç betiği ardışık olarak çalıştırır. Tek komutla encode, decode ve grafik üretme.
- `cleanup.py` – `fft.png` ve `zaman_domeni.png` gibi artık gereksiz dosyaları siler.
- `encoded.wav` – Örnek olarak üretilebilen ses/ton dosyası.


## Gereksinimler

Python 3 ve aşağıdaki paketler:

```sh
pip install numpy scipy sounddevice soundfile matplotlib
```

(opsiyonel) `winsound` Windows ile birlikte gelir.

## Kullanım

Aşağıdaki komutları proje dizininde çalıştırın.

### Tüm adımları çalıştırma

```powershell
python run_all.py
```

Bu komut önce metin isteyecek, sonra encode/decode yapacak ve `report.png` dosyasını oluşturacaktır.

Belirli bir metin vermek için:

```powershell
python run_all.py -t "MERHABA DÜNYA"
```

### Sadece encode

```powershell
python dtmf_encode.py
```

### WAV dosyasını dinleme

PowerShell'de:
```powershell
start encoded.wav
```

veya Python içinde:

```python
import winsound
winsound.PlaySound("encoded.wav", winsound.SND_FILENAME)
```

### Gereksiz dosyaları temizleme

```powershell
python cleanup.py
```


## Dosyalar nerede?

- `encoded.wav` ve `report.png` proje kökünde oluşturulur.

> **Not:** Proje Windows için tasarlanmıştır; paketler veya ses çalma komutları diğer platformlarda farklı olabilir.

---

Herhangi bir sorunuz olursa lütfen bildirin!