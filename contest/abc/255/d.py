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
    N, Q = map(int, input().split())
    A: List[int] = sorted(list(map(int, input().split())))
    X: List[int] = [int(input()) for i in range(Q)]

    B: List[int] = [0] + list(itertools.accumulate(A))

    minimum: int = min(A)
    maximum: int = max(A)
    total: int = sum(A)

    T: int = sum(A)
    for x in X:
        if minimum < x < maximum:
            left: int = bisect.bisect_left(A, x)
            right: int = bisect.bisect_right(A, x)

            answer: int = 0
            answer += left * x - B[left]
            answer += (B[N] - B[right]) - (N - right) * x

            print(answer)
        else:
            print(abs(total - x * N))


if __name__ == "__main__":
    main()
