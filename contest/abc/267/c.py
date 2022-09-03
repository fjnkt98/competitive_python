from typing import *
import collections
import itertools
import bisect
import math
import random


def solve(N, M, A):
    C1: List[int] = [0] + list(itertools.accumulate(A))
    C2: List[int] = [0] + list(
        itertools.accumulate([(i + 1) * a for i, a in enumerate(A)])
    )

    answer: int = -(1 << 60)
    for k in range(N - M + 1):
        X: int = C2[k + M] - C2[k]
        Y: int = k * (C1[k + M] - C1[k])
        answer = max(answer, X - Y)

    return answer


def naive(N, M, A):
    answer: int = -(1 << 60)
    for i in range(N - M + 1):
        X: int = 0
        for j in range(M):
            X += (j + 1) * A[i + j]

        answer = max(answer, X)

    return answer


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    # N = random.randrange(2, 1000)
    # M = random.randrange(1, N)
    # A = [random.randint(-100000, 100000) for i in range(N)]

    print(solve(N, M, A))
    # print(naive(N, M, A))

    # assert solve(N, M, A) == naive(N, M, A)


if __name__ == "__main__":
    main()
