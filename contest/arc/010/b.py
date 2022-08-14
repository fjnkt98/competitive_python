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
    if N == 0:
        print(2)
        return

    H: List[Tuple[int, int]] = sorted(
        [tuple(map(int, input().split("/"))) for i in range(N)]
    )

    days: List[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    C: List[int] = [0] + list(itertools.accumulate(days))

    A: List[bool] = [False] * 1000
    for i, h in zip(range(366), [True, False, False, False, False, False, True] * 53):
        A[i] = h

    for month, day in H:
        d: int = day - 1 + C[month - 1]
        if A[d]:
            i: int = d
            while A[i] is True:
                i += 1
                if i >= 365:
                    break
            A[i] = True
        else:
            A[d] = True

    B: List[Tuple[str, int]] = [
        len(list(v)) for k, v in itertools.groupby(A[:366]) if k is True
    ]
    print(max(B))


if __name__ == "__main__":
    main()
