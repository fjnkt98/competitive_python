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


def dfs(graph: List[List[int]], node: int, prev_node: int, counter: List[int]):

    for next_node in graph[node]:
        if next_node == prev_node:
            continue

        counter[next_node] += counter[node]
        dfs(graph, next_node, node, counter)


def main():
    N, Q = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    P, X = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    counter: List[int] = [0] * N
    for p, x in zip(P, X):
        counter[p - 1] += x

    dfs(graph, 0, -1, counter)
    print(*counter)


if __name__ == "__main__":
    main()
