#!/usr/bin/python3
"""
Computes the square of each element in a matrix using the map function.
"""


def square_matrix_map(matrix=[]):
    """
    Computes the square of each element in a matrix using the map function.

    Args:
        matrix (list): The input matrix.

    Returns:
        list: A new matrix with the square of each element.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
