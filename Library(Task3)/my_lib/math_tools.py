"""
Module: math_tools
Provides basic mathematical operations (factorial, greatest common divisor).
"""

import math
from typing import Tuple  # Importing Tuple for return types
# https://docs.python.org/3/library/typing.html#typing.Tuple

def factorial(n: int) -> int:
    """
    Computes the factorial of a given number.

    :param n: Non-negative integer.
    :return: Factorial of n.
    :rtype: int
    :raises ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def gcd(a: int, b: int) -> int:
    """
    Computes the greatest common divisor (GCD) of two integers.

    :param a: First integer.
    :param b: Second integer.
    :return: GCD of a and b.
    :rtype: int
    """
    return math.gcd(a, b)
