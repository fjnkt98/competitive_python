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
    R, C = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[int]] = [
        [0 if i == j else 1 << 60 for j in range(N + 1)] for i in range(N + 1)
    ]

    R = [0] + R
    C = [0] + C

    for i in range(1, N):
        dp[i][i + 1] = R[i] * R[i + 1] * C[i + 1]

    for l in range(2, N + 1):
        for i in range(1, N - l + 1):
            j: int = i + l
            for k in range(i, j + 1):
                dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k][j] + R[i] * R[k] * C[j])

    print(dp[1][N])


if __name__ == "__main__":
    main()
