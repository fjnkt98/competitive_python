from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        graph[A].append(B)
        graph[B].append(A)

    diameter: int = 0

    candidate: Deque[int] = collections.deque([0])
    distance: List[int] = [0 if i == 0 else -1 for i in range(N)]

    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    start: int = distance.index(max(distance))

    candidate.append(start)
    distance = [0 if i == start else -1 for i in range(N)]

    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    print(max(distance) + 1)


if __name__ == "__main__":
    main()
