#!/usr/bin/python3
"""
    Prints an integer with "{:d}".format().
"""


import sys
def safe_print_integer_err(value):
    """
    Safely prints an integer value.

    Args:
        value (int): The integer value to be printed.

    Returns:
        bool: True if the value was successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False