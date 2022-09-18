from typing import *
import collections
import itertools
import bisect
import math


def main():
    K: str = list(map(int, input()))
    D: int = int(input())
    mod: int = 1000000007

    N: int = len(K)
    dp: List[List[List[int]]] = [[[0, 0] for j in range(D)] for i in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(D):
            for k in range(10):
                dp[i + 1][(j + k) % D][1] += dp[i][j][1]
                dp[i + 1][(j + k) % D][1] %= mod

            for k in range(K[i]):
                dp[i + 1][(j + k) % D][1] += dp[i][j][0]
                dp[i + 1][(j + k) % D][1] %= mod

            dp[i + 1][(j + K[i]) % D][0] = dp[i][j][0]

    print((dp[N][0][0] + dp[N][0][1] - 1 + mod) % mod)


if __name__ == "__main__":
    main()
