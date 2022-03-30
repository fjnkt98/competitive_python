from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    K: int = int(input())

    mod: int = 1000000007

    if K % 9 != 0:
        print(0)
        return

    dp: List[int] = [1 if i == 0 else 0 for i in range(K + 1)]
    for i in range(1, K + 1):
        for j in range(1, min(i, 9) + 1):
            dp[i] += dp[i - j]
            dp[i] %= mod

    print(dp[K])


if __name__ == "__main__":
    main()
