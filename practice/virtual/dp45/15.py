from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    X, Y = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[List[int]]] = [
        [[1 << 60 for k in range(Y + 1)] for j in range(X + 1)] for i in range(N + 1)
    ]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

                dp[i + 1][min(X, j + A[i])][min(Y, k + B[i])] = min(
                    dp[i + 1][min(X, j + A[i])][min(Y, k + B[i])],
                    dp[i][j][k] + 1,
                )

    if dp[N][X][Y] == 1 << 60:
        print(-1)
    else:
        print(dp[N][X][Y])


if __name__ == "__main__":
    main()
