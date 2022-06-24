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
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    answer: List[List[str]] = [
        ["." for j in range(S - R + 1)] for i in range(Q - P + 1)
    ]

    for i in range(Q - P + 1):
        for j in range(S - R + 1):
            k: int = i + P
            l: int = j + R

            if abs(k - A) == abs(l - B):
                answer[i][j] = "#"

    for a in answer:
        print(*a, sep="")


if __name__ == "__main__":
    main()
