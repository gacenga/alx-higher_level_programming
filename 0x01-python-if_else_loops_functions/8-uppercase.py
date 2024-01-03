#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upperchar = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upperchar), end="")
        else:
            print("{}".format(char), end="")
    print()
