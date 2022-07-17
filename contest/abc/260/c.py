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
    N, X, Y = map(int, input().split())

    answer: int = 0
    red: List[int] = [0] * (N)
    red[0] = 1
    blue: List[int] = [0] * (N)

    for i in range(N - 1):
        red[i + 1] += red[i]
        blue[i] += red[i] * X
        red[i] = 0

        red[i + 1] += blue[i]
        blue[i + 1] += blue[i] * Y
        blue[i] = 0

    print(blue[-1])


if __name__ == "__main__":
    main()
