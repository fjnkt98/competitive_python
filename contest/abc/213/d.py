from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(
    graph: List[List[int]],
    node: int,
    explored: List[bool],
    order: List[int],
) -> None:
    explored[node] = True
    order.append(node)

    for next_node in graph[node]:
        if not explored[next_node]:
            dfs(graph, next_node, explored, order)
            order.append(node)


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for i in range(N):
        graph[i].sort()

    explored: List[bool] = [False] * N
    order: List[int] = []
    dfs(graph, 0, explored, order)
    print(*list(map(lambda x: x + 1, order)))


if __name__ == "__main__":
    main()
