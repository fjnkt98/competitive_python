from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    dp: List[List[int]] = [[0 for j in range(N)] for i in range(N)]
    dp[0][0] = A[0][0]
    for i in range(1, N):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j] + A[i][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + A[i][j])

    print(max(dp[N - 1]))


if __name__ == "__main__":
    main()
