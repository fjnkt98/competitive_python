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
    N, M, X, T, D = map(int, input().split())

    tall: List[int] = [0] * (N + 1)
    tall[N] = T

    for i in range(N, -1, -1):
        if i >= X:
            tall[i] = T
        else:
            tall[i] = tall[i + 1] - D

    print(tall[M])


if __name__ == "__main__":
    main()
