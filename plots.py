import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from dtmf_decode import decode_wav

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

# ---- 2) FFT (ilk karakter için) ----
N = int(fs * TONE_MS / 1000)
segment = sig[:N]

fft_vals = np.abs(np.fft.rfft(segment))
freqs = np.fft.rfftfreq(N, 1/fs)

# ---- Çözülen metni al ----
decoded = decode_wav("encoded.wav")

# ---- Tek sayfada rapor oluştur ----
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

axs[0].plot(t[:2000], sig[:2000])
axs[0].set_title("Zaman Domeni Grafiği")
axs[0].set_xlabel("Zaman (s)")
axs[0].set_ylabel("Genlik")
axs[0].grid()

axs[1].plot(freqs, fft_vals)
axs[1].set_xlim(600, 1800)
axs[1].set_title("FFT Grafiği (İki Tepe Görülecek)")
axs[1].set_xlabel("Frekans (Hz)")
axs[1].set_ylabel("Genlik")
axs[1].grid()

fig.suptitle(f"Çözülen metin: {decoded}")
plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.savefig("report.png")
print("Rapor kaydedildi: report.png")
plt.show()