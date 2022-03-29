from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]
    B: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    operation: int = 0
    for i in range(H - 1):
        for j in range(W - 1):
            diff: int = A[i][j] - B[i][j]
            if diff != 0:
                A[i][j] -= diff
                A[i + 1][j] -= diff
                A[i][j + 1] -= diff
                A[i + 1][j + 1] -= diff
                operation += abs(diff)

    ok: bool = True
    for i in range(H):
        if A[i][-1] != B[i][-1]:
            ok = False

    for j in range(W):
        if A[-1][j] != B[-1][j]:
            ok = False

    if ok:
        print("Yes")
        print(operation)
    else:
        print("No")


if __name__ == "__main__":
    main()
