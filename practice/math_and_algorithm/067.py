from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    grid: np.ndarray = np.array(
        [list(map(int, input().split())) for i in range(H)], dtype=np.int64
    )

    answer: np.ndarray = np.zeros((H, W), dtype=np.int64)
    row_sum: array = array("q", [0 for i in range(H)])
    for i in range(H):
        row_sum[i] = np.sum(grid[i])

    col_sum: array = array("q", [0 for i in range(W)])
    for j in range(W):
        col_sum[j] = np.sum(grid[:, j])

    for i in range(H):
        for j in range(W):
            answer[i, j] = row_sum[i] + col_sum[j] - grid[i, j]

    for r in answer.tolist():
        print(*r)


if __name__ == "__main__":
    main()
