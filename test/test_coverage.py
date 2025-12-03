"""
Verifikasi: Logika after_app bisa diuji dengan unit test → coverage terukur.
"""
from after_app.app.models import assess_student_health

test_cases = [
    (5, 8, 3, "Sangat Sehat"),
    (0, 4, 1, "Berisiko"),
]

all_passed = True
for exercise, sleep, water, expected in test_cases:
    result = assess_student_health(exercise, sleep, water)
    if result["status"] != expected:
        all_passed = False
        print(f"Gagal: ({exercise}, {sleep}, {water}) → {result['status']} ≠ {expected}")
    else:
        print(f"Lulus: ({exercise}, {sleep}, {water}) → {result['status']}")
