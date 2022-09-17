from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[0 for j in range(21)] for i in range(N - 1)]
    dp[0][A[0]] = 1
    for i in range(1, N - 1):
        for j in range(21):
            if 0 <= j - A[i] <= 20:
                dp[i][j] += dp[i - 1][j - A[i]]
            if 0 <= j + A[i] <= 20:
                dp[i][j] += dp[i - 1][j + A[i]]

    print(dp[-1][A[-1]])


if __name__ == "__main__":
    main()
