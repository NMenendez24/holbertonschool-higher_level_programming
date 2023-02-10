#!/usr/bin/python3
"""Creates a class called square that inherits from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
