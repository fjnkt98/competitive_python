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
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    answer: int = 1 << 60
    for i, j in itertools.product(range(N), repeat=2):
        if i == j:
            answer = min(answer, A[i] + B[j])
        else:
            answer = min(answer, max(A[i], B[j]))

    print(answer)


if __name__ == "__main__":
    main()
