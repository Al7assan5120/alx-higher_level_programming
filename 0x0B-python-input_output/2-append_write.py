#!/usr/bin/python3
"""python sc"""


def append_write(filename="", text=""):
    """write file"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
