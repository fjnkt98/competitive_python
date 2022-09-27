from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())

    answer: float = 0.0
    for i in range(1, N + 1):
        p: int = i
        c: int = 0

        while p < K:
            p *= 2
            c += 1

        answer += 1 / (N * 2 ** c)

    print(answer)


if __name__ == "__main__":
    main()
