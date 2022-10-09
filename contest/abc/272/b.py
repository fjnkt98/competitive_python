from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    X: List[List[int]] = [[] for i in range(M)]
    for i in range(M):
        k, *x = list(map(int, input().split()))
        X[i] = [p - 1 for p in x]

    Y: List[Set[int]] = [set() for i in range(N)]
    for i, x in enumerate(X):
        for p in x:
            Y[p].add(i)

    ok: bool = True
    for i, j in itertools.combinations(range(N), r=2):
        if not (Y[i] & Y[j]):
            ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
