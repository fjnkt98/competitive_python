from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    h: List[int] = list(map(int, input().split()))

    dp: List[int] = [9999999 for i in range(N)]
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
