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
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    answer: int = 0
    ok: bool = True

    for a1, a2, a4, a5 in itertools.product(range(1, 30), repeat=4):
        a3: int = h1 - a1 - a2
        a6: int = h2 - a4 - a5
        a7: int = w1 - a1 - a4
        a8: int = w2 - a2 - a5
        a9_1: int = w3 - a3 - a6
        a9_2: int = h3 - a7 - a8

        def check(a: int) -> bool:
            return 0 < a <= 30

        if (
            check(a3)
            and check(a6)
            and check(a7)
            and check(a8)
            and check(a9_1)
            and check(a9_2)
            and a9_1 == a9_2
        ):
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
