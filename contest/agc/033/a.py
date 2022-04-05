from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    H, W = map(int, input().split())
    grid: List[List[str]] = [list(input()) for i in range(H)]

    candidate: Deque[Tuple[int, int, int]] = collections.deque([])
    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                candidate.append((i, j, 0))

    answer: int = 0
    while candidate:
        row, col, count = candidate.popleft()

        for i in range(4):
            nr: int = row + dr[i]
            nc: int = col + dc[i]

            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == ".":
                grid[nr][nc] = "#"
                candidate.append((nr, nc, count + 1))

        answer = max(answer, count + 1)

    print(answer - 1)


if __name__ == "__main__":
    main()
