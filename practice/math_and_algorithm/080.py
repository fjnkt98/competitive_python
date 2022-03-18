from typing import List, Tuple
import sys
from array import array
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1

        graph[A].append((B, C))
        graph[B].append((A, C))

    candidate: List[Tuple[int, int]] = []
    heapq.heappush(candidate, (0, 0))
    distance: List[int] = [0 if i == 0 else 1 << 60 for i in range(N)]
    while candidate:
        d, v = heapq.heappop(candidate)

        if distance[v] < d:
            continue

        for next_node, weight in graph[v]:
            if distance[next_node] > distance[v] + weight:
                distance[next_node] = distance[v] + weight
                heapq.heappush(candidate, (distance[next_node], next_node))

    print(-1 if distance[-1] == 1 << 60 else distance[-1])


if __name__ == "__main__":
    main()
