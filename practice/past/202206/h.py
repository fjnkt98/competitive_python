from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, A, B = map(int, input().split())
    W, V = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    W = [0] + W
    V = [0] + V

    dp: List[List[list[int]]] = [
        [[0 for j in range(B + 1)] for j in range(A + 1)] for i in range(N + 1)
    ]

    for i in range(1, N + 1):
        for j, k in itertools.product(range(A + 1), range(B + 1)):
            dp[i][j][k] = dp[i - 1][j][k]

            if j - W[i] >= 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - W[i]][k] + V[i])
            if k - W[i] >= 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - W[i]] + V[i])

    print(dp[N][A][B])


if __name__ == "__main__":
    main()
