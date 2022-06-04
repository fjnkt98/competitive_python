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
    A: List[List[int]] = [[0 for j in range(i + 1)] for i in range(N)]

    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

    for a in A:
        print(*a)


if __name__ == "__main__":
    main()
