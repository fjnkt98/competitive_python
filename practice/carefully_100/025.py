from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(grid: List[List[int]], node: Tuple[int, int]):
    dr: List[int] = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc: List[int] = [1, 0, -1, -1, -1, 0, 1, 1]

    H: int = len(grid)
    W: int = len(grid[0])

    r, c = node
    grid[r][c] = 0

    for i in range(8):
        nr: int = r + dr[i]
        nc: int = c + dc[i]

        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 1:
            dfs(grid, (nr, nc))


def main():

    answer: List[int] = []

    while True:
        W, H = map(int, input().split())
        if (W, H) == (0, 0):
            break
        grid: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

        count: int = 0
        for i, j in itertools.product(range(H), range(W)):
            if grid[i][j] == 1:
                count += 1
                dfs(grid, (i, j))

        answer.append(count)

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
