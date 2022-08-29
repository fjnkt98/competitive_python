from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    dp: List[List[int]] = [[0 for j in range(N)] for i in range(61)]
    for j in range(N):
        dp[0][j] = A[j]

    for i in range(1, 61):
        for j in range(N):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    answer: int = 0
    i: int = 0
    while K:
        if K & 1:
            answer = dp[i][answer]

        K >>= 1
        i += 1

    print(answer + 1)


if __name__ == "__main__":
    main()
