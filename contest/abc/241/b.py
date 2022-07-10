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
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    C = collections.Counter(A)

    ok: bool = True
    for b in B:
        if C[b] == 0:
            ok = False
        else:
            C[b] -= 1

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
