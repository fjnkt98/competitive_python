from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: str = input()
    K: int = int(input())

    X: int = len(N)

    dp: List[List[List[int]]] = [[[0, 0] for j in range(K + 2)] for i in range(X + 1)]
    dp[0][0][0] = 1
    for i in range(X):
        for j in range(K + 1):
            dp[i + 1][j][1] += dp[i][j][1]
            for d in range(1, 10):
                dp[i + 1][j + 1][1] += dp[i][j][1]

            if int(N[i]) != 0:
                dp[i + 1][j][1] += dp[i][j][0]
            for d in range(1, int(N[i])):
                dp[i + 1][j + 1][1] += dp[i][j][0]

            if int(N[i]) != 0:
                dp[i + 1][j + 1][0] = dp[i][j][0]
            else:
                dp[i + 1][j][0] = dp[i][j][0]

    print(dp[X][K][0] + dp[X][K][1])


if __name__ == "__main__":
    main()
