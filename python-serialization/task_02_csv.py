#!/usr/bin/python3
"""
Convert CSV to JSON
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Serialize the list of dictionaries
        json_data = json.dumps(data)

        # Write the serialized JSON data to data.json
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        # Return True if the conversion was successful
        return True

    except FileNotFoundError:
        # Return False if the file was not found
        return False
