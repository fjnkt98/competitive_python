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
    A: List[int] = list(map(int, input().split()))
    K: List[int] = [int(input()) for i in range(Q)]

    R: List[int] = [a - (i + 1) for i, a in enumerate(A)]
    for k in K:
        i: int = bisect.bisect_left(R, k)
        if i == N:
            print(A[i - 1] + (k - R[i - 1]))
        else:
            print(A[i] - 1 - (R[i] - k))


if __name__ == "__main__":
    main()
