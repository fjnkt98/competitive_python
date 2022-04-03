from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    left: int = -1
    right: int = 10 ** 9

    limit: int = (K * K) // 2 + 1

    while right - left > 1:
        mid: int = (right + left) // 2

        S: List[List[int]] = [[0] * (N + 1) for i in range(N + 1)]
        for i in range(N):
            for j in range(N):
                S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j]
                if A[i][j] > mid:
                    S[i + 1][j + 1] += 1

        ok: bool = False
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if (S[i + K][j + K] + S[i][j] - S[i][j + K] - S[i + K][j]) < limit:
                    ok = True

        if ok:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
