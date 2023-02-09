#!/usr/bin/python3
class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Instance Method to print in order"""
        print(sorted(self))
        return sorted(self)
