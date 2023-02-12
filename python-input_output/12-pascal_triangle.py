#!/usr/bin/python3
"""Returns a list with a pascal triangle"""


def pascal_triangle(n):
    """Generates the pascal triangle"""
    if n <= 0:
        return [[]]
    else:
        triangle = [[1]]
    for i in range(0, n - 1):
        aux = [1]
        for j in range(1, i + 1):
            aux.append(triangle[i][j] + triangle[i][j - 1])
        aux.append(1)
        triangle.append(aux)
    return triangle
