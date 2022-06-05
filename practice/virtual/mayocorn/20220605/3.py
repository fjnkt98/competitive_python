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
    A, B, W = map(int, input().split())

    W *= 1000

    minimum: int = 1 << 60
    maximum: int = 0

    for i in range(1, 2000000):
        if A * i <= W <= B * i:
            minimum = min(minimum, i)
            maximum = max(maximum, i)

    if maximum == 0:
        print("UNSATISFIABLE")
    else:
        print(minimum, maximum)


if __name__ == "__main__":
    main()
