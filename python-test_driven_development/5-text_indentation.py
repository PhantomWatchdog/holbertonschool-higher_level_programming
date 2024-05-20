#!/usr/bin/python3
"""
This module contains a function that adds two new lines after '.', '?', and ':'
"""


def text_indentation(text):
    """
    Function to add two new lines after '.', '?', and ':'

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None. The function prints the modified text with added new lines.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for char in text:
        if i == 0:
            if char == " ":
                continue
            else:
                i = 1
        if i == 1:
            if char in [".", "?", ":"]:
                print((char))
                print()
                i = 0
            else:
                print((char), end=(""))
