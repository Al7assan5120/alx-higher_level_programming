#!/usr/bin/python3
"""python sc"""

import json


def save_to_json_file(my_obj, filename):
    """json file"""

    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
