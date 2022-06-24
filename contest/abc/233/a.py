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
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        print((Y - X + 9) // 10)


if __name__ == "__main__":
    main()
