from typing import *
import collections
import itertools
import bisect
import math
import sys


input = sys.stdin.readline


def main():
    H, W, K = map(int, input().split())
    C: List[List[int]] = [[0 for j in range(W + 1)] for i in range(H + 1)]
    for i in range(K):
        r, c, v = map(int, input().split())
        C[r][c] = v

    dp: List[List[List[int]]] = [[[0] * 4 for j in range(W + 1)] for i in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j][0] = max(dp[i - 1][j])
            dp[i][j][1] = max(dp[i - 1][j]) + C[i][j]

            for k in range(4):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + C[i][j])

    print(max(dp[H][W]))


if __name__ == "__main__":
    main()
