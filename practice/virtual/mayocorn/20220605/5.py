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
    H, W, C = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    dp1: List[List[int]] = [[1 << 60] * (W + 2) for i in range(H + 2)]
    answer: int = 1 << 60
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp1[i][j] = min(dp1[i - 1][j] + C, dp1[i][j - 1] + C, A[i - 1][j - 1])
            answer = min(
                answer,
                dp1[i - 1][j] + C + A[i - 1][j - 1],
                dp1[i][j - 1] + C + A[i - 1][j - 1],
            )

    dp2: List[List[int]] = [[1 << 60] * (W + 2) for i in range(H + 2)]
    for i in range(1, H + 1):
        for j in range(W, 0, -1):
            dp2[i][j] = min(dp2[i - 1][j] + C, dp2[i][j + 1] + C, A[i - 1][j - 1])
            answer = min(
                answer,
                dp2[i - 1][j] + C + A[i - 1][j - 1],
                dp2[i][j + 1] + C + A[i - 1][j - 1],
            )

    print(answer)


if __name__ == "__main__":
    main()
