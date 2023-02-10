#!/usr/bin/python3
"""Define a class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__height * self.__width
