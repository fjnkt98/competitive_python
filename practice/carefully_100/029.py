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
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    grid: List[str] = [input() for i in range(H)]

    sr -= 1
    sc -= 1
    gr -= 1
    gc -= 1

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    distance: List[List[int]] = [[-1] * W for i in range(H)]
    distance[sr][sc] = 0

    candidate = collections.deque([(sr, sc)])

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

    print(distance[gr][gc])


if __name__ == "__main__":
    main()
