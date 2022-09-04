from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[-(1 << 60) for j in range(M + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j]
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + j * A[i - 1])

    print(dp[N][M])


if __name__ == "__main__":
    main()
