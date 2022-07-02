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
input = sys.stdin.readline


def main():
    answer: List[int] = []

    while True:
        N, M = map(int, input().split())

        if (N, M) == (0, 0):
            break

        H: int = 2 * M - 1
        W: int = 2 * N - 1

        grid: List[List[int]] = [[0] * W if i % 2 == 0 else [1] * W for i in range(H)]

        for i in range(H):
            if i % 2 == 0:
                for j, w in enumerate(list(map(int, input().split()))):
                    if w == 1:
                        grid[i][2 * j + 1] = 1

            else:
                for j, w in enumerate(list(map(int, input().split()))):
                    if w == 0:
                        grid[i][2 * j] = 0

        candidate = collections.deque([(0, 0)])
        distance: List[List[int]] = [[-1] * W for i in range(H)]
        distance[0][0] = 0

        dr: List[int] = [0, 1, 0, -1]
        dc: List[int] = [1, 0, -1, 0]

        while candidate:
            r, c = candidate.popleft()

            for i in range(4):
                nr_d: int = r + dr[i]
                nc_d: int = c + dc[i]
                nr: int = r + 2 * dr[i]
                nc: int = c + 2 * dc[i]

                if (
                    0 <= nr < H
                    and 0 <= nc < W
                    and grid[nr_d][nc_d] == 0
                    and distance[nr][nc] == -1
                ):
                    distance[nr][nc] = distance[r][c] + 1
                    candidate.append((nr, nc))

        answer.append(distance[-1][-1] + 1)

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
