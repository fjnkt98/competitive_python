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


answer: int = 0


def dfs(prod: int, A: List[List[int]], L: List[int], i: int, N: int, X: int) -> None:
    global answer

    if i == N:
        if prod == X:
            answer += 1
        return

    for a in A[i]:
        dfs(prod * a, A, L, i + 1, N, X)


def main():
    N, X = map(int, input().split())
    L: List[int] = [0] * N
    A: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        L[i], *A[i] = list(map(int, input().split()))

    dfs(1, A, L, 0, N, X)

    print(answer)


if __name__ == "__main__":
    main()
