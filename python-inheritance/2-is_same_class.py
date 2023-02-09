#!/usr/bin/python3
"""Returns true if the object is from the selected class"""


def is_same_class(obj, a_class):
    """Function that returns"""
    return issubclass(a_class, type(obj))
