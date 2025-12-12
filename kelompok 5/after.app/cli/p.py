import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.models import lifestyle_score

print("=== SISTEM EVALUASI GAYA HIDUP ANAK KOS ===")

nongkrong = float(input("Jam nongkrong/minggu : "))
hiburan   = float(input("Pengeluaran hiburan (IDR) : "))
belajar   = float(input("Jam belajar/minggu : "))
kerja     = float(input("Jam kerja/minggu : "))

hasil = lifestyle_score(nongkrong, hiburan, belajar, kerja)

print("\n--- HASIL EVALUASI ---")
print("SKOR   :", hasil["score"])
print("STATUS :", hasil["status"])
