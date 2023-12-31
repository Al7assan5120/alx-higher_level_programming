#!/usr/bin/python3

"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):

    """Rectangle Class Inharites from Base Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, new_width):
        """width setter"""
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        """height setter"""
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @x.setter
    def x(self, new_x):
        """x setter"""
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        """y setter"""
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """calculate area of the rectangle"""
        return self.__width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.y, end="")
        for x in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """update fun"""
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
        attributes = [self.id, self.__width, self.__height, self.__x, self.__y]
        for i, value in enumerate(args):
            if i < len(attributes):
                attributes[i] = value
        self.id, self.__width, self.__height, self.__x, self.__y = attributes

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
        return dic
