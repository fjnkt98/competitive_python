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
        graph[A - 1].append(B - 1)
        graph[B - 1].append(A - 1)

    candidate: Deque[int] = collections.deque([0])
    distance: List[int] = [-1 for i in range(N)]
    distance[0] = 0

    while candidate:
        node: int = candidate.popleft()

        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    ok: bool = True
    for d in distance:
        if d == -1:
            ok = False

    print("The graph is connected." if ok else "The graph is not connected.")


if __name__ == "__main__":
    main()
