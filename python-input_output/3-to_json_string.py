#!/usr/bin/python3
"""
Converts a Python object to a JSON string
"""


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj (object): The object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    import json
    return json.dumps(my_obj)
