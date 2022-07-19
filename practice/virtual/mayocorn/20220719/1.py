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
    S: str = input().rstrip()

    C = collections.Counter(S)

    for k, v in C.items():
        if v != 1:
            print("no")
            return

    print("yes")


if __name__ == "__main__":
    main()
