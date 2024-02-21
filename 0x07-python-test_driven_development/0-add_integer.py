#!/usr/bin/python3


"""integer addition function"""


def add_integer(a, b=98):
    """Returns adddition of a and b

       Floats are cated to integers before addition

       Raises:
           TypeError when a or b are not either integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    x = int(a)
    y = int(b)
    return x + y
