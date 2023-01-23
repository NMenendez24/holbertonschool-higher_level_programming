#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for i in range(0, len(s)):
        if s[i] == 'c' or s[i] == 'C':
            s[i] = ''
    return "".join(s)
