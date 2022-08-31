from typing import *
import collections
import itertools
import bisect
import math


def main():
    A, op, B = input().split()
    a: int = int(A)
    b: int = int(B)

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)


if __name__ == "__main__":
    main()
