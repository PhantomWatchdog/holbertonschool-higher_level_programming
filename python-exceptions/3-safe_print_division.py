#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Safely divides two numbers and prints the result.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division, or None if the denominator is zero.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
