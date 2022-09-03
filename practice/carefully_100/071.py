from typing import *
import collections
import itertools
import bisect
import math
import random


def main():
    N, Q = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    C: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    mod: int = 1000000007

    B: List[int] = [0] * (N)
    for i in range(1, N):
        B[i] = pow(A[i - 1], A[i], mod)

    D: List[int] = list(itertools.accumulate(B))
    answer: int = 0
    current: int = 0
    for c in C:
        if current < c:
            i, j = current, c
        else:
            i, j = c, current

        answer += D[j] - D[i]
        answer %= mod
        current = c

    answer += D[c]

    print(answer % mod)


if __name__ == "__main__":
    main()
