#!/usr/bin/python3
def element_at(my_list, idx):
    listing = my_list
    for item in listing:
        if idx < 0:
            return None
        elif idx > len(listing):
            return None
        else:
            return idx + 1
