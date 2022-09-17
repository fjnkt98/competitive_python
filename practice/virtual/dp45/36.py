from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    T: str = input()

    N: int = len(S)
    M: int = len(T)
    S = " " + S
    T = " " + T

    dp: List[List[int]] = [[0 for j in range(M + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if S[i] == T[j]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1

    print(dp[N][M])


if __name__ == "__main__":
    main()
