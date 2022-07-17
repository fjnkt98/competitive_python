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
    C: List[int] = list(map(int, input().split()))

    minC: int = min(C)
    D: int = N // minC
    answer: List[str] = []
    for i in range(D):
        for j in range(9, 0, -1):
            if minC * (D - i - 1) + C[j - 1] <= N:
                N -= C[j - 1]
                answer.append(str(j))
                break

    print("".join(answer))


if __name__ == "__main__":
    main()
