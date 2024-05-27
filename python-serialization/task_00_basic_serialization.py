#!/usr/bin/python3
"""
Basic serialization
"""

def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data and saves it to a file.

    Args:
        data: The data to be serialized.
        filename: The name of the file to save the serialized data to.

    Returns:
        None
    """
    import json
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The deserialized JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON data.
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
