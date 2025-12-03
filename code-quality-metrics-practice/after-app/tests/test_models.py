# after-app/tests/test_models.py
import pytest
from app.models import assess_student_health

def test_sangat_sehat():
    res = assess_student_health(5, 8, 3)
    assert res["status"] == "Sangat Sehat"
    assert res["score"] == 1.0

def test_sehat():
    res = assess_student_health(3, 6, 2)
    assert res["status"] == "Sehat"
    assert 0.6 <= res["score"] < 0.8

def test_perlu_perbaikan():
    res = assess_student_health(1, 5, 1.5)
    assert res["status"] == "Perlu Perbaikan"
    assert 0.4 <= res["score"] < 0.6

def test_berisiko():
    res = assess_student_health(0, 4, 1)
    assert res["status"] == "Berisiko"
    assert res["score"] == 0.27  # (0 + 0.5 + 0.33)*0.4/0.4+... ≈ 0.27

def test_invalid_negative():
    with pytest.raises(ValueError):
        assess_student_health(-1, 6, 2)

def test_zero_values():
    res = assess_student_health(0, 0, 0)
    assert res["status"] == "Berisiko"