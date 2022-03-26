from typing import List, Tuple
import sys
import collections
import itertools
import copy


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    mod: int = 1000000007
    dp: List[List[int]] = [[0] * 6 for i in range(N)]
    dp[0] = copy.copy(A[0])
    for i in range(1, N):
        for j in range(6):
            for k in range(6):
                dp[i][j] += A[i][j] * dp[i - 1][k]
            dp[i][j] %= mod

    print(sum(dp[N - 1]) % mod)


if __name__ == "__main__":
    main()
