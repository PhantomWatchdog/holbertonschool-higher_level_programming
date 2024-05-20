#!/usr/bin/python3
"""
This module contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number

    Args:
        matrix (list): A matrix represented as a list of lists,
        containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with the elements divided by the given number.

    Raises:
        TypeError: If the matrix is not a list of lists of integers,
        floats, or simply a number.
        ZeroDivisionError: If the div is zero.
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(error_msg)

    if len(matrix) == 0:
        raise TypeError(error_msg)

    if not all(type(row) is list for row in matrix):
        raise TypeError(error_msg)

    if not all(all(type(i) in [int, float] for i in row) for row in matrix):
        raise TypeError(error_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
