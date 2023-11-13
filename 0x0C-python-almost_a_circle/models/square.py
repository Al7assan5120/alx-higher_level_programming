#!/usr/bin/python3

"""Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class Inharites from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, new_size):
        """size setter"""
        self.width = new_size
        self.height = self.width

    def update(self, *args, **kwargs):
        """update the attributes of the square"""
        if not args:
            for x, y in kwargs.items():
                if x == "size":
                    self.width = y
                if x == "x":
                    self.x = y
                if x == "y":
                    self.y = y
                if x == "id":
                    self.id = y
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
        return dic
