from typing import *
import collections
import itertools
import bisect
import math
import heapq


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    C: List[int] = [0] * N
    for i, g in enumerate(graph):
        C[i] = sum([A[node] for node in g])

    candidate = [(c, i) for i, c in enumerate(C)]
    heapq.heapify(candidate)

    answer: int = 0
    erased: List[bool] = [False] * N
    while candidate:
        cost, node = heapq.heappop(candidate)

        if erased[node]:
            continue

        erased[node] = True
        answer = max(answer, cost)

        for next_node in graph[node]:
            if erased[next_node]:
                continue
            C[next_node] -= A[node]
            heapq.heappush(candidate, (C[next_node], next_node))

    print(answer)


if __name__ == "__main__":
    main()
