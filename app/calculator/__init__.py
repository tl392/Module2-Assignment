"""
Interactive calculator runner.

This module owns the calculator loop and exposes a single
entry-point function that can be called from main.py.
"""

from app.operations import add, sub, mul, div, mod
from app.parser import parse_input


def calculate(op: str, a: float, b: float) -> float:
    """Perform a calculation based on the given operator."""
    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "%": mod,
    }

    try:
        return operators[op](a, b)
    except KeyError as exc:
        raise ValueError(f"Unknown operator: {op}") from exc


def start_calculator() -> None:
    """
    Start the interactive calculator loop.

    This function is intended to be called from main.py.
    """
    print(f"""Calculator program started !!!
    Please enter your input in below format
        <NUM1> <OPERATOR> <NUM2> => ex: 2 * 2
    Please use any one of the operator from this list below
        + - Addition
        - - Subtraction
        * - Multiplication
        / - Division
        % - Modulo
    If you want to quit type q or quit or exit""")
    while True:
        line = input("> ").strip()

        if line.lower() in {"q", "quit", "exit"}:
            print("Bye!")
            break

        try:
            op, a, b = parse_input(line)
            result = calculate(op, a, b)
            print(result)
        except Exception as e:
            print(f"Error: {e}")
