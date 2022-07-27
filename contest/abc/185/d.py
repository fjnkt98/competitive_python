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
    A: List[int] = [0] + sorted(list(map(int, input().split()))) + [N + 1]

    D: List[int] = [q - p - 1 for p, q in zip(A[:-1], A[1:]) if q - p != 1]

    if not D:
        print(0)
        return

    S: int = min(D)
    answer: int = 0
    for d in D:
        answer += (d + S - 1) // S

    print(answer)


if __name__ == "__main__":
    main()
