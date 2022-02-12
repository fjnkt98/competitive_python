from typing import List, Tuple
import sys
from array import array

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(
    graph: List[List[Tuple[int, int]]],
    distance: List[int],
    previous_node: int,
    current_node: int,
):
    for next_node, weight in graph[current_node]:
        if next_node == previous_node:
            continue

        distance[next_node] = distance[current_node] + weight
        dfs(graph, distance, current_node, next_node)


def main():
    N: int = int(input())
    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    for i in range(N - 1):
        s, t, w = map(int, input().split())
        graph[s].append((t, w))
        graph[t].append((s, w))

    distance: List[int] = [0 for i in range(N)]
    dfs(graph, distance, -1, 0)

    start: int = 0
    longest_distance: int = 0
    for i, d in enumerate(distance):
        if longest_distance < d:
            longest_distance = d
            start = i

    distance = [0 for i in range(N)]
    dfs(graph, distance, -1, start)

    print(max(distance))


if __name__ == "__main__":
    main()
