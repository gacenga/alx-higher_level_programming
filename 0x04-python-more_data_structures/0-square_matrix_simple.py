#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0] * len(row) for row in matrix]
    for i in range(len(matrix)):
        for m in range(len(matrix[i])):
            new_matrix[i][m] = matrix[i][m] ** 2
    return new_matrix
