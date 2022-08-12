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
    graph: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(N)]
    T: Dict[Tuple[int, int], int] = dict()
    for i in range(M):
        u, v, d, t = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = d
        graph[v][u] = d
        T[(u, v)] = t
        T[(v, u)] = t

    dp1: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(2 ** N)]
    dp1[0][0] = 0
    dp2: List[List[int]] = [[0 for j in range(N)] for i in range(2 ** N)]
    dp2[0][0] = 1

    for bits in itertools.product((0, 1), repeat=N):
        S: int = int("".join(map(str, bits)), 2)
        for u, v in itertools.product(range(N), repeat=2):
            if bits[N - u - 1] == 0 and S != 0:
                continue
            if graph[u][v] == 1 << 60:
                continue
            if bits[N - v - 1] == 0:
                D: int = dp1[S][u] + graph[u][v]
                if D > T[(u, v)]:
                    continue

                U: int = S | (1 << v)
                if dp1[U][v] > D:
                    dp1[U][v] = D
                    dp2[U][v] = 0
                if dp1[U][v] == D:
                    dp2[U][v] += dp2[S][u]

    if dp1[-1][0] == 1 << 60:
        print("IMPOSSIBLE")
    else:
        print(dp1[-1][0], dp2[-1][0])


if __name__ == "__main__":
    main()
