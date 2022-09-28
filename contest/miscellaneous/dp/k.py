from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    A: List[int] = sorted(list(map(int, input().split())))

    dp: List[int] = [-1] * (K + 1)
    dp[0] = 0
    for i in range(1, K + 1):
        dp[i] = 1 if any([dp[i - a] == 0 for a in A if i - a >= 0]) else 0

    print("First" if dp[K] == 1 else "Second")


if __name__ == "__main__":
    main()
