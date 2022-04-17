from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    mod: int = 998244353
    N, M, K = map(int, input().split())

    dp: List[List[int]] = [[0 for j in range(K + 1)] for i in range(N + 1)]
    dp[1] = [0 if i == 0 or i > M else 1 for i in range(K + 1)]
    for i in range(2, N + 1):
        for j in range(1, K + 1):
            for k in range(1, M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
            dp[i][j] %= mod

    print(sum(dp[N]) % mod)


if __name__ == "__main__":
    main()
