#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    set_1_list = list(set_1)
    set_2_list = list(set_2)
    new_list = set(set_1_list) ^ set(set_2_list)
    return new_list

#Also works this way

"""
def only_diff_elements(set_1, set_2):
    new_list = []
    # set_1_list = list(set_1)
    # set_2_list = list(set_2)
    new_list = set(set_1) ^ set(set_2)
    return new_list
"""
