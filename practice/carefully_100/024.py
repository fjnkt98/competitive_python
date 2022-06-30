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

time: int = 0


def dfs(
    graph: List[List[int]],
    node: int,
    d: List[int],
    f: List[int],
    explored: List[bool],
) -> None:

    global time
    time += 1

    explored[node] = True

    d[node] = time

    for next_node in graph[node]:
        if explored[next_node]:
            continue
        dfs(graph, next_node, d, f, explored)

    time += 1
    f[node] = time


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        u, k, *v = map(int, input().split())
        graph[u - 1] = [node - 1 for node in v]

    explored: List[bool] = [False] * N
    D: List[int] = [0] * N
    F: List[int] = [0] * N

    for i in range(N):
        if not explored[i]:
            dfs(graph, i, D, F, explored)

    for i, (d, f) in enumerate(zip(D, F)):
        print(i + 1, d, f)


if __name__ == "__main__":
    main()
