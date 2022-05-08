from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[False for j in range(M + 1)] for i in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] = dp[i][j] or dp[i - 1][j]

            if j - A[i - 1] >= 0:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]

    print("Yes" if dp[N][M] else "No")


if __name__ == "__main__":
    main()
