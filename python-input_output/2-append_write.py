#!/usr/bin/python3


"""Opens a file and appends the text to the end"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
