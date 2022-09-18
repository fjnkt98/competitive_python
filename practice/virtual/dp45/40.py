from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A: List[int] = [0] * M
    B: List[int] = [0] * M
    C: List[List[int]] = [[] for i in range(M)]
    for i in range(M):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
        C[i] = list(map(lambda x: int(x) - 1, input().split()))

    for i in range(M):
        X: int = 0
        for c in C[i]:
            X |= 1 << c

        B[i] = X

    dp: List[List[int]] = [1 << 60 for i in range(1 << N)]
    dp[0] = 0
    for bits in range(1 << N):
        for i in range(M):
            dp[bits | B[i]] = min(dp[bits | B[i]], dp[bits] + A[i])

    answer: int = dp[(1 << N) - 1]
    if answer == 1 << 60:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
