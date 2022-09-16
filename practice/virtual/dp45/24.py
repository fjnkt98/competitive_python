from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    N: int = len(S)
    T: str = "chokudai"
    M: int = len(T)
    mod: int = 1000000007

    S = " " + S
    T = " " + T

    dp: List[List[int]] = [
        [1 if j == 0 else 0 for j in range(M + 1)] for i in range(N + 1)
    ]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if S[i] == T[j]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

            dp[i][j] %= mod

    print(dp[N][M])


if __name__ == "__main__":
    main()
