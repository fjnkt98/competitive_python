from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    L: List[int] = list(map(int, input().split()))
    Q: int = int(input())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    C: List[int] = [0 for i in range(100001)]
    for l in L:
        C[l] += 1
    C = list(itertools.accumulate(C)) + [0]

    for a, b in zip(A, B):
        print(C[b] - C[a - 1])


if __name__ == "__main__":
    main()
