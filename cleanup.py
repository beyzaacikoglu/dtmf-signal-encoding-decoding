import os
from pathlib import Path

cwd = Path(__file__).resolve().parent
files = ["fft.png", "zaman_domeni.png"]
removed = []
for f in files:
    p = cwd / f
    if p.exists():
        try:
            p.unlink()
            removed.append(f)
        except Exception as e:
            print(f"Failed to remove {f}: {e}")
    else:
        print(f"Not found: {f}")

if removed:
    print("Removed:", ", ".join(removed))
else:
    print("No files removed.")
