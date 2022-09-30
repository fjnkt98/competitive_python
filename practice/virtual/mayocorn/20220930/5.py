from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, R = map(int, input().split())
    r: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    dp: List[List[int]] = [
        [0 if i == j else 1 << 60 for j in range(N)] for i in range(N)
    ]

    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dp[a][b] = c
        dp[b][a] = c

    for k, i, j in itertools.product(range(N), repeat=3):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answer: int = 1 << 60
    for route in itertools.permutations(r):
        cost: int = 0
        for i, j in zip(route[:-1], route[1:]):
            cost += dp[i][j]

        answer = min(answer, cost)

    print(answer)


if __name__ == "__main__":
    main()
