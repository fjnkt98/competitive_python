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


def reg_tetra(n: int) -> int:
    return (n * (n + 1) * (n + 2)) // 6


def main():
    A: List[int] = []
    while True:
        N: int = int(input())
        if N == 0:
            break

        A.append(N)

    M: int = max(A)
    B: List[int] = [reg_tetra(i) for i in range(1, M) if reg_tetra(i) <= M]
    C: List[int] = [
        reg_tetra(i) for i in range(1, M) if reg_tetra(i) <= M and reg_tetra(i) % 2 == 1
    ]

    dp1_c: List[List[int]] = [1 << 60 for j in range(M + 1)]
    dp1_p: List[List[int]] = [1 << 60 for j in range(M + 1)]
    dp1_p[0] = 0
    for b in B:
        for j in range(M + 1):
            dp1_c[j] = dp1_p[j]

            if j - b >= 0:
                dp1_c[j] = min(dp1_c[j], dp1_c[j - b] + 1)

        dp1_p = dp1_c

    dp2_c: List[List[int]] = [1 << 60 for j in range(M + 1)]
    dp2_p: List[List[int]] = [1 << 60 for j in range(M + 1)]
    dp2_p[0] = 0
    for c in C:
        for j in range(M + 1):
            dp2_c[j] = dp2_p[j]

            if j - c >= 0:
                dp2_c[j] = min(dp2_c[j], dp2_c[j - c] + 1)

        dp2_p = dp2_c

    for a in A:
        print(dp1_c[a], dp2_c[a])


if __name__ == "__main__":
    main()
