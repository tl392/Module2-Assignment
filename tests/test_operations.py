import pytest
from app.operations import add, sub, mul, div, mod


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 2) == 3


def test_mul():
    assert mul(4, 3) == 12


def test_div():
    assert div(10, 2) == 5


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_modulo():
    assert mod(10, 3) == 1

def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        mod(1, 0)