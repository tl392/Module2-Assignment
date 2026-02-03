"""
Arithmetic operation functions used by the calculator.

This module contains basic math operations based on user input.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def sub(a, b):
    """Return the difference of two numbers (a - b)."""
    return a - b


def mul(a, b):
    """Return the product of two numbers."""
    return a * b


def div(a, b):
    """
    Return the quotient of two numbers (a / b).

    Raises:
        ZeroDivisionError: if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
