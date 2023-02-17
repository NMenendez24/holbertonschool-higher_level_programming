#!/usr/bin/python3
"""Define a class Base"""


import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dicts"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    """
    @classmethod
    def save_to_file(cls, list_objs):
        dict_objs = []
        dict_objs = [lists.to_dictionary() for lists in list_objs]
        with open("{}.json".format(cls.__name__), mode='w',
                encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs))
        """
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to file"""
        dict_objs = []
        if list_objs is not None:
            dict_objs = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_objs))

