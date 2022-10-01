from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, Q = map(int, input().split())
    L: List[List[int]] = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(a)

    S, T = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))

    for s, t in zip(S, T):
        s -= 1
        t -= 1
        print(L[s][t])


if __name__ == "__main__":
    main()
