import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# ---- Parametreler (encode ile birebir) ----
FS_EXPECTED = 44100
TONE_MS = 40

# ---- WAV oku ----
fs, sig = read("encoded.wav")

if sig.ndim > 1:
    sig = sig[:, 0]

sig = sig.astype(np.float32)
sig = sig / (np.max(np.abs(sig)) + 1e-9)

# ---- 1) ZAMAN DOMENİ ----
t = np.arange(len(sig)) / fs
plt.figure(figsize=(10, 4))
plt.plot(t[:2000], sig[:2000])
plt.title("Zaman Domeni Grafiği")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid()
plt.tight_layout()
plt.savefig("zaman_domeni.png")
plt.close()

# ---- 2) FFT (ilk karakter için) ----
N = int(fs * TONE_MS / 1000)
segment = sig[:N]

fft_vals = np.abs(np.fft.rfft(segment))
freqs = np.fft.rfftfreq(N, 1/fs)

plt.figure(figsize=(10, 4))
plt.plot(freqs, fft_vals)
plt.xlim(600, 1800)
plt.title("FFT Grafiği (İki Tepe Görülecek)")
plt.xlabel("Frekans (Hz)")
plt.ylabel("Genlik")
plt.grid()
plt.tight_layout()
plt.savefig("fft.png")
plt.close()

print("Grafikler kaydedildi: zaman_domeni.png ve fft.png")
import matplotlib.pyplot as plt
plt.show()