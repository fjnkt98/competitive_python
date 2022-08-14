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
    A: List[int] = list(map(int, input().split()))

    answer: int = -100000
    for i in range(N):
        aoki: int = -100000
        a: int = 0
        for j in reversed(range(N)):
            if i == j:
                continue
            l, r = (i, j) if i < j else (j, i)

            B = A[l : r + 1]
            score: int = sum(B[1::2])

            if aoki <= score:
                aoki = score
                a = j

        l, r = (i, a) if i < a else (a, i)
        C = A[l : r + 1]
        score: int = sum(C[::2])
        answer = max(answer, score)

    print(answer)


if __name__ == "__main__":
    main()
