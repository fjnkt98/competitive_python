from typing import List, Tuple, Deque
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        graph[A].append(B)
        graph[B].append(A)

    candidate: Deque[int] = collections.deque([0])
    distance: List[int] = [0 if i == 0 else -1 for i in range(N)]
    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    for d in distance:
        if d >= 120 or d == -1:
            print(120)
        else:
            print(d)


if __name__ == "__main__":
    main()
