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
    R, C = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(2)]

    print(A[R - 1][C - 1])


if __name__ == "__main__":
    main()
