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
    A: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[0] * 21 for i in range(N)]
    dp[0][A[0]] = 1
    for i in range(1, N):
        for j in range(21):
            if j - A[i] >= 0:
                dp[i][j] += dp[i - 1][j - A[i]]

            if j + A[i] <= 20:
                dp[i][j] += dp[i - 1][j + A[i]]

    print(dp[-2][A[-1]])


if __name__ == "__main__":
    main()
