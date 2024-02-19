#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print(x)
    except NameError as ne:
        raise NameError(message) from ne
