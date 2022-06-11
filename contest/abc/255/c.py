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


def f(i: int, a: int, d: int) -> int:
    return a + i * d


def main():
    X, A, D, N = map(int, input().split())

    left: int = 0
    right: int = N + 1

    if D == 0:
        print(abs(X - A))
    elif D > 0:
        while right - left > 1:
            mid: int = (right + left) // 2

            if A + (mid - 1) * D <= X:
                left = mid
            else:
                right = mid

        answer: int = 1 << 63
        for i in range(-10, 11):
            if not (0 <= left + i < N):
                continue
            answer = min(answer, abs(X - f(left + i, A, D)))
        print(answer)
    else:
        while right - left > 1:
            mid: int = (right + left) // 2

            if A + (mid - 1) * D >= X:
                left = mid
            else:
                right = mid

        answer: int = 1 << 63
        for i in range(-10, 11):
            if not (0 <= left + i < N):
                continue
            answer = min(answer, abs(X - f(left + i, A, D)))
        print(answer)


if __name__ == "__main__":
    main()
