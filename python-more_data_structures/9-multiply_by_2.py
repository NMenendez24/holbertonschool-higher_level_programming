#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i in range(0, len(a_dictionary)):
        key = list(a_dictionary)[i]
        new_dict = update_dictionary(new_dict, key, a_dictionary[key] * 2)
    return new_dict


def update_dictionary(a_dictionary, key, value):
    a_dictionary.__setitem__(key, value)
    return a_dictionary
