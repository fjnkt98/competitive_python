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
    edges: List[Tuple[int, int]] = list(
        set([tuple(map(lambda s: int(s) - 1, input().split())) for i in range(M)])
    )
    for a, b in edges:
        graph[a].append(b)
        rgraph[b].append(a)

    explored: List[bool] = [False] * N
    order: List[int] = []
    for i in range(N):
        if explored[i]:
            continue
        dfs(graph, explored, i, order)

    component: List[int] = [-1] * N
    explored = [False] * N
    k: int = 0
    for node in reversed(order):
        if explored[node]:
            continue
        rdfs(rgraph, explored, component, node, k)
        k += 1

    count = collections.Counter(component)
    answer: int = 0
    for key, value in count.items():
        if key == -1:
            continue
        answer += value * (value - 1) // 2

    print(answer)


if __name__ == "__main__":
    main()
