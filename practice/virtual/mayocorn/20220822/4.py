from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W = map(int, input().split())
    grid: List[List[str]] = [list(input()) for i in range(H)]

    distance: List[List[int]] = [[-1] * W for i in range(H)]
    distance[0][0] = 1
    candidate = collections.deque([(0, 0)])

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

    count: int = sum([row.count(".") for row in grid])
    print(count - distance[-1][-1] if distance[-1][-1] != -1 else -1)


if __name__ == "__main__":
    main()
