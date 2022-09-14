from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    dp: List[List[bool]] = [[False] * 2 for i in range(N)]
    dp[0] = [True, True]
    for i in range(1, N):
        if abs(A[i] - A[i - 1]) <= K and (dp[i - 1][0]):
            dp[i][0] = True
        if abs(A[i] - B[i - 1]) <= K and (dp[i - 1][1]):
            dp[i][0] = True

        if abs(B[i] - A[i - 1]) <= K and (dp[i - 1][0]):
            dp[i][1] = True
        if abs(B[i] - B[i - 1]) <= K and (dp[i - 1][1]):
            dp[i][1] = True

    if dp[N - 1][0] or dp[N - 1][1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
