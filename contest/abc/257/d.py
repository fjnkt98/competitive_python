from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    X, Y, P = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(N)]
    for i, j in itertools.product(range(N), repeat=2):
        D: int = abs(X[i] - X[j]) + abs(Y[i] - Y[j])
        dp[i][j] = (D + P[i] - 1) // P[i]

    for k, i, j in itertools.product(range(N), repeat=3):
        dp[i][j] = min(dp[i][j], max(dp[i][k], dp[k][j]))

    answer: int = 1 << 60
    for i in range(N):
        tmp: int = 0
        for j in range(N):
            tmp = max(tmp, dp[i][j])

        answer = min(answer, tmp)

    print(answer)


if __name__ == "__main__":
    main()
