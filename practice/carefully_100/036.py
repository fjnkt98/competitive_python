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
    N, M = map(int, input().split())
    V, W = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[int] = [[0] * (M + 1) for i in range(N + 1)]
    for i, j in itertools.product(range(1, N + 1), range(M + 1)):
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

        if j - W[i - 1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j - W[i - 1]] + V[i - 1])

    print(dp[N][M])


if __name__ == "__main__":
    main()
