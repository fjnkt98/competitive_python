from typing import List, Deque
import sys
from array import array
import collections


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        u, k, *v = list(map(int, input().split()))
        graph[u - 1] = sorted(list(map(lambda x: x - 1, v)))

    distance: List[int] = [-1 for i in range(N)]
    candidate: Deque[int] = collections.deque()

    distance[0] = 0
    candidate.append(0)
    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] != -1:
                continue
            distance[next_node] = distance[node] + 1
            candidate.append(next_node)

    for i, d in enumerate(distance):
        print(f"{i + 1} {d}")


if __name__ == "__main__":
    main()
