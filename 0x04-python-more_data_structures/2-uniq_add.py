#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for m in range(0, len(my_list)):
        if my_list[m] not in new_list:
            i = my_list[m]
            new_list.append(i)
    num = 0
    for i in new_list:
        num += i
    return num
