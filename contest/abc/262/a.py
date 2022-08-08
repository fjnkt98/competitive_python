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
    Y: int = int(input())
    for y in range(Y, Y + 4):
        if y % 4 == 2:
            print(y)
            return


if __name__ == "__main__":
    main()
