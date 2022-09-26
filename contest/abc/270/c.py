from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


def dfs(
    graph: List[List[int]],
    distance: List[int],
    history: List[int],
    current: int,
    previous: int,
) -> None:
    for next_node in graph[current]:
        if next_node == previous:
            continue
        distance[next_node] = distance[current] + 1
        history[next_node] = current
        dfs(graph, distance, history, next_node, current)


def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    distance: List[int] = [-1] * N
    distance[X] = 0
    history: List[int] = [-1] * N
    dfs(graph, distance, history, X, -1)

    answer: List[int] = []
    current: int = Y
    while current != -1:
        answer.append(current)
        current = history[current]

    print(*reversed(list(map(lambda x: x + 1, answer))))


if __name__ == "__main__":
    main()
