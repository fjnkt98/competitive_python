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
    answer: List[int] = []
    while True:
        N: int = int(input())
        if N == 0:
            break
        W: List[int] = list(map(int, input().split()))

        dp: List[List[int]] = [[0 for j in range(N + 2)] for i in range(N)]
        for i in range(N - 1):
            dp[i][i + 2] = 2 if abs(W[i] - W[i + 1]) <= 1 else 0

        for l in range(2, N + 1):
            for i in range(N - l + 1):
                j: int = i + l

                if dp[i + 1][j - 1] == l - 2 and abs(W[i] - W[j - 1]) <= 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)

                dp[i][j] = max(
                    dp[i][j], *[dp[i][k] + dp[k][j] for k in range(i + 1, j)]
                )

        answer.append(dp[0][N])

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
