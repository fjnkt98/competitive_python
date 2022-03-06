from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))

    # 0 -> not study, 1 -> study
    dp: List[List[int]] = [[0 for j in range(2)] for i in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + A[i - 1]

    print(max(dp[N][0], dp[N][1]))


if __name__ == "__main__":
    main()
