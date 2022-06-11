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


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(lambda x: int(x) - 1, input().split()))
    P: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(N)]

    left: float = 0
    right: float = 1e6

    while right - left > 1e-7:
        mid: float = (left + right) / 2

        light: List[bool] = [False] * N

        for a in A:
            for i, (x, y) in enumerate(P):
                if i == a:
                    light[a] = True
                    continue

                xa, ya = P[a]

                if distance(x, y, xa, ya) <= mid:
                    light[i] = True

        if all(light):
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
