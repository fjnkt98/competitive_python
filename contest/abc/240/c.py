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

    dp: List[List[bool]] = [[False for j in range(20001)] for i in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(20001):
            if j - A[i - 1] >= 0:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]
            if j - B[i - 1] >= 0:
                dp[i][j] = dp[i][j] or dp[i - 1][j - B[i - 1]]

    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
