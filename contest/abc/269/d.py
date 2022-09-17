from typing import *
import collections
import itertools
import bisect
import math


import sys

sys.setrecursionlimit(1000000)


dx: List[int] = [-1, -1, 0, 0, 1, 1]
dy: List[int] = [-1, 0, -1, 1, 0, 1]


def dfs(
    nodes: Set[Tuple[int, int]],
    explored: Dict[Tuple[int, int], bool],
    node: Tuple[int, int],
):
    explored[node] = True
    x, y = node
    for i in range(6):
        nx: int = x + dx[i]
        ny: int = y + dy[i]
        if (nx, ny) in explored and explored[(nx, ny)]:
            continue
        if (nx, ny) in nodes:
            dfs(nodes, explored, (nx, ny))


def main():
    N: int = int(input())
    X, Y = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    nodes: Set[Tuple[int, int]] = {(x, y) for x, y in zip(X, Y)}
    explored: Dict[Tuple[int, int], bool] = {(x, y): False for x, y in zip(X, Y)}

    answer: int = 0
    for x, y in zip(X, Y):
        if explored[(x, y)]:
            continue
        dfs(nodes, explored, (x, y))
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
