#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print(f"{chr(ord(str[i]) - 32)}", end="")
        else:
            print(f"{str[i]}", end="")
    print("")
