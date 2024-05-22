#!/usr/bin/python3
"""
Module for inherits_from method.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class,
    that inherited from a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class,
        that inherited from the given class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
