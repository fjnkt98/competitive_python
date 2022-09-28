from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, X = map(int, input().split())
    W, V = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[int]] = [[0 for j in range(X + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(X + 1):
            dp[i][j] = dp[i - 1][j]

            if j - W[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i - 1]] + V[i - 1])

    print(dp[N][X])


if __name__ == "__main__":
    main()
