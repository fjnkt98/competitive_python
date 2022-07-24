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
    N, C = map(int, input().split())
    T, A = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    def get(x: int, k: int) -> int:
        return (x >> k) & 1

    answer: List[int] = [0] * N
    for k in range(30):
        f: Tuple[int, int] = (0, 1)

        b: int = get(C, k)
        for i, (t, a) in enumerate(zip(T, A)):
            x: int = get(a, k)
            if t == 1:
                g: Tuple[int, int] = (x & 0, x & 1)
            elif t == 2:
                g = (x | 0, x | 1)
            else:
                g = (x ^ 0, x ^ 1)

            f = (g[f[0]], g[f[1]])
            b = f[b]
            answer[i] |= b << k

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
