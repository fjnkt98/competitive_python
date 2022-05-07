from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    C: List[int] = [0] + list(map(int, input().split()))

    dp: List[List[int]] = [[1 << 60] * (N + 1) for i in range(M + 1)]
    for i in range(M + 1):
        dp[i][0] = 0

    for i in range(1, M + 1):
        for j in range(N + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j])

            if j - C[i] >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - C[i]] + 1)

    print(dp[M][N])


if __name__ == "__main__":
    main()
