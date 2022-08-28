from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W, D = map(int, input().split())
    A: List[List[int]] = [
        list(map(lambda x: int(x) - 1, input().split())) for i in range(H)
    ]
    Q: int = int(input())
    L, R = map(
        list, zip(*[list(map(lambda x: int(x) - 1, input().split())) for i in range(Q)])
    )

    P: List[Tuple[int, int]] = [(0, 0) for i in range(H * W)]
    for i, j in itertools.product(range(H), range(W)):
        P[A[i][j]] = (i, j)

    C: List[int] = [0] * (H * W + 1)
    for i in range(D, H * W):
        C[i] = C[i - D] + abs(P[i][0] - P[i - D][0]) + abs(P[i][1] - P[i - D][1])

    for l, r in zip(L, R):
        print(C[r] - C[l])


if __name__ == "__main__":
    main()
