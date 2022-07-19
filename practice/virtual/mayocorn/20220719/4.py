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


def f(a: int, n: int, d: int) -> int:
    return n * (2 * a + (n - 1) * d) // 2


def main():
    N, K = map(int, input().split())
    A: List[int] = sorted(list(map(int, input().split())), reverse=True) + [0]

    answer: int = 0
    for i in range(N):
        d: int = A[i] - A[i + 1]

        if d * (i + 1) <= K:
            answer += f(A[i], d, -1) * (i + 1)
            A[i] -= d
            K -= d * (i + 1)
        else:
            q: int = K // (i + 1)
            r: int = K % (i + 1)
            answer += f(A[i], q, -1) * (i + 1)
            answer += (A[i] - q) * r
            K = 0

        if K == 0:
            break

    print(answer)


if __name__ == "__main__":
    main()
