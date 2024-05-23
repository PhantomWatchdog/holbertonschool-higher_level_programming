#!/usr/bin/env python3

import abc from ABC, abstractmethod


class Verboselist(list):
    def append(self, item):
        print("Append {}".format(item))
        super().append(item)

    def extend(self, item):
        print("Extend {}".format(item))
        super().extend(item)

    def insert(self, index, item):
        print("Insert {} at position {}".format(item, index))
        super().insert(index, item)