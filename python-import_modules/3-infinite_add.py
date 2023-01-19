#!/usr/bin/python3
from add_0 import add
from sys import argv
sum = 0
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    elif len(argv) >= 3:
        for i in range (1, len(argv)):
            sum += int(argv[i])
        print(sum)
