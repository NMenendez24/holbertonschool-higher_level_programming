#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(0, x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except:
            return
    print("")
    return counter
