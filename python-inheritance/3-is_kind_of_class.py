#!/usr/bin/python3
"""Returns True if the object is from the specified class or inherited"""


def is_kind_of_class(obj, a_class):
    """Checks if the obj is instance of a_class"""

    return isinstance(obj, a_class)
