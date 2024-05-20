#!/usr/bin/python3
"""
Module for add_integer
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
