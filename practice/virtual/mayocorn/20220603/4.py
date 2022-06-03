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

    count: int = sum(a < 0 for a in A)

    B: List[int] = [abs(a) for a in A]

    if count % 2 == 0:
        print(sum(B))
    else:
        print(sum(B) - 2 * min(B))


if __name__ == "__main__":
    main()
