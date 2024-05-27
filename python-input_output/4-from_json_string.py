#!/usr/bin/python3
"""
Module for from_json_string
"""


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object representation of the JSON string.

    """
    import json
    return json.loads(my_str)
