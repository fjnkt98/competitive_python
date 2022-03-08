from typing import List, Tuple, Deque
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    R, C = map(int, input().split())
    sr, sc = map(int, input().split())
    sr -= 1
    sc -= 1
    s: Tuple[int, int] = (sr, sc)
    gr, gc = map(int, input().split())
    gr -= 1
    gc -= 1
    g: Tuple[int, int] = (gr, gc)

    grid: List[str] = ["" for i in range(R)]
    for i in range(R):
        grid[i] = input().rstrip()

    candidate: Deque[Tuple[int, int]] = collections.deque([s])
    distance: List[List[int]] = [[-1 for j in range(C)] for i in range(R)]
    distance[sr][sc] = 0

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    while candidate:
        r, c = candidate.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == ".":
                if distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1
                    candidate.append((nr, nc))

    print(distance[gr][gc])


if __name__ == "__main__":
    main()
