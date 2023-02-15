#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """Base Class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects