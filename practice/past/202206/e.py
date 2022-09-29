from typing import *
import collections
import itertools
import bisect
import math


def f(n: int) -> int:
    return 1 + (n - 1) ** 2


def main():
    N: int = int(input())

    left: int = 0
    right: int = N
    while right - left > 1:
        mid: int = (right + left) >> 1

        if f(mid) <= N:
            left = mid
        else:
            right = mid

    a: int = left
    v: int = f(left)

    l: int = 1 + 2 * (a - 1)
    i: int = N - v + 1
    if i < l // 2:
        print(a - (i - 1))
    else:
        print(1 + (i - l // 2 - 1))


if __name__ == "__main__":
    main()
