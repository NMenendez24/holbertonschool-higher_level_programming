#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = ord(i)
        if letter >= 97 and letter <= 122:
            letter -= 32
        print("{}".format(chr(letter)), end="")
    print("")