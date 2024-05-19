#!/usr/bin/python3
"""
This is a module for a class Square.
Defines a square.
"""


class Square:
    """
    This is a class representing a square.
    Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: area.
    """

    def __init__(self, size=0):
        """Initializes the Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return (self.__size) ** 2
