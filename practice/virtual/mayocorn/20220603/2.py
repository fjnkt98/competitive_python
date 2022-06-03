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
    R: List[Tuple[str, int, int]] = [
        (s, -int(p), i + 1)
        for i, (s, p) in enumerate([input().split() for i in range(N)])
    ]
    R.sort()

    for s, p, i in R:
        print(i)


if __name__ == "__main__":
    main()
