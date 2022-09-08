from typing import *
import collections
import itertools
import bisect
import math


def f(i: int, j: int, k: int, count: List[List[int]]) -> str:
    if i == 0:
        return "b" * j
    elif j == 0:
        return "a" * i
    elif count[i - 1][j] >= k:
        return "a" + f(i - 1, j, k, count)
    else:
        return "b" + f(i, j - 1, k - count[i - 1][j], count)


def main():
    A, B, K = map(int, input().split())

    count: List[List[int]] = [[0 for j in range(B + 1)] for i in range(A + 1)]
    count[0][0] = 1
    for i, j in itertools.product(range(A + 1), range(B + 1)):
        if i > 0:
            count[i][j] += count[i - 1][j]
        if j > 0:
            count[i][j] += count[i][j - 1]

    print(f(A, B, K, count))


if __name__ == "__main__":
    main()
