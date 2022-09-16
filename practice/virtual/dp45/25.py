from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: List[str] = [""] + [input() for i in range(N)]

    dp: List[List[List[int]]] = [[[0] * 2 for j in range(2)] for i in range(N + 1)]
    dp[0][0][0] = 1
    dp[0][1][1] = 1
    for i in range(1, N + 1):
        if S[i] == "AND":
            dp[i][1][1] += dp[i - 1][0][1] + dp[i - 1][1][1]
            dp[i][1][0] += dp[i - 1][0][0] + dp[i - 1][1][0]
            dp[i][0][1] = 0
            dp[i][0][0] += (
                dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][1][0] + dp[i - 1][1][1]
            )
        else:
            dp[i][1][1] += (
                dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][1][0] + dp[i - 1][1][1]
            )
            dp[i][1][0] = 0
            dp[i][0][1] += dp[i - 1][0][1] + dp[i - 1][1][1]
            dp[i][0][0] += dp[i - 1][0][0] + dp[i - 1][1][0]

    print(dp[N][0][1] + dp[N][1][1])


if __name__ == "__main__":
    main()
