#!/usr/bin/python3


"""Define a class student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for i in attrs:
            for j, k in self.__dict__.items():
                if j == i:
                    dictionary[k] = k
