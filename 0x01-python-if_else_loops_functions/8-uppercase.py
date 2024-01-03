#!/usr/bin/python3
def uppercase(str):
    cont = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            cont += chr(ord(char) - ord('a') + ord('A'))
        else:
            cont += char
    print("{}".format(cont), end="\n")
