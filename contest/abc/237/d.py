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

    A = collections.deque([N])
    for i, s in enumerate(reversed(S)):
        if s == "R":
            A.appendleft(N - i - 1)
        else:
            A.append(N - i - 1)

    print(*list(A))


if __name__ == "__main__":
    main()
