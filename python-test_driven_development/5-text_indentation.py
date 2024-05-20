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
    new_text = ""
    for i in text:
        new_text += i
        if i == '.' or i == '?' or i == ':':
            new_text += "\n\n"
    print(new_text, end="")
