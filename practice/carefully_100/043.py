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
    grid: List[List[str]] = list(map(list, zip(*[input() for i in range(5)])))

    dp: List[List[int]] = [[1 << 60] * 4 for i in range(N + 1)]
    dp[0] = [0, 0, 0, 0]

    M: Dict[int, str] = {0: "R", 1: "B", 2: "W", 3: "#"}

    for i in range(1, N + 1):
        for j in range(3):
            minimum: int = 1 << 60
            for k in range(3):
                if k == j:
                    continue
                minimum = min(minimum, dp[i - 1][k])

            dp[i][j] = min(dp[i][j], minimum + (5 - grid[i - 1].count(M[j])))

    print(min(dp[N]))


if __name__ == "__main__":
    main()
