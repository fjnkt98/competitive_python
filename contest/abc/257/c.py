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
    S: str = input().rstrip()
    W: List[int] = list(map(int, input().split()))

    adult: List[int] = []
    child: List[int] = []
    for s, w in zip(list(S), W):
        if s == "0":
            child.append(w)
        else:
            adult.append(w)

    adult.sort()
    child.sort()

    answer: int = 0

    for X in W:
        ok: int = 0
        for a in [-0.5, 0, 0.5]:
            x: float = X + a

            ok_adult: int = len(adult) - bisect.bisect_left(adult, x)
            ok_child: int = bisect.bisect_left(child, x)

            ok = max(ok, ok_adult + ok_child)

        answer = max(answer, ok)

    print(answer)


if __name__ == "__main__":
    main()
