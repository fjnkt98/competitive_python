from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    mod: int = 998244353

    dp: List[List[int]] = [[0 for j in range(10)] for i in range(N)]
    for j in range(1, 10):
        dp[0][j] = 1

    for i in range(1, N):
        for j in range(1, 10):
            dp[i][j] += dp[i - 1][j]
            if j != 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j != 9:
                dp[i][j] += dp[i - 1][j + 1]

            dp[i][j] %= mod

    print(sum(dp[N - 1]) % mod)


if __name__ == "__main__":
    main()
