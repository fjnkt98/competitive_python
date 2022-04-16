from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(graph: List[List[int]], explored: List[bool], node: int, order: List[int]):
    explored[node] = True

    for next_node in graph[node]:
        if explored[next_node]:
            continue
        dfs(graph, explored, next_node, order)

    order.append(node)


def rdfs(
    graph: List[List[int]],
    explored: List[bool],
    component: List[int],
    node: int,
    k: int,
) -> None:
    explored[node] = True
    component[node] = k

    for next_node in graph[node]:
        if explored[next_node]:
            continue
        rdfs(graph, explored, component, next_node, k)


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    rgraph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        s, t = map(int, input().split())
        graph[s].append(t)
        rgraph[t].append(s)

    Q: int = int(input())
    query: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(Q)]

    explored: List[bool] = [False] * N
    order: List[int] = []
    for node in range(N):
        if explored[node]:
            continue
        dfs(graph, explored, node, order)

    component: List[int] = [-1] * N
    explored = [False] * N
    k: int = 0
    for node in reversed(order):
        if explored[node]:
            continue
        rdfs(rgraph, explored, component, node, k)
        k += 1

    for u, v in query:
        if component[u] == -1 or component[v] == -1:
            print(0)
            continue

        if component[u] == component[v]:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
