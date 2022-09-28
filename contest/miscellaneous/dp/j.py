from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    C = collections.Counter(A)

    dp: List[List[List[float]]] = [
        [[0.0 for k in range(N + 1)] for j in range(N + 1)] for i in range(N + 1)
    ]

    for k, j, i in itertools.product(range(N + 1), repeat=3):
        if i == j == k == 0 or i + j + k > N:
            continue

        p: float = N / (i + j + k)

        dp[i][j][k] = p
        if i > 0:
            dp[i][j][k] += dp[i - 1][j][k] * (i / N) * p
        if j > 0:
            dp[i][j][k] += dp[i + 1][j - 1][k] * (j / N) * p
        if k > 0:
            dp[i][j][k] += dp[i][j + 1][k - 1] * (k / N) * p

    print(dp[C[1]][C[2]][C[3]])


if __name__ == "__main__":
    main()
