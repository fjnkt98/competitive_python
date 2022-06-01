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
    N: str = input()

    if N == "".join(reversed(N)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
