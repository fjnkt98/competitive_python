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
    P: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(N):
        m: int = int(input())
        P[i] = [tuple(map(int, input().split())) for j in range(m)]

    D: Dict[int, int] = collections.defaultdict(int)
    count: Dict[Tuple[int, int], int] = collections.defaultdict(int)
    for ps in P:
        for p, e in ps:
            D[p] = max(D[p], e)
            count[(p, e)] += 1

    answer: int = 0
    for ps in P:
        differ: bool = False
        for p, e in ps:
            if D[p] == e and count[(p, e)] == 1:
                differ = True

        if differ:
            answer += 1

    print(min(answer + 1, N))


if __name__ == "__main__":
    main()
