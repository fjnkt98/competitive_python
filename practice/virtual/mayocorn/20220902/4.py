from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    M: int = max(B)

    mod: int = 998244353

    dp: List[List[int]] = [[0 for j in range(M + 1)] for i in range(N + 1)]
    dp[0][0] = 1

    C: List[int] = list(itertools.accumulate(dp[0]))

    for i in range(1, N + 1):
        for j in range(A[i - 1], B[i - 1] + 1):
            dp[i][j] += C[j] % mod

        C = list(itertools.accumulate(dp[i]))

    print(sum(dp[N]) % mod)


if __name__ == "__main__":
    main()
