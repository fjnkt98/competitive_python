from typing import List, Deque
import sys
from array import array
import collections


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    indegree: List[int] = [0 for i in range(N)]
    for i in range(M):
        s, t = map(int, input().split())
        graph[s].append(t)
        indegree[t] += 1

    candidate: Deque = collections.deque()
    for i, d in enumerate(indegree):
        if d == 0:
            candidate.append(i)

    result: List[int] = []
    while candidate:
        node: int = candidate.popleft()

        result.append(node)

        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                candidate.append(next_node)

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
