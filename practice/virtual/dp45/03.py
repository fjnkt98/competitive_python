from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    H: List[int] = list(map(int, input().split()))

    dp: List[int] = [1 << 60] * N
    dp[0] = 0
    for i in range(1, N):
        for k in range(1, K + 1):
            if i - k < 0:
                continue
            dp[i] = min(dp[i], dp[i - k] + abs(H[i] - H[i - k]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
