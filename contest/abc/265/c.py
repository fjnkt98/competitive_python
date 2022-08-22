from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W = map(int, input().split())
    grid: List[List[str]] = [list(input()) for i in range(H)]

    position: Tuple[int, int] = (0, 0)
    explored: List[List[bool]] = [[False] * W for i in range(H)]

    D: Dict[str, Tuple[int, int]] = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    stuck: bool = False
    while not stuck:
        r, c = position
        if explored[r][c] is True:
            print(-1)
            return
        explored[r][c] = True

        if grid[r][c] == "U":
            if r != 0:
                position = (r - 1, c)
            else:
                stuck = True
        elif grid[r][c] == "D":
            if r != H - 1:
                position = (r + 1, c)
            else:
                stuck = True
        elif grid[r][c] == "L":
            if c != 0:
                position = (r, c - 1)
            else:
                stuck = True
        elif grid[r][c] == "R":
            if c != W - 1:
                position = (r, c + 1)
            else:
                stuck = True

    r, c = position
    print(r + 1, c + 1)


if __name__ == "__main__":
    main()
