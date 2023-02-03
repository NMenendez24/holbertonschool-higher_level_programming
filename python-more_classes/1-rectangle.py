#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Define a rectangle"""
    __width = None
    __height = None

    """Init"""
    def __init__(self, width=0, height=0):
        if width is None:
            width = 0
        else:
            self.__width = width
        if height is None:
            height = 0
        else:
            self.__height = height

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

######


Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)