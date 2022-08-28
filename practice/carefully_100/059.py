from typing import *
import collections
import itertools
import bisect
import math
import heapq


def bfs(
    graph: List[List[int]], R: List[int], C: List[int], start: int
) -> List[Tuple[int, int]]:
    N: int = len(graph)
    distance: List[int] = [0 if j == start else -1 for j in range(N)]
    candidate = collections.deque([start])

    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] != -1:
                continue
            distance[next_node] = distance[node] + 1
            if distance[next_node] > R[start]:
                continue
            candidate.append(next_node)

    return [
        (j, C[start])
        for j, d in enumerate(distance)
        if d != -1 and d <= R[start] and j != start
    ]


def main():
    N, K = map(int, input().split())
    C, R = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(K)]))

    graph: List[List[int]] = [[] for i in range(N)]
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    candidate: List[Tuple[int, int]] = [(0, 0)]
    distance: List[int] = [1 << 60] * N
    distance[0] = 0

    while candidate:
        d, node = heapq.heappop(candidate)

        if d > distance[node]:
            continue

        for next_node, weight in bfs(graph, R, C, node):
            if distance[next_node] > distance[node] + weight:
                distance[next_node] = distance[node] + weight
                heapq.heappush(candidate, (distance[next_node], next_node))

    print(distance[N - 1])


if __name__ == "__main__":
    main()
