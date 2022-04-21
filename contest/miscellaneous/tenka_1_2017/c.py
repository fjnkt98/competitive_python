from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    for h in range(1, 3501):
        for n in range(1, 3501):
            numerator: int = N * h * n
            denominator: int = 4 * h * n - N * n - N * h

            if denominator == 0:
                continue

            w: int = numerator // denominator

            if 1 <= w <= 3500 and 4 * h * n * w == N * (n * w + h * w + h * n):
                print(h, n, w)
                return


if __name__ == "__main__":
    main()
