#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''for key, value in sorted(a_dictionary.items()):
            print(key, ':', value)
    '''
    sorted_keys = sorted(a_dictionary)

    for key in sorted_keys:
        print(key, ':', a_dictionary[key])
