from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    indegree: List[int] = [0] * N
    for i in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
        indegree[y] += 1

    candidate = collections.deque([i for i, d in enumerate(indegree) if d == 0])
    order: List[int] = []
    while candidate:
        node = candidate.popleft()
        order.append(node)

        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                candidate.append(next_node)

    dp: List[int] = [0] * N
    for node in order:
        for next_node in graph[node]:
            dp[next_node] = max(dp[next_node], dp[node] + 1)

    print(max(dp))


if __name__ == "__main__":
    main()
