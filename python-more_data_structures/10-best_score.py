#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    a_list = list(a_dictionary)
    max = a_list[0]
    for i in range(0, len(a_dictionary)):
        if a_dictionary[max] < a_dictionary[a_list[i]]:
            max = a_list[i]
    return max
