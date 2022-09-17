from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, X = map(int, input().split())
    W, V = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    M: int = sum(V)

    dp: List[List[int]] = [[1 << 60 for j in range(M + 1)] for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] = dp[i - 1][j]

            if j - V[i - 1] >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - V[i - 1]] + W[i - 1])

    print(max([i for i, d in enumerate(dp[N]) if d <= X]))


if __name__ == "__main__":
    main()
