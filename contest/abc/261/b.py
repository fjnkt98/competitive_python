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
    A: List[List[int]] = [list(input()) for i in range(N)]

    ok: bool = True
    for i, j in itertools.combinations(range(N), r=2):
        if A[i][j] == "W" and A[j][i] != "L":
            ok = False
        if A[i][j] == "L" and A[j][i] != "W":
            ok = False
        if A[i][j] == "D" and A[j][i] != "D":
            ok = False

    print("correct" if ok else "incorrect")


if __name__ == "__main__":
    main()
