#!/usr/bin/python3
"""Indent a text in ., ? and :"""


def text_indentation(text):
    """Function that indents"""
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in {'.', '?', ':'}:
            print(text[i], end="")
            print("\n\n", end="")
            while text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end="")
        i += 1

