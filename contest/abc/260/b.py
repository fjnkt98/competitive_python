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
    N, X, Y, Z = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    S = set()

    C = sorted([(-a, i + 1) for i, a in enumerate(A)])
    D = sorted([(-b, i + 1) for i, b in enumerate(B)])
    E = sorted((-(a + b), i + 1) for i, (a, b) in enumerate(zip(A, B)))

    i: int = 0
    while X and i < N:
        a, j = C[i]
        if j in S:
            i += 1
            continue
        S.add(j)
        X -= 1
        i += 1

    i = 0
    while Y and i < N:
        b, j = D[i]
        if j in S:
            i += 1
            continue
        S.add(j)
        Y -= 1
        i += 1

    i = 0
    while Z and i < N:
        ab, j = E[i]
        if j in S:
            i += 1
            continue
        S.add(j)
        Z -= 1
        i += 1

    for a in sorted(list(S)):
        print(a)


if __name__ == "__main__":
    main()
