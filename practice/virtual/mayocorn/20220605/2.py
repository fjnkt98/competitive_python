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
    P: List[List[str]] = [input().split() for i in range(N)]

    S: Set[str] = set()
    O: List[Tuple[int, int]] = []

    for i, (s, t) in enumerate(P):
        if s in S:
            continue

        O.append((-int(t), i))
        S.add(s)

    O.sort()
    print(O[0][1] + 1)


if __name__ == "__main__":
    main()
