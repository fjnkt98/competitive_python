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
    N, X = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    answer: int = 1 << 60
    C: List[int] = list(itertools.accumulate([a + b for a, b in zip(A, B)]))
    D: List[int] = [1 << 60] * N
    D[0] = B[0]
    for i in range(1, N):
        D[i] = min(D[i - 1], B[i])
    time: List[int] = [1 << 60] * N
    for i, (a, b, c, d) in enumerate(zip(A, B, C, D)):
        target: int = X - i - 1
        time[i] = c + target * d

    print(min(time))


if __name__ == "__main__":
    main()
