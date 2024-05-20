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
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = ""
    for i in text:
        if i == " " and i == text[0] and char == "":
            char = "\n"
            continue
        if i == " " and char == "\n":
            continue
        if i in [".", "?", ":"]:
            print(i)
            print()
            char = "\n"
        else:
            print(i, end="")
            char = i
