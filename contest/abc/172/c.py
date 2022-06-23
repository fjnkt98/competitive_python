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
    N, M, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    A = list(itertools.accumulate(A, initial=0))
    B = list(itertools.accumulate(B, initial=0))

    answer: int = 0
    j: int = M
    for i in range(N + 1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1

        answer = max(answer, i + j)

    print(answer)


if __name__ == "__main__":
    main()
