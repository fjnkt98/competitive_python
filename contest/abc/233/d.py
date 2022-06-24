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
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(itertools.accumulate(A, initial=0))

    counter = collections.defaultdict(int)

    answer: int = 0
    for i in range(1, N + 1):
        counter[B[i - 1]] += 1
        answer += counter[B[i] - K]

    print(answer)


if __name__ == "__main__":
    main()
