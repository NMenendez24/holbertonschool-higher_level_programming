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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        if self.__size is not None:
            for i in range(0, self.__size):
                for k in range(0, self.__size):
                    print("#", end="")
                print("")
