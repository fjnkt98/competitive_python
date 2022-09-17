from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, L = map(int, input().split())
    X: Set[int] = set(map(int, input().split()))
    T1, T2, T3 = map(int, input().split())

    dp: List[int] = [1 << 60] * (L + 4)
    dp[0] = 0
    for i in range(L):
        dp[i + 1] = min(dp[i + 1], dp[i] + T1 + (T3 if (i + 1) in X else 0))
        dp[i + 2] = min(dp[i + 2], dp[i] + T1 + T2 + (T3 if (i + 2) in X else 0))
        dp[i + 4] = min(dp[i + 4], dp[i] + T1 + 3 * T2 + (T3 if (i + 4) in X else 0))

    answer: int = dp[L]
    if L - 1 >= 0:
        answer = min(answer, dp[L - 1] + (T1 + T2) // 2)
    if L - 2 >= 0:
        answer = min(answer, dp[L - 2] + (T1 + 3 * T2) // 2)
    if L - 3 >= 0:
        answer = min(answer, dp[L - 3] + (T1 + 5 * T2) // 2)

    print(answer)


if __name__ == "__main__":
    main()
