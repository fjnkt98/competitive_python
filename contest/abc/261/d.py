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
    N, M = map(int, input().split())
    X: List[int] = list(map(int, input().split()))
    C, Y = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))

    D: Dict[int, int] = {c: y for c, y in zip(C, Y)}

    dp: List[List[int]] = [[-1 for j in range(N + 1)] for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1])
        for j in range(1, N + 1):
            if dp[i - 1][j - 1] != -1:
                reward: int = dp[i - 1][j - 1] + X[i - 1]
                if j in D:
                    reward += D[j]
                dp[i][j] = max(dp[i][j], reward)

    print(max(dp[N]))


if __name__ == "__main__":
    main()
