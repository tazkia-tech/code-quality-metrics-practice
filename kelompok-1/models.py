def hitung_kalori(gender, berat, tinggi, usia, aktivitas):
    if gender == "pria":
        bmr = 10*berat + 6.25*tinggi - 5*usia + 5
    else:
        bmr = 10*berat + 6.25*tinggi - 5*usia - 161

    faktor = {
        "ringan": 1.375,
        "sedang": 1.55,
        "berat": 1.725
    }

    return round(bmr * faktor[aktivitas])


def rekomendasi_latihan(tujuan):
    if tujuan == "bulking":
        return [
            "Push Day (Dada, Bahu, Tricep)",
            "Pull Day (Punggung, Bicep)",
            "Leg Day (Kaki & Glutes)",
            "Istirahat 1 hari",
            "Repeat"
        ]
    elif tujuan == "cutting":
        return [
            "HIIT 20 menit",
            "Full Body Workout",
            "Cardio 30 menit",
            "Push-Pull-Legs ringan"
        ]
    else:
        return [
            "Full Body 3x seminggu",
            "Cardio 2x seminggu"
        ]


def estimasi_kekar(hari_latihan):
    if hari_latihan >= 6:
        return "sekitar 2–3 bulan"
    elif hari_latihan >= 4:
        return "sekitar 4–6 bulan"
    else:
        return "lebih dari 6 bulan"


def assess_fitness(gender, berat, tinggi, usia, aktivitas, tujuan, hari_latihan):
    return {
        "kalori": hitung_kalori(gender, berat, tinggi, usia, aktivitas),
        "latihan": rekomendasi_latihan(tujuan),
        "estimasi": estimasi_kekar(hari_latihan)
    }
