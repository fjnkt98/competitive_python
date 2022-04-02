from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W, A, B = map(int, input().split())

    grid: List[List[int]] = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if 0 <= i < B:
                grid[i][j] = 0 if 0 <= j < A else 1
            else:
                grid[i][j] = 1 if 0 <= j < A else 0

    for g in grid:
        print(*g, sep="")


if __name__ == "__main__":
    main()
