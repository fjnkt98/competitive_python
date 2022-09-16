from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    A: List[int] = [1]
    a: int = 6
    while a <= N:
        A.append(a)
        a *= 6
    a = 9
    while a <= N:
        A.append(a)
        a *= 9
    A = sorted(set(A))

    dp: List[int] = [1 << 60] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0:
                dp[i] = min(dp[i], dp[i - a] + 1)

    print(dp[N])


if __name__ == "__main__":
    main()
