import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from dtmf_decode import decode_wav
from matplotlib.colors import LinearSegmentedColormap

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

# ---- Premium tasarım tema ----
plt.style.use('default')
fig = plt.figure(figsize=(14, 12))
fig.patch.set_facecolor('#0f1419')

# Custom gradient colormap
colors_grad = ['#00d4ff', '#0099ff', '#ff0055', '#ff6b35']
n_bins = 100
cmap = LinearSegmentedColormap.from_list('premium', colors_grad, N=n_bins)

# ---- Alt grafikleri düzenle (2x2 grid) ----
gs = fig.add_gridspec(3, 2, hspace=0.45, wspace=0.32, top=0.92, bottom=0.12, left=0.08, right=0.95)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])
ax4 = fig.add_subplot(gs[2, :])

# ---- 1) ZAMAN DOMENİ GRAFIĞI (Premium) ----
ax1.plot(t[:2000], sig[:2000], linewidth=3, color='#00d4ff', label='Ses Sinyali', zorder=3)
ax1.fill_between(t[:2000], sig[:2000], alpha=0.4, color='#00d4ff', zorder=2)
ax1.set_title("🌊 Zaman Domeni Analizi", fontsize=13, fontweight='bold', pad=10, color='#ffffff')
ax1.set_xlabel("Zaman (s)", fontsize=10, fontweight='bold', color='#cccccc')
ax1.set_ylabel("Genlik", fontsize=10, fontweight='bold', color='#cccccc')
ax1.grid(True, alpha=0.15, linestyle='-', linewidth=0.5, color='#ffffff')
ax1.set_facecolor('#1a202c')
ax1.legend(loc='upper right', fontsize=10, framealpha=0.9, facecolor='#2d3748', edgecolor='#00d4ff')
for spine in ax1.spines.values():
    spine.set_edgecolor('#00d4ff')
    spine.set_linewidth(1.5)
ax1.tick_params(colors='#cccccc')

# ---- 2) FFT GRAFIĞI (Renkli Gradient) ----
# FFT'yi colormap ile göster
fft_normalized = (fft_vals - fft_vals.min()) / (fft_vals.max() - fft_vals.min() + 1e-9)
colors_fft = cmap(fft_normalized)
for i in range(len(freqs)-1):
    ax2.plot(freqs[i:i+2], fft_vals[i:i+2], color=colors_fft[i], linewidth=3.5)

ax2.fill_between(freqs, fft_vals, alpha=0.3, color='#ff0055')
ax2.set_xlim(600, 1800)
ax2.set_title("🎵 FFT Spektrumu", fontsize=12, fontweight='bold', pad=10, color='#ffffff')
ax2.set_xlabel("Frekans (Hz)", fontsize=9, fontweight='bold', color='#cccccc')
ax2.set_ylabel("Genlik", fontsize=9, fontweight='bold', color='#cccccc')
ax2.grid(True, alpha=0.15, linestyle='-', linewidth=0.5, color='#ffffff')
ax2.set_facecolor('#1a202c')
for spine in ax2.spines.values():
    spine.set_edgecolor('#ff0055')
    spine.set_linewidth(1.5)
ax2.tick_params(colors='#cccccc')

# ---- 3) DTMF FREKANS HARITASI ----
dtmf_freqs_dict = {'Düşük': [697, 770, 852, 941], 'Yüksek': [1209, 1336, 1477, 1633]}
freq_labels = {697: '1,2,3', 770: '4,5,6', 852: '7,8,9', 941: '*,0,#',
               1209: '1,4,7,*', 1336: '2,5,8,0', 1477: '3,6,9,#', 1633: 'A,B,C,D'}

dtmf_low = np.array([697, 770, 852, 941])
dtmf_high = np.array([1209, 1336, 1477, 1633])
intensity_grid = np.zeros((4, 4))

for i, low_f in enumerate(dtmf_low):
    for j, high_f in enumerate(dtmf_high):
        # Hangi DTMF tonlarına yakın olup olmadığına bak
        low_idx = np.argmin(np.abs(freqs - low_f))
        high_idx = np.argmin(np.abs(freqs - high_f))
        if low_idx < len(fft_vals) and high_idx < len(fft_vals):
            intensity_grid[i, j] = (fft_vals[low_idx] + fft_vals[high_idx]) / 2

im = ax3.imshow(intensity_grid, cmap='hot', aspect='auto', interpolation='bilinear')
ax3.set_xticks(range(4))
ax3.set_yticks(range(4))
ax3.set_xticklabels(['1209', '1336', '1477', '1633'], color='#cccccc', fontsize=8)
ax3.set_yticklabels(['697', '770', '852', '941'], color='#cccccc', fontsize=8)
ax3.set_title("🎚️ DTMF Matrisi", fontsize=12, fontweight='bold', pad=10, color='#ffffff')
ax3.set_xlabel("Yüksek Frekans (Hz)", fontsize=9, fontweight='bold', color='#cccccc')
ax3.set_ylabel("Düşük Frekans (Hz)", fontsize=9, fontweight='bold', color='#cccccc')
cbar = plt.colorbar(im, ax=ax3)
cbar.set_label('Yoğunluk', color='#cccccc', fontsize=9)
cbar.ax.tick_params(colors='#cccccc', labelsize=8)
ax3.set_facecolor('#1a202c')

# ---- 4) SONUÇ PANELI ----
ax4.axis('off')
ax4.set_xlim(0, 1)
ax4.set_ylim(0, 1)

# Ana sonuç kutusu
result_text = f"🎯 ÇÖZÜLEN METIN: {decoded}"
ax4.text(0.5, 0.65, result_text, 
        fontsize=19, fontweight='bold', 
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=1.2', facecolor='#2d3748', 
                 edgecolor='#00d4ff', linewidth=3, alpha=0.95),
        color='#00d4ff', family='monospace')

# Bilgi paneli
stats_text = f"📊 Analiz Bilgileri\n━━━━━━━━━━━━━━━━━━━━━━\nÖrnek Hızı: {fs} Hz  |  Sinyal: {len(sig)} örnek  |  Ton: {TONE_MS}ms"
ax4.text(0.5, 0.2, stats_text,
        fontsize=10, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=1', facecolor='#1a202c', 
                 edgecolor='#ff6b35', linewidth=2.5, alpha=0.95),
        color='#ff6b35', family='monospace')

# ---- Genel başlık ----
fig.text(0.5, 0.965, "🔊 DTMF SİNYAL ANALİZİ RAPORU", 
        fontsize=18, fontweight='bold', ha='center', color='#00d4ff')
fig.text(0.5, 0.01, "Advanced Frequency Analysis System", 
        fontsize=8, ha='center', style='italic', color='#666666')

plt.savefig("report.png", dpi=300, bbox_inches='tight', facecolor='#0f1419', edgecolor='none')
print("✅ Premium rapor kaydedildi: report.png")
plt.show()