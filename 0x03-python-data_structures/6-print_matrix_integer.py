#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for index, number in enumerate(row):
            print("{:d}".format(number), end="")
            if index < len(row) - 1:
                print(" ", end="")
        print()
