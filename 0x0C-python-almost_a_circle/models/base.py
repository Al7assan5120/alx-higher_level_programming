#!/usr/bin/python3

"""Base of my project"""


class Base:
    """Base class"""

    nb_objects = 0

    def init(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.nb_objects += 1
            self.id = Base.__nb_objects
