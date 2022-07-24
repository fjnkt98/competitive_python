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
    S: List[str] = [input() for i in range(N)]

    C = collections.Counter()

    for s in S:
        if s in C:
            print(s + "(" + f"{C[s]}" + ")")
            C[s] += 1
        else:
            print(s)
            C[s] = 1


if __name__ == "__main__":
    main()
