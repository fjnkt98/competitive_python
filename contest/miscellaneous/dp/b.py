from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    H: List[int] = list(map(int, input().split()))

    dp: List[int] = [1 << 60 for i in range(N)]
    dp[0] = 0
    for i in range(N):
        for j in range(1, K + 1):
            if i + j < N:
                dp[i + j] = min(dp[i + j], dp[i] + abs(H[i] - H[i + j]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
