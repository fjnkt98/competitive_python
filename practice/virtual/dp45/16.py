from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    P: List[float] = list(map(float, input().split()))

    dp: List[List[int]] = [[0 for j in range(N + 1)] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1] * P[i - 1]

            dp[i][j] += dp[i - 1][j] * (1 - P[i - 1])

    print(sum(dp[N][N // 2 + 1 :]))


if __name__ == "__main__":
    main()
