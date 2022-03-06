from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())

    dp: List[int] = [0 for i in range(N + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[N])


if __name__ == "__main__":
    main()
