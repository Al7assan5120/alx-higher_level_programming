#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy = a_dictionary.copy()
    copy = dict(sorted(a_dictionary.items()))
    for i , x in copy.items():
        print(f"{i}: {x}")
