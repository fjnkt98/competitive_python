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


def main():
    H, W = map(int, input().split())
    grid: List[str] = [input() for i in range(H)]

    candidate = collections.deque([(0, 0)])
    distance: List[List[int]] = [[-1] * W for i in range(H)]
    distance[0][0] = 0

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    while candidate:
        r, c = candidate.popleft()

        for i in range(4):
            nr: int = r + dr[i]
            nc: int = c + dc[i]

            if (
                0 <= nr < H
                and 0 <= nc < W
                and grid[nr][nc] == "."
                and distance[nr][nc] == -1
            ):
                distance[nr][nc] = distance[r][c] + 1
                candidate.append((nr, nc))

    if distance[H - 1][W - 1] == -1:
        print(-1)
        return

    answer: int = 0
    for row in grid:
        answer += row.count(".")

    answer -= distance[H - 1][W - 1] + 1
    print(answer)


if __name__ == "__main__":
    main()
