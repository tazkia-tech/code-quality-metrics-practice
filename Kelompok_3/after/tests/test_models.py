import pytest
from app.models import assess

def test_happy():
    res = assess(10,10,0)
    assert res["mood"]=="Happy"

def test_slow():
    res = assess(3,3,7)
    assert res["mood"] in ["Slow","Annoyed"]

def test_invalid():
    with pytest.raises(ValueError):
        assess(-1,5,5)
