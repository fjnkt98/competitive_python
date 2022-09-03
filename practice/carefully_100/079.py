from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M, Q = map(int, input().split())
    L, R = map(
        list, zip(*[list(map(lambda x: int(x) - 1, input().split())) for i in range(M)])
    )
    P, Q = map(
        list, zip(*[list(map(lambda x: int(x) - 1, input().split())) for i in range(Q)])
    )

    C: List[List[int]] = [[0 for j in range(N)] for i in range(N)]
    for l, r in zip(L, R):
        C[l][r] += 1

    for i in range(N):
        for j in range(1, N):
            C[i][j] += C[i][j - 1]

    for p, q in zip(P, Q):
        answer: int = 0
        for i in range(p, q + 1):
            answer += C[i][q]

        print(answer)


if __name__ == "__main__":
    main()
