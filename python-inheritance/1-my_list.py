#!/usr/bin/python3
"""Creates a class that inherits from list"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Instance Method to print in order"""
        print(sorted(self))
