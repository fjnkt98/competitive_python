from typing import *
import collections
import itertools
import bisect
import math


def main():
    M: int = int(input())
    D, C = map(list, zip(*[list(map(int, input().split())) for i in range(M)]))

    N: int = sum(C)
    S: int = sum([d * c for d, c in zip(D, C)])

    print((N - 1) + (S - 1) // 9)


if __name__ == "__main__":
    main()
