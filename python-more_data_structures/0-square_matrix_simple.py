#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    for i in range(0, 3):
        for j in range(0, 3):
            new_matrix[i][j] = new_matrix[i][j] ** 2
    return new_matrix
