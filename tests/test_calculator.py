import builtins
import pytest

from app.calculator import calculate, start_calculator


# ---- calculate() ----

@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        ("+", 2, 3, 5),
        ("-", 10, 4, 6),
        ("*", 3, 7, 21),
        ("/", 8, 2, 4),
        ("%", 8, 3, 2),
    ],
)
def test_calculate_all_ops(op, a, b, expected):
    assert calculate(op, a, b) == expected


def test_calculate_unknown_operator():
    with pytest.raises(ValueError):
        calculate("&", 1, 2)


def test_calculate_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("/", 1, 0)


# ---- start_calculator() ----

def test_start_calculator_quit(monkeypatch, capsys):
    inputs = iter(["q"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    start_calculator()

    out = capsys.readouterr().out
    assert "Calculator program started" in out
    assert "Bye!" in out


def test_start_calculator_happy_path(monkeypatch, capsys):
    inputs = iter(["10 + 5", "q"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    start_calculator()

    out = capsys.readouterr().out
    assert "15.0" in out
    assert "Bye!" in out


def test_start_calculator_error_path(monkeypatch, capsys):
    inputs = iter(["bad input", "q"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    start_calculator()

    out = capsys.readouterr().out
    assert "Error:" in out
    assert "Bye!" in out

def test_start_calculator_error_then_success(monkeypatch, capsys):
    inputs = iter(["bad input", "10 + 5", "q"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    start_calculator()

    out = capsys.readouterr().out
    assert "Error:" in out
    assert "15.0" in out
    assert "Bye!" in out