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
    N: int = int(input())
    S: str = input().rstrip()

    T: List[str] = []
    for s in S:
        if s == "x" and "".join(T[-2:]) == "fo":
            T.pop()
            T.pop()
        else:
            T.append(s)

    print(len(T))


if __name__ == "__main__":
    main()
