from typing import List, Tuple, Deque
import sys
from array import array
from collections import deque


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

    queue: Deque = deque()
    result: List[int] = []
    for i, d in enumerate(indegree):
        if d == 0:
            queue.append(i)

    while queue:
        node: int = queue.popleft()

        result.append(node)
        for next_node in graph[node]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    if len(result) == N:
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    main()
