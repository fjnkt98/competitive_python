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
import operator


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, D = map(int, input().split())
    W: List[Tuple[int]] = [tuple(map(int, input().split())) for i in range(N)]

    W.sort(key=operator.itemgetter(1))

    answer: int = 0
    broken: List[bool] = [False] * N
    last: int = 0

    for l, r in W:
        if l <= last:
            continue

        answer += 1
        last = r + D - 1

    print(answer)


if __name__ == "__main__":
    main()
