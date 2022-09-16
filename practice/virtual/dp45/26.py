from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    mod: int = 998244353

    dp: List[List[int]] = [[0 for j in range(10)] for i in range(N)]
    dp[0][A[0]] = 1
    for i in range(N - 1):
        for j in range(10):
            dp[i][j] %= mod
            dp[i + 1][(A[i + 1] + j) % 10] += dp[i][j]
            dp[i + 1][(A[i + 1] * j) % 10] += dp[i][j]

    for K in range(10):
        print(dp[N - 1][K] % mod)


if __name__ == "__main__":
    main()
