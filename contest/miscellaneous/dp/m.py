from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N, K = map(int, input().split())
    A: List[int] = [0] + list(map(int, input().split()))

    # N = 100
    # K = 100000
    # A = [0] + [random.randint(0, K) for i in range(N)]
    # print(N, K)
    # print(*A)

    mod: int = 1000000007

    dp: List[List[int]] = [[0 for j in range(K + 1)] for i in range(N + 1)]
    dp[0][0] = 1
    C = list(itertools.accumulate(dp[0]))
    for i in range(1, N + 1):
        for j in range(K + 1):
            if j - A[i] <= 0:
                dp[i][j] = C[j] % mod
            else:
                dp[i][j] = C[j] - C[j - A[i] - 1] % mod

        C = [c % mod for c in itertools.accumulate(dp[i])]

    print(dp[N][K] % mod)


if __name__ == "__main__":
    main()
