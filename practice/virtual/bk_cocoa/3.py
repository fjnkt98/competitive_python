from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    X: int = int(input())

    Y: List[int] = []
    i: int = 1
    while i ** 5 <= int(1e15):
        Y.append(i)
        i += 1

    Y.extend([-y for y in Y])
    Y.append(0)
    Y.sort()

    for a, b in itertools.product(Y, repeat=2):
        A: int = a ** 5
        B: int = b ** 5

        if A - B == X:
            print(a, b)
            return


if __name__ == "__main__":
    main()
