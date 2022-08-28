from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    dp: List[List[int]] = [
        [0 if i == j else 1 << 60 for j in range(N)] for i in range(N)
    ]
    for i in range(N):
        dp[i][i] = 0
    for i in range(M):
        a, b, t = map(int, input().split())
        a -= 1
        b -= 1
        dp[a][b] = t
        dp[b][a] = t

    for k, i, j in itertools.product(range(N), repeat=3):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answer: int = 1 << 60
    for i in range(N):
        answer = min(answer, max([d for j, d in enumerate(dp[i]) if i != j]))

    print(answer)


if __name__ == "__main__":
    main()
