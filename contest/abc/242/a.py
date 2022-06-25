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
    A, B, C, X = map(int, input().split())

    if X <= A:
        print(1.0)
    elif X <= B:
        print(C / (B - A))
    else:
        print(0)


if __name__ == "__main__":
    main()
