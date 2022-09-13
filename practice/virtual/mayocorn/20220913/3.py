from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


def dfs(
    graph: List[List[int]],
    T: List[int],
    explored: List[bool],
    current: int,
) -> int:
    time: int = 0

    for next_node in graph[current]:
        if explored[next_node]:
            continue
        time += dfs(graph, T, explored, next_node)

    time += T[current]

    explored[current] = True
    return time


def main():
    N: int = int(input())
    T: List[int] = [0] * N
    K: List[int] = [0] * N
    A: List[List[int]] = [[] for i in range(N)]
    for i in range(N):
        t, k, *a = map(int, input().split())
        T[i] = t
        K[i] = k
        A[i] = list(map(lambda x: x - 1, a))

    explored: List[bool] = [False] * N

    print(dfs(A, T, explored, N - 1))


if __name__ == "__main__":
    main()
