from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    R: List[int] = list(map(int, input().split()))

    dp: List[List[int]] = [[0] * 2 for i in range(N)]
    dp[0] = [1, 1]

    for i in range(1, N):
        for j in range(N):
            if R[i] < R[j]:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)

            if R[i] > R[j]:
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)

    answer: int = max(dp[-1])
    print(answer if answer >= 3 else 0)


if __name__ == "__main__":
    main()
