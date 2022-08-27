from typing import *
import collections
import itertools
import bisect
import math

import random


def main():
    N: int = int(input())
    mod: int = 998244353

    M: int = N

    while M < 0:
        M += mod

    x: int = M % mod
    print(x)


if __name__ == "__main__":
    main()
