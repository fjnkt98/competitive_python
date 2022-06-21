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
    A: List[int] = list(map(int, input().split()))

    grid = collections.deque([0] * 4)

    P: int = 0
    for a in A:
        grid[0] = 1
        for _ in range(a):
            grid.appendleft(0)
            P += grid.pop()

    print(P)


if __name__ == "__main__":
    main()
