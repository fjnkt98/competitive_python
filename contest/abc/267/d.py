from typing import *
import collections
import itertools
import bisect
import math
import random


def solve(N, M, A):
    dp: List[List[int]] = [[-(1 << 60) for j in range(M + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + j * A[i - 1])

    return dp[N][M]


def naive(N, M, A):
    answer = -(1 << 60)
    for bits in itertools.combinations(range(N), r=M):
        B = []
        for i in bits:
            B.append(A[i])

        C = [(i + 1) * b for i, b in enumerate(B)]

        answer = max(answer, sum(C))

    return answer


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    # N = random.randrange(2, 20)
    # M = random.randrange(1, N)
    # A = [random.randint(-100, 100) for i in range(N)]

    print(solve(N, M, A))


if __name__ == "__main__":
    main()
