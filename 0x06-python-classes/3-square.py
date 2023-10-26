#!/usr/bin/python3
"""
C and O tasks
"""


class Square:
    """
    sq. class
    """
    def __init__(self, size=0):
        """
        the constructor for Sq. class
        Args:
        size (int) : the size of the square. defaults to Zero.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """
        get the area of a square
        """
        return self.__size * self.__size
