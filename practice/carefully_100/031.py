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
    W, H = map(int, input().split())
    grid: List[List[int]] = (
        [[0] * (W + 2)]
        + [[0] + list(map(int, input().split())) + [0] for i in range(H)]
        + [[0] * (W + 2)]
    )

    dr: List[int] = [-1, -1, 0, 1, 1, 0]
    dc_even: List[int] = [0, -1, -1, -1, 0, 1]
    dc_odd: List[int] = [1, 0, -1, 0, 1, 1]

    candidate = collections.deque([(0, 0)])
    distance: List[List[int]] = [[-1] * (W + 2) for i in range(H + 2)]
    distance[0][0] = 0

    answer: int = 0

    while candidate:
        r, c = candidate.popleft()

        for i in range(6):
            nr: int = r + dr[i]
            if r % 2 == 0:
                nc: int = c + dc_even[i]
            else:
                nc: int = c + dc_odd[i]

            if 0 <= nr < (H + 2) and 0 <= nc < (W + 2):
                if grid[nr][nc] == 1:
                    answer += 1
                else:
                    if distance[nr][nc] == -1:
                        distance[nr][nc] = distance[r][c] + 1
                        candidate.append((nr, nc))

    print(answer)


if __name__ == "__main__":
    main()
