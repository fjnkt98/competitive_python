from typing import *
import collections
import itertools
import bisect
import math


import sys

sys.setrecursionlimit(1000000)


def dfs(graph: List[List[int]], distance: List[int], current: int, previous: int):
    for next_node in graph[current]:
        if next_node == previous:
            continue
        distance[next_node] = distance[current] + 1
        dfs(graph, distance, next_node, current)


def f(graph: List[List[int]], C: List[int], current: int, previous: int):
    for next_node in graph[current]:
        if next_node == previous:
            continue
        C[next_node] += C[current]
        f(graph, C, next_node, current)


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    edges: List[Tuple[int, int]] = [
        tuple(map(lambda x: int(x) - 1, input().split())) for i in range(N - 1)
    ]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    Q: int = int(input())
    query: List[Tuple[int, int, int]] = [
        tuple(map(int, input().split())) for i in range(Q)
    ]

    distance: List[int] = [0] * N
    dfs(graph, distance, 0, -1)

    C: List[int] = [0] * N
    for t, e, x in query:
        e -= 1
        if t == 1:
            a, b = edges[e]
            if distance[a] < distance[b]:
                C[0] += x
                C[b] -= x
            else:
                C[a] += x

        elif t == 2:
            a, b = edges[e]
            if distance[a] < distance[b]:
                C[b] += x
            else:
                C[0] += x
                C[a] -= x

    f(graph, C, 0, -1)
    for c in C:
        print(c)


if __name__ == "__main__":
    main()
