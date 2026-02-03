import pytest
from app.parser import parse_input


def test_valid_input():
    op, a, b = parse_input("10 / 2")
    assert op == "/"
    assert a == 10.0
    assert b == 2.0


def test_invalid_format():
    with pytest.raises(ValueError):
        parse_input("10 +")

def test_parse_input_non_numeric_operands():
    with pytest.raises(ValueError, match="Operands must be numbers"):
        parse_input("a + 2")