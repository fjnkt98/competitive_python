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
    graph: List[List[int]] = [[0 for j in range(N)] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = 1
        graph[v][u] = 1

    answer: int = 0
    for (
        a,
        b,
        c,
    ) in itertools.combinations(range(N), r=3):
        if graph[a][b] == graph[b][c] == graph[c][a] == 1:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
