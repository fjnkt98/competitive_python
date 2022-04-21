from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    H, W = map(int, input().split())
    grid: List[str] = [input() for i in range(H)]

    Z: List[List[int]] = [[1 << 60] * W for i in range(H)]
    if grid[0][0] == "#":
        Z[0][0] = 1
    else:
        Z[0][0] = 0

    for i in range(H):
        for j in range(W):
            if i + 1 < H:
                if grid[i][j] == "." and grid[i + 1][j] == "#":
                    Z[i + 1][j] = min(Z[i + 1][j], Z[i][j] + 1)
                else:
                    Z[i + 1][j] = min(Z[i + 1][j], Z[i][j])

            if j + 1 < W:
                if grid[i][j] == "." and grid[i][j + 1] == "#":
                    Z[i][j + 1] = min(Z[i][j + 1], Z[i][j] + 1)
                else:
                    Z[i][j + 1] = min(Z[i][j + 1], Z[i][j])

    print(Z[H - 1][W - 1])


if __name__ == "__main__":
    main()
