#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''new_list = {}
    for key, value in a_dictionary.items():
        new_list[key] = value * 2
    return new_list
    '''

    return {key: value * 2 for key, value in a_dictionary.items()}
