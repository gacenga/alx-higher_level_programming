#!/usr/bin/python3
def safe_print_division(a, b):
    x = None
    try:
        x = a/b
    except (ZeroDivisionError, ArithmeticError, ValueError, TypeError):
        pass
    finally:
        if x:
            print("Inside result:{}".format(x), end="\n")
            return x
        else:
            print("Inside result:{}".format("None"), end="\n")
            return None
