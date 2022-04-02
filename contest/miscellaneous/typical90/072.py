from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(
    grid: List[str],
    visited: List[List[bool]],
    start: Tuple[int, int],
    current: Tuple[int, int],
) -> int:
    H: int = len(grid)
    W: int = len(grid[0])
    r, c = current
    if start == current and visited[r][c]:
        return 0

    visited[r][c] = True

    result: int = -10000
    dr: List[int] = [1, 0, -1, 0]
    dc: List[int] = [0, 1, 0, -1]
    for i in range(4):
        nr: int = r + dr[i]
        nc: int = c + dc[i]

        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == ".":
            if (not (start == (nr, nc))) and visited[nr][nc]:
                continue
            result = max(result, dfs(grid, visited, start, (nr, nc)) + 1)

    visited[r][c] = False
    return result


def main():
    H, W = map(int, input().split())
    grid: List[str] = [input().rstrip() for i in range(H)]

    answer: int = 0
    visited: List[List[bool]] = [[False] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                answer = max(answer, dfs(grid, visited, (i, j), (i, j)))

    print(answer if answer > 2 else -1)


if __name__ == "__main__":
    main()
