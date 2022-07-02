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
    H, W, N = map(int, input().split())
    grid: List[str] = [input() for i in range(H)]

    coordinates: List[Tuple[int, int]] = [(0, 0)] * (N + 1)
    for i, j in itertools.product(range(H), range(W)):
        if grid[i][j] == "." or grid[i][j] == "X":
            continue
        elif grid[i][j] == "S":
            coordinates[0] = (i, j)
        else:
            coordinates[int(grid[i][j])] = (i, j)

    answer: int = 0
    for start, end in zip(coordinates[:-1], coordinates[1:]):
        sr, sc = start
        gr, gc = end

        candidate = collections.deque([start])
        distance: List[List[int]] = [[-1] * W for i in range(H)]
        distance[sr][sc] = 0

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
                    and grid[nr][nc] != "X"
                    and distance[nr][nc] == -1
                ):
                    distance[nr][nc] = distance[r][c] + 1
                    candidate.append((nr, nc))

        answer += distance[gr][gc]

    print(answer)


if __name__ == "__main__":
    main()
