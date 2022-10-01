from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    mod: int = 1000000007
    print((pow(10, N, mod) - pow(9, N, mod) - pow(9, N, mod) + pow(8, N, mod)) % mod)


if __name__ == "__main__":
    main()
