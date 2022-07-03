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
    K: int = int(input())

    hour: int = 21
    minute: int = 0

    hour += K // 60
    minute += K % 60

    print(f"{hour}:{str(minute).zfill(2)}")


if __name__ == "__main__":
    main()
