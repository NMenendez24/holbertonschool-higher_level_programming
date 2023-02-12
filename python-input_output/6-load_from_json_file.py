#!/usr/bin/python3


"""creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """creates a object from a file"""
    with open(filename, 'r') as f:
        return json.load(f)
