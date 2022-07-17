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
    segments: List[List[int]],
    token: List[int],
    current: int,
    previous: int,
):
    if current != 0 and len(graph[current]) == 1:
        segments[current] = [token[0], token[0]]
        token[0] += 1
        return

    for next_node in graph[current]:
        if next_node == previous:
            continue

        dfs(graph, segments, token, next_node, current)

    l: int = 1 << 60
    r: int = 0

    for next_node in graph[current]:
        if next_node == previous:
            continue

        l = min(l, segments[next_node][0])
        r = max(r, segments[next_node][1])

    segments[current] = [l, r]

    return


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        graph[u].append(v)
        graph[v].append(u)

    segments: List[List[int]] = [[] for i in range(N)]
    token: List[int] = [1]

    dfs(graph, segments, token, 0, -1)

    for l, r in segments:
        print(l, r)


if __name__ == "__main__":
    main()
