from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    H: List[int] = list(map(int, input().split()))

    dp: List[int] = [1 << 60 for i in range(N)]
    dp[0] = 0
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
