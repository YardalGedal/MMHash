# Script Name : MMHash.py
# Author : Yardal Gedal
# Created : 08 October 2016
# Last Modified	: 27 August 2017
# Version : 8.0.0

# Modifications	: 8.0.3

# Description : Hashing input string

from functools import reduce

class MMHash:
    def __init__(self, S):
        x = 256
        L = (x // 8) * 2
        f = lambda ords: str(hex(reduce(lambda x, y: int(x)*int(y),  ords) + int("".join(ords))))
        S = S + str(x)
        while len(S) < L:
            S = f([str((n + x) * x) + str(ord(i)) for n, i in enumerate(S)])
        print(S[-L//2:])
