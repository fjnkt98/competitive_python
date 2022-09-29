from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A: List[int] = [int(input()) - 1 for i in range(N)]
    C = collections.Counter(A)
    D: List[List[int]] = [[0 for j in range(N)] for i in range(M)]
    for i, a in enumerate(A):
        D[a][i] += 1
    for i in range(M):
        D[i] = list(itertools.accumulate(D[i])) + [0]

    dp: List[int] = [1 << 60 for i in range(1 << M)]
    dp[0] = 0
    for S in range(1 << M):
        X: int = sum([C[i] for i in range(M) if (S >> i) & 1 == 1])
        for j in range(M):
            if (S >> j) & 1 == 1:
                continue
            dp[S | (1 << j)] = min(
                dp[S | (1 << j)], dp[S] + C[j] - (D[j][X + C[j] - 1] - D[j][X - 1])
            )

    print(dp[(1 << M) - 1])


if __name__ == "__main__":
    main()
