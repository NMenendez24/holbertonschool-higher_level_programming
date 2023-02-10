#!/usr/bin/python3
"""Define a class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        if BaseGeometry.integer_validator("width", width):
            __width = width
        if BaseGeometry.integer_validator("height", height):
            __height = height
