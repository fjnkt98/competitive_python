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
    A: List[int] = [int(a) - 1 for a in input().split()]

    S: int = len([a for i, a in enumerate(A) if i == a])

    answer: int = S * (S - 1) // 2
    for i, j in enumerate(A):
        if i < j and A[j] == i:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
