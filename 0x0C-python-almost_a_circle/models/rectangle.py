#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def get_width(self):
        return self.__width

    def set_width(self, new_width):
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    def get_x(self):
        return self.__x

    def set_x(self, new_x):
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    def get_y(self):
        return self.__y

    def set_y(self, new_y):
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
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

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
