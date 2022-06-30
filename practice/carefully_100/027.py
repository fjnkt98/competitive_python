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


def dfs(grid: List[List[int]], node: Tuple[int, int]) -> int:
    stuck: bool = True

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    H: int = len(grid)
    W: int = len(grid[0])

    r, c = node
    grid[r][c] = 0

    count: int = 0

    for i in range(4):
        nr: int = r + dr[i]
        nc: int = c + dc[i]

        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 1:
            stuck = False
            count = max(count, dfs(grid, (nr, nc)))

    grid[r][c] = 1

    if stuck:
        return 1
    else:
        return count + 1


def main():
    M: int = int(input())
    N: int = int(input())
    grid: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    answer: int = 0
    for i, j in itertools.product(range(N), range(M)):
        if grid[i][j] == 1:
            answer = max(answer, dfs(grid, (i, j)))

    print(answer)


if __name__ == "__main__":
    main()
