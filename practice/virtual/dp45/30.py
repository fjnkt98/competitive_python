from typing import *
import collections
import itertools
import bisect
import math


def main():
    D, N = map(int, input().split())
    T: List[int] = [int(input()) for i in range(D)]
    A, B, C = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[int]] = [[0 for j in range(N)] for i in range(D)]

    for i in range(1, D):
        for j, k in itertools.product(range(N), repeat=2):
            if A[j] <= T[i] <= B[j] and A[k] <= T[i - 1] <= B[k]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(C[j] - C[k]))

    print(max(dp[D - 1]))


if __name__ == "__main__":
    main()
