#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_string = ''
    for i in range(0, length):
        letter = ord(my_string[i])
        if letter != ord('c') and letter != ord('C'):
            new_string += my_string[i]
    return new_string
