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

    mod: int = 998244353

    dp: List[List[int]] = [[0 for j in range(10)] for i in range(N + 1)]
    dp[1] = [1 for j in range(10)]
    for i in range(2, N + 1):
        for j in range(1, 10):
            if j > 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] += dp[i - 1][j]

            dp[i][j] %= mod

    print(sum(dp[N]) % mod)


if __name__ == "__main__":
    main()
