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
    A, B, C = map(int, input().split())

    answer: float = math.pi * (A + B + C) ** 2

    X: List[int] = sorted([A, B, C])
    if X[2] > X[0] + X[1]:
        answer -= math.pi * (X[2] - (X[0] + X[1])) ** 2

    print(answer)


if __name__ == "__main__":
    main()
