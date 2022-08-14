from random import randint
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
import random

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = [int(x) - 1 for x in input().split()]

    B: List[bool] = [False for _ in range(N - 1)]

    answer: List[int] = []
    last: int = -1
    for i in range(N - 1):
        if A[i] < A[i + 1]:
            continue

        index: int = i
        while last < index:
            A[index], A[index + 1] = A[index + 1], A[index]
            B[index] = True

            answer.append(index)
            index -= 1

        last = i

    if tuple(A) == tuple(range(N)) and B.count(False) == 0:
        for a in answer:
            print(a + 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
