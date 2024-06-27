#!/usr/bin/python3
"""

reads and prints ile

"""
def read_file(filename=""):
    """ reads file """
    with open(filename, encoding="utf-8") as file:
        k = file.read()
        print(k, end="")
