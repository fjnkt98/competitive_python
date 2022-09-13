from typing import *
import collections
import itertools
import bisect
import math


import sys

sys.setrecursionlimit(1000000)


def dfs(
    graph: List[List[int]],
    answer: List[int],
    edges: Dict[Tuple[int, int], int],
    current_node: int,
    previous_node: int,
    previous_color: int,
):
    current_color: int = 0
    for next_node in graph[current_node]:
        if next_node == previous_node:
            continue
        current_color += 1

        if current_color == previous_color:
            current_color += 1

        answer[edges[(current_node, next_node)]] = current_color
        dfs(graph, answer, edges, next_node, current_node, current_color)


def main():
    N: int = int(input())
    edges: List[Tuple[int, int]] = [
        tuple(map(lambda x: int(x) - 1, input().split())) for i in range(N - 1)
    ]
    graph: List[List[int]] = [[] for i in range(N)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    E: Dict[Tuple[int, int], int] = {
        **{(a, b): i for i, (a, b) in enumerate(edges)},
        **{(b, a): i for i, (a, b) in enumerate(edges)},
    }

    variety: int = max([len(g) for g in graph])
    answer: List[int] = [-1] * (N - 1)

    dfs(graph, answer, E, 0, -1, 0)
    print(variety)
    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
