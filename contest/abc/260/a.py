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
    S = input()

    C = collections.Counter(S)

    for k, v in C.items():
        if v == 1:
            print(k)
            return

    print(-1)


if __name__ == "__main__":
    main()
