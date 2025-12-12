# CLI interaktif — jalankan dari project root:
# PYTHONPATH=. python3 test/test_cli.py
import os
import sys

# tambahkan folder parent ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core import lifestyle_score  # gunakan core.py, bukan models.py

def run_cli():
    print("\n=== SISTEM EVALUASI GAYA HIDUP ANAK KOS ===\n")
    try:
        nongkrong = float(input("Jam nongkrong/minggu : ") or 0)
        hiburan   = float(input("Pengeluaran hiburan (IDR) : ") or 0)
        belajar   = float(input("Jam belajar/minggu  : ") or 0)
        kerja     = float(input("Jam kerja/minggu    : ") or 0)
    except ValueError:
        print("Input harus angka. Coba lagi.")
        return

    try:
        hasil = lifestyle_score(nongkrong, hiburan, belajar, kerja)
    except ValueError as e:
        print("Error:", e)
        return

    print("\n--- HASIL EVALUASI ---")
    print("SKOR   :", hasil["score"])
    print("STATUS :", hasil["status"])
    print()

if __name__ == "__main__":
    run_cli()
