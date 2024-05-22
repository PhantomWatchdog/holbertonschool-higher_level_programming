#!/usr/bin/python3
"""
Module for is_same_class method.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the given class, False otherwise.
    """
    return type(obj) is a_class
