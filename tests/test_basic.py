import pytest
from src.fact import fact
from matplotlib import pyplot as plt

def test_basic_eq0():
    assert fact(0) == 1

def test_basic_eq1():
    assert fact(1) == 1

def test_basic_eq2():
    assert fact(2) == 2

def test_basic_eq7():
    assert fact(7) == 5040

def test_basic_eq20():
    assert fact(20) == 2432902008176640000

def test_basic_eqneg():
    with pytest.raises(ValueError):
        fact(-1)
