from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    B: List[List[int]] = [[0] * W for i in range(H)]

    row_sum: List[int] = [0] * H
    col_sum: List[int] = [0] * W

    for i in range(H):
        row_sum[i] = sum(A[i])

    for j in range(W):
        total = 0
        for i in range(H):
            total += A[i][j]

        col_sum[j] = total

    for i in range(H):
        for j in range(W):
            B[i][j] = row_sum[i] + col_sum[j] - A[i][j]

    for b in B:
        print(*b)


if __name__ == "__main__":
    main()
