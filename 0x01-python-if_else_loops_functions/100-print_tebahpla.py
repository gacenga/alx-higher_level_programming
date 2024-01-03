#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') -1, -1):
    if (alpha % 2) == 0:
        newalpha = chr(alpha)
    elif (alpha % 2) != 0:
        newalpha = chr(alpha - ord('a') + ord('A'))
    print("{}".format(newalpha), end="")
