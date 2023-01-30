#!/usr/bin/python3
"""Define a square"""


class Square:
    """Define a square"""
    __size = None
    """Init"""
    def __init__(self, size=0):
        if size is None:
            size = 0
        else:
            self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""
        buff = self.__size
        if buff is not None:
            return buff ** 2
