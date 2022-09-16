from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    D: List[int] = [0 for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            D[j] += 1

    E: List[int] = [i * d for i, d in enumerate(D)]
    print(sum(E))


if __name__ == "__main__":
    main()
