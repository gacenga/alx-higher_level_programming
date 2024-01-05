#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    number = len(my_list)
    for i in range(number - 1, 0 - 1, -1):
        print("{}".format(my_list[i]))
