#!/usr/bin/python3


"""Opens a file and writes in it"""


def write_file(filename="", text=""):
    """Opens the file in write mode and writes in it"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
