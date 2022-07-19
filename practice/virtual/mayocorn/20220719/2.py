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


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    N: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    M: int = 1
    for i in range(1, N + 1):
        M *= i

    answer: float = 0.0
    for order in itertools.permutations(range(N)):
        for i, j in zip(order[:-1], order[1:]):
            answer += distance(X[i], Y[i], X[j], Y[j]) / M

    print(answer)


if __name__ == "__main__":
    main()
