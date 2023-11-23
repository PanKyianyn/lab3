# test.py
from main import calculator

def test_calculator():
    assert calculator(2, 3) == 5
    assert calculator(-5, 5) == 0
    assert calculator(5, 5) == 10
