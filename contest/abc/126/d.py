from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(
    graph: List[List[Tuple[int, int]]],
    colors: List[int],
    color: int,
    current_node: int,
    previous_node: int,
) -> None:
    colors[current_node] = color

    for next_node, weight in graph[current_node]:
        if next_node == previous_node or colors[next_node] != -1:
            continue
        if weight % 2 == 0:
            dfs(graph, colors, color, next_node, current_node)
        else:
            dfs(graph, colors, 1 - color, next_node, previous_node)


def main():
    N: int = int(input())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    color: List[int] = [-1] * N
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    colors: List[int] = [-1] * N

    dfs(graph, colors, 0, 0, -1)

    for c in colors:
        print(c)


if __name__ == "__main__":
    main()
