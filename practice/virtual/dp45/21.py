from typing import *
import collections
import itertools
import bisect
import math


def main():
    A = [25, 39, 51, 76, 163, 111, 136, 128, 133, 138]
    B = [25, 39, 51, 76, 163, 111, 58, 128, 133, 138]

    N: int = len(A)
    M: int = sum(A)

    dp1: List[List[int]] = [[0 for j in range(sum(A) + 1)] for i in range(N + 1)]
    dp1[0][0] = 1
    for i in range(1, N + 1):
        for j in range(sum(A) + 1):
            dp1[i][j] = dp1[i - 1][j]

            if j - A[i - 1] >= 0:
                dp1[i][j] += dp1[i - 1][j - A[i - 1]]

    dp2: List[List[int]] = [[0 for j in range(sum(B) + 1)] for i in range(N + 1)]
    dp2[0][0] = 1
    for i in range(1, N + 1):
        for j in range(sum(B) + 1):
            dp2[i][j] = dp2[i - 1][j]

            if j - B[i - 1] >= 0:
                dp2[i][j] += dp2[i - 1][j - B[i - 1]]

    for a in sorted(
        set(
            [i for i, d in enumerate(dp1[N]) if d != 0]
            + [i for i, d in enumerate(dp2[N]) if d != 0]
        )
    ):
        print(a)


if __name__ == "__main__":
    main()
