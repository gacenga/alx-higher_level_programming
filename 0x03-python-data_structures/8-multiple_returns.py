#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        charac = None
        tuple = length, charac
        return tuple
    elif length > 0:
        charac = sentence[0]
        tuple = length, charac
        return tuple
