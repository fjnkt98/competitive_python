from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    P: List[int] = list(map(int, input().split()))
    graph: List[List[int]] = [[] for i in range(N)]
    for i, p in enumerate(P):
        graph[p - 1].append(i + 1)

    distance: List[int] = [-1] * N
    distance[0] = 0
    candidate = collections.deque([0])
    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    print(distance[-1])


if __name__ == "__main__":
    main()
