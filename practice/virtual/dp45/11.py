from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W = map(int, input().split())
    A: List[List[str]] = [list(input()) for i in range(H)]

    mod: int = 1000000007

    dp: List[List[int]] = [[0 for j in range(W)] for i in range(H)]
    dp[0][0] = 1
    for i, j in itertools.product(range(H), range(W)):
        if A[i][j] == "#":
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]

        dp[i][j] %= mod

    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    main()
