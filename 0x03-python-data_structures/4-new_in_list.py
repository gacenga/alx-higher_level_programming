#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    number = len(my_list)
    new_list = my_list[:]
    if idx < 0 or idx > number:
        return my_list
    else:
        new_list[idx] = element
        return new_list
