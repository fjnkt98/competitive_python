from typing import List, Deque
import sys
from array import array
import collections


sys.setrecursionlimit(10000)
input = sys.stdin.readline


time: int = 0


def dfs(
    graph: List[List[int]], d: List[int], f: List[int], explored: List[bool], node: int
):
    global time
    explored[node] = True
    time += 1
    d[node] = time

    for next_node in graph[node]:
        if explored[next_node]:
            continue

        dfs(graph, d, f, explored, next_node)

    time += 1
    f[node] = time


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        u, k, *v = list(map(int, input().split()))
        graph[u - 1] = sorted(list(map(lambda x: x - 1, v)))

    explored: List[bool] = [False for i in range(N)]
    d: List[int] = [-1 for i in range(N)]
    f: List[int] = [-1 for i in range(N)]
    time: int = 1

    d[0] = 1
    for i in range(N):
        if explored[i]:
            continue
        dfs(graph, d, f, explored, i)

    for (i, d, f) in zip(list(range(N)), d, f):
        print(f"{i + 1} {d} {f}")


if __name__ == "__main__":
    main()
