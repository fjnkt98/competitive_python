from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))
    K: int = int(input())
    C, D = map(list, zip(*[list(map(int, input().split())) for i in range(K)]))

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=K):
        dish: List[int] = [0] * N
        for i, bit in enumerate(bits):
            if bit == 1:
                dish[C[i] - 1] += 1
            else:
                dish[D[i] - 1] += 1

        count: int = 0
        for i in range(M):
            if dish[A[i] - 1] >= 1 and dish[B[i] - 1] >= 1:
                count += 1
        answer = max(answer, count)

    print(answer)


if __name__ == "__main__":
    main()
