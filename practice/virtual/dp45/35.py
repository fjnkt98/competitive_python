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
        dp[0] = [1] * 10 + [0] * 3
    else:
        dp[0][int(S[0])] = 1

    for i in range(N - 1):
        for j in range(13):
            dp[i][j] %= mod
            if S[i + 1] == "?":
                for k in range(10):
                    dp[i + 1][(10 * j + k) % 13] += dp[i][j]
            else:
                dp[i + 1][(10 * j + int(S[i + 1])) % 13] += dp[i][j]

    print(dp[-1][5] % mod)


if __name__ == "__main__":
    main()
