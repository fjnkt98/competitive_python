from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A, B, C, D, E, F = map(int, input().split())
    if M != 0:
        X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))
    else:
        X = []
        Y = []
    obstacles: Set[Tuple[int, int]] = {(x, y) for x, y in zip(X, Y)}

    mod: int = 998244353
    dp: List[List[List[int]]] = [
        [[0] * (N + 1) for j in range(N + 1)] for i in range(N + 1)
    ]

    dp[0][0][0] = 1
    answer: int = 0

    for i, j, k in itertools.product(range(N + 1), repeat=3):
        if i + j + k > N:
            continue

        x: int = A * i + C * j + E * k
        y: int = B * i + D * j + F * k
        if (x, y) in obstacles:
            continue

        if i - 1 >= 0:
            dp[i][j][k] += dp[i - 1][j][k]
        if j - 1 >= 0:
            dp[i][j][k] += dp[i][j - 1][k]
        if k - 1 >= 0:
            dp[i][j][k] += dp[i][j][k - 1]

        dp[i][j][k] %= mod

        if i + j + k == N:
            answer += dp[i][j][k]
            answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
