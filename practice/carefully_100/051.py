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
    A: str = " " + input()

    dp: List[List[int]] = [[0] * 8 for i in range(N + 1)]

    D: Dict[str, int] = {"J": 2, "O": 1, "I": 0}
    for i in range(4):
        dp[1][4 | i | (1 << D[A[1]])] = 1

    for i in range(1, N):
        for j, k in itertools.product(range(8), repeat=2):
            if (j >> D[A[i + 1]]) & 1 != 0 and j & k != 0:
                dp[i + 1][j] += dp[i][k]

    print(sum(dp[-1]) % 10007)


if __name__ == "__main__":
    main()
