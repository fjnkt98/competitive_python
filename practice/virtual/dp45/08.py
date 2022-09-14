from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, X = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    A = [0] + A
    B = [0] + B

    dp: List[List[bool]] = [[False for j in range(20001)] for i in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(20001):
            if dp[i - 1][j - A[i]]:
                dp[i][j] = True
            if dp[i - 1][j - B[i]]:
                dp[i][j] = True

    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
