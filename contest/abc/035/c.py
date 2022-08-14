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
    N, Q = map(int, input().split())
    L, R = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    A: List[int] = [0] * (N + 1)
    for l, r in zip(L, R):
        A[l - 1] += 1
        A[r] -= 1

    A = [a % 2 for a in itertools.accumulate(A)][:-1]
    print("".join(map(str, A)))


if __name__ == "__main__":
    main()
