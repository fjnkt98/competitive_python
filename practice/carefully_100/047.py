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
    A: List[int] = [int(input()) for i in range(N)]

    dp: List[List[int]] = [[0 for j in range(2 * N)] for i in range(2 * N)]

    if N % 2 == 1:
        for i in range(2 * N):
            dp[i][i] = A[i % N]

    for l in range(2, N + 1):
        for i in range(2 * N + 1 - l):
            j: int = i + l - 1

            if l % 2 == N % 2:
                dp[i][j] = max(dp[i + 1][j] + A[i % N], dp[i][j - 1] + A[j % N])
            else:
                if A[i % N] > A[j % N]:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    answer: int = 0
    for i in range(N):
        answer = max(answer, dp[i][i + N - 1])

    print(answer)


if __name__ == "__main__":
    main()
