#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(0, cols):
        for r in range(0, rows):
            if r != rows - 1:
                print("{:d".format(matrix[i][r]), end=" ")
            if r == rows - 1:
                print("{:d}".format(matrix[i][r]), end="\n")
