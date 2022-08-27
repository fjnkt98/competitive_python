from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N: int = int(input())
    T, X, A = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    time: int = max(T)

    C: List[List[int]] = [[0] * 5 for i in range(time + 1)]
    for t, x, a in zip(T, X, A):
        C[t][x] = a

    dp: List[List[int]] = [[-(1 << 60)] * 5 for i in range(time + 1)]
    dp[0][0] = 0
    for i in range(1, time + 1):
        for j in range(5):
            dp[i][j] = (
                max(dp[i - 1][max(0, j - 1)], dp[i - 1][j], dp[i - 1][min(4, j + 1)])
                + C[i][j]
            )

    print(max(dp[time]))


if __name__ == "__main__":
    main()
