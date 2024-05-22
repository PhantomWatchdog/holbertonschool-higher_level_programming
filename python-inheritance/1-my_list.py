#!/usr/bin/python3
"""
Module for MyList class.
"""


from typing import Iterable


class MyList(list):
    """
    A class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted.
        """
        print(sorted(self))
