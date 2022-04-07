from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(3)]

    A = list(zip(*A))

    dp: List[List[int]] = [[1 << 60] * 3 for i in range(N)]
    dp[0] = [0, 0, 0]
    for i in range(1, N):
        for j in range(3):
            for k in range(3):
                dp[i][j] = min(dp[i][j], abs(A[i][j] - A[i - 1][k]) + dp[i - 1][k])

    print(min(dp[-1]))


if __name__ == "__main__":
    main()
