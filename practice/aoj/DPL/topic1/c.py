from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    V: List[int] = [0] * N
    W: List[int] = [0] * N
    for i in range(N):
        V[i], W[i] = map(int, input().split())

    dp: List[List[int]] = [[0] * (X + 1) for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(X + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

            if j - W[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - W[i - 1]] + V[i - 1])

    print(dp[N][X])


if __name__ == "__main__":
    main()
