#!/usr/bin/python3
"""Define a square"""


class Square:
    """Define a square"""
    __position = None
    __size = None
    """Init"""
    def __init__(self, size=0, position=(0, 0)):
        if size is None:
            size = 0
        else:
            self.__size = size
        if position is None:
            position = (0, 0)
        else:
            self.__position = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

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
        if self.__size is not None and self.__position is not None:
            for k in range(0, list(self.__position)[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, list(self.__position)[0]):
                    print(" ",end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
