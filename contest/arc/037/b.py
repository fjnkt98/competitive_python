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
    graph: List[List[int]], explored: List[int], current_node: int, previous_node: int
) -> bool:
    explored[current_node] = True

    is_tree: bool = True
    for next_node in graph[current_node]:
        if next_node == previous_node:
            continue
        if explored[next_node]:
            return False
        is_tree &= dfs(graph, explored, next_node, current_node)

    return is_tree


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    explored: List[bool] = [False] * N
    answer: int = 0
    for i in range(N):
        if explored[i]:
            continue
        if dfs(graph, explored, i, -1):
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
