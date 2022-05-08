from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = [0] * N
    B: List[int] = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    dp: List[List[int]] = [[-1] * (M + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(M + 1):
            if dp[i - 1][j] >= 0:
                dp[i][j] = B[i - 1]
            elif j < A[i - 1] or dp[i][j - A[i - 1]] <= 0:
                dp[i][j] = -1
            else:
                dp[i][j] = dp[i][j - A[i - 1]] - 1

    print("Yes" if dp[N][M] != -1 else "No")


if __name__ == "__main__":
    main()
