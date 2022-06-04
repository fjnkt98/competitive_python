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
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    selected: List[bool] = [False] * N
    B: List[List[int]] = []
    for i in range(N - K):
        if selected[i]:
            continue
        R: List[int] = []
        j: int = 0
        while i + j < N:
            R.append(A[i + j])
            selected[i + j] = True
            j += K

        B.append(R)

    for i in range(len(B)):
        B[i].sort()

    C: List[int] = [-1] * N
    for i in range(N):
        if i < len(B):
            k: int = 0
            for b in B[i]:
                C[i + k] = b
                k += K

        else:
            if C[i] == -1:
                C[i] = A[i]

    if tuple(sorted(A)) == tuple(C):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
