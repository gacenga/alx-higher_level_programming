#!/usr/bin/python3


"""function print_square"""


def print_square(size):
    """defines function print_square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    if size == 0:
        print("", end="\n")
    else:
        for i in range(0, size):
            for x in range(0, size):
                print("#", end="")
            print("", end="\n")
