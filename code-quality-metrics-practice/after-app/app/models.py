def validate_student_data(exercise: float, sleep: float, water: float):
    if any(x < 0 for x in (exercise, sleep, water)):
        raise ValueError("Nilai tidak boleh negatif.")

def calculate_health_score(exercise: float, sleep: float, water: float) -> float:
    return round(
        0.4 * min(exercise / 5.0, 1.0) +
        0.4 * min(sleep / 8.0, 1.0) +
        0.2 * min(water / 3.0, 1.0),
        2
    )

def get_health_status(score: float) -> str:
    if score >= 0.8:
        return "Sangat Sehat"
    elif score >= 0.6:
        return "Sehat"
    elif score >= 0.4:
        return "Perlu Perbaikan"
    else:
        return "Berisiko"

def assess_student_health(exercise: float, sleep: float, water: float):
    validate_student_data(exercise, sleep, water)
    score = calculate_health_score(exercise, sleep, water)
    status = get_health_status(score)
    return {"score": score, "status": status}