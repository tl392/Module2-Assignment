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
        raise ValueError("Format: <number> <operator> <number>")
    a, op, b = parts
    return op, float(a), float(b)
