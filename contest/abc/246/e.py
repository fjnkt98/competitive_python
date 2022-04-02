from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Ax -= 1
    Ay -= 1
    Bx -= 1
    By -= 1
    grid: List[str] = [input().rstrip() for i in range(N)]

    # if (Ax + Ay) % 2 != (Bx + By) % 2:
    #     print(-1)
    #     return

    distance: List[List[int]] = [[1 << 60] * N for i in range(N)]
    distance[Ax][Ay] = 0

    dx: List[int] = [1, 1, -1, -1]
    dy: List[int] = [1, -1, 1, -1]

    candidate: Deque[Tuple[int, int, int, int]] = collections.deque()
    for i in range(4):
        nx: int = Ax + dx[i]
        ny: int = Ay + dy[i]
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == ".":
            distance[nx][ny] = 1
            candidate.append((nx, ny, i, 1))

    while candidate:
        x, y, d, c = candidate.popleft()

        if c > distance[x][y]:
            continue

        for i in range(4):
            nx: int = x + dx[i]
            ny: int = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == ".":
                if d == i:
                    if c <= distance[nx][ny]:
                        distance[nx][ny] = distance[x][y]
                        candidate.appendleft((nx, ny, i, c))
                else:
                    if c < distance[nx][ny]:
                        distance[nx][ny] = distance[x][y] + 1
                        candidate.append((nx, ny, i, c + 1))

    print(distance[Bx][By] if distance[Bx][By] != 1 << 60 else -1)


if __name__ == "__main__":
    main()
