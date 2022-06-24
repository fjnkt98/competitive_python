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
    L, R = map(int, input().split())
    S: str = input().rstrip()

    L -= 1
    R -= 1

    T: str = list(S[:L]) + list(reversed(S[L : R + 1])) + list(S[R + 1 :])
    print("".join(T))


if __name__ == "__main__":
    main()
