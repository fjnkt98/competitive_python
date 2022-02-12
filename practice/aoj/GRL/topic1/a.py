from typing import List, Tuple
import sys
from array import array
import heapq


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M, r = map(int, input().split())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(M):
        s, t, d = map(int, input().split())
        graph[s].append((t, d))

    distance: List[int] = [int(1e9) for i in range(N)]
    distance[r] = 0

    heap: List[Tuple[int, int]] = []
    heapq.heappush(heap, (0, r))

    while heap:
        d, v = heapq.heappop(heap)

        if d > distance[v]:
            continue

        for node, weight in graph[v]:
            if distance[node] > distance[v] + weight:
                distance[node] = distance[v] + weight
                heapq.heappush(heap, (distance[node], node))

    for d in distance:
        if d == int(1e9):
            print("INF")
        else:
            print(d)


if __name__ == "__main__":
    main()
