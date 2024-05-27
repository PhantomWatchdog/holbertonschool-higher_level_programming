#!/usr/bin/python3
"""Module for load_from_json_file"""


def load_from_json_file(filename):
    """creates an Object from another file"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
