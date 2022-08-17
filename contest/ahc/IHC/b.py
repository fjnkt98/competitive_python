from typing import *
import collections
import itertools
import bisect
import math


def score(T: List[int], S: List[List[int]], C: List[int]) -> List[int]:
    A: List[int] = [0] * len(T)
    L: List[int] = [-1] * 26
    for i, t in enumerate(T):
        L[t] = i
        A[i] = S[i][t] - sum([C[j] * (i - l) for j, l in enumerate(L)])

    return list(itertools.accumulate(A))


def main():
    D: int = int(input())
    C: List[int] = list(map(int, input().split()))
    S: List[List[int]] = [list(map(int, input().split())) for i in range(D)]
    T: List[int] = [int(input()) - 1 for i in range(D)]

    for a in score(T, S, C):
        print(a)


if __name__ == "__main__":
    main()
