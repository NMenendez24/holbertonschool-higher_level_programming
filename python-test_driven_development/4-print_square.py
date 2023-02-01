#!/usr/bin/python3
def print_square(size):
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

###################################################


print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
"""
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
"""