from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    A.insert(0, 0)
    L: List[int] = [0 for i in range(Q)]
    R: List[int] = [0 for i in range(Q)]
    for i in range(Q):
        L[i], R[i] = map(int, input().split())

    cumsum = list(itertools.accumulate(A))

    for l, r in zip(L, R):
        print(cumsum[r] - cumsum[l - 1])


if __name__ == "__main__":
    main()
