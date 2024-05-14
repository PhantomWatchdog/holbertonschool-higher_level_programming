#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
    '''
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
