#!/usr/bin/python3


"""Returns a python object as a json string"""


import json


def from_json_string(my_str):
    """Returns a object froma JSOn string"""
    return json.loads(my_str)
