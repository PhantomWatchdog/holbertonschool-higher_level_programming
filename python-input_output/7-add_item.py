#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and then save them to a file.

Args:
    [args]: The arguments to be added to the list.

Example:
    $ ./7-add_item.py arg1 arg2 arg3
"""
import sys
saveFile = __import__('5-save_to_json_file').save_to_json_file
loadFile = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = loadFile(filename)
except FileNotFoundError:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

saveFile(my_list, filename)
