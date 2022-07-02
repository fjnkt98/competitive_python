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

    white: int = 0
    for r in grid:
        white += r.count(".")

    white -= 1

    candidate = collections.deque([(0, 0)])
    distance: List[List[int]] = [[-1] * W for i in range(H)]
    distance[0][0] = 0

    while candidate:
        r, c = candidate.popleft()

        for dr, dc in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nr: int = r + dr
            nc: int = c + dc

            if (
                0 <= nr < H
                and 0 <= nc < W
                and grid[nr][nc] == "."
                and distance[nr][nc] == -1
            ):
                distance[nr][nc] = distance[r][c] + 1
                candidate.append((nr, nc))

    if distance[-1][-1] == -1:
        print(-1)
    else:
        print(white - distance[-1][-1])


if __name__ == "__main__":
    main()
