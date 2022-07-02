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

    dp: List[int] = [1] * (N + 1)
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[N])


if __name__ == "__main__":
    main()
