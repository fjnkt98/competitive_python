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
    A: List[int] = [0] + list(map(int, input().split()))

    B: List[int] = list(itertools.accumulate(A))
    C: List[int] = list(itertools.accumulate([a ** 2 for a in A]))

    answer: int = 0
    for i in range(2, N + 1):
        answer += (i - 1) * A[i] ** 2 + C[i - 1] - 2 * A[i] * B[i - 1]

    print(answer)


if __name__ == "__main__":
    main()
