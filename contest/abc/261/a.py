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
    L1, R1, L2, R2 = map(int, input().split())

    A: List[int] = [0 for i in range(101)]

    A[L1] += 1
    A[R1] -= 1
    A[L2] += 1
    A[R2] -= 1

    A = list(itertools.accumulate(A))

    print(A.count(2))


if __name__ == "__main__":
    main()
