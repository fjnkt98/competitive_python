from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W, K, V = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(H)]

    C: List[List[int]] = [[0 for j in range(W + 1)] for i in range(H + 1)]
    for i, j in itertools.product(range(H), range(W)):
        C[i + 1][j + 1] = C[i][j + 1] + C[i + 1][j] - C[i][j] + A[i][j]

    answer: int = 0
    for i, j in itertools.product(range(1, H + 1), range(1, W + 1)):
        for k, l in itertools.product(range(i, H + 1), range(j, W + 1)):
            area: int = (k - i + 1) * (l - j + 1)
            cost: int = C[k][l] - C[i - 1][l] - C[k][j - 1] + C[i - 1][j - 1] + area * K

            if cost <= V:
                answer = max(answer, area)

    print(answer)


if __name__ == "__main__":
    main()
