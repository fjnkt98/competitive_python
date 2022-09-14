from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: List[List[str]] = list(zip(*[list(input()) for i in range(5)]))

    D: Dict[int, str] = {
        0: "R",
        1: "B",
        2: "W",
    }

    dp: List[List[int]] = [[1 << 60] * 3 for i in range(N)]
    for j in range(3):
        dp[0][j] = 5 - S[0].count(D[j])

    for i in range(1, N):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + (
                5 - S[i].count(D[j])
            )

    print(min(dp[N - 1]))


if __name__ == "__main__":
    main()
