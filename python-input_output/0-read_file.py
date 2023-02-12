#!/usr/bin/python3


"""Reads a file and prints to stdout"""


def read_file(filename=""):
    """Opens the file and prints"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
