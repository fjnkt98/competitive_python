from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    C: List[int] = list(map(int, input().split()))

    B: List[int] = [0] * (N + M + 1)
    for i in range(M, -1, -1):
        numerator: int = C[N + i]
        for j in range(1, N + 1):
            numerator -= A[N - j] * B[i + j]
        B[i] = numerator // A[N]

    print(*B[0:-N])


if __name__ == "__main__":
    main()
