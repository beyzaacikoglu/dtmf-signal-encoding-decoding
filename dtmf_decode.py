import numpy as np
from scipy.io.wavfile import read

FS = 44100
TONE_MS = 40
GAP_MS = 5

LOW_FREQS  = [700, 770, 840, 910, 980, 1050]
HIGH_FREQS = [1200, 1330, 1470, 1600, 1730]

CHARS = [
    "A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö",
    "P","R","S","Ş","T","U","Ü","V","Y","Z"," "
]

CHAR_TO_FREQ = {}
i = 0
for lf in LOW_FREQS:
    for hf in HIGH_FREQS:
        CHAR_TO_FREQ[(lf, hf)] = CHARS[i]
        i += 1


def get_freqs(x):
    X = np.abs(np.fft.rfft(x))
    freqs = np.fft.rfftfreq(len(x), 1/FS)
    idx = np.argsort(X)[-2:]
    f = np.sort(freqs[idx])
    return f


def nearest(f, arr):
    return min(arr, key=lambda x: abs(x - f))


def decode_wav(path="encoded.wav"):
    fs, sig = read(path)
    if sig.ndim > 1:
        sig = sig[:, 0]
    sig = sig.astype(np.float32)
    sig /= (np.max(np.abs(sig)) + 1e-9)

    out = ""
    i = 0
    TONE_SAMPLES = int(FS * TONE_MS / 1000)
    STEP = int(FS * (TONE_MS + GAP_MS) / 1000)
    while i + TONE_SAMPLES < len(sig):
        frame = sig[i:i+TONE_SAMPLES]
        if np.max(np.abs(frame)) < 0.05:
            i += STEP
            continue

        f1, f2 = get_freqs(frame)
        lf = nearest(f1, LOW_FREQS)
        hf = nearest(f2, HIGH_FREQS)
        out += CHAR_TO_FREQ.get((lf, hf), "?")
        i += STEP

    return out


def main():
    out = decode_wav("encoded.wav")
    print("Çözülen metin:", out)


if __name__ == "__main__":
    main()