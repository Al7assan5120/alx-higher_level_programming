#!/usr/bin/python3
"""Python Script."""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator.

        Args:
            name (str): str
            value (int): int
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from the base geometry class."""

    def __init__(self, width, height):
        """Validate and initialize width and height.

        Args:
            width (int): width
            height (int): height
        """
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
