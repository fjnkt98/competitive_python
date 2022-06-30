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
    N, M = map(int, input().split())
    P: List[int] = [int(input()) for i in range(N)]

    PP: List[int] = sorted([p + q for p, q in itertools.product([0] + P, repeat=2)])

    answer: int = 0
    for p in PP:
        if p > M:
            break
        i = bisect.bisect_right(PP, M - p)

        answer = max(answer, p + PP[i - 1])

    print(answer)


if __name__ == "__main__":
    main()
