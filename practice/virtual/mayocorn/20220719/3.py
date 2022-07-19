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
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if (r1, c1) == (r2, c2):
        print(0)
        return

    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    for dr in [-3, -2, -1, 1, 2, 3]:
        r: int = r1 + dr
        if r + c1 == r2 + c2 or r - c1 == r2 - c2 or abs(r - r2) + abs(c1 - c2) <= 3:
            print(2)
            return

    for dc in [-3, -2, -1, 1, 2, 3]:
        c: int = c1 + dc
        if r1 + c == r2 + c2 or r1 - c == r2 - c2 or abs(r1 - r2) + abs(c - c2) <= 3:
            print(2)
            return

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return

    print(3)


if __name__ == "__main__":
    main()
