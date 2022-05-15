from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = [0] + list(map(int, input().split()))

    dp: List[List[int]] = [[0] * 2 for i in range(N + 1)]
    answer: int = 1 << 60
    for j in [0, 1]:
        dp[1][j] = A[1] * j
        dp[1][1 - j] = 1 << 60
        for i in range(2, N + 1):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]

        if j == 0:
            answer = min(answer, dp[N][1])
        else:
            answer = min(answer, dp[N][0], dp[N][1])

    print(answer)


if __name__ == "__main__":
    main()
