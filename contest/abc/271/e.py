from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, K = map(int, input().split())
    A, B, C = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    E: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    D: List[int] = [1 << 60 for i in range(N)]
    D[0] = 0
    for e in E:
        if D[B[e]] > D[A[e]] + C[e]:
            D[B[e]] = D[A[e]] + C[e]

    if D[N - 1] == 1 << 60:
        print(-1)
    else:
        print(D[N - 1])


if __name__ == "__main__":
    main()
