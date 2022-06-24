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
    X: str = input().rstrip()

    s: int = sum([int(x) for x in X])

    print((10 * int(X) - s) // 9)


if __name__ == "__main__":
    main()
