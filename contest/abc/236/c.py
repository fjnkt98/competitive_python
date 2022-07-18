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
    S: List[str] = input().split()
    T: List[str] = input().split()

    U = set(T)
    for s in S:
        if s in U:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
