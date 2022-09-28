from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[1 << 60 for j in range(N + 1)] for i in range(N + 1)]
    C: List[int] = list(itertools.accumulate(A)) + [0]

    for i in range(N):
        dp[i][i + 1] = 0

    for l in range(2, N + 1):
        for i in range(N - l + 1):
            j: int = i + l
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (C[j - 1] - C[i - 1]))

    print(dp[0][N])


if __name__ == "__main__":
    main()
