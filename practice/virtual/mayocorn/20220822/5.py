from typing import *
import collections
import itertools


def main():
    H, W = map(int, input().split())
    grid: List[List[str]] = [list(input().rstrip()) for i in range(H)]

    alpha: Set[str] = {chr(code) for code in range(ord("a"), ord("z") + 1)}
    start: Tuple[int, int] = (-1, -1)
    goal: Tuple[int, int] = (-1, -1)
    teleporter: Dict[str, Set[Tuple[int, int]]] = {c: set() for c in alpha}

    for i, j in itertools.product(range(H), range(W)):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "G":
            goal = (i, j)
        elif grid[i][j] == "." or grid[i][j] == "#":
            continue
        else:
            teleporter[grid[i][j]].add((i, j))

    distance: List[List[int]] = [[-1] * W for i in range(H)]
    sr, sc = start
    distance[sr][sc] = 0
    candidate = collections.deque([start])
    direction: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    explored: Set[str] = set()

    while candidate:
        r, c = candidate.popleft()

        if (r, c) == goal:
            break

        for dr, dc in direction:
            nr: int = r + dr
            nc: int = c + dc

            if (
                0 <= nr < H
                and 0 <= nc < W
                and grid[nr][nc] != "#"
                and distance[nr][nc] == -1
            ):
                distance[nr][nc] = distance[r][c] + 1
                candidate.append((nr, nc))

            if grid[r][c] in alpha and grid[r][c] not in explored:
                explored.add(grid[r][c])
                for nr, nc in teleporter[grid[r][c]]:
                    if (r, c) == (nr, nc):
                        continue
                    if distance[nr][nc] == -1:
                        distance[nr][nc] = distance[r][c] + 1
                        candidate.append((nr, nc))

    gr, gc = goal
    print(distance[gr][gc])


if __name__ == "__main__":
    main()
