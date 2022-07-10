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
    x1, y1, x2, y2 = map(int, input().split())

    dx: List[int] = [2, 1, -1, -2, -2, -1, 1, 2]
    dy: List[int] = [1, 2, 2, 1, -1, -2, -2, -1]

    P: List[Tuple[int, int]] = []
    for i in range(8):
        x: int = x1 + dx[i]
        y: int = y1 + dy[i]

        P.append((x, y))

    Q: List[Tuple[int, int]] = []
    for i in range(8):
        x: int = x2 + dx[i]
        y: int = y2 + dy[i]

        Q.append((x, y))

    for p, q in itertools.product(P, Q):
        if p == q:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
