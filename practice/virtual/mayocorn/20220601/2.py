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
    N, M = map(int, input().split())
    if M == 0:
        print(0, 0)
        return
    P, S = map(list, zip(*[list(input().split()) for i in range(M)]))
    P = list(map(lambda p: int(p) - 1, P))

    answer: int = 0

    ac: List[bool] = [False] * N
    penalties: List[int] = [0] * N
    for p, s in zip(P, S):
        if ac[p]:
            continue
        if s == "AC":
            answer += 1
            ac[p] = True
        else:
            penalties[p] += 1

    penalty: int = 0
    for a, p in zip(ac, penalties):
        if a:
            penalty += p
    print(answer, penalty)


if __name__ == "__main__":
    main()
