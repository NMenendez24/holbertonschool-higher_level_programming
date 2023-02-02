#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """Function that prints the square"""
    if type(size) == float and size < 0:
        raise TypeError("suze must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
            print("")
    else:
        if size is not None:
            for i in range(0, size):
                for k in range(0, size):
                    print("#", end="")
                print("")
