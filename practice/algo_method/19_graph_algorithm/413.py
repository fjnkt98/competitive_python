from typing import List, Deque
import collections
from sys import setrecursionlimit


setrecursionlimit(10000)


def main():
    N, M, X = map(int, input().split())
    G: List[List[int]] = [[] for i in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)

    distance: List[int] = [-1 for i in range(N)]
    distance[X] = 0

    candidate: Deque[int] = collections.deque([X])

    while candidate:
        node: int = candidate.popleft()

        for next_node in G[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                candidate.append(next_node)

    answer: List[int] = []
    for i, d in enumerate(distance):
        if d == 2:
            answer.append(i)

    print(len(answer))


if __name__ == "__main__":
    main()
