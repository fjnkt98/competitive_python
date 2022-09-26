from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


def f(i: int, memo: List[int], A: List[int], K: int):
    if memo[i] != -1:
        return memo[i]

    result: int = -1
    for j in range(K):
        if i - A[j] >= 0:
            result = max(result, A[j] + (i - A[j]) - f(i - A[j], memo, A, K))
    memo[i] = result

    return memo[i]


def main():
    N, K = map(int, input().split())
    A: List[int] = sorted(list(map(int, input().split())))

    memo: List[int] = [-1] * (N + 1)
    memo[0] = 0
    memo[1] = 1

    print(f(N, memo, A, K))


if __name__ == "__main__":
    main()
