from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W = map(int, input().split())
    C: List[List[int]] = [list(map(int, input().split())) for i in range(10)]
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    dp: List[List[int]] = [
        [0 if i == j else 1 << 60 for j in range(10)] for i in range(10)
    ]
    for i, j in itertools.product(range(10), repeat=2):
        dp[i][j] = C[i][j]

    for k, i, j in itertools.product(range(10), repeat=3):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answer: int = 0
    for i, j in itertools.product(range(H), range(W)):
        if A[i][j] == -1:
            continue
        answer += dp[A[i][j]][1]

    print(answer)


if __name__ == "__main__":
    main()
