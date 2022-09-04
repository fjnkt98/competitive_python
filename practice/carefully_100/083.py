from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    P: List[int] = list(map(int, input().split()))
    A, B, C = map(list, zip(*[list(map(int, input().split())) for i in range(N - 1)]))

    count: List[int] = [0] * (N + 1)
    current: int = P[0]
    for p in P[1:]:
        if current < p:
            i, j = current, p
        else:
            i, j = p, current
        count[i] += 1
        count[j] -= 1

        current = p

    count = list(itertools.accumulate(count))
    cost: List[int] = [0] * N
    for i, c in enumerate(count):
        if not (1 <= i < N):
            continue
        cost1: int = A[i - 1] * c
        cost2: int = C[i - 1] + c * B[i - 1]

        cost[i] = min(cost1, cost2)

    print(sum(cost))


if __name__ == "__main__":
    main()
