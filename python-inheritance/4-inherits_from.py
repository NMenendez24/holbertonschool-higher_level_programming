#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Function that checks"""
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
