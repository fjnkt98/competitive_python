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
    N, K = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(K)]))

    mod: int = 10000

    D: Dict[int, int] = {a: b - 1 for a, b in zip(A, B)}

    dp: List[List[int]] = [[0] * 3 for i in range(N + 1)]
    dp: List[List[List[int]]] = [[[0] * 2 for j in range(3)] for i in range(N + 1)]

    if 1 in D:
        dp[1][D[1]] = [1, 0]
        dp[1][(D[1] + 1) % 3] = [0, 0]
        dp[1][(D[1] + 2) % 3] = [0, 0]
    else:
        dp[1] = [[1, 0] for i in range(3)]

    for i in range(2, N + 1):
        for j in range(3):
            dp[i][j][0] = sum(dp[i - 1][(j + 1) % 3]) + sum(dp[i - 1][(j + 2) % 3])
            dp[i][j][1] = dp[i - 1][j][0]

            dp[i][j][0] %= mod
            dp[i][j][1] %= mod

        if i in D:
            dp[i][(D[i] + 1) % 3] = [0, 0]
            dp[i][(D[i] + 2) % 3] = [0, 0]

    print(sum(itertools.chain(*dp[N])) % mod)


if __name__ == "__main__":
    main()
