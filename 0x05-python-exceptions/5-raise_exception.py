#!/usr/bin/python3
def raise_exception():
    try:
        "H" + 5
    except TypeError as te:
        raise te
