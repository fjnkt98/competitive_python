from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: str = " " + input()
    T: str = " atcoder"
    mod: int = 1000000007

    dp: List[List[int]] = [[1 if j == 0 else 0 for j in range(8)] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, 8):
            if S[i] == T[j]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

            dp[i][j] %= mod

    print(dp[N][7] % mod)


if __name__ == "__main__":
    main()
