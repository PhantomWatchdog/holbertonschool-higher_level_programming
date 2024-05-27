#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
