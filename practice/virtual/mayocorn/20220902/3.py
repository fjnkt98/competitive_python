from typing import *
import collections
import itertools
import bisect
import math
import random


def naive(N, P, Q, R, A) -> bool:
    for x, y, z, w in itertools.combinations(range(N + 1), r=4):
        if sum(A[x:y]) == P and sum(A[y:z]) == Q and sum(A[z:w]) == R:
            return True

    return False


def solve(N, P, Q, R, A) -> bool:
    C: List[int] = [0] + list(itertools.accumulate(A))

    candidate: List[Tuple[int, int]] = []
    for i in range(N):
        j: int = bisect.bisect_left(C, C[i] + P + Q + R)

        if j <= N and (C[j] - C[i]) == P + Q + R:
            candidate.append((i, j))

    for x, w in candidate:
        y: int = bisect.bisect_left(C, C[x] + P)
        if not (x < y < w) or (C[y] - C[x]) != P:
            continue

        z: int = bisect.bisect_left(C, C[y] + Q)
        if not (y < z < w) or (C[z] - C[y]) != Q:
            continue

        if C[y] - C[x] == P and C[z] - C[y] == Q and C[w] - C[z] == R:
            return True

    return False


def main():
    N, P, Q, R = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    print("Yes" if solve(N, P, Q, R, A) else "No")


if __name__ == "__main__":
    main()
