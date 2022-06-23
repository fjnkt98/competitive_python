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


def f(x: int, N: int) -> int:
    y: int = N // x
    return y * (y + 1) * x // 2


def main():
    N: int = int(input())
    answer: int = 0
    for i in range(1, N + 1):
        answer += f(i, N)

    print(answer)


if __name__ == "__main__":
    main()
