#!/usr/bin/python3
"""python sc"""

import json


def load_from_json_file(filename):
    """json file"""

    with open(filename, mode="r") as f:
        return (json.load(f))
