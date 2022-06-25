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
    c: str = input().rstrip()
    left: Set[str] = {
        "Q",
        "W",
        "E",
        "R",
        "T",
        "Y",
        "A",
        "S",
        "D",
        "F",
        "G",
        "H",
        "Z",
        "X",
        "C",
        "V",
        "B",
    }

    if c in left:
        print("Left")
    else:
        print("Right")


if __name__ == "__main__":
    main()
