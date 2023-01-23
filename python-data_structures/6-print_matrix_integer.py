#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print("")
        return
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print("{:d}".format(matrix[i][j]), end="")
            if j < (len(matrix) - 1):
                print(" ", end="")
            else:
                print("")
