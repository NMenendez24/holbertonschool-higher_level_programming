#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list=[]
    set_1_list = list(set_1)
    set_2_list = list(set_2)
    for i in range(0, len(set_1)):
        for j in range(0, len(set_2)):
            if set_1_list[i] == set_2_list[j]:
                new_list.append(set_1_list[i])
    return new_list
