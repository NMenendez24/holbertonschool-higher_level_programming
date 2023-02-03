#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Define a rectangle"""
    __width = None
    __height = None

    """Init"""
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if width is None:
            width = 0
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
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
        self.__height = value

    @width.setter
    def width(self, value):
        self.__width = value
