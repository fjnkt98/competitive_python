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

    dp: List[List[int]] = [[0] * N for i in range(N)]

    if N % 2 == 1:
        for i in range(N):
            dp[i][i] = A[i]

    for l in range(1, N):
        for i in range(N):
            j: int = i + l

            if l % 2 == N % 2:
                if A[i] > A[j % N]:
                    dp[i][j % N] = dp[(i + 1) % N][j % N]
                else:
                    dp[i][j % N] = dp[i][(j - 1) % N]
            else:
                dp[i][j % N] = max(
                    dp[(i + 1) % N][j % N] + A[i], dp[i][(j - 1) % N] + A[j % N]
                )

    answer: int = 0
    for i in range(N):
        answer = max(answer, dp[i][(i + N - 1) % N])

    print(answer)


if __name__ == "__main__":
    main()
