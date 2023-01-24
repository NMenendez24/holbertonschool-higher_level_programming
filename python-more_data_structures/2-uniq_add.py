#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    a = 0
    for i in range(0, len(uniq_list)):
        a += int(uniq_list[i])
    return a
