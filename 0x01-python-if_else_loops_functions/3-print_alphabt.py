#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) is not 'e' and chr(a) is not 'q':
        print("{}".format(chr(a)), end="")
