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
    D, N = map(int, input().split())
    T: List[int] = [int(input()) for i in range(D)]
    A, B, C = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[int]] = [[0 for j in range(N)] for i in range(D + 1)]

    for i in range(2, D + 1):
        for j, k in itertools.product(range(N), repeat=2):
            if A[j] <= T[i - 1] <= B[j] and A[k] <= T[i - 2] <= B[k]:
                dp[i][j] = max(dp[i][j], abs(C[j] - C[k]) + dp[i - 1][k])

    print(max(dp[D]))


if __name__ == "__main__":
    main()
