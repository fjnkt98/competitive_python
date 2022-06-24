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
    N: int = int(input())

    if N < 42:
        print("AGC" + str(N).zfill(3))
    else:
        print("AGC" + str(N + 1).zfill(3))


if __name__ == "__main__":
    main()
