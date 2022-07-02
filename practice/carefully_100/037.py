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
    C: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[1 << 60] * (N + 1) for i in range(M + 1)]
    dp[0][0] = 0
    for i, j in itertools.product(range(1, M + 1), range(N + 1)):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])

        if j - C[i - 1] >= 0:
            dp[i][j] = min(dp[i][j], dp[i][j - C[i - 1]] + 1)

    print(dp[M][N])


if __name__ == "__main__":
    main()
