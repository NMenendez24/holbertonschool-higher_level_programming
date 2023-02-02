#!/usr/bin/python3
"""Divides a matrix by integer"""


def matrix_divided(matrix, div):
    """Function that divides"""
    new_matrix = list(map(list, matrix))
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(0, len(matrix)):
        if i + 1 < len(matrix):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix \
must have the same size")
        for j in range(0, len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix
