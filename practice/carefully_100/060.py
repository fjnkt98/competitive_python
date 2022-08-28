from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    if M == 0:
        S: List[int] = []
        T: List[int] = []
        D: List[int] = []
    else:
        S, T, D = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))

    dp: List[List[int]] = [
        [0 if i == j else 1 << 60 for j in range(N)] for i in range(N)
    ]
    for s, t, d in zip(S, T, D):
        dp[s][t] = d

    for k, i, j in itertools.product(range(N), repeat=3):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    if any(map(lambda x: x < 0, [dp[i][i] for i in range(N)])):
        print("NEGATIVE CYCLE")
        return

    for r in dp:
        print(*["INF" if d >= 1 << 59 else d for d in r])


if __name__ == "__main__":
    main()
