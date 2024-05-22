#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    A class that inherits from list.
    """

    def __init__(self):
        """
        Initializes a MyList object.
        """
        pass

    def print_sorted(self):
        """
        Prints the list, but sorted.
        """
        print(sorted(self))
