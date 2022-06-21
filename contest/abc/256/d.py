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
    L, R = map(list, zip(*[tuple(map(int, input().split())) for i in range(N)]))

    A: List[int] = [0] * (200002)

    for l, r in zip(L, R):
        A[l] += 1
        A[r] -= 1

    B: List[int] = list(itertools.accumulate(A))
    C: List[bool] = [b != 0 for b in B]

    stack: List[int] = []
    answer: List[Tuple[int, int]] = []
    for i in range(1, len(B)):
        if C[i] and not C[i - 1]:
            stack.append(i)
        elif not C[i] and C[i - 1]:
            answer.append((stack.pop(), i))

    for a in sorted(answer):
        print(*a)


if __name__ == "__main__":
    main()
