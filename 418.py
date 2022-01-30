from typing import List, Deque
from sys import setrecursionlimit
import collections


setrecursionlimit(10000)


def main():
    N, M = map(int, input().split())
    G: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)

    candidate: Deque[int] = collections.deque([0])
    distance: List[int] = [-1 for i in range(N)]
    distance[0] = 0

    while candidate:
        node: int = candidate.popleft()

        for next_node in G[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    print(max(distance))


if __name__ == "__main__":
    main()
