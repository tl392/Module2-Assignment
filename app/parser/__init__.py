"""
User input parsing utilities for the calculator.

This module is responsible for validating and converting raw
string input into structured data used by the calculator logic.
"""

def parse_input(line: str):
    """
    Parse user input into operator and operands.

    Expected format:
        <number> <operator> <number>
        Example: "10 / 2"

    Returns:
        tuple: (operator, left_operand, right_operand)

    Raises:
        ValueError: if input format is invalid.
    """
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError("Expected input format: <number> <operator> <number>")
    a_str, op, b_str = parts

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError as exc:
        raise ValueError("Operands must be numbers") from exc

    return op, a, b
