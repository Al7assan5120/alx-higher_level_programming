#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for data in copy:
        copy[data] *= 2
    return copy
