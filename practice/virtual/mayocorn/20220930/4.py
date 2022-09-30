from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


def main():
    N, X = map(int, input().split())
    X -= 1

    P: List[int] = [0 for i in range(N + 1)]
    L: List[int] = [0 for i in range(N + 1)]
    P[0] = L[0] = 1
    for i in range(1, N + 1):
        P[i] = 2 * P[i - 1] + 1
        L[i] = 2 * L[i - 1] + 3

    def f(n: int, x: int) -> int:
        if n == 0:
            return 1
        if x < 1:
            return 0

        if 1 <= x < L[n] // 2:
            return f(n - 1, x - 1)
        elif x == L[n] // 2:
            return P[n - 1] + 1
        else:
            return f(n - 1, x - L[n - 1] - 2) + P[n - 1] + 1

    print(f(N, X))


if __name__ == "__main__":
    main()
