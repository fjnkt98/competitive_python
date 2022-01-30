from typing import List, Deque
from sys import setrecursionlimit
import collections


setrecursionlimit(10000)


def main():
    N, M = map(int, input().split())
    G: List[List[int]] = [[] for i in range(N)]
    indegree: List[int] = [0 for i in range(N)]
    for i in range(M):
        F, S = map(int, input().split())
        G[F].append(S)
        indegree[S] += 1

    candidate: Deque[int] = collections.deque()
    for i, d in enumerate(indegree):
        if d == 0:
            candidate.append(i)

    result: List[int] = []
    while candidate:
        node = candidate.popleft()

        result.append(node)
        for next_node in G[node]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                candidate.append(next_node)

    if len(result) == N:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
