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
import functools
import operator

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(A: List[List[int]], pairs: List[Tuple[int, int]], decided: List[bool]) -> int:
    N: int = len(decided) // 2

    if len(pairs) == N:
        return functools.reduce(operator.xor, [A[i][j] for i, j in pairs])

    i = decided.index(False)
    decided[i] = True

    result = 0
    for j in range(2 * N):
        if decided[j]:
            continue
        pairs.append((i, j))
        decided[j] = True

        result = max(result, dfs(A, pairs, decided))

        pairs.pop()
        decided[j] = False

    decided[i] = False

    return result


def main():
    N: int = int(input())
    A: List[List[int]] = [
        [0] * (i + 1) + list(map(int, input().split())) for i in range(2 * N - 1)
    ]

    pairs: List[Tuple[int, int]] = []
    decided: List[bool] = [False for i in range(2 * N)]

    print(dfs(A, pairs, decided))


if __name__ == "__main__":
    main()
