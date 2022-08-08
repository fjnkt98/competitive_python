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
    A, B, C, D, E = map(int, input().split())

    count = collections.Counter([A, B, C, D, E])

    if tuple(sorted(count.values())) == (2, 3):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
