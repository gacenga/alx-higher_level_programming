#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv
    num = 0
    numarg = len(argument) - 1
    for i in range(1, numarg + 1):
        num += int(argument[i])
    print(num)
