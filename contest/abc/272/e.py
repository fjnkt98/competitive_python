from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    X: List[Set[int]] = [set() for i in range(M + 1)]
    X[0] = {a for a in A if 0 <= a <= N}
    for i, a in enumerate(A):
        l: int = 1 if a >= 0 else (-a + i) // (i + 1)
        r: int = min(M + 1, (N - a + i) // (i + 1))

        for j in range(l, r):
            X[j].add(a + (i + 1) * j)

    for i, x in enumerate(X):
        if i == 0:
            continue
        answer: int = 0
        while answer in x:
            answer += 1

        print(answer)


if __name__ == "__main__":
    main()
