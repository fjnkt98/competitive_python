from textwrap import fill
from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, S = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    dp = [[False for j in range(S + 1)] for i in range(N + 1)]
    dp[0][0] = True
    for i in range(N + 1):
        for j in range(S + 1):
            dp[i][j] = dp[i][j] or dp[i - 1][j]

            if j - A[i - 1] >= 0:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]

    print("Yes" if dp[N][S] else "No")


if __name__ == "__main__":
    main()
