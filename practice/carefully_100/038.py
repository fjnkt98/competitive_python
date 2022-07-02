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


def main():
    N: int = int(input())
    for i in range(N):
        S: str = input()
        T: str = input()

        dp: List[List[int]] = [[0] * (len(T) + 1) for i in range(len(S) + 1)]
        for i, j in itertools.product(range(1, len(S) + 1), range(1, len(T) + 1)):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp[-1][-1])


if __name__ == "__main__":
    main()
