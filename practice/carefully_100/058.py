from typing import *
import collections
import itertools
import bisect
import math
import heapq


def main():
    N, M, K, S = map(int, input().split())
    P, Q = map(int, input().split())
    C: Set[int] = set([int(input()) - 1 for i in range(K)])
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    cost: List[int] = [0] * N
    for c in C:
        cost[c] = S + 1
    candidate = collections.deque(C)
    while candidate:
        node: int = candidate.popleft()
        if cost[node] == 0:
            continue
        for next_node in graph[node]:
            if cost[next_node] != 0:
                continue
            cost[next_node] = cost[node] - 1
            candidate.append(next_node)

    dominated: List[bool] = [c != 0 for c in cost]
    wgraph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(N):
        for j in graph[i]:
            if j == N - 1:
                wgraph[i].append((j, 0))
            elif dominated[j]:
                wgraph[i].append((j, Q))
            else:
                wgraph[i].append((j, P))

    distance: List[int] = [1 << 60 for i in range(N)]
    candidate: List[Tuple[int, int]] = [(0, 0)]
    # Set zero to the distance of the start node.
    distance[0] = 0

    # Start to search dijkstra
    while candidate:
        d, node = heapq.heappop(candidate)

        if d > distance[node]:
            continue

        for next_node, weight in wgraph[node]:
            if next_node in C:
                continue
            if distance[next_node] > distance[node] + weight:
                distance[next_node] = distance[node] + weight
                heapq.heappush(candidate, (distance[next_node], next_node))

    print(distance[N - 1])


if __name__ == "__main__":
    main()
