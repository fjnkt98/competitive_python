from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, K = map(int, input().split())

    mod: int = 998244353

    dp: List[List[int]] = [[0 for j in range(M + 1)] for i in range(N + 1)]
    dp[1] = [0 if i == 0 else 1 for i in range(M + 1)]

    C: List[int] = list(itertools.accumulate(dp[1]))

    for i in range(2, N + 1):
        for j in range(1, M + 1):
            if K == 0:
                dp[i][j] = C[M]
            else:
                if j - K >= 1:
                    dp[i][j] += C[j - K]
                if j + K <= M:
                    dp[i][j] += C[M] - C[j + K - 1]

            dp[i][j] %= mod

        C = list(itertools.accumulate(dp[i]))

    print(sum(dp[N]) % mod)


if __name__ == "__main__":
    main()
