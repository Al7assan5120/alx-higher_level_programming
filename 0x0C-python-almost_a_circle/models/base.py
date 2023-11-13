#!/usr/bin/python3

"""Base of my project"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string"""

        pass

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""

        if json_string is None:
            return []
        return json.loads(json_string)
