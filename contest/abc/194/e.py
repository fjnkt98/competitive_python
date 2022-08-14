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
import random


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    if N == 1:
        print(1 if A[0] == 0 else 0)
        return

    X: List[int] = [0] * N
    for a in A[:M]:
        X[a] += 1

    answer: int = min([N] + [i for i, x in enumerate(X) if x == 0])
    for i in range(1, N - M + 1):
        left: int = A[i - 1]
        right: int = A[i + M - 1]
        X[left] -= 1
        X[right] += 1

        if X[left] == 0:
            answer = min(answer, left)

    print(answer)


if __name__ == "__main__":
    main()
