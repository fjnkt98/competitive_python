from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, A = map(int, input().split())
    X: List[int] = [0] + list(map(int, input().split()))

    M: int = sum(X)
    dp: List[List[List[int]]] = [
        [[0 for k in range(M + 1)] for j in range(N + 1)] for i in range(N + 1)
    ]
    dp[0][0][0] = 1
    for i in range(1, N + 1):
        for j in range(i + 1):
            for k in range(M + 1):
                dp[i][j][k] = dp[i - 1][j][k]

                if k - X[i] >= 0:
                    dp[i][j][k] += dp[i - 1][j - 1][k - X[i]]

    answer: int = 0
    for j in range(1, N + 1):
        for k in range(M + 1):
            q, r = divmod(k, j)
            if r == 0 and q == A:
                answer += dp[N][j][k]

    print(answer)


if __name__ == "__main__":
    main()
