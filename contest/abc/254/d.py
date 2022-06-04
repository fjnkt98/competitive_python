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

    answer: int = 0
    for i in range(1, N + 1):
        k: int = i
        d: int = 2
        while d ** 2 <= k:
            while k % (d ** 2) == 0:
                k //= d ** 2
            d += 1

        d = 1
        while k * d ** 2 <= N:
            answer += 1
            d += 1

    print(answer)


if __name__ == "__main__":
    main()
