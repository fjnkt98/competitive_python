from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    T: List[int] = list(map(int, input().split()))

    M: int = sum(T)
    dp: List[List[bool]] = [[False for j in range(M + 1)] for i in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] |= dp[i - 1][j]

            if j - T[i - 1] >= 0:
                dp[i][j] |= dp[i - 1][j - T[i - 1]]

    time: List[int] = []
    for j in range(M + 1):
        if dp[N][j]:
            time.append(max(j, M - j))
    answer: int = min(time)

    print(answer)


if __name__ == "__main__":
    main()
