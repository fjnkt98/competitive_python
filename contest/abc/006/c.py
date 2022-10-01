from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())

    for a in range(N + 1):
        c: int = M - 3 * N + a
        b: int = 4 * N - M - 2 * a

        if 0 <= c <= N and 0 <= c <= N and a + b + c == N:
            print(a, b, c)
            return

    print(-1, -1, -1)


if __name__ == "__main__":
    main()
