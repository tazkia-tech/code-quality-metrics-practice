from models import assess_fitness

result = assess_fitness(
    "pria",
    60,
    170,
    20,
    "sedang",
    "bulking",
    5
)

print("===== HASIL FITNESS =====")
print("Kebutuhan Kalori :", result["kalori"])
print("\nRekomendasi Latihan:")
for item in result["latihan"]:
    print("-", item)

print("\nEstimasi Kekar :", result["estimasi"])
