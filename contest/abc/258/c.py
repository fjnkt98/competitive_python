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
    N, Q = map(int, input().split())
    S: str = input()
    T, X = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    offset: int = 0
    for t, x in zip(T, X):
        if t == 1:
            offset -= x
            if offset < 0:
                offset += N
        elif t == 2:
            print(S[(x - 1 + offset) % N])


if __name__ == "__main__":
    main()
