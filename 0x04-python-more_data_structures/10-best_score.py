#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_dict = a_dictionary.copy()
        sorted_stuff = sorted(a_dictionary.items(), key=lambda x: x[1])
        newest_dict = dict(sorted_stuff)
        last_key = list(newest_dict.keys())[-1]
        last_value = newest_dict[last_key]
        return last_value
    else:
        return None
