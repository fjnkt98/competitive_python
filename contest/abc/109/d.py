from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    operations: List[Tuple[int, int, int, int]] = []
    for i in range(H):
        for j in range(W - 1):
            if A[i][j] & 1:
                A[i][j] -= 1
                A[i][j + 1] += 1
                operations.append((i, j, i, j + 1))

    for i in range(H - 1):
        if A[i][W - 1] & 1:
            A[i][W - 1] -= 1
            A[i + 1][W - 1] += 1
            operations.append((i, W - 1, i + 1, W - 1))

    print(len(operations))
    for op in operations:
        print(*tuple(map(lambda x: x + 1, op)))


if __name__ == "__main__":
    main()
