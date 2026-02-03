"""
Interactive command-line calculator application.

This module wires together input parsing, calculation logic,
and an infinite input loop to provide a simple CLI calculator.
"""

from operations import add, sub, mul, div
from parser import parse_input


def calculate(op, a, b):
    """
    Perform a calculation based on the given operator.

    Supported operators: +, -, *, /

    Raises:
        ValueError: if the operator is unsupported.
    """
    if op == "+":
        return add(a, b)
    if op == "-":
        return sub(a, b)
    if op == "*":
        return mul(a, b)
    if op == "/":
        return div(a, b)
    raise ValueError("Unknown operator")


def main():
    """
    Run the calculator in an interactive infinite loop.

    The loop continues until the user enters 'q', 'quit', or 'exit'.
    """
    print("Calculator (q to quit)")
    while True:
        line = input("> ")
        if line.lower() in {"q", "quit", "exit"}:
            break
        try:
            op, a, b = parse_input(line)
            print(calculate(op, a, b))
        except Exception as e:
            print(f"Error: {e}")
