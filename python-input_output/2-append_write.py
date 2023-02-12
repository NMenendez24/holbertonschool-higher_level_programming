#!/usr/bin/python3


"""Opens a file and appends the text to the end"""


def append_write(filename="", text=""):
    """Appends to a file and returns the caracters appended"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
