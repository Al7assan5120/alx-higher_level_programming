#!/usr/bin/python3
"""python sc"""


def read_file(filename=""):
    """read file"""

    with open(filename, mode='r', encoding='utf-8') as f:
        for lines in f:
            print(lines, end="")
