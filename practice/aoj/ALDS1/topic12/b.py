from typing import List, Tuple
import sys
from array import array
import heapq


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(N):
        u, k, *a = list(map(int, input().split()))

        edges: List[Tuple[int, int]] = []
        for j in range(k):
            edges.append((a[2 * j], a[2 * j + 1]))

        graph[u] = edges

    distance: List[int] = [1000000000 for i in range(N)]
    distance[0] = 0

    heap: List[Tuple[int, int]] = [[0, 0]]

    while heap:
        d, v = heapq.heappop(heap)

        if d > distance[v]:
            continue

        for node, weight in graph[v]:
            if distance[node] > distance[v] + weight:
                distance[node] = distance[v] + weight
                heapq.heappush(heap, (distance[node], node))

    for i, d in enumerate(distance):
        print(f"{i} {d}")


if __name__ == "__main__":
    main()
