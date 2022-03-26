from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, L = map(int, input().split())
    mod: int = 1000000007

    dp: List[int] = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] += dp[i - 1]

        if i - L >= 0:
            dp[i] += dp[i - L]

        dp[i] %= mod

    print(dp[N])


if __name__ == "__main__":
    main()
