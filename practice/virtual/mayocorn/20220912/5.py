from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    N: int = len(S)

    mod: int = 1000000007

    dp: List[List[int]] = [[0 for j in range(13)] for i in range(N)]
    if S[0] == "?":
        for j in range(10):
            dp[0][j] = 1
    else:
        dp[0][int(S[0])] = 1

    for i in range(1, N):
        for j in range(13):
            if S[i] == "?":
                for k in range(10):
                    dp[i][(10 * j + k) % 13] += dp[i - 1][j]
                    dp[i][(10 * j + k) % 13] %= mod
            else:
                dp[i][(10 * j + int(S[i])) % 13] += dp[i - 1][j]
                dp[i][(10 * j + int(S[i])) % 13] %= mod

    print(dp[N - 1][5])


if __name__ == "__main__":
    main()
