#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

# Another way with .update


"""
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key:value})
    return a_dictionary_
"""

# Another way with __setitem__


"""
def update_dictionary(a_dictionary, key, value):
    a_dictionary.__setitem__(key,value)
    return a_dictionary_
"""
