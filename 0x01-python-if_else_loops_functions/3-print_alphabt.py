#!/usr/bin/python3
for ascii_alp in range(ord('a'), ord('z') + 1):
    rem = chr(ascii_alp)
    if rem not in ['q', 'e']:
        print(rem, end="")
