from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    mod: int = 1000000007

    dp: List[int] = [0 for i in range(1 << N)]
    dp[0] = 1
    for S in range(1, 1 << N):
        i: int = bin(S).count("1")
        for j in range(N):
            if ((S >> j) & 1) == 1 and A[i - 1][j] == 1:
                dp[S] += dp[S ^ (1 << j)]
        dp[S] %= mod

    print(dp[(1 << N) - 1])


if __name__ == "__main__":
    main()
