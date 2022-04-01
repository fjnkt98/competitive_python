from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = [1]
    for i in [6, 9]:
        for j in range(N):
            C: int = pow(i, j)
            if C > N:
                break
            A.append(C)
    A = sorted(list(set(A)))

    dp: List[int] = [1 << 60] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0:
                dp[i] = min(dp[i], dp[i - a] + 1)

    print(dp[N])


if __name__ == "__main__":
    main()
