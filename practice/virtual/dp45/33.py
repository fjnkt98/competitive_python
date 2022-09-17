from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, N = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[int]] = [[1 << 60 for j in range(50000)] for i in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(50000):
            dp[i][j] = dp[i - 1][j]

            if j - A[i - 1] >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - A[i - 1]] + B[i - 1])

    print(min(dp[N][H:]))


if __name__ == "__main__":
    main()
