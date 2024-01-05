#!/usr/bin/python3
def element_at(my_list, idx):
    number = len(my_list)
    if idx < 0 or idx > number:
        return None
    else:
        elem = my_list[idx]
        return elem
