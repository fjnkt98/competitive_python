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


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        u, k, *v = map(int, input().split())
        graph[u - 1] = [node - 1 for node in v]

    candidate = collections.deque([0])
    distance: List[int] = [0 if i == 0 else -1 for i in range(N)]

    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    for i, d in enumerate(distance):
        print(i + 1, d)


if __name__ == "__main__":
    main()
