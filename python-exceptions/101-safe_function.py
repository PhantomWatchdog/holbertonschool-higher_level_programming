#!/usr/bin/python3
"""
Safe function
"""

import sys


def safe_function(fct, *args):
    """
    Executes a function safely by handling any exceptions that may occur.

    Args:
        fct (function): The function to be executed.
        *args: Variable length argument list to be passed to the function.

    Returns:
        The result of the function execution if successful, None otherwise.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e))
        return None
