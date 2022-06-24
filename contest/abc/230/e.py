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
    M: int = math.floor(math.sqrt(N))

    answer: int = 0
    for i in range(1, M + 1):
        answer += N // i

    answer *= 2
    answer -= M * M

    print(answer)


if __name__ == "__main__":
    main()
