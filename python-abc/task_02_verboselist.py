#!/usr/bin/env python3
""" Shapes, Interfaces, and Duck Typing
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            index = -1
        popped = super().pop(index)
        print("Popped [{}] from the list".format(popped))
        return popped
