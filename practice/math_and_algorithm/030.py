from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, W = map(int, input().split())
    w: List[int] = [0 for i in range(N)]
    v: List[int] = [0 for i in range(N)]
    for i in range(N):
        w[i], v[i] = map(int, input().split())

    dp: List[List[int]] = [[0 for j in range(W + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j - w[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

    print(dp[N][W])


if __name__ == "__main__":
    main()
