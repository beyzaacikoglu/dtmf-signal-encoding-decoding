import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd

# -----------------------------
# 1) Karakter seti (30 karakter)
# -----------------------------
CHARS = [
    "A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö",
    "P","R","S","Ş","T","U","Ü","V","Y","Z"," "
]

# 6x5 = 30 kombinasyon
LOW_FREQS  = [700, 770, 840, 910, 980, 1050]
HIGH_FREQS = [1200, 1330, 1470, 1600, 1730]

# Karakter -> (flow, fhigh)
CHAR_TO_FREQ = {}
idx = 0
for lf in LOW_FREQS:
    for hf in HIGH_FREQS:
        CHAR_TO_FREQ[CHARS[idx]] = (lf, hf)
        idx += 1

# -----------------------------
# 2) Parametreler
# -----------------------------
FS = 44100
TONE_MS = 40
TONE_SEC = TONE_MS / 1000.0
AMP = 0.5
GAP_MS = 5
GAP_SAMPLES = int(FS * (GAP_MS / 1000.0))

def synth_char(ch):
    f1, f2 = CHAR_TO_FREQ[ch]
    t = np.linspace(0, TONE_SEC, int(FS * TONE_SEC), endpoint=False)
    s = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)
    s = AMP * s / np.max(np.abs(s))
    return s.astype(np.float32)

def encode_text(text):
    parts = []
    for ch in text.upper():
        parts.append(synth_char(ch))
        parts.append(np.zeros(GAP_SAMPLES, dtype=np.float32))
    return np.concatenate(parts)

def main():
    text = input("Metin gir (örn: MERHABA DÜNYA): ")

    for c in text.upper():
        if c not in CHAR_TO_FREQ:
            print("Desteklenmeyen karakter:", c)
            return

    sig = encode_text(text)
    sig16 = np.int16(sig / np.max(np.abs(sig)) * 32767)
    write("encoded.wav", FS, sig16)

    print("encoded.wav oluşturuldu, çalınıyor...")
    sd.play(sig, FS)
    sd.wait()

if __name__ == "__main__":
    main()