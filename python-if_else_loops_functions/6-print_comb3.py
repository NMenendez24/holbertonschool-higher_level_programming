#!/usr/bin/python3
for i in range(0, 10):
    print("0{}, ".format(i), end="")
for i in range(10, 100):
    if (i % 10 > i / 10) and (i % 10 != i / 10):
        print("{}".format(i), end="")
        if i != 89:
            print(", ", end="")
        else:
            print("")
