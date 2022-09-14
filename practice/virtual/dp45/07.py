from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A: Set[int] = set([int(input()) for i in range(M)])

    mod: int = 1000000007

    dp: List[int] = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 0 if 1 in A else 1

    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= mod

    print(dp[N])


if __name__ == "__main__":
    main()
