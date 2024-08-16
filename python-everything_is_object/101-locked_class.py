#!/usr/bin/python3

"""
Define a locked class with restricted attribute assignment.
"""


class LockedClass:
    """
    This class represents a locked class
    with restricted attribute assignment.

    Attributes:
        first_name (str): The first name of the locked class instance.
    """

    __slots__ = ['first_name']
