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
    S: str = input().rstrip()
    a, b = map(int, input().split())

    T: List[str] = list(S)
    T[a - 1], T[b - 1] = T[b - 1], T[a - 1]
    print("".join(T))


if __name__ == "__main__":
    main()
