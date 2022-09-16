from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = [int(input()) for i in range(N)]
    M: int = sum(A)

    dp: List[List[int]] = [[0 for j in range(M + 1)] for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] = dp[i - 1][j]
            if j - A[i - 1] >= 0:
                dp[i][j] += dp[i - 1][j - A[i - 1]]

    P: List[int] = [i for i, d in enumerate(dp[N]) if d != 0 and i % 10 != 0]
    if not P:
        print(0)
    else:
        print(max(P))


if __name__ == "__main__":
    main()
