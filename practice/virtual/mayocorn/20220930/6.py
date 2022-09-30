from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


time: int = -1


def dfs(
    graph: List[List[int]],
    E: List[List[int]],
    T: List[List[int]],
    depth: int,
    current: int,
    previous: int,
):
    global time

    time += 1

    T[current][0] = time
    E[depth].append(time)

    for next_node in graph[current]:
        if next_node == previous:
            continue
        dfs(graph, E, T, depth + 1, next_node, current)

    time += 1
    T[current][1] = time


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i, p in enumerate(map(int, input().split())):
        graph[p - 1].append(i + 1)

    Q: int = int(input())
    U, D = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    E: List[List[int]] = [[] for i in range(N)]
    T: List[List[int]] = [[0, 0] for i in range(N)]
    dfs(graph, E, T, 0, 0, -1)
    for i in range(N):
        E[i].sort()

    for u, d in zip(U, D):
        u -= 1
        answer: int = 0
        left: int = bisect.bisect_left(E[d], T[u][0])
        right: int = bisect.bisect_left(E[d], T[u][1])
        print(right - left)


if __name__ == "__main__":
    main()
