#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_list = list(roman_string)
    a = 0
    for i in range(0, len(roman_list)):
        if roman_list[i] == 'I':
            roman_list[i] = 1
        if roman_list[i] == 'V':
            roman_list[i] = 5
        if roman_list[i] == 'X':
            roman_list[i] = 10
        if roman_list[i] == 'L':
            roman_list[i] = 50
        if roman_list[i] == 'C':
            roman_list[i] = 100
        if roman_list[i] == 'D':
            roman_list[i] = 500
        if roman_list[i] == 'M':
            roman_list[i] = 1000
    for i in range(0, len(roman_list)):
        if i + 1 < len(roman_list):
            if int(roman_list[i]) >= int(roman_list[i + 1]):
                a += int(roman_list[i])
            else:
                a -= int(roman_list[i])
        if i == len(roman_list) - 1:
            a += int(roman_list[i])
    return a
