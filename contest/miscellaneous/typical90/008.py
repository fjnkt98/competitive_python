from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: str = input().rstrip()

    mod: int = 1000000007

    atcoder: str = " atcoder"

    dp: List[List[int]] = [
        [1 if i == 0 else 0 for j in range(N)] for i in range(len(atcoder))
    ]

    for i in range(1, len(atcoder)):
        for j in range(N):
            if atcoder[i] == S[j]:
                dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

                dp[i][j] %= mod
            else:
                if j > 0:
                    dp[i][j] = dp[i][j - 1]

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
