#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = a_dictionary.copy()
    sorted_list = sorted(new_dict.items())
    newest_dict = dict(sorted_list)
    for key, value in newest_dict.items():
        print("{}: {}".format(key, value))
