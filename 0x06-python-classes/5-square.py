#!/usr/bin/python3


"""class square"""


class Square:
    """defines square"""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("", end="\n")
        else:
            for i in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                print("", end="\n")
