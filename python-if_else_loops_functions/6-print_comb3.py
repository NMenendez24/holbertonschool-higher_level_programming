#!/usr/bin/python3
for i in range(0, 100):
    if ((i % 10 > i / 10) and (i % 10 != i / 10)) and i != 89:
        print("%02d, " % (i), end="")
    elif i == 89:
        print("89")
