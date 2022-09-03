from typing import *
import collections
import itertools
import bisect
import math
import operator
import heapq


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    W: Dict[int, int] = {i: a for i, a in enumerate(A)}
    graph: List[Set[int]] = [set() for i in range(N)]
    wgraph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].add(v)
        graph[v].add(u)
        wgraph[u].append(W[v])
        wgraph[v].append(W[u])

    cost: List[Tuple[int, int]] = [(sum(w), i) for i, w in enumerate(wgraph)]
    C = [0 for i in range(N)]
    for w, i in cost:
        C[i] = w
    eliminated = [False] * N
    heapq.heapify(cost)

    answer: int = 0
    while cost:
        w, node = heapq.heappop(cost)

        if eliminated[node]:
            continue

        answer = max(answer, w)

        for next_node in graph[node]:
            graph[next_node].remove(node)
            C[next_node] -= A[node]
            heapq.heappush(cost, (C[next_node], next_node))

        eliminated[node] = True

    print(answer)


if __name__ == "__main__":
    main()
