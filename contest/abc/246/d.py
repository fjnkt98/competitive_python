from typing import List, Tuple, Set
import sys
import collections
import itertools
import math
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(a: int, b: int) -> int:
    return a ** 3 + a * b ** 2 + b * a ** 2 + b ** 3


def main():
    N: int = int(input())

    X: int = 1 << 64
    j: int = 1000000
    for i in range(1000000):
        while f(i, j) >= N and j >= 0:
            X = min(X, f(i, j))
            j -= 1

    print(X)


if __name__ == "__main__":
    main()
