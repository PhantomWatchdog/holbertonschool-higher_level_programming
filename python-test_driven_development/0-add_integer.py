#!/usr/bin/python3
""" Module for add_integer function.
    This module provides a simple function,
    add_integer(a, b),
    that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
