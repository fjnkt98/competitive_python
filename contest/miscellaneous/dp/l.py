from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[0 for j in range(N + 1)] for i in range(N + 1)]

    for l in range(1, N + 1):
        for i in range(N - l + 1):
            j: int = i + l
            dp[i][j] = max(A[i] - dp[i + 1][j], A[j - 1] - dp[i][j - 1])

    print(dp[0][N])


if __name__ == "__main__":
    main()
