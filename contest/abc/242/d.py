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
    S: str = input().rstrip()
    Q: int = int(input())
    query: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(Q)]

    def g(c: str, x: int) -> str:
        return chr(ord("A") + (ord(c) - ord("A") + x) % 3)

    def f(t: int, k: int) -> str:
        if t == 0:
            return S[k]
        elif k == 0:
            return g(S[0], t)
        else:
            return g(f(t - 1, k // 2), k % 2 + 1)

    for t, k in query:
        print(f(t, k - 1))


if __name__ == "__main__":
    main()
