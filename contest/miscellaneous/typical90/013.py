from typing import List, Tuple, Deque
import sys
import collections
import itertools
import heapq


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dijkstra(graph: List[List[Tuple[int, int]]], start: int) -> List[int]:
    N: int = len(graph)
    candidate: List[Tuple[int, int]] = [(0, start)]
    distance: List[int] = [0 if i == start else 1 << 60 for i in range(N)]

    while candidate:
        d, node = heapq.heappop(candidate)

        if d > distance[node]:
            continue

        for next_node, weight in graph[node]:
            if distance[next_node] > distance[node] + weight:
                distance[next_node] = distance[node] + weight
                heapq.heappush(candidate, (distance[next_node], next_node))

    return distance


def main():
    N, M = map(int, input().split())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a - 1].append((b - 1, c))
        graph[b - 1].append((a - 1, c))

    distance_from_0: List[int] = dijkstra(graph, 0)
    distance_from_N: List[int] = dijkstra(graph, N - 1)

    for i in range(N):
        answer: int = distance_from_0[i] + distance_from_N[i]
        print(answer)


if __name__ == "__main__":
    main()
