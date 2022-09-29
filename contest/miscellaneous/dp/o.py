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
    for S in range(1 << N):
        i: int = bin(S).count("1")
        for j in range(N):
            if ((S >> j) & 1) == 0 and A[i][j] == 1:
                dp[S | (1 << j)] += dp[S]
        dp[S] %= mod

    # for i, d in enumerate(dp):
    #     print(bin(i)[2:].zfill(N), d)
    print(dp[(1 << N) - 1])


if __name__ == "__main__":
    main()
