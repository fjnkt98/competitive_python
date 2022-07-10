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


def dfs(
    graph: List[List[int]],
    order: List[List[int]],
    X: List[int],
    current_node: int,
    previous_node: int,
):

    L: List[int] = order[current_node]
    for next_node in graph[current_node]:
        if next_node == previous_node:
            continue
        dfs(graph, order, X, next_node, current_node)
        L.extend(order[next_node])

    L.sort(reverse=True)
    if len(L) > 20:
        L = L[:20]

    order[current_node] = L


def main():
    N, Q = map(int, input().split())
    X: List[int] = list(map(int, input().split()))
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    V, K = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    order: List[List[int]] = [[X[i]] for i in range(N)]
    dfs(graph, order, X, 0, -1)

    for v, k in zip(V, K):
        print(order[v - 1][k - 1])


if __name__ == "__main__":
    main()
