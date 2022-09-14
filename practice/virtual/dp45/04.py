from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    P: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for i in range(N)]

    dp: List[List[int]] = [[0, 0, 0] for i in range(N)]
    dp[0][0] = P[0][0]
    dp[0][1] = P[0][1]
    dp[0][2] = P[0][2]

    for i in range(1, N):
        for j in range(3):
            dp[i][j] = max(
                dp[i - 1][(j + 1) % 3] + P[i][j], dp[i - 1][(j + 2) % 3] + P[i][j]
            )

    print(max(dp[N - 1]))


if __name__ == "__main__":
    main()
