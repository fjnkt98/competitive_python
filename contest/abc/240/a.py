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
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    if a == 1 and b == 10:
        print("Yes")
    elif b - a == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
