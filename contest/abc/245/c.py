from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    dpA: List[bool] = [False] * N
    dpB: List[bool] = [False] * N
    dpA[0] = True
    dpB[0] = True

    for i in range(1, N):
        if dpA[i - 1]:
            if abs(A[i] - A[i - 1]) <= K:
                dpA[i] = True
            if abs(B[i] - A[i - 1]) <= K:
                dpB[i] = True
        if dpB[i - 1]:
            if abs(A[i] - B[i - 1]) <= K:
                dpA[i] = True
            if abs(B[i] - B[i - 1]) <= K:
                dpB[i] = True

    print("Yes" if dpA[-1] or dpB[-1] else "No")


if __name__ == "__main__":
    main()
