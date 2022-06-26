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
    N, X = map(int, input().split())
    S: List[str] = []
    for i in range(26):
        S.extend([chr(ord("A") + i)] * N)

    print(S[X - 1])


if __name__ == "__main__":
    main()
