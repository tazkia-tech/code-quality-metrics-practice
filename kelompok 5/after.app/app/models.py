# Core logic file
from typing import Dict

# -------------------------
# Modul Lifestyle anak kos
# -------------------------
def lifestyle_score(nongkrong: float, hiburan: float, belajar: float, kerja: float) -> Dict:
    """
    Input:
      - nongkrong : jam nongkrong per minggu (jam)
      - hiburan   : pengeluaran hiburan per bulan (IDR)
      - belajar   : jam belajar per minggu (jam)
      - kerja     : jam kerja part-time per minggu (jam)

    Output:
      dict { "score": float(0..1), "status": <str> }
    """
    # Validasi
    if any(x is None for x in (nongkrong, hiburan, belajar, kerja)):
        raise ValueError("Semua input harus diisi.")
    if any(x < 0 for x in (nongkrong, hiburan, belajar, kerja)):
        raise ValueError("Input tidak boleh negatif.")

    # komponen skor (normalisasi + bobot)
    # belajar: ideal 14 jam/minggu (2 jam/hari)
    # kerja: ideal 20 jam/minggu (part-time heavy)
    # nongkrong: ideal <= 5-10 jam; semakin banyak mengurangi skor
    # hiburan: pengeluaran tinggi menurunkan skor (normal cap 500k)
    belajar_component = min(belajar / 14.0, 1.0)       # max 1.0
    kerja_component = min(kerja / 20.0, 1.0)           # max 1.0
    nongkrong_component = max(1.0 - (nongkrong / 25.0), 0.0)   # semakin kecil kalau banyak nongkrong
    hiburan_component = max(1.0 - (hiburan / 500000.0), 0.0)  # cap; besar hiburan -> turun

    score = round(
        0.4 * belajar_component +
        0.3 * kerja_component +
        0.2 * nongkrong_component +
        0.1 * hiburan_component,
        2
    )

    # Status mapping
    if score >= 0.8:
        status = "Produktif"
    elif score >= 0.6:
        status = "Cukup Seimbang"
    elif score >= 0.4:
        status = "Terlalu Santai"
    else:
        status = "Boros & Tidak Terarah"

    return {"score": score, "status": status}
