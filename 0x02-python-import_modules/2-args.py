#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    num = len(arguments) - 1
    if num == 0:
        print("{} arguments.".format(num))
    elif num > 0:
        if num == 1:
            print("{} argument:".format(num))
        elif num > 1:
            print("{} arguments:".format(num))
        for i in range(1, num + 1):
            print(f"{i}: {arguments[i]}")
