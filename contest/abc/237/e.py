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
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    H: List[int] = list(map(int, input().split()))
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        graph[u].append((v, max(H[v] - H[u], 0)))
        graph[v].append((u, max(H[u] - H[v], 0)))

    D: List[int] = [1 << 60 for i in range(N)]
    D[0] = 0

    answer: int = 0
    candidate: List[Tuple[int, int]] = [(0, 0)]

    while candidate:
        d, node = heapq.heappop(candidate)

        if D[node] < d:
            continue

        answer = max(answer, H[0] - H[node] - D[node])
        for next_node, weight in graph[node]:
            if D[next_node] > D[node] + weight:
                D[next_node] = D[node] + weight
                heapq.heappush(candidate, (D[next_node], next_node))

    print(answer)


if __name__ == "__main__":
    main()
