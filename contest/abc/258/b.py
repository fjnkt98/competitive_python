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
    grid: List[List[int]] = [list(map(int, list(input()))) for i in range(N)]

    answer: int = 0
    for dr, dc in zip([0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]):
        for j, k in itertools.product(range(N), range(N)):

            r: int = j
            c: int = k
            result: List[int] = [grid[r][c]]

            for _ in range(N - 1):
                r += dr
                if r < 0:
                    r += N
                r %= N
                c += dc
                if c < 0:
                    c += N
                c %= N

                result.append(grid[r][c])

            answer = max(answer, int("".join(map(str, reversed(result)))))

    print(answer)


if __name__ == "__main__":
    main()
