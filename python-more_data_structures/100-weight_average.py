#!/usr/bin/python3
"""
Module for weight_average function.
"""


def weight_average(my_list=[]):
    """
    Calculates the weighted average of a list of tuples.

    Args:
        my_list (list):
            A list of tuples,
            where each tuple contains two elements:
            the value and its corresponding weight.

    Returns:
        float: The weighted average of the values in the list.

    """
    if not my_list:
        return 0
    return sum([x * y for x, y in my_list]) / sum([y for x, y in my_list])
