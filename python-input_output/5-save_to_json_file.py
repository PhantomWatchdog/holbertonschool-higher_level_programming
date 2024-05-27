#!/usr/bin/python3
"""
save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save the given object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
